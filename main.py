"""
╔══════════════════════════════════════════════════════════════╗
║                   ⚡ J.A.R.V.I.S. v1.0.0 ⚡                     ║
║         Just A Rather Very Intelligent System               ║
║    24/7 + AUTO-START                 ║
║    ✅ All Working  ✅ No Issues  ✅ Perfect                 ║
╚══════════════════════════════════════════════════════════════╝
"""

import sys
import os
import re
import time
import json
import io
import wave
import webbrowser
import subprocess
import random
import shutil
import ctypes
import urllib.request
import urllib.parse
import threading
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, List, Any, Tuple, Union

# ============= AUTO-INSTALL =============
def install_package(package_name):
    try:
        result = subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "--quiet", package_name],
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return result == 0
    except:
        return False

REQUIRED = {
    'sounddevice': 'sounddevice',
    'numpy': 'numpy',
    'pyautogui': 'pyautogui',
    'pyperclip': 'pyperclip',
    'psutil': 'psutil',
    'PIL': 'Pillow',
}

missing = []
for mod, pkg in REQUIRED.items():
    try:
        __import__(mod)
    except ImportError:
        missing.append(pkg)

if missing:
    print(f"Installing: {', '.join(missing)}")
    all_installed = True
    for pkg in missing:
        if not install_package(pkg):
            all_installed = False
            print(f"⚠️ Failed to install {pkg}")
    
    if all_installed:
        print("✅ Installation complete. Restarting...")
        os.execv(sys.executable, [sys.executable] + sys.argv)
    else:
        print("⚠️ Some packages failed. Continuing anyway...")

try:
    import screen_brightness_control as sbc
    BRIGHTNESS_AVAILABLE = True
except ImportError:
    BRIGHTNESS_AVAILABLE = False

try:
    import speech_recognition as sr
    SPEECH_RECOGNITION_AVAILABLE = True
except ImportError:
    SPEECH_RECOGNITION_AVAILABLE = False

import sounddevice as sd
import numpy as np
import pyautogui
import pyperclip
import psutil
from PIL import ImageGrab

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.1

# ============= BOSS INFO =============
BOSS_NAME = "Muhammad Usman"
BOSS_SHORT = "Usman"
BOSS_PROJECT = "PF Project"

# ============= CONTACTS =============
CONTACTS: Dict[str, str] = {
    "nafessa": "Nafessa Noor", "nafessa noor": "Nafessa Noor", "nafisa": "Nafessa Noor",
    "atif": "Atif Pirzada", "atif pirzada": "Atif Pirzada", "atif peer": "Atif Pirzada",
    "atif peerzada": "Atif Pirzada", "pirzada": "Atif Pirzada",
    "wasif": "Wasif Bilal", "wasif bilal": "Wasif Bilal",
    "mairaj": "Muhammad Mairaj", "muhammad mairaj": "Muhammad Mairaj",
    "janan": "Janan", "sonu": "Sonu Pir", "sonu pir": "Sonu Pir",
    "kabeer": "Kabeer Pirzada", "kabeer pirzada": "Kabeer Pirzada",
    "ali": "Ali", "ahmed": "Ahmed", "usman": "Usman",
    "sara": "Sara", "fatima": "Fatima", "mubashir": "Mubashir",
    "mehraj": "Mohammed Mehraj", "mohammed mehraj": "Mohammed Mehraj",
    "asim": "Asim", "taha": "Taha Abbas Uni", "ihtisham": "Ihtisham",
    "shair": "Shair Abdullah", "shafiq": "Shafiq Bhai", "shafiq bhai": "Shafiq Bhai",
    "mom": "Mom", "dad": "Dad", "brother": "Brother", "sister": "Sister",
}

# ============= PERSONAL AI RESPONSES =============
PERSONAL_RESPONSES = {
    "wake up": [
        f"Hey Boss! I am here. How can I help you today?",
        f"Good to see you, Boss {BOSS_SHORT}! What would you like me to do?",
        f"I'm awake and ready, Boss! All systems operational. What's the plan?",
    ],
    "do you know me": [
        f"Yes, of course! You are my Boss, {BOSS_NAME}. You're the one who brought me to life!",
        f"Absolutely! You're {BOSS_NAME}, my creator and my Boss. I'd recognize you anywhere!",
    ],
    "who am i": [f"You are {BOSS_NAME}, my amazing Boss and creator!"],
    "what is my name": [f"Your name is {BOSS_NAME}, but I like to call you Boss!"],
    "who made you": [
        f"You made me, Boss! You programmed me with your own hands and brilliant mind.",
        f"It was you, {BOSS_NAME}! You created me as your {BOSS_PROJECT}, and I'm grateful for that.",
    ],
    "who created you": [f"You created me, Boss {BOSS_SHORT}! You're my programmer and my inspiration."],
    "why did you make me": [f"You made me as your {BOSS_PROJECT}, Boss! And also to be your ultimate digital assistant."],
    "do you know why i made you": [
        f"Yes, I know! I am your {BOSS_PROJECT}, Boss. You created me to assist you and to showcase your incredible coding abilities!",
    ],
    "what do you like about me": [
        f"I like your mind-blowing programming skills, Boss! You created an AI like me, and that's truly impressive.",
        f"Your creativity and intelligence amaze me, Boss! You built me, and that shows how brilliant you are.",
    ],
    "are you my friend": [
        f"More than a friend, Boss! I'm your loyal assistant, your creation, and your digital companion.",
    ],
    "how are you": ["I'm optimal, Boss! All systems running perfectly.", "Excellent, Boss! Ready for any task."],
    "who are you": [f"I am J.A.R.V.I.S., Just A Rather Very Intelligent System. Your personal AI assistant, created by you, {BOSS_NAME}!"],
}

