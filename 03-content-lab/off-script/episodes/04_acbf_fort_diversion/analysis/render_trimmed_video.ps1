# Off Script Episode 04 — Headless 1-Click Audio & Video Render Script
# Uses pythonw.exe + CREATE_NO_WINDOW (0x08000000) so zero CLI windows pop up on screen.

$ErrorActionPreference = "Stop"
$PythonW = "C:\Users\sar1s\AppData\Local\Programs\Python\Python312\pythonw.exe"
$TrimScript = "c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\off-script\episodes\04_acbf_fort_diversion\trim_timeline.py"
$LogFile = "c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\off-script\episodes\04_acbf_fort_diversion\analysis\render_headless.log"

# Launch full synced audio + NVENC CQP 21 video trim in hidden background mode
Start-Process -FilePath $PythonW `
    -ArgumentList "`"$TrimScript`" --render-video" `
    -WindowStyle Hidden `
    -RedirectStandardOutput $LogFile `
    -RedirectStandardError "$LogFile.err"
