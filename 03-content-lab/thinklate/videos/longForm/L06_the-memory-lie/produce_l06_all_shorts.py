#!/usr/bin/env python3
"""
Builds and renders all 3 Complete Standalone Vertical Documentary Shorts (1080x1920 @ 30fps)
from ThinkLate Episode 06 ("The Memory Lie") — EACH WITH ITS OWN FULL 4-BEAT MIC-DROP CLIMAX:

  1. Short 01 (S02_the-eyewitness-lie): Hosted by Eddy Thinklate (~52s)
     - Hook: 1984 Jennifer Thompson swears on a Bible -> sends Ronald Cotton to prison for life.
     - Escalation: 11 years later DNA exonerates him; 70% of DNA exonerations are caused by calm, confident eyewitnesses.
     - Mechanism: She passed every polygraph; viewing the police lineup overwrote the real attacker's face in her 20W brain.
     - MIC-DROP CLIMAX: "Your skull does not have a hard drive, and your eyes are not a security camera. Every time you swear on your life you remember a face, your brain isn't playing back a recording—it is painting a brand-new suspect from scratch."

  2. Short 02 (S03_the-holographic-shard): Hosted by Vera Vance (~52s)
     - Hook: Cut a paper family photo in half -> lose 50%. Smash a 3D glass hologram into 50 shards -> something miraculous happens.
     - Escalation: Dennis Gabor (1948) proved shining a laser through any tiny broken shard reconstructs 100% of the family portrait intact.
     - Mechanism: Solved the 20-year Karl Lashley cortical lesion mystery & why epilepsy brain surgery never deletes isolated years of your life.
     - MIC-DROP CLIMAX: "Because your brain never stores a memory inside a single neuron. Your past is a living optical hologram—smeared as an interference wave across one hundred trillion synapses at once."

  3. Short 03 (S04_the-photocopy-trap): Hosted by Eddy Thinklate (~52s)
     - Hook: In 2000, Karim Nader proved the simple act of remembering your past physically melts the memory you are trying to recall.
     - Escalation: Retrieving an old memory destabilizes its protein synthesis bonds for 3 to 5 hours into malleable liquid clay.
     - Mechanism: Your current anxiety, nostalgia, or bragging over drinks gets baked into the trace and saved over the original during sleep.
     - MIC-DROP CLIMAX: "You never remember your actual childhood. You only remember the last time you remembered it, adding five percent distortion every single round. By age thirty-five, your favorite childhood memory is a twenty-fifth-generation photocopy of a photocopy—an epic Hollywood screenplay that your own neurons wrote behind your back."
"""
import asyncio
import json
import os
import pathlib
import shutil
import subprocess
import edge_tts
import whisper

VIDEO_DIR = pathlib.Path(__file__).resolve().parent
REPO_ROOT = VIDEO_DIR.parents[5]
MOTION_ENGINE_DIR = REPO_ROOT / "digital-lab" / "03-content-lab" / "shared" / "motion_engine"
SHARED_BROLL_DIR = REPO_ROOT / "digital-lab" / "03-content-lab" / "shared" / "assets" / "broll"
CINEMA_SFX_DIR = REPO_ROOT / "digital-lab" / "03-content-lab" / "shared" / "assets" / "sfx" / "cinema_vault"
BGM_VAULT_DIR = REPO_ROOT / "digital-lab" / "03-content-lab" / "shared" / "assets" / "bgm_vault"
BGM_SRC = BGM_VAULT_DIR / "bgm_dark_tension_free-stock-music_ambient.mp3"
SHORTFORM_ROOT = REPO_ROOT / "digital-lab" / "03-content-lab" / "thinklate" / "videos" / "shortForm"

SHORTS_OUT_DIR = VIDEO_DIR / "shorts"
SHORT_PLATES_DIR = VIDEO_DIR / "assets" / "short_plates"

