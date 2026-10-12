import os
import subprocess
from pathlib import Path

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
BASE_DIR = Path(r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\scuff-sensei\brand")
BASE_DIR.mkdir(parents=True, exist_ok=True)

# HTML Template for Watermark (150x150) — Pure English Tactical SS
watermark_html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@900&family=Rajdhani:wght@800&display=swap');
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 150px;
    height: 150px;
    background: transparent;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
  }
  .box {
    width: 140px;
    height: 140px;
    border-radius: 28px;
    background: rgba(10, 16, 28, 0.95);
    border: 3px solid #00F0FF;
    box-shadow: 0 0 20px rgba(0, 240, 255, 0.6);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    font-family: 'Orbitron', sans-serif;
  }
  .top-tag {
    font-family: 'Rajdhani', sans-serif;
    font-size: 16px;
    font-weight: 800;
    color: #F59E0B;
    letter-spacing: 3px;
    margin-bottom: -2px;
  }
  .ss {
    font-size: 56px;
    font-weight: 900;
    color: #FFFFFF;
    text-shadow: 0 0 15px #00F0FF;
    line-height: 1;
  }
</style>
</head>
<body>
  <div class="box">
    <div class="top-tag">SCUFF</div>
    <div class="ss">SS</div>
  </div>
</body>
</html>"""

watermark_html_path = BASE_DIR / "watermark.html"
watermark_html_path.write_text(watermark_html, encoding="utf-8")

watermark_png = BASE_DIR / "watermark.png"
subprocess.run([
    CHROME,
    "--headless=new",
    f"--screenshot={watermark_png}",
    "--window-size=150,150",
    "--default-background-color=00000000",
    "--hide-scrollbars",
    str(watermark_html_path)
], check=True)

print("Generated Watermark (Pure English):", watermark_png, watermark_png.stat().st_size)