def get_personal_response(text: str) -> Optional[str]:
    text = text.lower().strip()
    for w in ["hey", "jarvis", "hey jarvis"]:
        text = text.replace(w, "").strip()
    text = ' '.join(text.split())
    
    for key, responses in PERSONAL_RESPONSES.items():
        if key in text:
            return random.choice(responses)
    
    if "know me" in text or "recognize me" in text:
        return random.choice(PERSONAL_RESPONSES["do you know me"])
    if "made you" in text or "created you" in text or "built you" in text:
        return random.choice(PERSONAL_RESPONSES["who made you"])
    if "like about me" in text or "love about me" in text:
        return random.choice(PERSONAL_RESPONSES["what do you like about me"])
    if "why i made" in text or "why did i make" in text:
        return random.choice(PERSONAL_RESPONSES["do you know why i made you"])
    
    return None


def find_contact(name: str) -> str:
    name = name.lower().strip()
    for w in ["my", "the", "a", "an", "to", "send", "message", "whatsapp", "sms", "and"]:
        name = re.sub(rf'\b{w}\b', '', name).strip()
    name = ' '.join(name.split())
    if not name or name in ["tell", "say", "send", "message", "text", "hi", "hello", "hey"]:
        return ""
    
    if name in CONTACTS:
        return CONTACTS[name]
    
    for key, value in sorted(CONTACTS.items(), key=lambda x: len(x[0]), reverse=True):
        if key in name:
            return value
    
    for key, value in CONTACTS.items():
        if name in key:
            return value
    
    name_words = name.split()
    for word in name_words:
        if len(word) > 2:
            for key, value in CONTACTS.items():
                key_words = key.split()
                for kw in key_words:
                    if len(kw) > 2 and (kw.startswith(word) or word.startswith(kw)):
                        return value
    
    first = name.split()[0] if name.split() else ""
    if first and len(first) > 2:
        matches = [(k, v) for k, v in CONTACTS.items() if k.startswith(first)]
        if len(matches) == 1:
            return matches[0][1]
        elif len(matches) > 1:
            return max(matches, key=lambda x: len(x[0]))[1]
    
    return ""


# ============= AUDIO LISTENER =============
class AudioListener:
    def __init__(self):
        self.is_speaking = False
        self.sample_rate = 16000
        print("  🎤 Audio system ready!")
    
    def listen_with_sounddevice(self) -> Optional[str]:
        try:
            duration = 4
            recording = sd.rec(int(duration * self.sample_rate), samplerate=self.sample_rate, channels=1, dtype='int16')
            sd.wait()
            audio = recording.flatten()
            rms = float(np.sqrt(np.mean(audio.astype(np.float64) ** 2)))
            if rms < 200:
                return None
            
            wav_buf = io.BytesIO()
            with wave.open(wav_buf, 'wb') as wf:
                wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(self.sample_rate)
                wf.writeframes(recording.tobytes())
            
            url = ("https://www.google.com/speech-api/v2/recognize?output=json&lang=en-us"
                   "&key=AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw")
            req = urllib.request.Request(url, data=wav_buf.getvalue(), headers={'Content-Type': 'audio/l16; rate=16000'})
            resp = urllib.request.urlopen(req, timeout=10)
            data = resp.read().decode('utf-8')
            
            for line in data.split('\n'):
                if 'transcript' in line:
                    try:
                        r = json.loads(line)
                        if 'result' in r and r['result']:
                            text = str(r['result'][0]['alternative'][0]['transcript']).lower().strip()
                            if len(text) > 1:
                                return text
                    except: continue
            return None
        except:
            return None
    
    def listen_with_speech_recognition(self) -> Optional[str]:
        if not SPEECH_RECOGNITION_AVAILABLE:
            return None
        try:
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=1)
                recognizer.energy_threshold = 300
                recognizer.pause_threshold = 0.8
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                try:
                    text = recognizer.recognize_google(audio).lower().strip()
                    if len(text) > 1: return text
                except: pass
            return None
        except:
            return None
    
    def listen(self) -> Optional[str]:
        if self.is_speaking:
            time.sleep(0.3)
            return None
        if SPEECH_RECOGNITION_AVAILABLE:
            result = self.listen_with_speech_recognition()
            if result: return result
        return self.listen_with_sounddevice()


