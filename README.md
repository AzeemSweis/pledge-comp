# 🏛️ Church Pledge CSV Manager

A modern web application that automates the process of managing and comparing monthly church pledge donations. This tool replaces your manual CSV processing workflow with a beautiful, user-friendly interface.

## ✨ Features

- **📁 Smart CSV Upload**: Automatically detects and processes QuickBooks exports and other CSV formats
- **🧹 Automatic Cleanup**: Converts any CSV format to the clean name/amount format (like your apr25.csv)
- **📊 Total Calculation**: Instantly shows donation totals and donor counts
- **🔤 Alphabetical Organization**: Automatically sorts donors alphabetically
- **🔍 Month-to-Month Comparison**: Easily identify new donors, removed donors, and changed donations
- **📥 Download Cleaned Files**: Get your processed files ready for QuickBooks Online
- **📱 Responsive Design**: Works perfectly on desktop, tablet, and mobile devices

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Application

```bash
python app.py
```

### 3. Open Your Browser

Navigate to `http://localhost:5001` to access the application.

## 📋 How It Works

### Your Current Workflow (Replaced)
1. ❌ Manually clean CSV files to match apr25.csv format
2. ❌ Run get_total.py to confirm totals
3. ❌ Run organize_csv.py to sort alphabetically
4. ❌ Run compare.py to find differences

### New Automated Workflow
1. ✅ **Upload**: Drag & drop any CSV file (QuickBooks export, etc.)
2. ✅ **Auto-Process**: File is automatically cleaned, totaled, and organized
3. ✅ **Compare**: Select two months and instantly see all changes
4. ✅ **Download**: Get your cleaned files ready for QuickBooks Online

## 🎯 Perfect For

- **Monthly Pledge Processing**: Upload new month's data and compare with previous
- **QuickBooks Online Updates**: Get clean, organized data ready for import
- **Donor Change Tracking**: Instantly see who's new, who's gone, who changed amounts
- **Audit & Reporting**: Maintain organized records of all monthly donations

## 📁 File Structure

```
pledge-comp/
├── app.py                 # Main Flask application
├── templates/
│   └── index.html        # Web interface
├── requirements.txt       # Python dependencies
├── uploads/              # Processed files (created automatically)
├── apr25.csv            # Your clean format example
├── may25.csv            # QuickBooks export example
├── jun25.csv            # QuickBooks export example
├── jul25.csv            # QuickBooks export example
├── aug25.csv            # QuickBooks export example
└── [your original scripts]
```

## 🔧 How the Cleanup Works

The application intelligently detects donation data in various CSV formats:

- **QuickBooks Exports**: Automatically finds the name and amount columns
- **Header Detection**: Skips template information, company details, etc.
- **Amount Parsing**: Handles different currency formats and column positions
- **Data Validation**: Ensures only valid donation records are processed

## 💡 Usage Examples

### Monthly Processing
1. **Upload** your new month's CSV (e.g., `sep25.csv`)
2. **View** the automatic total and donor count
3. **Compare** with previous month to see changes
4. **Download** the cleaned file for QuickBooks Online

### Quick Comparison
1. **Select** two months from the dropdown menus
2. **Click** "Compare Files"
3. **Review** new donors, removed donors, and changed amounts
4. **Use** this information to update your QuickBooks template

## 🛠️ Technical Details

- **Backend**: Flask (Python)
- **Frontend**: Modern HTML5, CSS3, JavaScript
- **File Processing**: CSV parsing with intelligent data extraction
- **Storage**: Local file system with automatic organization
- **Security**: File type validation and secure filename handling

## 🔒 Security Features

- File type validation (CSV only)
- Secure filename handling
- Maximum file size limits
- Input sanitization

## 📱 Browser Compatibility

- ✅ Chrome (recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ✅ Mobile browsers

## 🚨 Troubleshooting

### Common Issues

**File won't upload?**
- Ensure it's a CSV file
- Check file size (max 16MB)
- Try refreshing the page

**Comparison not working?**
- Make sure both files are uploaded
- Select different files for comparison
- Check that files contain valid donation data

**Can't see processed files?**
- Click "Refresh Files" button
- Check the uploads folder
- Ensure file processing completed successfully

### Getting Help

If you encounter issues:
1. Check the browser console for error messages
2. Verify your CSV file format
3. Try with a smaller test file first
4. Ensure all dependencies are installed

## 🔄 Updates & Maintenance

The application automatically:
- Creates necessary directories
- Processes files in the background
- Maintains file organization
- Provides real-time feedback

## 📈 Future Enhancements

Potential improvements:
- Export comparison results to PDF
- Email notifications for large changes
- Historical trend analysis
- Backup and restore functionality
- Multi-church support

## 🤝 Contributing

This application was created specifically for church pledge management. If you have suggestions or improvements, feel free to contribute!

---

**Made with ❤️ for efficient church administration**
