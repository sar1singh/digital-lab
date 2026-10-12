import os
import subprocess
from pathlib import Path

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
BASE_DIR = Path(r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\scuff-sensei\brand")
BASE_DIR.mkdir(parents=True, exist_ok=True)

# 1. HTML Template for Avatar (800x800) — Pure English / Clean Cyber Tactical
avatar_html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@800;900&family=Rajdhani:wght@700;800&display=swap');
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 800px;
    height: 800px;
    background: radial-gradient(circle at 50% 45%, #151D2F 0%, #0A0E17 75%, #05070B 100%);
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    position: relative;
    font-family: 'Orbitron', sans-serif;
  }
  
  .grid {
    position: absolute;
    inset: 0;
    background-image: 
      linear-gradient(rgba(0, 240, 255, 0.06) 1px, transparent 1px),
      linear-gradient(90deg, rgba(0, 240, 255, 0.06) 1px, transparent 1px);
    background-size: 32px 32px;
  }
  
  .glow-ring {
    position: absolute;
    width: 680px;
    height: 680px;
    border-radius: 50%;
    border: 2px dashed rgba(0, 240, 255, 0.4);
  }
  
  .inner-ring {
    position: absolute;
    width: 610px;
    height: 610px;
    border-radius: 50%;
    border: 3px solid rgba(245, 158, 11, 0.6);
    box-shadow: 0 0 60px rgba(0, 240, 255, 0.3), inset 0 0 50px rgba(245, 158, 11, 0.2);
  }

  .badge-container {
    position: relative;
    z-index: 10;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  .top-label {
    font-size: 20px;
    color: #F59E0B;
    text-shadow: 0 0 20px rgba(245, 158, 11, 0.9);
    letter-spacing: 10px;
    margin-bottom: 2px;
    font-family: 'Rajdhani', sans-serif;
    font-weight: 800;
  }

  .emblem {
    width: 300px;
    height: 300px;
    position: relative;
    margin: 4px 0;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .headset-arch {
    position: absolute;
    width: 270px;
    height: 200px;
    border: 15px solid #00F0FF;
    border-bottom: none;
    border-radius: 150px 150px 0 0;
    top: 20px;
    box-shadow: 0 -5px 30px rgba(0, 240, 255, 0.7);
  }

  .earcup-l, .earcup-r {
    position: absolute;
    width: 44px;
    height: 105px;
    background: #0F172A;
    border: 4px solid #F59E0B;
    border-radius: 18px;
    box-shadow: 0 0 25px rgba(245, 158, 11, 0.6);
    top: 100px;
  }
  .earcup-l { left: 8px; transform: rotate(-5deg); }
  .earcup-r { right: 8px; transform: rotate(5deg); }

  .mask {
    position: absolute;
    width: 190px;
    height: 155px;
    background: linear-gradient(180deg, #1E293B 0%, #0B1120 100%);
    border: 4px solid #00F0FF;
    clip-path: polygon(15% 0%, 85% 0%, 100% 70%, 50% 100%, 0% 70%);
    top: 92px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.9);
  }

  .visor {
    width: 140px;
    height: 42px;
    background: #00F0FF;
    border-radius: 8px;
    box-shadow: 0 0 30px #00F0FF;
    position: relative;
    overflow: hidden;
  }

  .crack {
    position: absolute;
    width: 4px;
    height: 48px;
    background: #0B1120;
    left: 52px;
    top: -5px;
    transform: rotate(25deg);
  }
  .crack::after {
    content: '';
    position: absolute;
    width: 22px;
    height: 4px;
    background: #0B1120;
    top: 20px;
    left: 0;
    transform: rotate(-45deg);
  }

  .monogram {
    font-size: 72px;
    font-weight: 900;
    color: #FFFFFF;
    letter-spacing: 5px;
    text-shadow: 0 0 35px rgba(0, 240, 255, 0.9), 0 5px 15px rgba(0,0,0,0.9);
    margin-top: 10px;
  }

  .sub-tag {
    font-family: 'Rajdhani', sans-serif;
    font-size: 30px;
    font-weight: 800;
    color: #F59E0B;
    letter-spacing: 14px;
    text-transform: uppercase;
    text-shadow: 0 0 20px rgba(245, 158, 11, 0.7);
    margin-top: 2px;
  }
</style>
</head>
<body>
  <div class="grid"></div>
  <div class="glow-ring"></div>
  <div class="inner-ring"></div>
  
  <div class="badge-container">
    <div class="top-label">// UNFILTERED //</div>
    <div class="emblem">
      <div class="headset-arch"></div>
      <div class="earcup-l"></div>
      <div class="earcup-r"></div>
      <div class="mask">
        <div class="visor">
          <div class="crack"></div>
        </div>
      </div>
    </div>
    <div class="monogram">SCUFF</div>
    <div class="sub-tag">SENSEI</div>
  </div>
</body>
</html>"""

# 2. Enhanced Banner Template (2560x1440) — Pure English / Clean Cyber
banner_html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@800;900&family=Rajdhani:wght@600;700;800&family=Space+Grotesk:wght@500;700&display=swap');
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 2560px;
    height: 1440px;
    background: #06090F;
    overflow: hidden;
    position: relative;
    font-family: 'Orbitron', sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .bg-glow-center {
    position: absolute;
    width: 1800px;
    height: 900px;
    background: radial-gradient(ellipse at 50% 50%, rgba(0, 240, 255, 0.16) 0%, rgba(245, 158, 11, 0.08) 45%, transparent 70%);
  }

  .grid-pattern {
    position: absolute;
    inset: 0;
    background-image: 
      linear-gradient(rgba(0, 240, 255, 0.04) 1px, transparent 1px),
      linear-gradient(90deg, rgba(0, 240, 255, 0.04) 1px, transparent 1px);
    background-size: 50px 50px;
  }

  .laser-bar-top {
    position: absolute;
    top: 508px;
    left: 0;
    right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent 5%, rgba(0, 240, 255, 0.5) 25%, rgba(245, 158, 11, 0.6) 75%, transparent 95%);
    box-shadow: 0 0 15px rgba(0, 240, 255, 0.4);
  }
  .laser-bar-bottom {
    position: absolute;
    top: 931px;
    left: 0;
    right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent 5%, rgba(245, 158, 11, 0.5) 25%, rgba(0, 240, 255, 0.6) 75%, transparent 95%);
    box-shadow: 0 0 15px rgba(245, 158, 11, 0.4);
  }

  /* Safe Area (1546 x 423 px) Centered Exactly */
  .safe-area {
    width: 1546px;
    height: 423px;
    position: relative;
    z-index: 10;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 30px;
  }

  /* Left Side: Avatar / Mascot Crest */
  .hero-crest {
    display: flex;
    align-items: center;
    gap: 40px;
  }

  .crest-box {
    width: 240px;
    height: 240px;
    border-radius: 40px;
    background: linear-gradient(135deg, rgba(20, 30, 48, 0.95) 0%, rgba(10, 16, 28, 0.98) 100%);
    border: 3px solid rgba(0, 240, 255, 0.7);
    box-shadow: 0 0 70px rgba(0, 240, 255, 0.4), inset 0 0 40px rgba(0, 240, 255, 0.2);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    position: relative;
    flex-shrink: 0;
  }

  .crest-top-tag {
    font-family: 'Rajdhani', sans-serif;
    font-size: 20px;
    font-weight: 800;
    color: #F59E0B;
    letter-spacing: 5px;
    text-shadow: 0 0 15px rgba(245, 158, 11, 0.8);
    margin-bottom: 2px;
  }

  .crest-initials {
    font-size: 96px;
    font-weight: 900;
    color: #FFFFFF;
    text-shadow: 0 0 35px rgba(0, 240, 255, 1);
    letter-spacing: 4px;
    line-height: 0.95;
  }

  /* Brand Typography */
  .brand-text-col {
    display: flex;
    flex-direction: column;
  }

  .tag-sup {
    font-family: 'Rajdhani', sans-serif;
    font-size: 26px;
    font-weight: 800;
    color: #00F0FF;
    letter-spacing: 10px;
    text-transform: uppercase;
    margin-bottom: 4px;
    display: flex;
    align-items: center;
    gap: 14px;
    text-shadow: 0 0 15px rgba(0, 240, 255, 0.6);
  }
  .tag-sup::before {
    content: '';
    display: inline-block;
    width: 14px;
    height: 14px;
    background: #F59E0B;
    border-radius: 50%;
    box-shadow: 0 0 15px #F59E0B;
  }

  .main-title {
    font-size: 105px;
    font-weight: 900;
    color: #FFFFFF;
    line-height: 0.95;
    letter-spacing: 4px;
    text-shadow: 0 0 50px rgba(0, 240, 255, 0.5), 0 8px 25px rgba(0,0,0,0.9);
  }

  .main-title span {
    color: #F59E0B;
    text-shadow: 0 0 45px rgba(245, 158, 11, 0.7);
  }

  .subtitle {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 25px;
    font-weight: 600;
    color: #CBD5E1;
    margin-top: 16px;
    letter-spacing: 2px;
  }

  /* Right Side Tactical Badges */
  .meta-pills {
    display: flex;
    flex-direction: column;
    gap: 14px;
    align-items: flex-end;
    flex-shrink: 0;
  }

  .pill {
    padding: 12px 26px;
    background: rgba(15, 23, 42, 0.9);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 30px;
    font-family: 'Rajdhani', sans-serif;
    font-size: 21px;
    font-weight: 800;
    color: #F1F5F9;
    letter-spacing: 3px;
    display: flex;
    align-items: center;
    gap: 12px;
    box-shadow: 0 6px 25px rgba(0,0,0,0.6);
  }

  .pill-accent {
    border-color: rgba(0, 240, 255, 0.5);
    color: #00F0FF;
    background: rgba(0, 240, 255, 0.12);
    box-shadow: 0 0 20px rgba(0, 240, 255, 0.25);
  }
  .pill-gold {
    border-color: rgba(245, 158, 11, 0.5);
    color: #F59E0B;
    background: rgba(245, 158, 11, 0.12);
    box-shadow: 0 0 20px rgba(245, 158, 11, 0.25);
  }
</style>
</head>
<body>
  <div class="grid-pattern"></div>
  <div class="bg-glow-center"></div>
  <div class="laser-bar-top"></div>
  <div class="laser-bar-bottom"></div>

  <div class="safe-area">
    <div class="hero-crest">
      <div class="crest-box">
        <div class="crest-top-tag">TACTICAL</div>
        <div class="crest-initials">SS</div>
      </div>
      <div class="brand-text-col">
        <div class="tag-sup">The Unscripted Journey</div>
        <div class="main-title">SCUFF <span>SENSEI</span></div>
        <div class="subtitle">UNPOLISHED PC WALKTHROUGHS · ZERO SWEAT · PURE BACKLOG</div>
      </div>
    </div>

    <div class="meta-pills">
      <div class="pill pill-accent">● 4K 60FPS MASTER PC</div>
      <div class="pill pill-gold">● THE LAST OF US · RDR 2</div>
      <div class="pill">● ZERO EDITING · RAW ACTION</div>
    </div>
  </div>
</body>
</html>"""

# Write HTML files
avatar_html_path = BASE_DIR / "avatar.html"
banner_html_path = BASE_DIR / "banner.html"
avatar_html_path.write_text(avatar_html, encoding="utf-8")
banner_html_path.write_text(banner_html, encoding="utf-8")

# Generate Avatar PNG
avatar_png = BASE_DIR / "avatar.png"
subprocess.run([
    CHROME,
    "--headless=new",
    f"--screenshot={avatar_png}",
    "--window-size=800,800",
    "--hide-scrollbars",
    str(avatar_html_path)
], check=True)

# Generate Banner PNG
banner_png = BASE_DIR / "banner.png"
subprocess.run([
    CHROME,
    "--headless=new",
    f"--screenshot={banner_png}",
    "--window-size=2560,1440",
    "--hide-scrollbars",
    str(banner_html_path)
], check=True)

print("Generated Avatar (Pure English):", avatar_png, avatar_png.stat().st_size)
print("Generated Banner (Pure English):", banner_png, banner_png.stat().st_size)
