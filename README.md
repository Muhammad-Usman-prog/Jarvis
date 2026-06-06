🚀 J.A.R.V.I.S. - Just A Rather Very Intelligent System

## Your Personal AI-Powered Voice Assistant for Windows

![Python Version](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%2010%2F11-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

📌 Overview

**J.A.R.V.I.S.** is a sophisticated, voice-activated personal AI assistant designed for Windows, inspired by Tony Stark's iconic AI from Iron Man. Built entirely in Python, this project transforms your laptop into a smart, voice-controlled powerhouse that can handle everything from system automation to casual conversation.

As a **PF (Programming Fundamentals) Project**, J.A.R.V.I.S. demonstrates practical implementation of core programming concepts including speech recognition, natural language processing, system automation, API integration, and multi-threading - all wrapped in an engaging, user-friendly interface.

✨ Key Features

### 🎤 Voice Control & Speech Recognition
- **24/7 Background Operation** - Runs silently in the background, always ready
- **Wake Word Detection** - Activate with "Hey Jarvis" or "Jarvis wake up"
- **Multi-Engine Speech Recognition** - Uses Google Speech API + SpeechRecognition library
- **Custom Voice Selection** - Switch between multiple system voices
- **Natural Conversation** - Engages in casual, friendly dialogue

### 📱 Communication
- **WhatsApp Automation** - Send messages to any contact hands-free
- **Smart Contact Matching** - Fuzzy name recognition for 30+ contacts
- **Auto-Search & Type** - Automatically finds contacts and types messages

### 🎵 Entertainment
- **YouTube Integration** - Search and play any song, artist, or video
- **Auto-Play** - Automatically clicks the first video result
- **Tab Management** - Close YouTube without closing the browser

### 💻 System Control
- **Application Management** - Open/close any application (VS Code, Chrome, WhatsApp, etc.)
- **Close All Programs** - One command to close all running applications
- **Volume Control** - Increase, decrease, mute, unmute
- **Brightness Control** - Adjust screen brightness via voice
- **System Power** - Restart, shutdown, sleep, lock controls
- **Screenshots** - Capture and save screenshots to Desktop

### 📁 File Management
- **Create Files/Folders** - Create files and folders in any location
- **Delete Files/Folders** - Delete from Desktop, Downloads, Documents, etc.
- **Smart Search** - Find and delete files by partial name matching

### 💡 Code Generation
- **15+ Code Templates** - Generate ready-to-use code snippets
- **Multi-Language Support** - HTML, CSS, Python, C++, C, JavaScript
- **Auto-Open in VS Code** - Created files automatically open in editor
- **Templates Include**:
  - Login Form (HTML/CSS)
  - Signup Form (HTML/CSS)
  - Navigation Bar (HTML/CSS)
  - Calculator (Python, C++)
  - Fibonacci Series (Python)
  - Factorial (Python)
  - Hello World (All languages)

### 🌐 Web & Search
- **Google Search** - Search anything on the web
- **YouTube Search** - Find and play videos
- **Gmail Access** - Open Gmail instantly

### 🤖 AI Personality
- **Personalized Responses** - Knows your name and remembers you
- **Emotional Intelligence** - Responds to mood and feelings
- **Project Awareness** - Knows it's your PF Project
- **Friendly Banter** - Jokes, greetings, and casual conversation

---

## 🏗️ Technical Architecture

```
J.A.R.V.I.S.
├── Audio Input Layer
│   ├── sounddevice (Primary)
│   └── SpeechRecognition (Enhanced)
├── Speech Processing
│   ├── Google Speech API
│   └── Offline Recognition (Fallback)
├── Natural Language Understanding
│   ├── Command Parser
│   └── Intent Recognition
├── Action Executor
│   ├── System Commands
│   ├── File Operations
│   ├── Web Automation
│   └── Code Generator
├── Text-to-Speech
│   ├── SAPI (Windows)
│   └── pyttsx3 (Cross-platform)
└── Background Service
    ├── Auto-start with Windows
    └── 24/7 Silent Listening
```

---

## 📋 Tech Stack

| Category | Technology |
|----------|------------|
| **Language** | Python 3.8+ |
| **Speech Recognition** | Google Speech API, SpeechRecognition |
| **Audio Processing** | sounddevice, PyAudio, wave |
| **Text-to-Speech** | SAPI (Windows), pyttsx3 |
| **GUI Automation** | PyAutoGUI |
| **System Control** | psutil, subprocess, ctypes |
| **Image Processing** | Pillow (PIL) |
| **Web Integration** | webbrowser, urllib |
| **Screen Control** | screen-brightness-control |
| **Data Handling** | json, re (Regex), pathlib |

---

## 🎯 Commands Reference

### Wake & Greet
```
"Hey Jarvis"                    → Activates assistant
"Hey Jarvis wake up"            → Wakes from sleep mode
"Hello"                         → Friendly greeting
```

### System Control
```
"Open [app name]"               → Opens any application
"Close [app name]"              → Closes specific app
"Close all programs"            → Closes everything
"Restart"                       → Restarts system
"Shutdown"                      → Shuts down system
"Sleep"                         → Puts system to sleep
"Volume up/down"                → Adjusts volume
"Brightness up/down"            → Adjusts brightness
"Take a screenshot"             → Captures screen
```

### Communication
```
"Send SMS to [name] say [msg]"  → WhatsApp message
"Message [name] tell [msg]"     → Alternative format
```

### Entertainment
```
"Play [song name]"              → Plays on YouTube
"Play [artist] songs"           → Artist search
"Open YouTube"                  → Opens YouTube
"Close YouTube"                 → Closes YouTube tab
```

### Productivity
```
"Code for login form"           → Generates HTML login form
"Hello world in python"         → Creates Python file
"Calculator in c++"             → Creates C++ calculator
"Create folder [name]"          → Creates folder
"Delete [file name]"            → Deletes file/folder
"Search [query]"                → Google search
"Open Gmail"                    → Opens Gmail
```

### Personal Interaction
```
"Do you know me?"               → Personal recognition
"Who made you?"                 → Creator info
"What do you like about me?"    → Compliments
"Do you know why I made you?"   → Project awareness
"How are you?"                  → Status check
"Tell me a joke"                → Entertainment
```

---

## 🚀 Installation & Setup

### Prerequisites
- Windows 10 or 11
- Python 3.8 or higher
- Internet connection (for speech recognition)
- Microphone

### Quick Start
```bash
# Clone the repository
git clone https://github.com/yourusername/JARVIS-AI-Assistant.git
cd JARVIS-AI-Assistant

# Install dependencies
pip install -r requirements.txt

# Run J.A.R.V.I.S.
python main.py
```

### Auto-Start Setup
J.A.R.V.I.S. automatically configures itself to start with Windows:
1. Creates a startup batch file
2. Adds registry entry for auto-launch
3. Runs minimized in system tray

## 🔧 Customization

Edit these variables in `main.py` to personalize:

```python
BOSS_NAME = "Muhammad Usman"    # Your full name
BOSS_SHORT = "Usman"            # Your nickname
BOSS_PROJECT = "PF Project"     # Your project name
```

Add contacts:
```python
CONTACTS = {
    "name": "WhatsApp Contact Name",
    "another": "Another Contact",
}
```

---

## 🎓 Learning Outcomes

This project demonstrates proficiency in:
- **Speech Recognition & NLP** - Real-time voice processing
- **System Programming** - OS-level automation
- **API Integration** - Google Speech API, web services
- **GUI Automation** - PyAutoGUI for desktop control
- **Multi-threading** - Non-blocking speech and listening
- **File I/O** - Dynamic file creation and management
- **Error Handling** - Robust exception management
- **Regex Pattern Matching** - Natural language parsing

---

## 🏆 Achievements

- ✅ 24/7 Background Operation
- ✅ 30+ Voice Commands
- ✅ 15+ Code Templates
- ✅ 30+ Contact Database
- ✅ Multi-language Support
- ✅ Auto-start with Windows
- ✅ Zero configuration needed
- ✅ Works offline for basic commands

---

## 🔮 Future Enhancements

- [ ] GUI Dashboard Interface
- [ ] Email Sending Integration
- [ ] Weather & News Updates
- [ ] Calendar & Reminders
- [ ] Custom Voice Training
- [ ] Multi-language Support (Urdu)
- [ ] Smart Home Integration
- [ ] Face Recognition

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Muhammad Usman**
- 🎓 Student | Programmer | AI Enthusiast
- 📧 mrusmanpirzada@gmail.com
- 💼 https://www.linkedin.com/in/muhammad-usman-pirzada/

## 🙏 Acknowledgments

- Inspired by J.A.R.V.I.S. from Marvel's Iron Man
- Google Speech Recognition API
- Python Open Source Community

---

## ⭐ Show Your Support

If you found this project interesting or helpful:
- ⭐ Star this repository
- 🔄 Share with your network
- 📝 Provide feedback

---

## 📸 Screenshots

```
╔══════════════════════════════════════════╗
║        ⚡ J.A.R.V.I.S. v33 ⚡           ║
║    24/7 + BACKGROUND + CLOSE ALL + SYS  ║
║    Made by: Muhammad Usman              ║
║    Project: PF Project                 ║
╚══════════════════════════════════════════╝

  ✅ Auto-start enabled!
  
  🤫 Running in background. Say 'hey jarvis wake up'
  🔴 'close all programs' - Close everything
  🔄 'restart' | 'shutdown' | 'sleep' - System control
  📝 'code for login form' - Generate code
  🎤 Listening: ✅ Enhanced
  🎤 Voice: Microsoft David Desktop - English (United States)
```

---

### Sample Interaction:

```
🗣️  "hey jarvis wake up"
🤖 J.A.R.V.I.S.: Hey Boss! I am here. How can I help you today?

🗣️  "play atif aslam songs on youtube"
▶️ YouTube: atif aslam songs
🤖 J.A.R.V.I.S.: Playing atif aslam songs on YouTube, Boss.

🗣️  "send sms to wasif bilal say hello"
📱 WhatsApp → Wasif Bilal: hello
🤖 J.A.R.V.I.S.: Message sent to Wasif Bilal, Boss.

🗣️  "code for login form"
🔍 Searching code for: 'login form'
🤖 J.A.R.V.I.S.: Created login_form.html on your Desktop, Boss! Opening in VS Code.

🗣️  "close all programs"
🔒 Closing all programs...
🤖 J.A.R.V.I.S.: Closed 5 programs successfully, Boss!

Made with ❤️ and Python | PF Project 2026