VOICE_CONFIGS = {
    "owl": {
        "voice": "en-US-ChristopherNeural",
        "rate": "+14%",
        "pitch": "-4Hz",
        "eq_filter": (
            "silenceremove=start_periods=1:start_duration=0.01:start_threshold=-42dB:"
            "stop_periods=-1:stop_duration=0.060:stop_threshold=-44dB,"
            "lowpass=f=8500,equalizer=f=180:t=q:w=1.2:g=2.5,equalizer=f=1500:t=q:w=1.5:g=-2,"
            "loudnorm=I=-16:TP=-1.0:LRA=7"
        ),
    },
    "falcon": {
        "voice": "en-US-AvaNeural",
        "rate": "+16%",
        "pitch": "+0Hz",
        "eq_filter": (
            "silenceremove=start_periods=1:start_duration=0.01:start_threshold=-42dB:"
            "stop_periods=-1:stop_duration=0.060:stop_threshold=-44dB,"
            "highpass=f=100,lowpass=f=9500,equalizer=f=2800:t=q:w=1.4:g=2.0,"
            "loudnorm=I=-16:TP=-1.0:LRA=7"
        ),
    },
}

SHORTS_SPECS = [
    {
        "idx": 1,
        "folder_name": "S02_the-eyewitness-lie",
        "master_name": "ThinkLate_Short01_The_Eyewitness_Lie_1080x1920_MASTER.mp4",
        "canonical_name": "ThinkLate_Short02_The_Eyewitness_Lie_1080x1920_MASTER.mp4",
        "speaker": "owl",
        "host_display": "Eddy Thinklate (Founder & Lead Host)",
        "script_text": (
            "In nineteen eighty-four, a college student named Jennifer Thompson looked straight into the eyes of a judge "
            "and swore on a Bible. She was one hundred percent certain she recognized the man who attacked her. "
            "She studied his face during the assault, picked Ronald Cotton out of a police lineup, and sent him to prison for life! "
            "Eleven years later, modern DNA forensics tested the crime scene evidence. Ronald Cotton was completely innocent. "
            "In fact, over seventy percent of wrongful convictions overturned by DNA in America share this exact horrifying flaw: "
            "an eyewitness who was calm, totally confident, and dead wrong. "
            "Here is the terrifying part: Jennifer Thompson wasn't lying. She passed every polygraph. "
            "When police showed her Ronald Cotton's mugshot in a lineup, her twenty-watt brain didn't open a saved video file "
            "of the crime scene. It ran a live generative simulation, and permanently overwrote the real attacker's face "
            "with the man in the lineup photo. "
            "Your skull does not have a hard drive, and your eyes are not a security camera. "
            "Every time you swear on your life you remember a face, your brain isn't playing back a recording. "
            "It is painting a brand-new suspect from scratch."
        ),
        "plates": [0, 1, 2, 3],
        "bgm_file": BGM_VAULT_DIR / "bgm_dark_tension_free-stock-music_ambient.mp3",
        "brolls": [
            "courtroom.mp4",
            "prison_bars.mp4",
            "dna_lab.mp4",
            "archive_files.mp4",
            "broll_eye_macro.mp4",
            "brain_synapse.mp4",
        ],
        "title": "She Swore on a Bible. She Was 100% Wrong. #Shorts",
        "target_timestamp": "0:00",
        "target_chapter": "Chapter 1: Why Did an Honest Honor Student Send an Innocent Man to Prison?",
        "pinned_comment": (
            "📌 WATCH THE FULL 7-MINUTE INVESTIGATION (Tap '▶ Related Video' right above the title!):\n"
            "In 1984, Jennifer Thompson passed every polygraph and swore under oath she recognized her attacker—sending an innocent man, Ronald Cotton, to prison for 11 years.\n\n"
            "👉 Tap the Related Video link above to watch the full neuroscience breakdown on @wethinklate!"
        ),
    },
    {
        "idx": 2,
        "folder_name": "S03_the-holographic-shard",
        "master_name": "ThinkLate_Short02_The_Holographic_Shard_1080x1920_MASTER.mp4",
        "canonical_name": "ThinkLate_Short03_The_Holographic_Shard_1080x1920_MASTER.mp4",
        "speaker": "falcon",
        "host_display": "Vera Vance (Forensic Investigator)",
        "script_text": (
            "If you take a normal paper photograph of your family, cut it in half with scissors, and throw away the left side, "
            "you permanently lose half your family. But if you record a three-dimensional optical hologram on a glass plate, "
            "and smash that glass with a hammer into fifty jagged shards, something miraculous happens! "
            "In nineteen forty-eight, Nobel physicist Dennis Gabor proved that if you pick up any tiny broken sliver of that hologram "
            "and shine a laser beam through it, you do not see a tiny corner of the room. You see the entire family portrait, "
            "one hundred percent intact, just at softer resolution. "
            "That single optical equation solved the greatest mystery in brain surgery. For twenty years, Harvard neuroscientist "
            "Karl Lashley sliced into the cortices of rats trying to delete a single maze memory, and failed every single time. "
            "Even when neurosurgeons remove brain tissue to stop epilepsy, patients never lose a specific year of their life "
            "or forget their mother's face. "
            "Because your brain never stores a memory inside a single neuron. Your past is a living optical hologram, "
            "smeared as an interference wave across one hundred trillion synapses at once."
        ),
        "plates": [4, 5, 6, 7],
        "bgm_file": BGM_VAULT_DIR / "bgm_documentary_free-stock-music_ambient.mp3",
        "brolls": [
            "broll_vintage_camcorder.mp4",
            "broll_laser_optics.mp4",
            "broll_shattered_glass.mp4",
            "broll_neurosurgery_mri.mp4",
            "brain_synapse.mp4",
            "broll_lightbulb_filament.mp4",
        ],
        "title": "Why Smashing a Hologram Doesn't Erase the Picture #Shorts",
        "target_timestamp": "2:25",
        "target_chapter": "Chapter 3: Why Can You Smash a Hologram and Still See the Whole Picture?",
        "pinned_comment": (
            "📌 FULL EPISODE LINKED ABOVE (Tap '▶ Related Video' at the bottom of the screen & jump to 2:25!):\n"
            "In 1948, Nobel physicist Dennis Gabor proved optical wave interference: smash a hologram into 50 shards, and every single shard still holds 100% of the family portrait—the exact reason brain surgery never deletes isolated years of your life.\n\n"
            "👉 Tap the Related Video link above and scrub to 2:25 for the full documentary!"
        ),
    },
    {
        "idx": 3,
        "folder_name": "S04_the-photocopy-trap",
        "master_name": "ThinkLate_Short03_The_Photocopy_Trap_1080x1920_MASTER.mp4",
        "canonical_name": "ThinkLate_Short04_The_Photocopy_Trap_1080x1920_MASTER.mp4",
        "speaker": "owl",
        "host_display": "Eddy Thinklate (Founder & Lead Host)",
        "script_text": (
            "In the year two thousand, neuroscientist Karim Nader proved something that terrified cognitive psychologists: "
            "the simple act of remembering your past physically melts the memory you are trying to recall! "
            "Whenever you retrieve an old memory, your brain does not perform a safe, read-only playback. "
            "Remembering unlocks and destabilizes the protein synthesis bonds holding those neurons together. "
            "For three to five hours after you think about an event, that memory turns into malleable liquid clay. "
            "If you are anxious, nostalgic, or bragging to friends over drinks, your current mood gets permanently baked "
            "into the trace. When you fall asleep that night, your brain synthesizes fresh proteins and saves the edited version "
            "right over the original file. "
            "You never remember your actual childhood. You only remember the last time you remembered it, adding five percent "
            "distortion every single round. By age thirty-five, your favorite childhood memory is a twenty-fifth-generation "
            "photocopy of a photocopy: an epic Hollywood screenplay that your own neurons wrote behind your back."
        ),
        "plates": [8, 9, 10, 11],
        "bgm_file": BGM_VAULT_DIR / "bgm_dark_tension_free-stock-music_drone-music.mp3",
        "brolls": [
            "broll_protein_molecules.mp4",
            "broll_birthday_candles.mp4",
            "broll_photocopier_scan.mp4",
            "broll_soccer_sunset.mp4",
            "broll_couple_argument.mp4",
            "broll_eye_macro.mp4",
        ],
        "title": "Why Your Childhood Memories Are 25th-Gen Photocopies #Shorts",
        "target_timestamp": "5:01",
        "target_chapter": "Chapter 5: What Happens to Your Brain Proteins Every Time You Remember?",
        "pinned_comment": (
            "📌 WATCH THE FULL BREAKDOWN (Tap '▶ Related Video' right below @wethinklate & jump to 5:01!):\n"
            "In 2000, neuroscientist Karim Nader proved Memory Reconsolidation: every time you recall a memory, its protein bonds melt for 3 to 5 hours. By age 35, your favorite childhood memory is a 25th-generation photocopy of a photocopy.\n\n"
            "👉 Tap the Related Video link above and jump to 5:01 for the full experiment!"
        ),
    },
]