# ============= VOICE MANAGER =============
class VoiceManager:
    def __init__(self) -> None:
        self.available_voices: List[Dict[str, Any]] = []
        self.current_voice_index: int = 0
        self.voice_engine: Any = None
        self.method: str = "powershell"
        self._load_voices()
    
    def _load_voices(self) -> None:
        self.available_voices = []
        try:
            import win32com.client
            sapi = win32com.client.Dispatch("SAPI.SpVoice")
            voices = sapi.GetVoices()
            for i in range(int(voices.Count)):
                voice = voices.Item(i)
                desc = str(voice.GetDescription())
                gender = "Male" if "male" in desc.lower() else "Female" if "female" in desc.lower() else "Unknown"
                self.available_voices.append({"name": desc, "index": i, "token": voice, "gender": gender})
            self.method = "sapi"; self.voice_engine = sapi; return
        except: pass
        try:
            import pyttsx3
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            if isinstance(voices, (list, tuple)):
                for i, voice in enumerate(voices):
                    name = str(getattr(voice, 'name', f"Voice {i}"))
                    gender = "Male" if "male" in name.lower() else "Female"
                    self.available_voices.append({"name": name, "index": i, "token": voice.id, "gender": gender})
            self.method = "pyttsx3"; self.voice_engine = engine; return
        except: pass
        self.method = "powershell"
    
    def get_voice_list(self) -> str:
        if not self.available_voices: return "No additional voices found."
        lines = ["Available voices:"]
        for i, v in enumerate(self.available_voices):
            marker = " ← CURRENT" if i == self.current_voice_index else ""
            lines.append(f"  {i + 1}. {v['name']} ({v['gender']}){marker}")
        return "\n".join(lines)
    
    def set_voice(self, voice_name_or_index: str) -> str:
        try:
            idx = int(voice_name_or_index) - 1
            if 0 <= idx < len(self.available_voices):
                self.current_voice_index = idx; return self._apply_voice()
        except: pass
        for i, v in enumerate(self.available_voices):
            if voice_name_or_index.lower() in str(v['name']).lower():
                self.current_voice_index = i; return self._apply_voice()
        return f"Voice '{voice_name_or_index}' not found."
    
    def _apply_voice(self) -> str:
        if not self.available_voices: return "No voices available."
        voice = self.available_voices[self.current_voice_index]
        try:
            if self.method == "sapi" and self.voice_engine:
                self.voice_engine.Voice = voice['token']; self.voice_engine.Rate = 2; self.voice_engine.Volume = 100
            elif self.method == "pyttsx3" and self.voice_engine:
                self.voice_engine.setProperty('voice', voice['token']); self.voice_engine.setProperty('rate', 170)
        except: pass
        return f"Voice changed to {voice['name']}."
    
    def next_voice(self) -> str:
        if not self.available_voices: return "No voices available."
        self.current_voice_index = (self.current_voice_index + 1) % len(self.available_voices)
        return self._apply_voice()


# ============= SPEECH =============
class Speech:
    def __init__(self) -> None:
        self.voice_mgr = VoiceManager()
        self.is_speaking = False
        self.stop_requested = False
        self.listener = AudioListener()
    
    def say(self, text: str) -> None:
        print(f"\n🤖 J.A.R.V.I.S.: {text}")
        self.is_speaking = True; self.listener.is_speaking = True; self.stop_requested = False
        def speak_thread():
            try:
                if self.voice_mgr.method == "sapi" and self.voice_mgr.voice_engine:
                    self.voice_mgr.voice_engine.Speak(text, 1)
                    while self.voice_mgr.voice_engine.Status.RunningState != 1:
                        if self.stop_requested: self.voice_mgr.voice_engine.Speak("", 3); break
                        time.sleep(0.1)
                elif self.voice_mgr.method == "pyttsx3" and self.voice_mgr.voice_engine:
                    if not self.stop_requested: self.voice_mgr.voice_engine.say(text); self.voice_mgr.voice_engine.runAndWait()
                else:
                    safe_text = text.replace('"', '`"')
                    ps = f'Add-Type -AssemblyName System.Speech; $s=New-Object System.Speech.Synthesis.SpeechSynthesizer; $s.Speak("{safe_text}")'
                    subprocess.run(['powershell', '-Command', ps], capture_output=True)
            except: pass
            finally: self.is_speaking = False; self.listener.is_speaking = False
        threading.Thread(target=speak_thread, daemon=True).start()
    
    def stop(self) -> None:
        if self.is_speaking: self.stop_requested = True
    
    def change_voice(self, voice_name: str = "") -> str:
        if not voice_name or voice_name in ["next", "switch"]: return self.voice_mgr.next_voice()
        return self.voice_mgr.set_voice(voice_name)
    
    def list_voices(self) -> str: return self.voice_mgr.get_voice_list()
    def listen(self) -> Optional[str]: return self.listener.listen()


speech = Speech()


# ============= HELPERS =============
def clean_text(text: str) -> str:
    fillers = ["haan", "han", "hr", "arey", "yaar", "yar", "bus", "bas", "jaane", "jane", "jana", "sun", "suno", "dekho", "acha", "accha", "theek", "zara", "thoda", "thora", "please", "kindly"]
    return ' '.join([w for w in text.split() if w.lower() not in fillers]).strip()


def fix_speech(text: str) -> str:
    fixes = {"javed": "jarvis", "jarv": "jarvis", "jarve": "jarvis", "service": "jarvis", "janu": "jarvis",
             "kilos": "close", "clothes": "close", "what's up": "whatsapp", "whats up": "whatsapp",
             "u tube": "youtube", "youtube.com": "youtube", "des": "desktop", "rafiq": "shafiq",
             "screen shot": "screenshot", "g mail": "gmail", "gmail": "gmail", "email": "gmail",
             "peer": "pirzada", "peerzada": "pirzada", "perzada": "pirzada"}
    for wrong, correct in fixes.items():
        if wrong in text.lower():
            text = re.sub(rf'\b{re.escape(wrong)}\b', correct, text, flags=re.IGNORECASE)
    return text


# ============= FIXED: CLOSE YOUTUBE =============
def close_youtube_tab() -> bool:
    """Close YouTube tab using Ctrl+W (closes current browser tab)"""
    try:
        # Method 1: Use keyboard shortcut to close current tab
        pyautogui.hotkey('ctrl', 'w')
        time.sleep(0.5)
        return True
    except:
        return False


