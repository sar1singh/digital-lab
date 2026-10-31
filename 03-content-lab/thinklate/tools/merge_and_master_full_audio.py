import subprocess

# We will concatenate Part 1 (Take 2) and Part 2 seamlessly
# Let's inspect the silence at the end of Part 1 (Take 2) and start of Part 2
t2 = r"digital-lab/03-content-lab/thinklate/videos/04_the-subscription-trap/assets/audio/elevenlabs_part1_take2.mp3"
t1 = r"digital-lab/03-content-lab/thinklate/videos/04_the-subscription-trap/assets/audio/elevenlabs_part1_take1.mp3"
p2 = r"digital-lab/03-content-lab/thinklate/videos/04_the-subscription-trap/assets/audio/elevenlabs_part2.mp3"

out_merged_raw = r"digital-lab/03-content-lab/thinklate/videos/04_the-subscription-trap/assets/audio/voiceover_raw_merged.mp3"
out_mastered = r"digital-lab/03-content-lab/thinklate/videos/04_the-subscription-trap/assets/audio/voiceover_mastered.mp3"

# Concat with 0.75s silence between them
# We can use ffmpeg filter_complex
concat_filter = (
    "[0:a][1:a]concat=n=2:v=0:a=1[aout]"
)

# Also let's prepare the Studio Sharp DSP mastering chain:
dsp_chain = (
    "highpass=f=90,"
    "equalizer=f=220:t=q:w=1.2:g=-3.5,"
    "equalizer=f=340:t=q:w=1.4:g=-2.0,"
    "equalizer=f=3500:t=q:w=1.5:g=3.5,"
    "equalizer=f=5200:t=q:w=1.8:g=2.0,"
    "treble=g=2.5:f=11000,"
    "speechnorm=e=4:r=0.0001:l=1,"
    "acompressor=threshold=-18dB:ratio=2.6:attack=15:release=120:makeup=2.5,"
    "loudnorm=I=-16.0:LRA=7.0:TP=-1.5"
)

# 1. Merge Take 2 + Part 2
cmd_merge = [
    "ffmpeg", "-y",
    "-i", t2,
    "-i", p2,
    "-filter_complex", concat_filter,
    "-map", "[aout]",
    "-c:a", "libmp3lame", "-b:a", "320k",
    out_merged_raw
]
subprocess.run(cmd_merge, check=True)

# 2. Master full voiceover
cmd_master = [
    "ffmpeg", "-y",
    "-i", out_merged_raw,
    "-af", dsp_chain,
    "-c:a", "libmp3lame", "-b:a", "320k",
    out_mastered
]
subprocess.run(cmd_master, check=True)

print("Merged and Mastered Successfully!")

