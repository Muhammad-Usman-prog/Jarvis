Dim WshShell
Set WshShell = CreateObject("WScript.Shell")
WshShell.CurrentDirectory = "C:\Users\Muhammad usman\Desktop\My Jarvis"
WshShell.Run "pythonw main.py", 0, False
Set WshShell = Nothing