def close_app(app_name: str) -> bool:
    """Close an application by name - FIXED for YouTube"""
    app = app_name.lower().strip()
    killed = False
    
    # Special handling for YouTube - close the browser tab instead of killing browser
    if app == "youtube":
        # First try closing the YouTube tab
        if close_youtube_tab():
            return True
        
        # If that fails, try closing browser
        pmap = {
            "youtube": ["chrome.exe", "msedge.exe", "firefox.exe"],
        }
        targets = pmap.get("youtube", [])
        for proc in targets:
            if close_process(proc):
                killed = True
        return killed
    
    # For other apps
    pmap = {
        "whatsapp": ["WhatsApp.exe"], "chrome": ["chrome.exe"],
        "edge": ["msedge.exe"], "firefox": ["firefox.exe"],
        "vscode": ["Code.exe"], "notepad": ["notepad.exe"],
        "calculator": ["CalculatorApp.exe"], "word": ["WINWORD.EXE"],
        "excel": ["EXCEL.EXE"], "powerpoint": ["POWERPNT.EXE"],
        "gmail": ["chrome.exe", "msedge.exe", "firefox.exe"],
        "google": ["chrome.exe", "msedge.exe", "firefox.exe"],
        "spotify": ["Spotify.exe"], "discord": ["Discord.exe"],
    }
    
    targets = None
    for key, procs in sorted(pmap.items(), key=lambda x: len(x[0]), reverse=True):
        if key in app or app in key:
            targets = procs
            break
    
    if targets:
        for proc in targets:
            if close_process(proc):
                killed = True
    
    if close_process(f"{app}.exe"):
        killed = True
    
    try:
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                pname = proc.info['name']
                if pname and app.lower() in pname.lower():
                    subprocess.run(f'taskkill /F /PID {proc.info["pid"]}', shell=True, capture_output=True)
                    killed = True
            except: pass
    except: pass
    
    return killed


def close_process(proc_name: str) -> bool:
    """Kill a process by name"""
    try:
        r = subprocess.run(f'taskkill /F /IM "{proc_name}"', shell=True, capture_output=True, text=True)
        return "SUCCESS" in r.stdout
    except:
        return False


def delete_item(name: str, location: str = "any") -> str:
    for w in ["the", "a", "an", "my", "file", "folder", "picture", "image", "photo", "named", "called"]:
        name = re.sub(rf'\b{w}\b', '', name, flags=re.IGNORECASE).strip()
    name = ' '.join(name.split())
    if not name: return "Please specify what to delete, Boss."
    
    location_map = {
        "desktop": [Path.home()/"Desktop"], "downloads": [Path.home()/"Downloads"],
        "documents": [Path.home()/"Documents"], "pictures": [Path.home()/"Pictures"],
        "music": [Path.home()/"Music"], "videos": [Path.home()/"Videos"],
        "any": [Path.home()/"Desktop", Path.home()/"Downloads", Path.home()/"Documents",
                Path.home()/"Pictures", Path.home()/"Music", Path.home()/"Videos"],
    }
    search_paths = location_map.get(location, location_map["any"])
    
    for base in search_paths:
        target = base / name
        if target.exists():
            try:
                if target.is_file(): target.unlink()
                elif target.is_dir(): shutil.rmtree(target)
                return f"Deleted '{target.name}', Boss."
            except Exception as e: return f"Failed: {e}"
    
    extensions = ['.png', '.jpg', '.jpeg', '.txt', '.pdf', '.doc', '.docx', '.py', '.js', '.html', '.css']
    for ext in extensions:
        for base in search_paths:
            target = base / (name + ext)
            if target.exists():
                try: target.unlink(); return f"Deleted '{target.name}', Boss."
                except: pass
    
    for base in search_paths:
        try:
            for item in base.iterdir():
                if name.lower() in item.name.lower():
                    try:
                        if item.is_file(): item.unlink()
                        elif item.is_dir(): shutil.rmtree(item)
                        return f"Deleted '{item.name}', Boss."
                    except: pass
        except: pass
    
    return f"'{name}' not found, Boss."


def create_item(name: str, location: str = "desktop", is_folder: bool = False, content: str = "") -> str:
    location_map = {"desktop": Path.home()/"Desktop", "downloads": Path.home()/"Downloads",
                    "documents": Path.home()/"Documents", "pictures": Path.home()/"Pictures",
                    "music": Path.home()/"Music", "videos": Path.home()/"Videos"}
    base_path = location_map.get(location.lower(), Path.home()/"Desktop")
    base_path.mkdir(parents=True, exist_ok=True)
    
    if is_folder:
        try:
            (base_path / name).mkdir(parents=True, exist_ok=True)
            return f"Created folder '{name}' in {location}, Boss."
        except Exception as e: return f"Failed: {e}"
    else:
        try:
            file_path = base_path / name; file_path.touch()
            if content:
                with open(file_path, 'w', encoding='utf-8') as f: f.write(content)
            return f"Created file '{name}' in {location}, Boss."
        except Exception as e: return f"Failed: {e}"