def probe_dur(path: pathlib.Path) -> float:
    out = subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
        creationflags=0x08000000
    ).decode().strip()
    return float(out)

def fmt_ass_time(sec: float) -> str:
    sec = max(0.0, sec)
    h = int(sec // 3600)
    m = int((sec % 3600) // 60)
    s = sec % 60
    return f"{h}:{m:02d}:{s:05.2f}"

def fmt_srt_time(sec: float) -> str:
    sec = max(0.0, sec)
    h = int(sec // 3600)
    m = int((sec % 3600) // 60)
    s = int(sec % 60)
    ms = int(round((sec - int(sec)) * 1000))
    if ms >= 1000:
        ms = 999
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

def generate_short_subtitles(short_spec: dict, words_all: list, dur: float, ass_path: pathlib.Path, srt_path: pathlib.Path):
    is_owl = short_spec["speaker"] == "owl"
    hl_bgr = "&H0000FFE2&" if is_owl else "&H00FFF000&"

    PHONETIC_WORD_MAP = {
        "KAREEM": "KARIM",
        "RECONCILITATION": "RECONSOLIDATION",
        "RECONCILITATION.": "RECONSOLIDATION.",
        "DAMN": "DIM",
        "SAFE": "SAVE",
        "SAFE.": "SAVE.",
        "-WHAT": "-WATT",
        "WHAT": "WATT",
        "CARL": "KARL",
        "SHINA": "SHINE A",
    }

    win_words = []
    for w in words_all:
        raw_w = w["word"].strip()
        if not raw_w:
            continue
        up_check = raw_w.upper()
        if up_check in PHONETIC_WORD_MAP:
            raw_w = PHONETIC_WORD_MAP[up_check]
        win_words.append({
            "word": raw_w,
            "start": max(0.0, float(w["start"])),
            "end": min(dur, float(w["end"])),
        })

    chunks = []
    cur = []
    for w in win_words:
        cur.append(w)
        if len(cur) >= 4 or w["word"].endswith((".", "!", "?", ",", ":")):
            chunks.append(cur)
            cur = []
    if cur:
        chunks.append(cur)

    ass_header = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: ShortSub,Arial,52,&H00FFFFFF,&H0000FFFF,&H00050811,&HDC050811,-1,0,0,0,100,100,1.5,0,3,14,0,2,50,50,635,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    ass_events = []
    srt_blocks = []

    for c_idx, chunk in enumerate(chunks, 1):
        c_start = chunk[0]["start"]
        c_end = chunk[-1]["end"]
        plain = " ".join(x["word"].upper() for x in chunk)
        srt_blocks.append(f"{c_idx}\n{fmt_srt_time(c_start)} --> {fmt_srt_time(c_end)}\n{plain}\n")

        for i, active in enumerate(chunk):
            w_st = active["start"]
            w_en = chunk[i + 1]["start"] if i + 1 < len(chunk) else active["end"]
            if w_en <= w_st:
                w_en = w_st + 0.08
            tokens = []
            for j, tok in enumerate(chunk):
                up = tok["word"].upper()
                if j == i:
                    tokens.append(f"{{\\c{hl_bgr}}}{up}{{\\c&H00FFFFFF&}}")
                else:
                    tokens.append(up)
            line_str = " ".join(tokens)
            ass_events.append(f"Dialogue: 0,{fmt_ass_time(w_st)},{fmt_ass_time(w_en)},ShortSub,,0,0,0,,{line_str}")

    ass_path.write_text(ass_header + "\n".join(ass_events) + "\n", encoding="utf-8")
    srt_path.write_text("\n".join(srt_blocks) + "\n", encoding="utf-8")

def render_short_plates():
    SHORT_PLATES_DIR.mkdir(parents=True, exist_ok=True)
    if all((SHORT_PLATES_DIR / f"element-{p:02d}.png").exists() for p in range(12)):
        print("[*] All 12 Remotion RGBA Plates already exist on disk. Skipping re-render.")
        return
    npx_cmd = "npx.cmd" if os.name == "nt" else "npx"
    cmd = [
        npx_cmd, "remotion", "render", "src/index.ts", "L06VerticalShortOverlay",
        str(SHORT_PLATES_DIR), "--sequence", "--image-format=png", "--gl=angle"
    ]
    print("[*] Rendering 12 Vertical 1080x1920 RGBA Plates (4 per Short incl. Climax Verdict) via Remotion...")
    subprocess.run(cmd, cwd=str(MOTION_ENGINE_DIR), check=True, creationflags=0x08000000)

async def synthesize_short_audio(spec: dict, work_dir: pathlib.Path) -> tuple[pathlib.Path, pathlib.Path, float]:
    speaker = spec["speaker"]
    cfg = VOICE_CONFIGS[speaker]
    temp_mp3 = work_dir / "tts_raw.mp3"
    vocal_wav = work_dir / "vocal_clean.wav"
    mixed_wav = work_dir / "short_audio_master.wav"

    print(f"[*] Synthesizing standalone complete climax script for {spec['folder_name']} [{spec['host_display']}]...")
    comm = edge_tts.Communicate(text=spec["script_text"], voice=cfg["voice"], rate=cfg["rate"], pitch=cfg["pitch"])
    await comm.save(str(temp_mp3))

    subprocess.run([
        "ffmpeg", "-y", "-i", str(temp_mp3),
        "-af", cfg["eq_filter"] + ",apad=pad_dur=0.35",
        "-ar", "48000", "-ac", "2", str(vocal_wav)
    ], check=True, creationflags=0x08000000)
    temp_mp3.unlink(missing_ok=True)

    dur = round(probe_dur(vocal_wav), 2)

    # Ultra-Clean Voice-Forward Mix:
    # 1. Voice sits 100% upfront (normalized to -16 LUFS / -1.0 dBFS True Peak)
    # 2. Distinct ambient drone BGM ducked to -32dB (barely noticeable psychological undertone)
    #    with deep vocal pocket EQ (-10dB @ 1500Hz, -8dB @ 3000Hz, 3500Hz lowpass ceiling)
    # 3. Softened Cinema Vault SFX hits (0.14 - 0.18, lowpass 6000Hz)
    # 4. Zero loudnorm on [mixed] to prevent music/SFX pumping during vocal pauses
    bgm_file = spec.get("bgm_file", BGM_SRC)
    sfx_1 = CINEMA_SFX_DIR / "sub_impact_deep_cinematic.mp3"
    sfx_2 = CINEMA_SFX_DIR / "paper_slide_document.mp3"
    sfx_3 = CINEMA_SFX_DIR / "whoosh_tunnel_smooth.mp3"
    sfx_4 = CINEMA_SFX_DIR / "camera_vintage_shutter.mp3"

    d1 = 1200
    d2 = int(dur * 0.26 * 1000)
    d3 = int(dur * 0.52 * 1000)
    d4 = int(dur * 0.76 * 1000)

    fc = (
        "[0:a]volume=1.0[vocal];"
        f"[1:a]atrim=0:{dur:.2f},volume=-32dB,lowpass=f=3500,highpass=f=90,equalizer=f=1500:t=q:w=1.5:g=-10,equalizer=f=3000:t=q:w=1.5:g=-8,afade=t=out:st={max(0.5, dur-1.5):.2f}:d=1.5[bgm];"
        f"[2:a]adelay={d1}|{d1},volume=0.14,lowpass=f=6000[s1];"
        f"[3:a]adelay={d2}|{d2},volume=0.16,lowpass=f=6000[s2];"
        f"[4:a]adelay={d3}|{d3},volume=0.16,lowpass=f=6000[s3];"
        f"[5:a]adelay={d4}|{d4},volume=0.18,lowpass=f=6000[s4];"
        "[vocal][bgm][s1][s2][s3][s4]amix=inputs=6:duration=first:dropout_transition=0:normalize=0[mixed]"
    )
    subprocess.run([
        "ffmpeg", "-y",
        "-i", str(vocal_wav),
        "-stream_loop", "-1", "-i", str(bgm_file),
        "-i", str(sfx_1), "-i", str(sfx_2), "-i", str(sfx_3), "-i", str(sfx_4),
        "-filter_complex", fc,
        "-map", "[mixed]", "-ar", "48000", "-ac", "2", str(mixed_wav)
    ], check=True, creationflags=0x08000000)

    return vocal_wav, mixed_wav, dur

async def build_single_short(spec: dict, whisper_model):
    SHORTS_OUT_DIR.mkdir(parents=True, exist_ok=True)
    idx = spec["idx"]
    work_dir = SHORTS_OUT_DIR / f"work_s0{idx}"
    work_dir.mkdir(parents=True, exist_ok=True)

    vocal_wav, short_wav, dur = await synthesize_short_audio(spec, work_dir)

    # Transcribe vocal_wav with Whisper for 100% word-level subtitle sync through the final Climax
    res = whisper_model.transcribe(str(vocal_wav), word_timestamps=True, language="en")
    words_all = []
    for seg in res.get("segments", []):
        for w in seg.get("words", []):
            words_all.append(w)

    ass_path = work_dir / "subs.ass"
    srt_path = work_dir / "subtitles_en.srt"
    generate_short_subtitles(spec, words_all, dur, ass_path, srt_path)

    # Render 6 B-roll beats (~8.5s each) while stepping through all 4 RGBA plates (Hook -> Escalation -> Mechanism -> Climax Verdict!)
    plates = [SHORT_PLATES_DIR / f"element-{p:02d}.png" for p in spec["plates"]]
    if not plates[0].exists():
        plates = [SHORT_PLATES_DIR / f"element-{p}.png" for p in spec["plates"]]
    brolls = [SHARED_BROLL_DIR / b for b in spec["brolls"]]

    n_beats = 6
    beat_dur = round(dur / float(n_beats), 2)
    beat_files = []
    # Map 6 B-roll beats across the 4 story plates (0, 1, 1, 2, 2, 3) so Plate 3 is the Climax Verdict!
    plate_map = [plates[0], plates[1], plates[1], plates[2], plates[2], plates[3]]

    for b_i in range(n_beats):
        b_dur = beat_dur if b_i < (n_beats - 1) else round(dur - beat_dur * (n_beats - 1), 2)
        b_clip = brolls[b_i] if brolls[b_i].exists() else (SHARED_BROLL_DIR / "brain_synapse.mp4")
        plate_img = plate_map[b_i]
        seg_out = work_dir / f"beat_{b_i}.mp4"
        vf = (
            "[0:v]scale=1200:2134:force_original_aspect_ratio=increase,"
            "crop=1080:1920:x='(iw-ow)/2+sin(t*0.6)*45':y='(ih-oh)/2+cos(t*0.4)*35',"
            "fps=30,setsar=1,eq=brightness=-0.12:contrast=1.20:saturation=0.88,boxblur=10:1[bg];"
            "[1:v]format=yuva420p[plate];"
            "[bg][plate]overlay=0:0[outv]"
        )
        subprocess.run([
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
            "-stream_loop", "-1", "-t", f"{b_dur:.2f}", "-i", str(b_clip),
            "-loop", "1", "-t", f"{b_dur:.2f}", "-i", str(plate_img),
            "-filter_complex", vf, "-map", "[outv]",
            "-c:v", "h264_nvenc", "-preset", "p4", "-cq", "19", "-pix_fmt", "yuv420p", "-r", "30",
            str(seg_out)
        ], check=True, creationflags=0x08000000)
        beat_files.append(seg_out)

    concat_txt = work_dir / "concat.txt"
    concat_txt.write_text("\n".join(f"file '{f.name}'" for f in beat_files), encoding="utf-8")
    concat_mp4 = work_dir / "concat_raw.mp4"
    subprocess.run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-f", "concat", "-safe", "0", "-i", str(concat_txt), "-c", "copy", str(concat_mp4)
    ], cwd=str(work_dir), check=True, creationflags=0x08000000)

    # Burn in ASS subtitles and mux short_wav
    out_master = SHORTS_OUT_DIR / spec["master_name"]
    subprocess.run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-i", str(concat_mp4), "-i", str(short_wav),
        "-vf", "ass=subs.ass",
        "-map", "0:v:0", "-map", "1:a:0",
        "-c:v", "h264_nvenc", "-preset", "p4", "-cq", "19", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-shortest", "-movflags", "+faststart",
        str(out_master)
    ], cwd=str(work_dir), check=True, creationflags=0x08000000)

    # Populate canonical shortForm folder (S02, S03, S04)
    canon_dir = SHORTFORM_ROOT / spec["folder_name"]
    canon_dir.mkdir(parents=True, exist_ok=True)
    canon_mp4 = canon_dir / spec["canonical_name"]
    shutil.copy2(out_master, canon_mp4)
    shutil.copy2(srt_path, canon_dir / "subtitles_en.srt")

    # Save SHORT_SCRIPT.md in canonical folder
    (canon_dir / "SHORT_SCRIPT.md").write_text(
        f"# {spec['title']}\n\n- **Host:** {spec['host_display']}\n- **Duration:** {dur:.2f}s (Complete 4-Beat Story with Mic-Drop Climax)\n\n## Spoken Script\n\n{spec['script_text']}\n",
        encoding="utf-8"
    )

    # Extract 4 cover frames across the 4 story beats (including the Climax Verdict beat!)
    for c_i, t_sec in enumerate([2.0, dur * 0.30, dur * 0.60, dur * 0.88], 1):
        subprocess.run([
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
            "-ss", f"{min(dur - 1.0, t_sec):.2f}", "-i", str(out_master),
            "-frames:v", "1", "-q:v", "2", str(canon_dir / f"cover_frame_0{c_i}.jpg")
        ], check=True, creationflags=0x08000000)

    # Write COPY_PASTE_METADATA.txt
    meta_txt = f"""======================================================================
THINKLATE VERTICAL SHORT PUBLISHING PACKAGE ({spec['folder_name']})
======================================================================
MASTER FILE:       {spec['canonical_name']}
DURATION:          {dur:.2f}s (1080x1920 @ 30fps, Complete 4-Beat Story + Mic-Drop Climax)
HOST VOICE:        {spec['host_display']}
YOUTUBE TITLE:     {spec['title']}

----------------------------------------------------------------------
🎙️ FULL STANDALONE SPOKEN SCRIPT (WITH MIC-DROP CLIMAX):
----------------------------------------------------------------------
{spec['script_text']}

----------------------------------------------------------------------
🔗 HOW TO ENABLE THE CLICKABLE LONG-VIDEO & TIMESTAMP BRIDGE:
----------------------------------------------------------------------
1. In YouTube Studio -> Content -> Shorts -> Edit "{spec['title']}":
   - Scroll to the "Related video" field on the right sidebar.
   - Select the Long-Form Episode 06 video: "Your Memories Never Happened".
   - This activates the clickable "▶ Related Video" pill right underneath the
     animated on-screen "👇 CLICK LINK BELOW • JUMP TO @ {spec['target_timestamp']}" banner!
2. Exact Timestamp Deep-Link Mechanics:
   - The on-screen badge instructs viewers who want the full 7-minute deep dive
     to jump directly to **{spec['target_timestamp']}** ({spec['target_chapter']}).

----------------------------------------------------------------------
📌 COPY-PASTE PINNED COMMENT FOR THIS SHORT:
----------------------------------------------------------------------
{spec['pinned_comment']}
"""
    (canon_dir / "COPY_PASTE_METADATA.txt").write_text(meta_txt, encoding="utf-8")
    shutil.rmtree(work_dir, ignore_errors=True)
    sz_mb = out_master.stat().st_size / (1024 * 1024)
    print(f"  ✓ Rendered Complete Climax Short: {spec['master_name']} ({dur:.2f}s | {sz_mb:.2f} MB) -> Synced to {canon_dir.name}")

async def main():
    render_short_plates()
    whisper_model = whisper.load_model("base")
    for spec in SHORTS_SPECS:
        await build_single_short(spec, whisper_model)

if __name__ == "__main__":
    asyncio.run(main())
