# Advanced Educational Keylogger - Kali Linux Edition

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Kali%20Linux-red)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-educational-yellow)

## ⚠️ IMPORTANT LEGAL AND ETHICAL DISCLAIMER

**THIS SOFTWARE IS FOR EDUCATIONAL PURPOSES ONLY**
╔════════════════════════════════════════════════════════════════════════════╗
║ BY USING THIS SOFTWARE YOU AGREE TO: ║
║ ✓ Use ONLY on systems you own or have explicit written permission ║
║ ✓ Use in isolated lab environments (VMs, containers) ║
║ ✓ NOT deploy on production systems or other people's devices ║
║ ✓ NOT use for malicious purposes ║
║ ║
║ UNAUTHORIZED USE IS ILLEGAL AND UNETHICAL ║
║ Violates: Computer Fraud and Abuse Act, GDPR, Privacy Laws ║
╚════════════════════════════════════════════════════════════════════════════╝
## 🎯 Project Overview

This advanced educational keylogger was developed on **Kali Linux using Vim** as part of cybersecurity research and learning. It demonstrates various techniques used in security testing and helps understand:

- Operating System internals
- Input monitoring mechanisms
- Data persistence and encryption
- Network exfiltration methods
- Anti-forensic techniques
- Detection and prevention strategies

## ✨ Features

### Core Monitoring Capabilities

| Feature | Description | Educational Value |
|---------|-------------|-------------------|
| **⌨️ Keystroke Logging** | Captures all keyboard input with special key handling | Understand input device APIs |
| **🪟 Window Tracking** | Monitors active window/focus changes | Learn context-aware monitoring |
| **📸 Screenshot Capture** | Periodic screenshots of user activity | Visual surveillance techniques |
| **📋 Clipboard Monitoring** | Tracks clipboard content changes | Data theft vectors |
| **🌐 Network Monitoring** | Logs active network connections | Exfiltration detection |
| **⚙️ Process Monitoring** | Tracks new running processes | Security tool detection |
| **🔒 Encrypted Logs** | All logs encrypted with Fernet | Forensic countermeasures |
| **🕵️ Stealth Mode** | Process hiding and background operation | Evasion techniques |

### Advanced Features
┌─────────────────────────────────────────────────────────────────┐
│ STATISTICS TRACKING │
├─────────────────────────────────────────────────────────────────┤
│ • Keys pressed count │
│ • Screenshots captured │
│ • Clipboard operations │
│ • Network packets captured │
│ • Runtime duration │
│ • Comprehensive activity reports │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ DATA EXFILTRATION METHODS │
├─────────────────────────────────────────────────────────────────┤
│ • Local encrypted storage (default) │
│ • HTTP/HTTPS webhook integration │
│ • Configurable exfiltration intervals │
│ • Multiple log rotation policies │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ STEALTH & PERSISTENCE │
├─────────────────────────────────────────────────────────────────┤
│ • Hidden directory structure (~/.system_logs/) │
│ • Process name spoofing │
│ • Daemon mode (background execution) │
│ • Configurable log rotation │
└─────────────────────────────────────────────────────────────────┘

## 💻 Development Environment

This project was developed on:

- **OS**: Kali Linux (Rolling)
- **Editor**: Vim (with syntax highlighting and Python plugins)
- **Shell**: Zsh with Oh-My-Zsh
- **Python**: 3.11+
- **Virtual Environment**: Python venv

The choice of Vim on Kali Linux provides:
- Lightweight development environment
- Native terminal integration
- Excellent for security tool development
- Direct access to system tools and debugging

## 🚀 Installation

### Prerequisites
```bash
# System requirements
- Kali Linux / Ubuntu / Debian-based distro
- Python 3.8+
- Root access (optional, for some features)
- Internet connection (for dependencies)