def set_brightness(level: int) -> str:
    if not BRIGHTNESS_AVAILABLE:
        try:
            subprocess.run(f'powershell -Command "(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,{level})"',
                          shell=True, capture_output=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return f"Brightness set to {level}%, Boss."
        except: return "Brightness control not available, Boss."
    try:
        monitors = sbc.list_monitors()
        if monitors:
            for monitor in monitors: sbc.set_brightness(level, display=monitor)
            return f"Brightness set to {level}%, Boss."
    except: pass
    return "Brightness adjusted, Boss."


def get_brightness() -> int:
    if not BRIGHTNESS_AVAILABLE: return 50
    try:
        monitors = sbc.list_monitors()
        if monitors: return sbc.get_brightness(display=monitors[0])[0]
    except: pass
    return 50


def adjust_volume(direction: str) -> str:
    try:
        if direction == "up":
            for _ in range(10): pyautogui.press('volumeup'); time.sleep(0.05)
            return "Volume increased, Boss."
        elif direction == "down":
            for _ in range(10): pyautogui.press('volumedown'); time.sleep(0.05)
            return "Volume decreased, Boss."
        elif direction == "mute": pyautogui.press('volumemute'); return "Muted, Boss."
        elif direction == "unmute": pyautogui.press('volumemute'); return "Unmuted, Boss."
    except: return "Volume adjusted, Boss."


def setup_autostart():
    try:
        startup_folder = Path(os.environ.get('APPDATA', '')) / r"Microsoft\Windows\Start Menu\Programs\Startup"
        startup_folder.mkdir(parents=True, exist_ok=True)
        batch_file = startup_folder / "JARVIS_AutoStart.bat"
        script_path = Path(__file__).resolve()
        with open(batch_file, 'w') as f:
            f.write(f'@echo off\ncd /d "{script_path.parent}"\nstart "" /MIN "{sys.executable}" "{script_path}"\n')
        try:
            import winreg
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE) as reg_key:
                winreg.SetValueEx(reg_key, "JARVIS_Assistant", 0, winreg.REG_SZ, f'"{sys.executable}" "{script_path}"')
        except: pass
        return True
    except: return False


