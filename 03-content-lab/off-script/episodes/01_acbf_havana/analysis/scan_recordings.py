import subprocess
import json
from pathlib import Path

def probe(file):
    cmd = [
        'ffprobe', '-v', 'quiet', '-print_format', 'json',
        '-show_format', '-show_streams', file
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, creationflags=0x08000000)
    data = json.loads(res.stdout)
    fmt = data.get('format', {})
    dur = float(fmt.get('duration', 0))
    size = int(fmt.get('size', 0))
    print(f"File: {file}")
    print(f"Duration: {dur:.2f}s ({dur/60:.2f} mins)")
    print(f"Size: {size / (1024**3):.2f} GB")
    for s in data.get('streams', []):
        codec_type = s.get('codec_type')
        codec_name = s.get('codec_name')
        if codec_type == 'video':
            print(f"  Stream #{s.get('index')}: video {codec_name} {s.get('width')}x{s.get('height')} @ {s.get('r_frame_rate')} fps")
        elif codec_type == 'audio':
            print(f"  Stream #{s.get('index')}: audio {codec_name} {s.get('sample_rate')}Hz channels={s.get('channels')}")

if __name__ == '__main__':
    probe(r'C:\Users\sar1s\Videos\obs\2026-10-14 00-45-18.mkv')
    print('-' * 50)
    probe(r'C:\Users\sar1s\Videos\obs\2026-10-14 21-06-11.mkv')
