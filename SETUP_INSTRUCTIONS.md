# 🚀 Quick Setup Guide

## Your Church Pledge CSV Manager is Ready!

### ✨ What You Now Have

1. **Modern Web Interface** - Beautiful, easy-to-use UI for managing your CSV files
2. **Automatic Cleanup** - Converts any QuickBooks export to clean name/amount format
3. **Smart Processing** - Automatically calculates totals, organizes alphabetically
4. **Month-to-Month Comparison** - Instantly see donor changes between months
5. **File Management** - Upload, download, and organize all your pledge files

### 🎯 How to Use

#### Option 1: Quick Start (Recommended)
```bash
./start.sh
```
Then open your browser to: **http://localhost:5001**

#### Option 2: Manual Setup
```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

### 📱 Using the Web Interface

1. **Upload Files**: Drag & drop any CSV (QuickBooks exports work perfectly!)
2. **Auto-Process**: Files are automatically cleaned, totaled, and organized
3. **Compare Months**: Select two months to see all changes
4. **Download Clean Files**: Get your processed files ready for QuickBooks Online

### 🔧 What the Cleanup Does

- **QuickBooks Exports** → Clean name/amount format (like your apr25.csv)
- **Header Removal** → Automatically skips template information
- **Data Validation** → Only processes valid donation records
- **Alphabetical Sorting** → Organizes donors by name
- **Total Calculation** → Shows donation totals and donor counts

### 📊 Your Current Files

- ✅ **apr25.csv** - Clean format (186 donors, $13,000 total)
- ✅ **may25.csv** - QuickBooks export (187 donors, $13,015 total)
- ✅ **jun25.csv** - QuickBooks export (188 donors, $13,035 total)
- ✅ **jul25.csv** - QuickBooks export (190 donors, $13,285 total)
- ✅ **aug25.csv** - QuickBooks export (190 donors, $13,060 total)

### 🎉 Benefits Over Your Old Workflow

| Old Process | New Process |
|-------------|-------------|
| ❌ Manual CSV cleanup | ✅ Automatic cleanup |
| ❌ Run get_total.py | ✅ Instant totals |
| ❌ Run organize_csv.py | ✅ Auto-sorting |
| ❌ Run compare.py | ✅ Visual comparison |
| ❌ Command line only | ✅ Beautiful web interface |

### 🚨 Troubleshooting

**Port 5000 in use?** The app now uses port 5001 to avoid conflicts with macOS AirPlay.

**Files not uploading?** Make sure they're CSV format and under 16MB.

**Need to restart?** Just run `./start.sh` again.

### 🔄 Monthly Workflow

1. **Get new month's CSV** from QuickBooks
2. **Upload to the web app**
3. **Review totals and donor count**
4. **Compare with previous month**
5. **Download cleaned file** for QuickBooks Online
6. **Update your template** with the changes

### 📈 Next Steps

1. **Test the app** with your existing files
2. **Upload new month's data** when you get it
3. **Use the comparison** to update QuickBooks Online
4. **Enjoy the time savings!** 🎉

---

**Your church administration just got a whole lot easier!** 🏛️✨