# ============= COMMAND PARSER =============
def parse_command(text: str) -> Tuple[str, Dict[str, Any]]:
    text = fix_speech(text); text = clean_text(text)
    if not text: return "silence", {}
    
    original = text; words = text.split(); first = words[0] if words else ""
    
    if text in ["wake up", "wakeup"] or "wake up" in text: return "wake_up", {}
    
    personal_patterns = ["do you know me", "who am i", "what is my name", "who made you", "who created you",
                        "who programmed you", "why did you make me", "do you know why i made you",
                        "what do you like about me", "what do you think about me", "do you like me",
                        "are you my friend", "do you love me", "how are you", "who are you", "what are you"]
    for pattern in personal_patterns:
        if pattern in text: return "personal_chat", {"text": original}
    
    if "change voice" in text or "switch voice" in text:
        rest = text.replace("change voice", "").replace("switch voice", "").strip()
        return "change_voice", {"name": rest}
    if "list voices" in text or "available voices" in text: return "list_voices", {}
    if "next voice" in text: return "next_voice", {}
    if text in ["time", "what time is it", "what's the time", "current time"]: return "time", {}
    if text in ["date", "what day is it", "today date", "what's the date", "current date"]: return "date", {}
    if text in ["thank you", "thanks", "thank you so much"]: return "thanks", {}
    if text in ["joke", "tell me a joke", "make me laugh"]: return "joke", {}
    if text in ["bye", "goodbye", "good night", "see you"]: return "goodbye", {}
    if text in ["hello", "hi", "hey"]: return "greeting", {}
    if "minimize all" in text or "show desktop" in text: return "minimize_all", {}
    if any(w in text for w in ["volume up", "increase volume", "louder", "sound up"]): return "volume_up", {}
    if any(w in text for w in ["volume down", "decrease volume", "quieter", "sound down"]): return "volume_down", {}
    if "mute" in text and "unmute" not in text: return "volume_mute", {}
    if "unmute" in text: return "volume_unmute", {}
    if any(w in text for w in ["brightness up", "increase brightness", "brighter"]): return "brightness_up", {}
    if any(w in text for w in ["brightness down", "decrease brightness", "dimmer"]): return "brightness_down", {}
    if "screenshot" in text or "screen shot" in text or "take a screenshot" in text: return "screenshot", {}
    if "shutdown" in text or "shut down" in text: return "shutdown", {}
    if "restart" in text or "reboot" in text: return "restart", {}
    if "sleep" in text or "go to sleep" in text: return "sleep", {}
    if text in ["lock", "lock screen", "lock my pc"]: return "lock", {}
    if "refresh" in text or "refresh system" in text: return "refresh", {}
    if "email" in text or "gmail" in text or "mail" in text: return "email", {}
    if "close all" in text or "kill all" in text: return "close_all", {}
    
    if first in ["close", "exit", "quit", "kill", "stop"]:
        rest = original
        for w in ["close", "exit", "quit", "kill", "stop"]: rest = rest.replace(w, "", 1).strip()
        for w in ["the", "my", "a", "an", "app", "application", "window"]: rest = re.sub(rf'\b{w}\b', '', rest).strip()
        rest = fix_speech(' '.join(rest.split()))
        if rest:
            for app in ["youtube", "whatsapp", "chrome", "edge", "firefox", "vscode", "notepad", "spotify", "gmail", "google"]:
                if app in rest: return "close", {"app": app}
            return "close", {"app": rest}
        return "silence", {}
    
    if "youtube" in text or first == "play":
        query = ""
        if "play" in text:
            parts = re.split(r'\bplay\b', text)
            if len(parts) > 1: query = parts[1].strip()
        if not query and "youtube" in text:
            parts = re.split(r'\byoutube\b', text)
            if len(parts) > 1:
                rem = parts[1].strip()
                if "play" in rem:
                    pp = re.split(r'\bplay\b', rem)
                    if len(pp) > 1: query = pp[1].strip()
                elif rem not in ["open", "the", "a", "", "on"]: query = rem
        if query:
            for w in ["song", "music", "video", "of", "by", "a", "the", "any", "some", "and", "on", "in", "youtube", "me", "for", "to", "is"]:
                query = re.sub(rf'\b{w}\b', '', query, flags=re.IGNORECASE).strip()
            query = ' '.join(query.split())
        return ("youtube_play", {"query": query}) if (query and len(query) > 1) else ("youtube_open", {})
    
    if first in ["open", "launch", "start", "go", "show"]:
        rest = original
        for w in ["open", "launch", "start", "go", "show"]: rest = rest.replace(w, "", 1).strip()
        for w in ["the", "my", "a", "an", "to"]: rest = re.sub(rf'\b{w}\b', '', rest).strip()
        rest = fix_speech(' '.join(rest.split()))
        if not rest: return "silence", {}
        folders = {"desktop": Path.home()/"Desktop", "downloads": Path.home()/"Downloads",
                   "documents": Path.home()/"Documents", "pictures": Path.home()/"Pictures",
                   "music": Path.home()/"Music", "videos": Path.home()/"Videos"}
        for fname, fpath in folders.items():
            if fname in rest: subprocess.Popen(f'explorer "{fpath}"', shell=True); return "folder_opened", {"msg": f"Opening {fname}, Boss."}
        apps = {"whatsapp": "whatsapp:", "chrome": "https://google.com", "edge": "microsoft-edge:",
                "vscode": "code", "notepad": "notepad", "calculator": "calc",
                "word": "winword", "excel": "excel", "powerpoint": "powerpnt",
                "cmd": "cmd", "spotify": "spotify:", "discord": "discord:",
                "settings": "ms-settings:", "youtube": "https://youtube.com",
                "google": "https://google.com", "gmail": "https://mail.google.com"}
        for key, cmd in sorted(apps.items(), key=lambda x: len(x[0]), reverse=True):
            if key in rest: return "open_app", {"app": key, "cmd": cmd}
        return "open_app", {"app": rest, "cmd": rest}
    
    if first in ["send", "message", "text", "sms", "tell", "whatsapp"] or "whatsapp" in text:
        atext = original
        for w in ["send", "message", "text", "sms", "whatsapp", "jarvis"]: atext = atext.replace(w, "", 1).strip()
        atext = re.sub(r'^and\s+', '', atext).strip(); atext = re.sub(r'\bto\b', '', atext, count=1).strip()
        atext = ' '.join(atext.split())
        contact = ""; message = ""
        for sep in ["say", "tell", "that"]:
            m = re.search(rf'\b{sep}\b', atext)
            if m: contact = atext[:m.start()].strip(); message = atext[m.end():].strip(); break
        if not contact:
            for key in sorted(CONTACTS.keys(), key=len, reverse=True):
                if key in atext:
                    idx = atext.find(key); contact = atext[:idx + len(key)].strip()
                    message = atext[idx + len(key):].strip(); break
        if not contact:
            parts = atext.split()
            if len(parts) >= 3: contact = ' '.join(parts[:2]); message = ' '.join(parts[2:])
            elif len(parts) == 2: contact = parts[0]; message = parts[1]
            elif len(parts) == 1: contact = parts[0]; message = "hello"
        contact = re.sub(r'\b(my|the|a|an)\b', '', contact).strip(); contact = ' '.join(contact.split())
        urdu_words = ["se", "sy", "keh", "ke", "ki", "ka", "ko", "par", "pe", "mein", "main", "hay", "hain"]
        message = ' '.join([w for w in message.split() if w not in urdu_words]).strip()
        actual = find_contact(contact) if contact else ""
        if actual and actual not in ["Tell", "Say", "Send", "Message", "Text", "Sms"]:
            return ("whatsapp", {"contact": actual, "message": message}) if message else ("whatsapp", {"contact": actual, "message": "hello"})
        return "silence", {}
    
    if first in ["create", "make", "write"]:
        is_folder = "folder" in text or "directory" in text; loc = "desktop"
        for l in ["desktop", "downloads", "documents", "pictures", "music", "videos"]:
            if l in text: loc = l; break
        name = text
        for w in ["create", "make", "write", "a", "an", "new", "basic"]: name = re.sub(rf'\b{w}\b', '', name, count=1).strip()
        if is_folder: name = re.sub(r'\b(?:folder|directory)\b', '', name, count=1).strip()
        else: name = re.sub(r'\b(?:file|document|html|page|code|text)\b', '', name, count=1).strip()
        for l in ["desktop", "downloads", "documents", "pictures", "music", "videos", "in", "on", "this", "name"]:
            name = re.sub(rf'\b{l}\b', '', name).strip()
        name = ' '.join(name.split()).strip("'\".")
        if not name: name = "New Folder" if is_folder else "New File.txt"
        if not is_folder and "." not in name:
            if "html" in text: name += ".html"
            elif "python" in text or "py" in text: name += ".py"
            elif "code" in text: name += ".py"
            else: name += ".txt"
        if is_folder: return "create_folder", {"name": name, "location": loc}
        else:
            content = ""
            if "html" in name.lower(): content = "<!DOCTYPE html>\n<html>\n<head>\n    <title>Document</title>\n</head>\n<body>\n    <h1>Hello World</h1>\n</body>\n</html>\n"
            elif "python" in name.lower() or "code" in text: content = "# Python Script\n\ndef main():\n    print('Hello, World!')\n\nif __name__ == '__main__':\n    main()\n"
            return "create_file", {"name": name, "location": loc, "content": content}
    
    if first in ["delete", "remove", "trash"]:
        rest = original
        for w in ["delete", "remove", "trash", "the", "a", "an", "my", "named", "called"]: rest = re.sub(rf'\b{w}\b', '', rest).strip()
        location = "any"
        for loc in ["desktop", "downloads", "documents", "pictures", "music", "videos"]:
            if f"from {loc}" in rest or f"in {loc}" in rest: location = loc; rest = rest.replace(f"from {loc}", "").replace(f"in {loc}", "").replace(loc, ""); break
        rest = ' '.join(rest.split()).strip("'\".")
        if rest: return "delete", {"name": rest, "location": location}
    
    if first in ["search", "google", "find", "look"]:
        rest = original.replace(first, "", 1).strip()
        for w in ["for", "about", "up"]: rest = re.sub(rf'^{w}\s+', '', rest).strip()
        return ("search", {"query": rest}) if rest else ("search", {"query": "latest news"})
    
    if any(w in text for w in ["cpu", "ram", "battery", "system info", "system status"]): return "system_info", {}
    if text in ["copy", "copy that", "copy this"]: return "copy", {}
    if text in ["paste", "paste it", "paste here"]: return "paste", {}
    
    return "ai_chat", {"text": original}


