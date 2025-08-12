from flask import Flask, render_template, request, jsonify, send_file
import csv
import os
import tempfile
from werkzeug.utils import secure_filename
import json

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def cleanup_csv(input_file_path, output_file_path):
    """
    Clean up CSV files to match the apr25.csv format (name, amount only)
    """
    cleaned_data = []
    
    with open(input_file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        
        for row in reader:
            # Skip completely empty rows
            if len(row) == 0:
                continue
                
            name = None
            amount = None
            
            # Try QuickBooks format first (more columns)
            if len(row) >= 6:
                name = row[3].strip()  # Column 4 - Donor name
                amount_str = row[5].strip()  # Column 6 - Amount
                
                # Skip if name is empty or looks like a header
                if not name or name.lower() in ['template information', 'template name', 'request type', 'company name', 'company id', 'template description', 'debit account', 'effective date', 'confirmation number', 'status', 'credit/destination accounts', 'aba/trc', 'account', 'account type', 'name', 'detail id', 'amount', 'additional information', 'st sharbel pledges']:
                    continue
                
                # Skip rows that look like template data
                if len(name) > 50 or name.replace('.', '').replace('-', '').isdigit():
                    continue
                
                # Try to parse amount
                try:
                    if amount_str.replace('.', '', 1).isdigit() and float(amount_str) > 0:
                        amount = float(amount_str)
                    else:
                        continue
                except ValueError:
                    continue
            
            # If QuickBooks format didn't work, try simple format
            if not name or not amount:
                if len(row) >= 2:
                    name = row[0].strip()
                    amount_str = row[1].strip()
                    
                    # Skip if name is empty
                    if not name:
                        continue
                    
                    # Try to parse amount
                    try:
                        if amount_str.replace('.', '', 1).isdigit() and float(amount_str) > 0:
                            amount = float(amount_str)
                        else:
                            continue
                    except ValueError:
                        continue
            
            if amount is not None and name and amount > 0:
                cleaned_data.append([name, amount])
    
    # Write cleaned data
    with open(output_file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(cleaned_data)
    
    return len(cleaned_data)

def get_total(csv_file_path):
    """Calculate total from CSV file"""
    total = 0
    count = 0
    try:
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 2:
                    try:
                        amount = float(row[1])
                        total += amount
                        count += 1
                    except ValueError:
                        continue
        return total, count
    except Exception as e:
        return 0, 0

def organize_csv(csv_file_path):
    """Sort CSV by name alphabetically"""
    try:
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)
        
        if len(data) <= 1:
            return False
        
        # Sort by name (first column)
        sorted_data = sorted(data, key=lambda x: x[0].lower())
        
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(sorted_data)
        
        return True
    except Exception as e:
        return False

def compare_csvs(file1_path, file2_path):
    """Compare two CSV files and return differences"""
    def read_csv_to_list(csv_file):
        data = []
        try:
            with open(csv_file, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) >= 2:
                        name = row[0].strip()
                        try:
                            amount = float(row[1])
                            data.append((name.lower(), name, amount))  # (lower_name, original_name, amount)
                        except ValueError:
                            continue
        except Exception:
            pass
        return data
    
    data1 = read_csv_to_list(file1_path)  # Previous month
    data2 = read_csv_to_list(file2_path)  # Current month
    
    added_donors = []
    removed_donors = []
    changed_donations = []
    
    # Create lookup dictionaries for easier comparison
    # Group by name and collect all amounts
    def group_by_name(data_list):
        grouped = {}
        for lower_name, original_name, amount in data_list:
            if lower_name not in grouped:
                grouped[lower_name] = []
            grouped[lower_name].append((original_name, amount))
        return grouped
    
    grouped1 = group_by_name(data1)
    grouped2 = group_by_name(data2)
    
    # Check for added donors (names that don't exist in previous month)
    for name in grouped2:
        if name not in grouped1:
            for original_name, amount in grouped2[name]:
                added_donors.append((original_name, amount))
    
    # Check for removed donors (names that don't exist in current month)
    for name in grouped1:
        if name not in grouped2:
            for original_name, amount in grouped1[name]:
                removed_donors.append((original_name, amount))
    
    # Check for changed donations (names that exist in both but with different amounts)
    for name in grouped1:
        if name in grouped2:
            # Get all amounts for this name in both months
            amounts1 = [amount for _, amount in grouped1[name]]
            amounts2 = [amount for _, amount in grouped2[name]]
            
            # Sort amounts for consistent comparison
            amounts1.sort()
            amounts2.sort()
            
            # If the sorted lists are different, there are changes
            if amounts1 != amounts2:
                # Find specific changes
                for original_name, amount in grouped2[name]:
                    # Check if this specific amount exists in the previous month
                    if amount not in amounts1:
                        # This is a new amount for this donor
                        changed_donations.append((original_name, "multiple amounts", amount))
    
    return {
        'added': added_donors,
        'removed': removed_donors,
        'changed': changed_donations
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file and file.filename.endswith('.csv'):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Clean up the file
        cleaned_filename = f'cleaned_{filename}'
        cleaned_filepath = os.path.join(app.config['UPLOAD_FOLDER'], cleaned_filename)
        record_count = cleanup_csv(filepath, cleaned_filepath)
        
        # Get total
        total, count = get_total(cleaned_filepath)
        
        # Organize alphabetically
        organize_csv(cleaned_filepath)
        
        # Delete the original uploaded file (keep only the cleaned version)
        try:
            os.remove(filepath)
        except Exception as e:
            print(f"Warning: Could not delete original file {filepath}: {e}")
        
        return jsonify({
            'success': True,
            'filename': cleaned_filename,  # Return cleaned filename as main filename
            'record_count': record_count,
            'total': total,
            'count': count
        })
    
    return jsonify({'error': 'Invalid file type'}), 400

@app.route('/compare', methods=['POST'])
def compare_files():
    data = request.get_json()
    file1 = data.get('file1')
    file2 = data.get('file2')
    
    if not file1 or not file2:
        return jsonify({'error': 'Both files are required'}), 400
    
    file1_path = os.path.join(app.config['UPLOAD_FOLDER'], file1)
    file2_path = os.path.join(app.config['UPLOAD_FOLDER'], file2)
    
    if not os.path.exists(file1_path) or not os.path.exists(file2_path):
        return jsonify({'error': 'One or both files not found'}), 400
    
    comparison = compare_csvs(file1_path, file2_path)
    return jsonify(comparison)

@app.route('/download/<filename>')
def download_file(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(filepath):
        return send_file(filepath, as_attachment=True, download_name=filename)
    return jsonify({'error': 'File not found'}), 404

@app.route('/delete/<filename>', methods=['DELETE'])
def delete_file(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(filepath):
        try:
            os.remove(filepath)
            return jsonify({'success': True, 'message': f'File {filename} deleted successfully'})
        except Exception as e:
            return jsonify({'error': f'Could not delete file: {str(e)}'}), 500
    return jsonify({'error': 'File not found'}), 404

@app.route('/files')
def list_files():
    files = []
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        if filename.endswith('.csv'):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            total, count = get_total(filepath)
            files.append({
                'name': filename,
                'total': total,
                'count': count,
                'size': os.path.getsize(filepath)
            })
    return jsonify(files)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
