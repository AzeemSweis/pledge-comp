#!/bin/bash

# Church Pledge CSV Manager Startup Script

echo "🏛️ Starting Church Pledge CSV Manager..."
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment and install dependencies
echo "Activating virtual environment and installing dependencies..."
source venv/bin/activate
pip install -r requirements.txt

# Start the application
echo ""
echo "🚀 Starting the application..."
echo "📱 Open your browser and go to: http://localhost:5001"
echo "🛑 Press Ctrl+C to stop the application"
echo ""

python app.py