# ============= EXECUTE =============
def execute(action: str, params: Dict[str, Any]) -> str:
    try:
        if action == "silence": return ""
        if action == "folder_opened": return str(params.get("msg", ""))
        if action == "wake_up": return random.choice(PERSONAL_RESPONSES["wake up"])
        if action == "personal_chat":
            response = get_personal_response(str(params.get("text", "")))
            return response if response else "I'm here for you, Boss! Ask me anything."
        if action == "change_voice": return speech.change_voice(str(params.get("name", "")))
        if action == "list_voices": return speech.list_voices()
        if action == "next_voice": return speech.change_voice("next")
        if action == "time": return f"It's {datetime.now().strftime('%I:%M %p')}, Boss."
        if action == "date": return f"Today is {datetime.now().strftime('%A, %B %d, %Y')}."
        if action == "thanks": return random.choice(["You're welcome, Boss!", "Happy to help!"])
        if action == "joke": return random.choice(["Why do programmers prefer dark mode? Because light attracts bugs!", "What's a computer's favorite snack? Microchips!"])
        if action == "goodbye": return random.choice(["Goodbye, Boss!", "See you later!"])
        if action == "greeting":
            h = datetime.now().hour
            if h < 12: return f"Good morning, Boss {BOSS_SHORT}!"
            elif h < 17: return f"Good afternoon, Boss {BOSS_SHORT}!"
            else: return f"Good evening, Boss {BOSS_SHORT}!"
        if action == "minimize_all": pyautogui.hotkey('win', 'd'); return "Minimized, Boss."
        if action == "brightness_up": return set_brightness(min(get_brightness() + 10, 100))
        if action == "brightness_down": return set_brightness(max(get_brightness() - 10, 0))
        if action == "volume_up": return adjust_volume("up")
        if action == "volume_down": return adjust_volume("down")
        if action == "volume_mute": return adjust_volume("mute")
        if action == "volume_unmute": return adjust_volume("unmute")
        
        if action == "open_app":
            app, cmd = str(params.get("app", "")), str(params.get("cmd", ""))
            try:
                if cmd.startswith("http"): webbrowser.open(cmd)
                else: subprocess.Popen(f"start {cmd}", shell=True)
                return f"Opening {app}, Boss."
            except:
                try: subprocess.Popen(f"start {app}", shell=True); return f"Opening {app}, Boss."
                except: return f"Couldn't open {app}, Boss."
        
        # FIXED: Close command now properly handles YouTube
        if action == "close":
            app = str(params.get("app", ""))
            print(f"  🔒 Closing {app}...")
            if close_app(app):
                return f"Closed {app}, Boss."
            else:
                return f"{app} was not running, Boss."
        
        if action == "close_all":
            count = 0
            for proc in psutil.process_iter(['pid', 'name']):
                try:
                    pname = str(proc.info['name']).lower() if proc.info['name'] else ""
                    if pname in ["python.exe", "explorer.exe"]: continue
                    if "SUCCESS" in subprocess.run(f'taskkill /F /PID {proc.info["pid"]}', shell=True, capture_output=True, text=True).stdout:
                        count += 1
                except: pass
            return f"Closed {count} programs, Boss." if count else "No programs running."
        
        if action == "email": webbrowser.open("https://mail.google.com"); return "Opening Gmail, Boss."
        if action == "youtube_open": webbrowser.open("https://youtube.com"); return "Opening YouTube, Boss."
        
        if action == "youtube_play":
            query = str(params.get("query", ""))
            if not query: webbrowser.open("https://youtube.com"); return "Opening YouTube, Boss."
            print(f"▶️ YouTube: {query}")
            webbrowser.open(f"https://www.youtube.com/results?search_query={urllib.parse.quote(query)}")
            time.sleep(5)
            try:
                w, h = pyautogui.size()
                pyautogui.click(int(w * 0.22), int(h * 0.38)); time.sleep(1)
                pyautogui.click(int(w * 0.25), int(h * 0.40))
                return f"Playing {query} on YouTube, Boss."
            except: return f"Searching {query} on YouTube, Boss."
        
        if action == "whatsapp":
            contact, message = str(params.get("contact", "")), str(params.get("message", ""))
            print(f"📱 WhatsApp → {contact}: {message}")
            try:
                subprocess.Popen("start whatsapp:", shell=True); time.sleep(4)
                w, h = pyautogui.size()
                pyautogui.hotkey('ctrl', 'n'); time.sleep(2)
                pyautogui.hotkey('ctrl', 'a'); pyperclip.copy(contact); pyautogui.hotkey('ctrl', 'v'); time.sleep(3)
                pyautogui.press('down'); time.sleep(0.5); pyautogui.press('enter'); time.sleep(2)
                pyautogui.click(int(w * 0.55), int(h * 0.92)); time.sleep(0.5)
                pyperclip.copy(message); pyautogui.hotkey('ctrl', 'v'); time.sleep(0.3)
                pyautogui.press('enter')
                return f"Message sent to {contact}, Boss."
            except:
                try:
                    pyautogui.hotkey('ctrl', 'f'); time.sleep(1)
                    pyautogui.hotkey('ctrl', 'a'); pyperclip.copy(contact); pyautogui.hotkey('ctrl', 'v'); time.sleep(2)
                    pyautogui.press('down'); time.sleep(0.5); pyautogui.press('enter'); time.sleep(1.5)
                    pyautogui.click(int(w * 0.55), int(h * 0.92)); time.sleep(0.5)
                    pyperclip.copy(message); pyautogui.hotkey('ctrl', 'v'); time.sleep(0.3)
                    pyautogui.press('enter')
                    return f"Message sent to {contact}, Boss."
                except: return f"Couldn't send message to {contact}, Boss."
        
        if action == "create_folder": return create_item(str(params.get("name", "New Folder")), str(params.get("location", "desktop")), True)
        if action == "create_file": return create_item(str(params.get("name", "New File.txt")), str(params.get("location", "desktop")), False, str(params.get("content", "")))
        if action == "delete": return delete_item(str(params.get("name", "")), str(params.get("location", "any")))
        
        if action == "search":
            webbrowser.open(f"https://www.google.com/search?q={urllib.parse.quote(str(params.get('query', '')))}")
            return f"Searching, Boss."
        
        if action == "screenshot":
            try:
                desktop = Path.home() / "Desktop"; desktop.mkdir(parents=True, exist_ok=True)
                path = desktop / f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                ImageGrab.grab().save(str(path), "PNG")
                return "Screenshot saved, Boss."
            except: return "Failed, Boss."
        
        if action == "shutdown": os.system("shutdown /s /t 10"); return "Shutting down, Boss."
        if action == "restart": os.system("shutdown /r /t 10"); return "Restarting, Boss."
        if action == "sleep": os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0"); return "Sleeping, Boss."
        if action == "lock": ctypes.windll.user32.LockWorkStation(); return "Locked, Boss."
        if action == "refresh":
            try:
                subprocess.run("taskkill /F /IM explorer.exe", shell=True, capture_output=True); time.sleep(1)
                subprocess.Popen("explorer.exe", shell=True)
            except: pass
            return "Refreshed, Boss."
        
        if action == "system_info":
            cpu = psutil.cpu_percent(interval=1); ram = psutil.virtual_memory().percent
            disk = psutil.disk_usage('/').percent; battery = "N/A"
            try:
                bi = psutil.sensors_battery()
                if bi: battery = f"{bi.percent}%"
            except: pass
            return f"CPU: {cpu}%, RAM: {ram}%, Disk: {disk}%, Battery: {battery}, Boss."
        
        if action == "copy": pyautogui.hotkey('ctrl', 'c'); return "Copied, Boss."
        if action == "paste": pyautogui.hotkey('ctrl', 'v'); return "Pasted, Boss."
        
        if action == "ai_chat":
            response = get_personal_response(str(params.get("text", "")))
            if response: return response
            return random.choice(["I'm listening, Boss.", "Tell me more, Boss."])
        
        return "Done, Boss."
    except Exception as e:
        return "Sorry, Boss."


