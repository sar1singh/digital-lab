import React from "react";
import { AbsoluteFill, staticFile, useCurrentFrame } from "remotion";

export interface VerticalShortPlateSpec {
  id: number;
  shortTag: string;
  speaker: "owl" | "falcon";
  hookHeadline: string;
  hookAccent: string;
  badge: string;
  docketTitle: string;
  docketSub: string;
  quote: string;
  metrics: { label: string; value: string; color: string }[];
  imageFile: string;
  imageCaption: string;
  stampText?: string;
  stampColor?: string;
  relatedCtaText: string;
  relatedTimestamp: string;
}

const SHORT_PLATES: VerticalShortPlateSpec[] = [
  // ================= SHORT 01 (S02: THE EYEWITNESS LIE — COMPLETE 4-BEAT STORY WITH CLIMAX) =================
  {
    id: 0,
    shortTag: "S02 // EYEWITNESS PARADOX",
    speaker: "owl",
    hookHeadline: "100% CERTAIN.",
    hookAccent: "100% WRONG.",
    badge: "🏛️ BURLINGTON COURT DOCKET #84-CR-1102",
    docketTitle: "SWORN ON A BIBLE IN 1984",
    docketSub: "Star Witness: Jennifer Thompson (22-Year-Old Student)",
    quote: "\"She looked straight into the eyes of a judge, picked Ronald Cotton out of a police lineup, and sent him to prison for life.\"",
    metrics: [
      { label: "WITNESS CONFIDENCE", value: "100.0%", color: "#00F0FF" },
      { label: "SENTENCE HANDED DOWN", value: "LIFE + 54 YRS", color: "#FF2A4B" },
    ],
    imageFile: "images/memory_lie/Jennifer_Thompson_Cannino_and_Ronald_Cot.jpg",
    imageCaption: "JENNIFER THOMPSON & RONALD COTTON (ARCHIVAL)",
    relatedCtaText: "TAP 'RELATED VIDEO' BELOW FOR FULL DOCUMENTARY",
    relatedTimestamp: " STARTS @ 0:00",
  },
  {
    id: 1,
    shortTag: "S02 // FORENSIC DNA SHOCK",
    speaker: "owl",
    hookHeadline: "11 YEARS IN PRISON",
    hookAccent: "FOR NOTHING.",
    badge: "🧬 1995 DNA EXONERATION REGISTRY",
    docketTitle: "70% OF DNA EXONERATIONS: MEMORY ERROR",
    docketSub: "Ronald Cotton Was 100% Innocent • 375+ Proven Cases",
    quote: "\"Eleven years later, DNA forensics proved Ronald Cotton was completely innocent. Over 70% of DNA exonerations were caused by calm, confident eyewitnesses.\"",
    metrics: [
      { label: "WRONGFUL PRISON TIME", value: "11 YEARS", color: "#F59E0B" },
      { label: "FALSE CONVICTION CAUSE", value: "70% EYEWITNESS", color: "#10B981" },
    ],
    imageFile: "images/memory_lie/GelDoc_DNA_gel_electrophoresis_photograp.jpg",
    imageCaption: "GELDOC FORENSIC DNA ELECTROPHORESIS BANDS",
    stampText: "INNOCENT",
    stampColor: "#10B981",
    relatedCtaText: "TAP 'RELATED VIDEO' BELOW FOR FULL DOCUMENTARY",
    relatedTimestamp: " STARTS @ 0:00",
  },
  {
    id: 2,
    shortTag: "S02 // THE LINEUP OVERWRITE",
    speaker: "owl",
    hookHeadline: "SHE PASSED EVERY",
    hookAccent: "POLYGRAPH TEST.",
    badge: "🔍 COGNITIVE CONTAMINATION MECHANISM",
    docketTitle: "HOW THE LINEUP ERASED THE REAL ATTACKER",
    docketSub: "Zero Deception • Her 20W Brain Overwrote the Crime Scene",
    quote: "\"Jennifer Thompson wasn't lying. When police showed her Ronald Cotton's mugshot, her brain ran a live simulation and overwrote the real attacker's face!\"",
    metrics: [
      { label: "POLYGRAPH RESULT", value: "100% TRUTHFUL", color: "#10B981" },
      { label: "ORIGINAL MEMORY", value: "OVERWRITTEN", color: "#FF2A4B" },
    ],
    imageFile: "memes/always_has_been.png",
    imageCaption: "WAIT, MY MEMORIES ARE SIMULATIONS? ALWAYS HAVE BEEN.",
    stampText: "REWRITTEN",
    stampColor: "#FF2A4B",
    relatedCtaText: "TAP 'RELATED VIDEO' BELOW • FULL EPISODE",
    relatedTimestamp: " JUMP TO @ 0:00",
  },
  {
    id: 3,
    shortTag: "S02 // THE CLIMAX VERDICT",
    speaker: "owl",
    hookHeadline: "YOUR SKULL HAS NO",
    hookAccent: "SECURITY CAMERA.",
    badge: "⚡ FINAL VERDICT // NEUROBIOLOGY OF RECALL",
    docketTitle: "PAINTING A BRAND-NEW SUSPECT FROM SCRATCH",
    docketSub: "Zero MP4 Files • Zero Hard Drive • 100% Generative Reconstruction",
    quote: "\"Every time you swear on your life you remember a face, your brain isn't playing back a recording—it is painting a brand-new suspect from scratch.\"",
    metrics: [
      { label: "ANATOMICAL HARD DRIVE", value: "0 BYTES", color: "#FF2A4B" },
      { label: "HUMAN RECALL ENGINE", value: "LIVE PAINTING", color: "#E2FF00" },
    ],
    imageFile: "memes/spiderman_pointing_at_spiderman.jpg",
    imageCaption: "YOUR BRAIN REPLACING THE REAL CULPRIT WITH A LINEUP MUGSHOT",
    stampText: "CASE CLOSED",
    stampColor: "#E2FF00",
    relatedCtaText: "TAP 'RELATED VIDEO' BELOW • FULL EPISODE",
    relatedTimestamp: " JUMP TO @ 0:00",
  },

  // ================= SHORT 02 (S03: THE HOLOGRAPHIC SHARD — COMPLETE 4-BEAT STORY WITH CLIMAX) =================
  {
    id: 4,
    shortTag: "S03 // OPTICAL PHYSICS",
    speaker: "falcon",
    hookHeadline: "CUT A PHOTO IN HALF:",
    hookAccent: "LOSE 50%.",
    badge: "✂️ LOCALIZED PIXELS VS. WAVE INTERFERENCE",
    docketTitle: "WHY YOUR BRAIN IS NOT A PAPER PHOTO",
    docketSub: "Dennis Gabor's 1948 Nobel Prize Holography Discovery",
    quote: "\"Take a normal paper photograph of your family, cut it in half with scissors, and throw away the left side—you permanently lose half your family.\"",
    metrics: [
      { label: "PAPER PHOTOGRAPH", value: "LOCALIZED PIXELS", color: "#FF2A4B" },
      { label: "CUT IN HALF RESULT", value: "50% DATA LOST", color: "#F59E0B" },
    ],
    imageFile: "images/memory_lie/dennis_gabor_portrait.jpg",
    imageCaption: "DENNIS GABOR (1948) • FATHER OF OPTICAL HOLOGRAPHY",
    relatedCtaText: "TAP 'RELATED VIDEO' BELOW • FULL EPISODE",
    relatedTimestamp: " JUMP TO @ 2:25",
  },
  {
    id: 5,
    shortTag: "S03 // SMASHED HOLOGRAM",
    speaker: "falcon",
    hookHeadline: "SMASH A HOLOGRAM:",
    hookAccent: "KEEP 100%.",
    badge: "🔨 THE 50-SHARD LASER EXPERIMENT",
    docketTitle: "EVERY TINY SHARD HOLDS THE WHOLE PICTURE",
    docketSub: "Wavefront Interference Equation: I(x,y) = |R + O|²",
    quote: "\"Smash a 3D glass hologram into 50 jagged shards. Shine a laser through any tiny sliver—and you see the ENTIRE family portrait intact!\"",
    metrics: [
      { label: "BROKEN GLASS SHARDS", value: "50 PIECES", color: "#00F0FF" },
      { label: "IMAGE IN 1 TINY SHARD", value: "100% INTACT", color: "#10B981" },
    ],
    imageFile: "images/memory_lie/holography_diagram.jpg",
    imageCaption: "3D HOLOGRAPHIC WAVEFRONT RECONSTRUCTION",
    stampText: "100% INTACT",
    stampColor: "#10B981",
    relatedCtaText: "TAP 'RELATED VIDEO' BELOW • FULL EPISODE",
    relatedTimestamp: " JUMP TO @ 2:25",
  },
  {
    id: 6,
    shortTag: "S03 // BRAIN SURGERY MYSTERY",
    speaker: "falcon",
    hookHeadline: "20 YEARS OF SURGERY:",
    hookAccent: "ZERO MEMORIES LOST.",
    badge: "🏥 KARL LASHLEY (1950) & EPILEPSY NEUROSURGERY",
    docketTitle: "SLICING THE CORTEX NEVER DELETED A SINGLE YEAR",
    docketSub: "Why Removing Brain Tissue Doesn't Erase Your Mother's Face",
    quote: "\"Harvard's Karl Lashley spent 20 years cutting rat cortices trying to delete one maze memory—and failed. Epilepsy patients never lose isolated years.\"",
    metrics: [
      { label: "LASHLEY CORTICAL CUTS", value: "20 YRS // 0 ERASED", color: "#F59E0B" },
      { label: "ISOLATED FILE LOSS", value: "IMPOSSIBLE", color: "#10B981" },
    ],
    imageFile: "images/memory_lie/hippocampus_brain.jpg",
    imageCaption: "DISTRIBUTED CORTICAL & HIPPOCAMPAL ENGRAM NETWORK",
    relatedCtaText: "TAP 'RELATED VIDEO' BELOW • FULL EPISODE",
    relatedTimestamp: " JUMP TO @ 2:25",
  },
  {
    id: 7,
    shortTag: "S03 // THE CLIMAX VERDICT",
    speaker: "falcon",
    hookHeadline: "YOUR PAST IS A",
    hookAccent: "LIVING HOLOGRAM.",
    badge: "🧠 FINAL VERDICT // HOLONOMIC BRAIN ARCHITECTURE",
    docketTitle: "SMEARED ACROSS 100 TRILLION SYNAPSES AT ONCE",
    docketSub: "No Single Neuron Holds a Memory • Non-Local Interference Wave",
    quote: "\"Your brain never stores a memory inside a single neuron. Your past is a living optical hologram—smeared across 100 trillion synapses at once.\"",
    metrics: [
      { label: "NEURAL TOPOLOGY", value: "HOLOGRAPHIC WAVE", color: "#00F0FF" },
      { label: "SYNAPTIC WEIGHTS", value: "100 TRILLION", color: "#E2FF00" },
    ],
    imageFile: "memes/charlie_conspiracy.jpg",
    imageCaption: "100 TRILLION SYNAPSES RECONSTRUCTING YOUR PAST IN REAL TIME",
    stampText: "NON-LOCAL",
    stampColor: "#00F0FF",
    relatedCtaText: "TAP 'RELATED VIDEO' BELOW • FULL EPISODE",
    relatedTimestamp: " JUMP TO @ 2:25",
  },

  // ================= SHORT 03 (S04: THE PHOTOCOPY TRAP — COMPLETE 4-BEAT STORY WITH CLIMAX) =================
  {
    id: 8,
    shortTag: "S04 // RECONSOLIDATION",
    speaker: "owl",
    hookHeadline: "REMEMBERING A MEMORY",
    hookAccent: "MELTS IT.",
    badge: "🧪 KARIM NADER (NATURE, 2000) DISCOVERY",
    docketTitle: "PROTEIN SYNTHESIS DESTABILIZATION",
    docketSub: "Retrieving an Old Memory Unlocks Its Molecular Bonds",
    quote: "\"In 2000, neuroscientist Karim Nader proved that when you retrieve an old memory, the act of remembering physically melts its protein bonds!\"",
    metrics: [
      { label: "LANDMARK STUDY", value: "NATURE (2000)", color: "#E2FF00" },
      { label: "MOLECULAR STATE", value: "LIQUID CLAY", color: "#FF2A4B" },
    ],
    imageFile: "images/memory_lie/hippocampus_brain.jpg",
    imageCaption: "DE NOVO PROTEIN SYNTHESIS IN AMYGDALA & HIPPOCAMPUS",
    relatedCtaText: "TAP 'RELATED VIDEO' BELOW • FULL EPISODE",
    relatedTimestamp: " JUMP TO @ 5:01",
  },
  {
    id: 9,
    shortTag: "S04 // THE 5-HOUR WINDOW",
    speaker: "owl",
    hookHeadline: "3 TO 5 HOURS OF",
    hookAccent: "LIQUID CLAY.",
    badge: "⏳ THE MALLEABLE RE-WRITE WINDOW",
    docketTitle: "TODAY'S MOOD OVERWRITES YESTERDAY'S FILE",
    docketSub: "Anxiety, Nostalgia & Friends' Comments Get Baked Right In",
    quote: "\"For 3 to 5 hours after you think about an event, your current mood gets baked into the trace. When you sleep, new proteins save the edited version over the original.\"",
    metrics: [
      { label: "UNLOCKED WINDOW", value: "3 TO 5 HOURS", color: "#F59E0B" },
      { label: "ORIGINAL MEMORY", value: "OVERWRITTEN", color: "#FF2A4B" },
    ],
    imageFile: "memes/the_scroll_of_truth.jpg",
    imageCaption: "YOUR BRAIN QUIETLY OVERWRITING THE ORIGINAL RECORDING",
    stampText: "OVERWRITTEN",
    stampColor: "#FF2A4B",
    relatedCtaText: "TAP 'RELATED VIDEO' BELOW • FULL EPISODE",
    relatedTimestamp: " JUMP TO @ 5:01",
  },
  {
    id: 10,
    shortTag: "S04 // +5% DRIFT PER RECALL",
    speaker: "owl",
    hookHeadline: "YOU ONLY REMEMBER",
    hookAccent: "YOUR LAST DRAFT.",
    badge: "🖨️ AUTOBIOGRAPHICAL MEMORY MUTATION",
    docketTitle: "+5% DISTORTION EVERY SINGLE RECALL",
    docketSub: "Bragging Over Drinks Nudges the Defenders 2 Feet Back",
    quote: "\"You never remember your actual childhood. You only remember the last time you remembered it—adding 5% emotional polish and distortion every single round.\"",
    metrics: [
      { label: "DRIFT PER RECALL", value: "+5% MUTATION", color: "#FF2A4B" },
      { label: "ORIGINAL ARCHIVE", value: "DELETED", color: "#00F0FF" },
    ],
    imageFile: "memes/clown_makeup.jpg",
    imageCaption: "ADDING +5% HOLLYWOOD DRAMA EVERY TIME YOU TELL THE STORY",
    relatedCtaText: "TAP 'RELATED VIDEO' BELOW • FULL EPISODE",
    relatedTimestamp: " JUMP TO @ 5:01",
  },
  {
    id: 11,
    shortTag: "S04 // THE CLIMAX VERDICT",
    speaker: "owl",
    hookHeadline: "BY AGE 35, IT'S A",
    hookAccent: "HOLLYWOOD SCRIPT.",
    badge: "🎬 FINAL VERDICT // THE 25TH-GEN PHOTOCOPY",
    docketTitle: "A SCREENPLAY AUTHORED BY YOUR OWN NEURONS",
    docketSub: "25th-Generation Photocopy of a Photocopy • <20% Original Fact",
    quote: "\"By age 35, your favorite childhood memory is a 25th-generation photocopy of a photocopy—an epic Hollywood screenplay your own neurons wrote behind your back.\"",
    metrics: [
      { label: "BY AGE 35", value: "25TH PHOTOCOPY", color: "#00F0FF" },
      { label: "FACTUAL FIDELITY", value: "< 20% REAL", color: "#E2FF00" },
    ],
    imageFile: "memes/they_re_the_same_picture.jpg",
    imageCaption: "COMPARING WHAT ACTUALLY HAPPENED TO YOUR 25TH RECALL DRAFT",
    stampText: "PURE FICTION",
    stampColor: "#E2FF00",
    relatedCtaText: "TAP 'RELATED VIDEO' BELOW • FULL EPISODE",
    relatedTimestamp: " JUMP TO @ 5:01",
  },
];

