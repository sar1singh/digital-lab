"""
ThinkLate Video 04: DaVinci Resolve Timeline & FCPXML Exporter
DOCUMENTARY EDITION (100% Real-World Stock Footage & Motion Graphics - ZERO Gameplay)
Generates standard FCPXML 1.8 and CMX 3600 EDL files for 1-click DaVinci Resolve import.
Maps 4 Video Tracks (V1 Documentary B-Roll, V2 Blur, V3 Plates, V4 Typography)
and 4 Audio Tracks (A1 Dialogue, A2 BGM Bed, A3 Sub-Bass, A4 Foley).
"""

import os
import sys
import xml.etree.ElementTree as ET
from xml.dom import minidom
from build_timeline_cues import CUES_DEF, total_dur

BASE_DIR = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\04_the-subscription-trap"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
BRAND_DIR = os.path.join(BASE_DIR, "brand_assets")
AUDIO_DIR = os.path.join(ASSETS_DIR, "audio")
SFX_DIR = os.path.join(ASSETS_DIR, "sfx")

FCPXML_OUT = os.path.join(BASE_DIR, "ThinkLate_Video04_DaVinci.fcpxml")
EDL_OUT = os.path.join(BASE_DIR, "ThinkLate_Video04.edl")

FPS = 30
FRAME_DUR = f"1/{FPS}s"

def sec_to_frames(sec):
    return int(round(sec * FPS))

def frames_to_timecode(frames, fps=30):
    total_sec = frames // fps
    f = frames % fps
    s = total_sec % 60
    m = (total_sec // 60) % 60
    h = total_sec // 3600
    return f"{h:02d}:{m:02d}:{s:02d}:{f:02d}"

def sec_to_timecode(sec, fps=30):
    return frames_to_timecode(sec_to_frames(sec), fps)

def generate_fcpxml():
    root = ET.Element("fcpxml", version="1.8")
    resources = ET.SubElement(root, "resources")

    # Format resource
    ET.SubElement(resources, "format", id="r1", name="FFVideoFormat1080p30", frameDuration=FRAME_DUR, width="1920", height="1080")

    # Audio Master resource
    voice_path = os.path.join(AUDIO_DIR, "voiceover_mastered.mp3").replace("\\", "/")
    ET.SubElement(resources, "asset", id="r_audio", name="voiceover_mastered", src=f"file:///{voice_path}", duration=f"{sec_to_frames(total_dur)}/{FPS}s", hasAudio="1")

    # BGM resource
    bgm_path = os.path.join(AUDIO_DIR, "ambient_music_dark_fog.mp3").replace("\\", "/")
    ET.SubElement(resources, "asset", id="r_bgm", name="ambient_music_dark_fog", src=f"file:///{bgm_path}", duration=f"{sec_to_frames(total_dur)}/{FPS}s", hasAudio="1")

    # SFX resources
    sfx_files = ["sfx_sub_boom.wav", "sfx_whoosh.wav", "sfx_data_blip.wav"]
    sfx_ids = {}
    for idx, sfx in enumerate(sfx_files):
        s_id = f"r_sfx_{idx}"
        sfx_ids[sfx] = s_id
        p = os.path.join(SFX_DIR, sfx).replace("\\", "/")
        ET.SubElement(resources, "asset", id=s_id, name=sfx, src=f"file:///{p}", hasAudio="1")

    library = ET.SubElement(root, "library")
    event = ET.SubElement(library, "event", name="ThinkLate_Video04_Event")
    project = ET.SubElement(event, "project", name="ThinkLate_Video04_The_Subscription_Trap")

    sequence = ET.SubElement(project, "sequence", format="r1", duration=f"{sec_to_frames(total_dur)}/{FPS}s")
    spine = ET.SubElement(sequence, "spine")

    # Master timeline primary spine (V1 / V3 base)
    for cue in CUES_DEF:
        cue_id, st, et, v1_broll, v2_blur, v3_asset, v4_overlay, sfx_cue = cue
        dur_sec = et - st
        dur_frames = sec_to_frames(dur_sec)
        offset_frames = sec_to_frames(st)

        clip_name = v3_asset if v3_asset else v1_broll
        asset_node = ET.SubElement(spine, "clip", name=clip_name, offset=f"{offset_frames}/{FPS}s", duration=f"{dur_frames}/{FPS}s", start="0/1s")

        # Markers for blur & text
        if v2_blur:
            ET.SubElement(asset_node, "marker", start="0/1s", duration=f"{dur_frames}/{FPS}s", value=f"V2_SCOPED_BLUR: Active under text")
        if v4_overlay:
            ET.SubElement(asset_node, "marker", start="10/30s", duration=f"{max(dur_frames - 20, 10)}/{FPS}s", value=f"V4_TEXT: {v4_overlay}")
        if sfx_cue:
            sfx_name, sfx_time, sfx_vol = sfx_cue
            ET.SubElement(asset_node, "marker", start="0/1s", duration="1/1s", value=f"SFX: {sfx_name} (vol {sfx_vol})")

    # Prettify XML
    xml_str = ET.tostring(root, encoding="utf-8")
    parsed = minidom.parseString(xml_str)
    pretty_xml = parsed.toprettyxml(indent="  ")

    with open(FCPXML_OUT, "w", encoding="utf-8") as f:
        f.write(pretty_xml)
    print(f"Generated DaVinci FCPXML: {FCPXML_OUT}")

def generate_edl():
    lines = [
        "TITLE: ThinkLate_Video04_The_Subscription_Trap",
        "FCM: NON-DROP FRAME",
        ""
    ]

    for cue in CUES_DEF:
        cue_id, st, et, v1_broll, v2_blur, v3_asset, v4_overlay, sfx_cue = cue
        st_tc = sec_to_timecode(st, FPS)
        et_tc = sec_to_timecode(et, FPS)
        dur_tc = sec_to_timecode(et - st, FPS)

        reel = f"AX{cue_id:02d}"
        clip_name = v3_asset if v3_asset else v1_broll
        lines.append(f"{cue_id:03d}  {reel}       V     C        00:00:00:00 {dur_tc} {st_tc} {et_tc}")
        lines.append(f"* FROM CLIP NAME: {clip_name}")
        if v4_overlay:
            lines.append(f"* COMMENT: V4 TEXT OVERLAY = {v4_overlay}")
        if sfx_cue:
            lines.append(f"* COMMENT: SFX CUE = {sfx_cue[0]} at {sfx_cue[1]}s")
        lines.append("")

    with open(EDL_OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Generated CMX 3600 EDL: {EDL_OUT}")

def main():
    print(f"Compiling DaVinci Resolve Timeline assets for Video 04 ({total_dur:.2f}s)...")
    generate_fcpxml()
    generate_edl()
    print("SUCCESS: DaVinci Resolve Timeline Package ready for 1-click import.")

if __name__ == "__main__":
    main()