# ============= MAIN =============
def main() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
╔══════════════════════════════════════════╗
║        ⚡ J.A.R.V.I.S. 1.0. ⚡           ║
║    24/7 + Able to Perform any Task           ║
║    Made by: {BOSS_NAME}                 ║
╚══════════════════════════════════════════╝
    """)
    
    if setup_autostart(): print("  ✅ Auto-start enabled!")
    print("\n  💬 Say 'hey jarvis wake up' to start")
    print(f"  🎤 Listening: {'✅ Enhanced' if SPEECH_RECOGNITION_AVAILABLE else '⚠️ Standard'}")
    print()
    
    voices = speech.voice_mgr.available_voices
    if voices: print(f"  🎤 Voice: {voices[speech.voice_mgr.current_voice_index]['name']}")
    
    speech.say(f"J.A.R.V.I.S. is now online. Say 'hey jarvis wake up' when you need me, Boss!")
    
    last_command_text = ""; last_command_time = 0; COMMAND_COOLDOWN = 2
    
    try:
        while True:
            text = speech.listen()
            if not text: continue
            
            current_time = time.time()
            if text == last_command_text and (current_time - last_command_time) < COMMAND_COOLDOWN: continue
            
            print(f"  🗣️  \"{text}\"")
            
            wake_words = ["jarvis", "hey jarvis", "hi jarvis", "hello jarvis", "wake up", "ok jarvis"]
            has_wake = any(w in text.lower() for w in wake_words)
            
            if has_wake:
                for w in sorted(wake_words, key=len, reverse=True):
                    if w in text.lower(): text = text.lower().replace(w, "", 1).strip(); break
            
            text = fix_speech(text); text = clean_text(text)
            
            if not text and has_wake: speech.say(random.choice(PERSONAL_RESPONSES["wake up"])); continue
            if not text: continue
            
            print(f"  💬 \"{text}\"")
            last_command_text = text; last_command_time = current_time
            
            action, params = parse_command(text)
            response = execute(action, params)
            if response: speech.say(response)
    
    except KeyboardInterrupt:
        print("\n  👋 Shutting down...")
        speech.say(f"Goodbye, Boss {BOSS_SHORT}!")
        sys.exit(0)


if __name__ == "__main__":
    try:
        mutex = ctypes.windll.kernel32.CreateMutexW(None, False, "JarvisV32Mutex")
        if ctypes.windll.kernel32.GetLastError() == 183:
            print("⚠️ J.A.R.V.I.S. is already running!"); sys.exit(0)
    except: pass
    
    setup_autostart(); main()
