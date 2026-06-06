' start_jarvis_hidden.vbs
' Runs Jarvis silently in background on Windows startup

Dim WshShell
Set WshShell = CreateObject("WScript.Shell")

' Hide the console window
WshShell.Run "pythonw ""C:\Users\Muhammad usman\Desktop\My Jarvis\main.py""", 0, False

Set WshShell = Nothing