export const L06VerticalShortOverlay: React.FC = () => {
  const frame = useCurrentFrame();
  const spec = SHORT_PLATES[frame] || SHORT_PLATES[0];
  const isOwl = spec.speaker === "owl";
  const accent = isOwl ? "#E2FF00" : "#00F0FF";

  return (
    <AbsoluteFill
      style={{
        backgroundColor: "transparent",
        fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif",
        color: "#FFFFFF",
        overflow: "hidden",
      }}
    >
      {/* 1. TOP CHANNEL & SERIES PILL (y=72) */}
      <div
        style={{
          position: "absolute",
          top: 72,
          left: 52,
          right: 52,
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
        }}
      >
        <div
          style={{
            backgroundColor: "rgba(6, 10, 20, 0.9)",
            border: `2px solid ${accent}`,
            padding: "10px 22px",
            borderRadius: 30,
            fontSize: 19,
            fontWeight: 900,
            letterSpacing: 2.5,
            color: accent,
            boxShadow: "0 10px 30px rgba(0,0,0,0.8)",
          }}
        >
          ● @WETHINKLATE // {spec.shortTag}
        </div>
      </div>

      {/* 2. MASSIVE VVSA HOOK BANNER (y=146) */}
      <div
        style={{
          position: "absolute",
          top: 146,
          left: 52,
          right: 52,
          backgroundColor: "rgba(6, 10, 20, 0.92)",
          border: "2px solid rgba(255,255,255,0.22)",
          borderRadius: 24,
          padding: "18px 26px",
          textAlign: "center",
          boxShadow: "0 20px 50px rgba(0,0,0,0.85)",
        }}
      >
        <div
          style={{
            fontSize: 46,
            fontWeight: 950,
            letterSpacing: -1,
            lineHeight: 1.04,
            color: "#FFFFFF",
          }}
        >
          {spec.hookHeadline}
        </div>
        <div
          style={{
            fontSize: 52,
            fontWeight: 950,
            letterSpacing: -1,
            lineHeight: 1.06,
            color: accent,
            marginTop: 4,
          }}
        >
          {spec.hookAccent}
        </div>
      </div>

      {/* 3. PRIMARY FORENSIC EVIDENCE DOSSIER + ARCHIVAL IMAGE (y=328..1168) */}
      <div
        style={{
          position: "absolute",
          top: 328,
          left: 52,
          right: 52,
          height: 840,
          backgroundColor: "rgba(8, 13, 26, 0.90)",
          border: `2px solid ${accent}66`,
          borderRadius: 28,
          padding: "24px 30px",
          display: "flex",
          flexDirection: "column",
          justifyContent: "space-between",
          boxShadow: "0 25px 70px rgba(0,0,0,0.9)",
          overflow: "hidden",
        }}
      >
        <div>
          <div
            style={{
              fontSize: 15,
              fontWeight: 900,
              color: accent,
              letterSpacing: 2,
              marginBottom: 6,
            }}
          >
            {spec.badge}
          </div>
          <div
            style={{
              fontSize: 31,
              fontWeight: 950,
              color: "#FFFFFF",
              lineHeight: 1.12,
              marginBottom: 4,
            }}
          >
            {spec.docketTitle}
          </div>
          <div
            style={{
              fontSize: 19,
              fontWeight: 700,
              color: "#CBD5E1",
              marginBottom: 12,
            }}
          >
            {spec.docketSub}
          </div>
        </div>

        {/* Archival / Meme Hero Plate */}
        <div
          style={{
            width: "100%",
            height: 355,
            borderRadius: 18,
            overflow: "hidden",
            border: "2px solid rgba(255,255,255,0.18)",
            position: "relative",
            backgroundColor: "#04070F",
          }}
        >
          <img
            src={staticFile(spec.imageFile)}
            alt={spec.imageCaption}
            style={{
              width: "100%",
              height: "100%",
              objectFit: "cover",
            }}
          />
          {/* Optional Stamp placed cleanly inside bottom-right of the image box so it NEVER touches docketTitle! */}
          {spec.stampText && (
            <div
              style={{
                position: "absolute",
                bottom: 46,
                right: 18,
                border: `5px solid ${spec.stampColor || "#FF2A4B"}`,
                color: spec.stampColor || "#FF2A4B",
                backgroundColor: "rgba(4, 7, 15, 0.94)",
                padding: "6px 18px",
                fontSize: 24,
                fontWeight: 950,
                letterSpacing: 3,
                transform: "rotate(-6deg)",
                boxShadow: `0 0 25px ${spec.stampColor || "#FF2A4B"}66`,
              }}
            >
              {spec.stampText}
            </div>
          )}
          <div
            style={{
              position: "absolute",
              bottom: 0,
              left: 0,
              right: 0,
              backgroundColor: "rgba(4, 7, 15, 0.88)",
              padding: "7px 14px",
              fontSize: 13,
              fontWeight: 800,
              color: "#E2E8F0",
              textAlign: "center",
              letterSpacing: 1.5,
            }}
          >
            {spec.imageCaption}
          </div>
        </div>

        {/* Quote Block */}
        <div
          style={{
            backgroundColor: "rgba(255,255,255,0.05)",
            borderLeft: `5px solid ${accent}`,
            padding: "12px 16px",
            borderRadius: "0 12px 12px 0",
            fontSize: 20,
            fontStyle: "italic",
            lineHeight: 1.32,
            color: "#F8FAFC",
          }}
        >
          {spec.quote}
        </div>

        {/* 2-Column Metrics */}
        <div
          style={{
            display: "grid",
            gridTemplateColumns: "1fr 1fr",
            gap: 16,
          }}
        >
          {spec.metrics.map((m, idx) => (
            <div
              key={idx}
              style={{
                backgroundColor: "rgba(3, 7, 15, 0.85)",
                border: `1px solid ${m.color}66`,
                borderRadius: 14,
                padding: "10px 16px",
              }}
            >
              <div
                style={{
                  fontSize: 13,
                  fontWeight: 800,
                  color: "#94A3B8",
                  letterSpacing: 1.5,
                }}
              >
                {m.label}
              </div>
              <div
                style={{
                  fontSize: 25,
                  fontWeight: 950,
                  color: m.color,
                  fontFamily: "monospace",
                  marginTop: 2,
                }}
              >
                {m.value}
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* 4. CLICKABLE 'RELATED VIDEO' DEEP-LINK POINTER BRIDGE (y=1335, 100% ABOVE YouTube Shorts' bottom mobile UI!) */}
      <div
        style={{
          position: "absolute",
          top: 1335,
          left: 52,
          right: 120,
          backgroundColor: "rgba(6, 10, 20, 0.95)",
          border: `2px solid ${accent}`,
          borderRadius: 18,
          padding: "12px 20px",
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
          boxShadow: `0 12px 35px rgba(0,0,0,0.9), 0 0 20px ${accent}33`,
        }}
      >
        <div style={{ display: "flex", alignItems: "center", gap: 14 }}>
          <div
            style={{
              width: 40,
              height: 40,
              borderRadius: 10,
              backgroundColor: accent,
              color: "#050811",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              fontSize: 24,
              fontWeight: 950,
            }}
          >
            ▶
          </div>
          <div>
            <div
              style={{
                fontSize: 16,
                fontWeight: 900,
                color: "#FFFFFF",
                letterSpacing: 1,
              }}
            >
              {spec.relatedCtaText}
            </div>
            <div
              style={{
                fontSize: 15,
                fontWeight: 800,
                color: accent,
                letterSpacing: 1.5,
              }}
            >
              👇 CLICK LINK BELOW • {spec.relatedTimestamp}
            </div>
          </div>
        </div>
        <div
          style={{
            fontSize: 30,
            fontWeight: 950,
            color: accent,
          }}
        >
          👇
        </div>
      </div>
    </AbsoluteFill>
  );
};

