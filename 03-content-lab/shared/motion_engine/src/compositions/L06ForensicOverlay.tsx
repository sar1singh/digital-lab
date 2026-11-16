import React from "react";
import { AbsoluteFill, staticFile, useCurrentFrame } from "remotion";

export interface L06OverlayProps {
  sceneId?: number;
}

interface SceneSpec {
  id: number;
  chapter: string;
  speaker: "owl" | "falcon";
  badge: string;
  badgeColor: string;
  title: string;
  subtitle: string;
  metrics?: { label: string; value: string; color: string }[];
  quote?: string;
  citation: string;
  imageFile?: string;
  imageCaption?: string;
  stampText?: string;
  stampColor?: string;
}

const SCENE_SPECS: Record<number, SceneSpec> = {
  1: {
    id: 1,
    chapter: "01 // THE EYEWITNESS DISASTER",
    speaker: "owl",
    badge: "🏛️ BURLINGTON, NORTH CAROLINA • 1984",
    badgeColor: "#C5A059",
    title: "SUPERIOR COURT DOCKET #84-CR-1102",
    subtitle: "Star Witness: Jennifer Thompson (22-Year-Old Honor Student)",
    quote: "\"I looked straight into the eyes of the judge and swore on a Bible. I was 100% certain that was the man who attacked me.\"",
    metrics: [
      { label: "SUBJECTIVE CERTAINTY", value: "100.0%", color: "#00F0FF" },
      { label: "TESTIMONY STATUS", value: "UNDER OATH", color: "#C5A059" },
      { label: "DOUBT REGISTERED", value: "0.0%", color: "#10B981" },
    ],
    citation: "SOURCE: STATE OF NORTH CAROLINA V. RONALD JUNIOR COTTON (1984)",
    imageFile: "images/memory_lie/Jennifer_Thompson_Cannino_and_Ronald_Cot.jpg",
    imageCaption: "JENNIFER THOMPSON & RONALD COTTON (ARCHIVAL)",
  },
  2: {
    id: 2,
    chapter: "01 // THE EYEWITNESS DISASTER",
    speaker: "owl",
    badge: "🚨 POLICE LINEUP IDENTIFICATION #4",
    badgeColor: "#FF2A4B",
    title: "SENTENCED TO LIFE + 54 YEARS",
    subtitle: "Defendant: Ronald Junior Cotton • Burlington Police Dept.",
    quote: "She studied his face during the assault. She picked him out of a photo array and physical police lineup without hesitation.",
    metrics: [
      { label: "LINEUP SELECTION", value: "SUSPECT #4", color: "#FF2A4B" },
      { label: "PRISON SENTENCE", value: "LIFE + 54 YRS", color: "#FF2A4B" },
      { label: "PHYSICAL EVIDENCE", value: "EYEWITNESS ONLY", color: "#F59E0B" },
    ],
    citation: "SOURCE: ALAMANCE COUNTY COURT ARCHIVES // CONVICTION RECORD",
    imageFile: "images/memory_lie/dna_profiling.jpg",
    imageCaption: "PRE-DNA ERA: EYEWITNESS TESTIMONY OVERRULED ALIBIS",
    stampText: "GUILTY // LIFE",
    stampColor: "#FF2A4B",
  },
  3: {
    id: 3,
    chapter: "01 // THE EYEWITNESS DISASTER",
    speaker: "owl",
    badge: "🧬 1995 FORENSIC DNA EXONERATION",
    badgeColor: "#10B981",
    title: "70% OF DNA EXONERATIONS: EYEWITNESS ERROR",
    subtitle: "11 Years Served in Maximum Security Prison Before DNA Testing",
    quote: "Ronald Cotton was 100% innocent. Across 375+ DNA exonerations in the United States, 70% were caused by confident, calm, mistaken eyewitnesses.",
    metrics: [
      { label: "TIME WRONGFULLY SERVED", value: "11 YEARS", color: "#F59E0B" },
      { label: "DNA MATCH RESULT", value: "BOBBY POOLE", color: "#10B981" },
      { label: "FALSE CONVICTION RATE", value: "70% EYEWITNESS", color: "#FF2A4B" },
    ],
    citation: "SOURCE: THE INNOCENCE PROJECT // NATIONAL REGISTRY OF EXONERATIONS",
    imageFile: "images/memory_lie/GelDoc_DNA_gel_electrophoresis_photograp.jpg",
    imageCaption: "GELDOC DNA ELECTROPHORESIS EXCLUSION PROOF",
    stampText: "100% INNOCENT",
    stampColor: "#10B981",
  },
  4: {
    id: 4,
    chapter: "02 // THE 20-WATT SKULL",
    speaker: "falcon",
    badge: "🔍 POLYGRAPH & NEUROBIOLOGY AUDIT",
    badgeColor: "#00F0FF",
    title: "SHE PASSED EVERY POLYGRAPH TEST",
    subtitle: "Zero Deception Detected • Steady Heart Rate • Total Conviction",
    quote: "\"Jennifer Thompson wasn't lying. In her mind, she was viewing a sharp photograph. But your temporal lobe has zero camera lenses and zero MP4 folders.\"",
    metrics: [
      { label: "POLYGRAPH RESULT", value: "TRUTHFUL", color: "#10B981" },
      { label: "ANATOMICAL SSD", value: "NOT FOUND", color: "#FF2A4B" },
      { label: "STORED MP4 FILES", value: "0 BYTES", color: "#00F0FF" },
    ],
    citation: "SOURCE: COGNITIVE NEUROBIOLOGY OF EPISODIC MEMORY RETRIEVAL",
    imageFile: "images/memory_lie/Jennifer_Thompson_Cannino_and_Ronald_Cot.jpg",
    imageCaption: "PICKING COTTON: FORGIVENESS AFTER INJUSTICE",
  },
  5: {
    id: 5,
    chapter: "02 // THE 20-WATT SKULL",
    speaker: "owl",
    badge: "📱 THE SMARTPHONE CAMERA ROLL ILLUSION",
    badgeColor: "#E2FF00",
    title: "SILICON FLASH MEMORY vs. HUMAN WETWARE",
    subtitle: "Why Your 10th Birthday Party Was Never 'Saved' to Disk",
    quote: "You assume blowing out birthday candles writes an immutable file you can double-click decades later. In physics, that model is pure fantasy.",
    metrics: [
      { label: "SILICON STORAGE", value: "EXACT BIT ARRAYS", color: "#00F0FF" },
      { label: "HUMAN MEMORY", value: "LIVE SIMULATION", color: "#E2FF00" },
      { label: "WAIT, IT'S ALL FAKE?", value: "ALWAYS HAS BEEN", color: "#FF2A4B" },
    ],
    citation: "SOURCE: SCHACTER (2001) • THE SEVEN SINS OF MEMORY (HARVARD PRESS)",
    imageFile: "memes/always_has_been.png",
    imageCaption: "WAIT, MY MEMORIES ARE SIMULATIONS? ALWAYS HAVE BEEN.",
  },
  6: {
    id: 6,
    chapter: "02 // THE 20-WATT SKULL",
    speaker: "falcon",
    badge: "⚡ THERMODYNAMIC HARDWARE CONSTRAINTS",
    badgeColor: "#FF5500",
    title: "THE 20-WATT METABOLIC POWER BUDGET",
    subtitle: "86 Billion Neurons • 100 Trillion Synapses • Dim Refrigerator Bulb",
    quote: "Recording lossless 24fps raw video for 75 straight years across 100 trillion synapses would generate enough thermodynamic heat to boil your skull.",
    metrics: [
      { label: "BRAIN POWER DRAW", value: "20 WATTS", color: "#E2FF00" },
      { label: "NEURON COUNT", value: "86 BILLION", color: "#00F0FF" },
      { label: "SYNAPTIC LINKS", value: "100 TRILLION", color: "#FF5500" },
    ],
    citation: "SOURCE: LANDAUER'S PRINCIPLE & CORTICAL METABOLIC ENERGETICS",
    imageFile: "memes/this_is_fine.jpg",
    imageCaption: "YOUR 20W BRAIN IF IT TRIED TO RECORD LOSSLESS 4K RAW VIDEO",
  },
  7: {
    id: 7,
    chapter: "02 // THE 20-WATT SKULL",
    speaker: "owl",
    badge: "🧩 GENERATIVE FRAGMENT STITCHING",
    badgeColor: "#E2FF00",
    title: "HOW YOUR BRAIN FAKES A MEMORY ON THE FLY",
    subtitle: "Zero Archival Playback • 100% Real-Time Improvisation",
    quote: "Your brain grabs a fragment of strawberry frosting, a generic vibe of joy, and the smell of melted wax—and stitches them into a movie in real time.",
    metrics: [
      { label: "FRAGMENT 01", value: "FROSTING TASTE", color: "#FF2A4B" },
      { label: "FRAGMENT 02", value: "MELTED WAX SCENT", color: "#F59E0B" },
      { label: "SYNTHESIS ENGINE", value: "LIVE HALLUCINATION", color: "#E2FF00" },
    ],
    citation: "SOURCE: CONSTRUCTIVE EPISODIC SIMULATION HYPOTHESIS",
    imageFile: "memes/charlie_conspiracy.jpg",
    imageCaption: "YOUR HIPPOCAMPUS STITCHING 3 RANDOM CLUES INTO A 'MEMORY'",
  },
  8: {
    id: 8,
    chapter: "03 // THE HOLOGRAPHIC SHARD",
    speaker: "falcon",
    badge: "🔬 1948 OPTICAL INTERFERENCE BREAKTHROUGH",
    badgeColor: "#00F0FF",
    title: "DENNIS GABOR & THE INVENTION OF HOLOGRAPHY",
    subtitle: "Rejected by Mainstream Physics • 1971 Nobel Prize in Physics",
    quote: "Critics laughed at the idea that information could exist everywhere at once without a local address—until Gabor's equations proved optical holography.",
    metrics: [
      { label: "WAVEFRONT EQUATION", value: "I = |R + O|²", color: "#00F0FF" },
      { label: "PATENT FILING", value: "GB 685,286 (1948)", color: "#C5A059" },
      { label: "VINDICATION", value: "NOBEL PRIZE 1971", color: "#10B981" },
    ],
    citation: "SOURCE: GABOR, D. (1948) 'A NEW MICROSCOPIC PRINCIPLE', NATURE 161",
    imageFile: "images/memory_lie/dennis_gabor_portrait.jpg",
    imageCaption: "DENNIS GABOR (1900–1979) • NOBEL LAUREATE IN PHYSICS",
  },
  9: {
    id: 9,
    chapter: "03 // THE HOLOGRAPHIC SHARD",
    speaker: "falcon",
    badge: "🔨 THE SMASHED HOLOGRAM EXPERIMENT",
    badgeColor: "#10B981",
    title: "50 BROKEN SHARDS = 50 COMPLETE PICTURES",
    subtitle: "Cut a JPEG in Half -> Lose 50% • Smash a Hologram -> Keep 100%",
    quote: "Shine a coherent laser through any tiny broken sliver of a holographic glass plate, and you reconstruct the entire 3D family portrait intact.",
    metrics: [
      { label: "PAPER PHOTOGRAPH", value: "LOCALIZED PIXELS", color: "#FF2A4B" },
      { label: "OPTICAL HOLOGRAM", value: "NON-LOCAL WAVE", color: "#10B981" },
      { label: "SINGLE SHARD OUTPUT", value: "100% SCENE (SOFT RES)", color: "#00F0FF" },
    ],
    citation: "SOURCE: OPTICAL DIFFRACTION & WAVEFRONT RECONSTRUCTION PHYSICS",
    imageFile: "images/memory_lie/holography_diagram.jpg",
    imageCaption: "HOLOGRAPHIC WAVEFRONT INTERFERENCE RECONSTRUCTION",
  },
  10: {
    id: 10,
    chapter: "03 // THE HOLOGRAPHIC SHARD",
    speaker: "owl",
    badge: "🧠 HOLONOMIC BRAIN ARCHITECTURE",
    badgeColor: "#C5A059",
    title: "WHY CORTICAL SURGERY DOESN'T DELETE SINGLE YEARS",
    subtitle: "Karl Pribram's Holonomic Model • Distributed Synaptic Weights",
    quote: "When neurosurgeons removed cortical tissue to treat epilepsy, patients never forgot a specific year or person. Memories are ripples across millions of synapses.",
    metrics: [
      { label: "STORAGE TOPOLOGY", value: "DISTRIBUTED MESH", color: "#C5A059" },
      { label: "ISOLATED FILE LOSS", value: "0% OBSERVED", color: "#10B981" },
      { label: "NEURAL MECHANISM", value: "PHASE INTERFERENCE", color: "#00F0FF" },
    ],
    citation: "SOURCE: PRIBRAM, K. H. (1991) 'BRAIN AND PERCEPTION: HOLONOMY'",
    imageFile: "images/memory_lie/hippocampus_brain.jpg",
    imageCaption: "GRAY'S ANATOMY FIG. 739: HIPPOCAMPAL & CORTICAL NETWORK",
  },
  11: {
    id: 11,
    chapter: "03 // THE HOLOGRAPHIC SHARD",
    speaker: "falcon",
    badge: "⚠️ CRITICAL WETWARE SECURITY LOOPHOLE",
    badgeColor: "#FF2A4B",
    title: "READING A MEMORY PHYSICALLY ALTERS IT",
    subtitle: "Digital Disk: Non-Destructive Read • Human Brain: Destructive Read",
    quote: "In a computer, opening a file leaves the disk untouched. In a holographic neural net, recalling a memory unlocks and rewires its physical structure.",
    metrics: [
      { label: "SSD FILE READ", value: "READ-ONLY LOCK", color: "#10B981" },
      { label: "HUMAN RECALL", value: "WRITE-ENABLED", color: "#FF2A4B" },
      { label: "CORRUPTION RISK", value: "100% ON ACCESS", color: "#F59E0B" },
    ],
    citation: "SOURCE: SYNAPTIC PLASTICITY & RETRIEVAL-INDUCED DISTORTION",
    imageFile: "memes/surprised_pikachu.jpg",
    imageCaption: "WHEN OPENING A MEMORY FILE ACCIDENTALLY UNLOCKS WRITE-MODE",
    stampText: "VULNERABLE",
    stampColor: "#FF2A4B",
  },
  12: {
    id: 12,
    chapter: "04 // LOST IN THE MALL",
    speaker: "owl",
    badge: "📋 1995 LANDMARK PSYCHOLOGICAL STUDY",
    badgeColor: "#00F0FF",
    title: "ELIZABETH LOFTUS: 'LOST IN THE MALL'",
    subtitle: "3 True Childhood Stories + 1 Completely Fabricated Lie",
    quote: "Loftus secretly partnered with subjects' parents to gather three real childhood events—a road trip, a beach visit, a broken bike—and slipped in a fake fourth story.",
    metrics: [
      { label: "STORIES 1–3", value: "VERIFIED TRUE", color: "#10B981" },
      { label: "STORY #4", value: "100% PLANTED LIE", color: "#FF2A4B" },
      { label: "COERCION USED", value: "ZERO (3 CHATS)", color: "#00F0FF" },
    ],
    citation: "SOURCE: LOFTUS & PICKRELL (1995), PSYCHIATRIC ANNALS 25(12)",
    imageFile: "images/memory_lie/elizabeth_loftus_portrait.jpg",
    imageCaption: "DR. ELIZABETH LOFTUS • DISTINGUISHED PROFESSOR OF COGNITIVE SCIENCE",
  },
  13: {
    id: 13,
    chapter: "04 // LOST IN THE MALL",
    speaker: "falcon",
    badge: "🎠 THE MANUFACTURED FALSE SCRIPT",
    badgeColor: "#F59E0B",
    title: "INJECTING A FAKE TRAUMA AT AGE FIVE",
    subtitle: "Crowded Shopping Mall • Crying Near Carousel • Elderly Stranger",
    quote: "Subjects were told they got lost at age 5, cried by a carousel, and were rescued by an elderly woman wearing a blue flannel shirt. Initially, they said: 'I don't recall.'",
    metrics: [
      { label: "FAKE SETTING", value: "SHOPPING MALL", color: "#F59E0B" },
      { label: "PLANTED DETAIL", value: "BLUE FLANNEL SHIRT", color: "#00F0FF" },
      { label: "DAY 1 RESPONSE", value: "NO MEMORY", color: "#94A3B8" },
    ],
    citation: "SOURCE: EXPERIMENTAL FALSE MEMORY IMPLANTATION PROTOCOL",
    imageFile: "memes/panik_kalm_panik.png",
    imageCaption: "DAY 1: 'NEVER HAPPENED' -> DAY 3: 'I REMEMBER HER FLANNEL SHIRT!'",
  },
  14: {
    id: 14,
    chapter: "04 // LOST IN THE MALL",
    speaker: "owl",
    badge: "🤡 25% FULL HALLUCINATION ADOPTION",
    badgeColor: "#FF2A4B",
    title: "1 IN 4 ADULTS INVENTED SENSORY DETAILS",
    subtitle: "Describing the Flannel Texture & Ice Cream That Never Existed",
    quote: "After just three casual interviews, 25% of healthy adults swore the fake event was real—volunteering the rough feel of her flannel shirt and the taste of ice cream!",
    metrics: [
      { label: "FALSE MEMORY RATE", value: "25% OF ADULTS", color: "#FF2A4B" },
      { label: "SENSORY HALLUCINATION", value: "FLANNEL & ICE CREAM", color: "#E2FF00" },
      { label: "SUBJECTIVE BELIEF", value: "GOSPEL TRUTH", color: "#00F0FF" },
    ],
    citation: "SOURCE: LOFTUS (1995) • EMPIRICAL CONFABULATION VERIFICATION",
    imageFile: "memes/clown_makeup.jpg",
    imageCaption: "OUR BRAIN CONFIDENTLY INVENTING FLANNEL SHIRT TEXTURES",
  },
  15: {
    id: 15,
    chapter: "04 // LOST IN THE MALL",
    speaker: "falcon",
    badge: "🔄 THE IMAGINATION INFLATION BUG",
    badgeColor: "#00F0FF",
    title: "HYPOTHETICAL SIMULATION -> SAVED AS HISTORY",
    subtitle: "Why Asking 'Do You Remember?' Rewrites the Neural Ledger",
    quote: "Every time the researcher asked 'Do you remember the mall?', the brain simulated the scene to check—and then accidentally saved that simulation as a real memory.",
    metrics: [
      { label: "STEP 1: PROMPT", value: "RUN SIMULATION", color: "#00F0FF" },
      { label: "STEP 2: GLITCH", value: "SOURCE AMNESIA", color: "#F59E0B" },
      { label: "STEP 3: COMMIT", value: "OVERWRITE PAST", color: "#FF2A4B" },
    ],
    citation: "SOURCE: SOURCE MONITORING FRAMEWORK & IMAGINATION INFLATION",
    imageFile: "memes/scooby_doo_mask_reveal.jpg",
    imageCaption: "UNMASKING A 'VIVID MEMORY' TO FIND A RECENT IMAGINATION RUN",
  },
  16: {
    id: 16,
    chapter: "05 // MEMORY RECONSOLIDATION",
    speaker: "owl",
    badge: "💣 21ST-CENTURY NEUROSCIENCE BOMBSHELL",
    badgeColor: "#E2FF00",
    title: "THE MOLECULAR MECHANISM OF THE REWRITE",
    subtitle: "Karim Nader, Glenn Schafe & Joseph LeDoux (Nature, 2000)",
    quote: "For decades, textbooks claimed consolidated memories were permanent concrete. In 2000, Karim Nader proved that remembering physically melts the concrete.",
    metrics: [
      { label: "LANDMARK PAPER", value: "NATURE VOL. 406", color: "#E2FF00" },
      { label: "DISCOVERY", value: "RECONSOLIDATION", color: "#00F0FF" },
      { label: "DOGMA SHATTERED", value: "PERMANENT STORAGE", color: "#FF2A4B" },
    ],
    citation: "SOURCE: NADER, SCHAFE & LEDOUX (2000), NATURE 406, 722–726",
    imageFile: "images/memory_lie/hippocampus_brain.jpg",
    imageCaption: "AMYGDALA & HIPPOCAMPAL SYNAPTIC CONSOLIDATION CIRCUIT",
  },
  17: {
    id: 17,
    chapter: "05 // MEMORY RECONSOLIDATION",
    speaker: "owl",
    badge: "🧪 PROTEIN SYNTHESIS DESTABILIZATION",
    badgeColor: "#FF2A4B",
    title: "3 TO 5 HOURS OF MALLEABLE LIQUID CLAY",
    subtitle: "You Never Remember the Event — Only the Last Time You Remembered It",
    quote: "Retrieving a memory dissolves its protein bonds for 3–5 hours. Your current mood, anxiety, or friend's comment gets baked in before new proteins re-save it overnight.",
    metrics: [
      { label: "LABILE WINDOW", value: "3 TO 5 HOURS", color: "#FF2A4B" },
      { label: "DRIFT PER RECALL", value: "+5% DISTORTION", color: "#F59E0B" },
      { label: "ORIGINAL FILE", value: "OVERWRITTEN", color: "#00F0FF" },
    ],
    citation: "SOURCE: DE NOVO PROTEIN SYNTHESIS IN AMYGDALA & HIPPOCAMPUS",
    imageFile: "memes/the_scroll_of_truth.jpg",
    imageCaption: "YOU ONLY EVER REMEMBER YOUR LAST RECONSOLIDATED DRAFT",
    stampText: "OVERWRITTEN",
    stampColor: "#FF2A4B",
  },
  18: {
    id: 18,
    chapter: "05 // MEMORY RECONSOLIDATION",
    speaker: "falcon",
    badge: "🖨️ THE 25TH-GENERATION PHOTOCOPY TRAP",
    badgeColor: "#00F0FF",
    title: "YOUR CHILDHOOD IS A HOLLYWOOD SCREENPLAY",
    subtitle: "Middle-School Soccer Goal: Pushing Defenders 2 Feet Back Every Year",
    quote: "Every time you brag about your teenage triumph over drinks, the defenders move further back and the sunset gets more golden. By 35, you're defending pure fiction.",
    metrics: [
      { label: "AGE 12 REALITY", value: "LUCKY SHIN KICK", color: "#10B981" },
      { label: "25 RECALL CYCLES", value: "30-YARD BICYCLE KICK", color: "#E2FF00" },
      { label: "FIDELITY REMAINING", value: "< 20% ACCURATE", color: "#FF2A4B" },
    ],
    citation: "SOURCE: AUTOBIOGRAPHICAL MEMORY DRIFT & SELF-ENHANCEMENT BIAS",
    imageFile: "memes/they_re_the_same_picture.jpg",
    imageCaption: "YOUR BRAIN COMPARING THE 1999 EVENT TO THE 25TH PHOTOCOPY",
  },
  19: {
    id: 19,
    chapter: "06 // FORTUNE-TELLERS",
    speaker: "owl",
    badge: "🌍 THE EVOLUTIONARY PARADOX",
    badgeColor: "#C5A059",
    title: "WHY DIDN'T EVOLUTION BUILD READ-ONLY MEMORY?",
    subtitle: "If Accuracy Matters, Why Is Human Wetware So Corruptible?",
    quote: "Why would natural selection spend millions of years engineering a brain that systematically corrupts its own historical database?",
    metrics: [
      { label: "POP ASSUMPTION", value: "DESIGN DEFECT", color: "#FF2A4B" },
      { label: "BIOLOGICAL REALITY", value: "SURVIVAL FEATURE", color: "#10B981" },
      { label: "OPTIMIZATION TARGET", value: "TOMORROW MORNING", color: "#E2FF00" },
    ],
    citation: "SOURCE: EVOLUTIONARY COGNITIVE ARCHITECTURE",
    imageFile: "images/memory_lie/dna_profiling.jpg",
    imageCaption: "EVOLUTIONARY GENETICS: SURVIVAL OVER ARCHIVAL PRECISION",
  },
  20: {
    id: 20,
    chapter: "06 // FORTUNE-TELLERS",
    speaker: "falcon",
    badge: "🦁 SAVANNA SURVIVAL MATHEMATICS",
    badgeColor: "#FF5500",
    title: "THE ACACIA TREE LION vs. THE RIVERBANK LEOPARD",
    subtitle: "Evolution Doesn't Care About Court Testimony — It Cares About Tomorrow",
    quote: "An exact photographic memory of a lion behind one specific acacia tree is useless—because the next predator will be a leopard crouching by a dark riverbank.",
    metrics: [
      { label: "PAST ARCHIVE", value: "ACACIA TREE LION", color: "#94A3B8" },
      { label: "NEXT THREAT", value: "RIVERBANK LEOPARD", color: "#FF5500" },
      { label: "RIGID PHOTO MEMORY", value: "FATAL INFLEXIBILITY", color: "#FF2A4B" },
    ],
    citation: "SOURCE: ADAPTIVE PROSPECTIVE SIMULATION IN HOMINID EVOLUTION",
    imageFile: "memes/bell_curve.png",
    imageCaption: "EVOLUTIONARY FITNESS: RIGID PHOTO ARCHIVE VS. PREDICTIVE ENGINE",
  },
  21: {
    id: 21,
    chapter: "06 // FORTUNE-TELLERS",
    speaker: "owl",
    badge: "🧱 FLEXIBLE NEURAL LEGO BRICKS",
    badgeColor: "#10B981",
    title: "WE DIDN'T EVOLVE TO BE HISTORIANS",
    subtitle: "We Evolved to Be Fortune-Tellers • Simulating 10 Futures Before Breakfast",
    quote: "Your brain keeps the past pliable so it can shatter experiences into modular Lego bricks, recombine them on demand, and predict ten hypothetical futures.",
    metrics: [
      { label: "RIGID ARCHIVE", value: "FRAGILE IN NEW ENV", color: "#FF2A4B" },
      { label: "MODULAR BRICKS", value: "INFINITE RECOMBINATION", color: "#10B981" },
      { label: "TRUE PURPOSE", value: "FUTURE PREDICTION", color: "#00F0FF" },
    ],
    citation: "SOURCE: SCHACTER & ADDIS (2007) 'THE COGNITIVE NEUROSCIENCE OF FUTURE THINKING'",
    imageFile: "memes/roll_safe_think_about_it.jpg",
    imageCaption: "CAN'T FAIL AT HISTORY IF YOUR BRAIN WAS BUILT FOR FORTUNE-TELLING",
  },
  22: {
    id: 22,
    chapter: "06 // FORTUNE-TELLERS",
    speaker: "falcon",
    badge: "🌙 THE 2:00 AM ARGUMENT REALITY CHECK",
    badgeColor: "#00F0FF",
    title: "PUT THE EGO DOWN IN YOUR NEXT ARGUMENT",
    subtitle: "Spouse • Sibling • Co-Founder: Nobody Owns the Master Tape",
    quote: "When you argue about what was said three years ago, you aren't comparing two videotapes. You are comparing two fictional novels written by two neural networks.",
    metrics: [
      { label: "YOUR MEMORY", value: "FICTIONAL NOVEL A", color: "#00F0FF" },
      { label: "THEIR MEMORY", value: "FICTIONAL NOVEL B", color: "#FF5500" },
      { label: "MASTER VIDEOTAPE", value: "DOES NOT EXIST", color: "#E2FF00" },
    ],
    citation: "SOURCE: INTERPERSONAL MEMORY DISCORDANCE & SHARED CONFABULATION",
    imageFile: "memes/spiderman_pointing_at_spiderman.jpg",
    imageCaption: "TWO HUMANS AT 2:00 AM DEFENDING THEIR 15TH-GEN HALLUCINATIONS",
  },
  23: {
    id: 23,
    chapter: "06 // THE REALITY CHECK",
    speaker: "owl",
    badge: "👁️ THINKLATE FINAL REALITY CHECK",
    badgeColor: "#E2FF00",
    title: "YOU INVENT YOUR PAST EVERY MORNING",
    subtitle: "And the Kindest Thing Your Brain Ever Did Was Make Sure You'd Never Notice",
    quote: "\"You don't own your past. You invent it every time you open your eyes. Subscribe to ThinkLate for first-principles breakdowns of how reality actually works.\"",
    metrics: [
      { label: "PAST OWNERSHIP", value: "ILLUSION", color: "#FF2A4B" },
      { label: "DAILY REBOOT", value: "LIVE SIMULATION", color: "#00F0FF" },
      { label: "CHANNEL", value: "@WETHINKLATE", color: "#E2FF00" },
    ],
    citation: "THINKLATE MEDIA // PILLAR D: PHILOSOPHY OF MIND & COGNITIVE PHYSICS",
    imageFile: "memes/absolute_cinema.png",
    imageCaption: "YOUR BRAIN DIRECTING A FRESH SIMULATION EVERY SINGLE MORNING",
    stampText: "CASE CLOSED",
    stampColor: "#E2FF00",
  },
};

export const L06ForensicOverlay: React.FC<L06OverlayProps> = ({ sceneId }) => {
  const frame = useCurrentFrame();
  const resolvedId = sceneId || frame + 1;
  const spec = SCENE_SPECS[resolvedId] || SCENE_SPECS[1];
  const isOwl = spec.speaker === "owl";
  const hostAccent = isOwl ? "#C5A059" : "#00F0FF";
  const hostName = isOwl ? "EDDY THINKLATE" : "VERA VANCE";
  const hostRole = isOwl ? "FOUNDER & LEAD HOST // @WETHINKLATE" : "FORENSIC INVESTIGATOR // RECEIPTS";
  const hostSprite = isOwl
    ? staticFile("characters/mr_owl_executive_full.png")
    : staticFile("characters/falcon_forensic_full.png");

  return (
    <AbsoluteFill
      style={{
        backgroundColor: "transparent",
        fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif",
        color: "#FFFFFF",
        overflow: "hidden",
      }}
    >
      {/* 1. TOP DOCUMENTARY HEADER BAR */}
      <div
        style={{
          position: "absolute",
          top: 38,
          left: 56,
          right: 56,
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
        }}
      >
        <div
          style={{
            display: "flex",
            alignItems: "center",
            gap: 14,
            backgroundColor: "rgba(6, 10, 20, 0.85)",
            border: "1px solid rgba(255,255,255,0.18)",
            padding: "10px 22px",
            borderRadius: 30,
            boxShadow: "0 10px 30px rgba(0,0,0,0.7)",
          }}
        >
          <div
            style={{
              width: 12,
              height: 12,
              borderRadius: "50%",
              backgroundColor: "#E2FF00",
              boxShadow: "0 0 12px #E2FF00",
            }}
          />
          <span
            style={{
              fontSize: 17,
              fontWeight: 900,
              letterSpacing: 3,
              color: "#E2E8F0",
            }}
          >
            THINKLATE // {spec.chapter}
          </span>
        </div>

        <div
          style={{
            backgroundColor: "rgba(6, 10, 20, 0.85)",
            border: `1px solid ${spec.badgeColor}`,
            padding: "10px 22px",
            borderRadius: 30,
            fontSize: 16,
            fontWeight: 800,
            letterSpacing: 2.5,
            color: spec.badgeColor,
            boxShadow: "0 10px 30px rgba(0,0,0,0.7)",
          }}
        >
          {spec.badge}
        </div>
      </div>

      {/* 2. MAIN WIDESCREEN FORENSIC EVIDENCE DOSSIER CARD */}
      <div
        style={{
          position: "absolute",
          top: 118,
          left: 56,
          right: 56,
          bottom: 195,
          display: "flex",
          gap: 32,
          alignItems: "stretch",
        }}
      >
        {/* Left / Primary Dossier Column */}
        <div
          style={{
            flex: spec.imageFile ? 1.35 : 1,
            backgroundColor: "rgba(8, 13, 26, 0.86)",
            border: `2px solid ${spec.badgeColor}66`,
            borderRadius: 24,
            padding: "36px 42px",
            display: "flex",
            flexDirection: "column",
            justifyContent: "space-between",
            boxShadow: "0 25px 70px rgba(0,0,0,0.85), inset 0 1px 0 rgba(255,255,255,0.12)",
            position: "relative",
            overflow: "hidden",
          }}
        >
          {/* Top Accent Line */}
          <div
            style={{
              position: "absolute",
              top: 0,
              left: 0,
              right: 0,
              height: 5,
              background: `linear-gradient(90deg, ${spec.badgeColor}, transparent)`,
            }}
          />

          <div>
            <div
              style={{
                fontSize: 16,
                fontWeight: 800,
                color: "#94A3B8",
                letterSpacing: 3,
                textTransform: "uppercase",
                marginBottom: 10,
              }}
            >
              FORENSIC EXHIBIT #{String(spec.id).padStart(2, "0")} // VERIFIED PRIMARY RECORD
            </div>

            <div
              style={{
                fontSize: 42,
                fontWeight: 950,
                color: "#FFFFFF",
                lineHeight: 1.12,
                letterSpacing: -0.5,
                marginBottom: 10,
              }}
            >
              {spec.title}
            </div>

            <div
              style={{
                fontSize: 22,
                fontWeight: 700,
                color: spec.badgeColor,
                marginBottom: 24,
              }}
            >
              {spec.subtitle}
            </div>

            {spec.quote && (
              <div
                style={{
                  backgroundColor: "rgba(255, 255, 255, 0.04)",
                  borderLeft: `5px solid ${spec.badgeColor}`,
                  padding: "18px 24px",
                  borderRadius: "0 14px 14px 0",
                  fontSize: 23,
                  lineHeight: 1.42,
                  color: "#F1F5F9",
                  fontStyle: "italic",
                  marginBottom: 24,
                }}
              >
                {spec.quote}
              </div>
            )}
          </div>

          {/* Metrics Row */}
          {spec.metrics && (
            <div
              style={{
                display: "grid",
                gridTemplateColumns: `repeat(${spec.metrics.length}, 1fr)`,
                gap: 18,
                marginTop: "auto",
              }}
            >
              {spec.metrics.map((m, idx) => (
                <div
                  key={idx}
                  style={{
                    backgroundColor: "rgba(3, 7, 15, 0.78)",
                    border: `1px solid ${m.color}55`,
                    borderRadius: 16,
                    padding: "16px 20px",
                  }}
                >
                  <div
                    style={{
                      fontSize: 13,
                      fontWeight: 800,
                      color: "#94A3B8",
                      letterSpacing: 2,
                      marginBottom: 6,
                    }}
                  >
                    {m.label}
                  </div>
                  <div
                    style={{
                      fontSize: 28,
                      fontWeight: 950,
                      color: m.color,
                      fontFamily: "monospace",
                    }}
                  >
                    {m.value}
                  </div>
                </div>
              ))}
            </div>
          )}

          {/* Citation Footer */}
          <div
            style={{
              marginTop: 20,
              paddingTop: 14,
              borderTop: "1px solid rgba(255,255,255,0.1)",
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
              fontSize: 14,
              fontWeight: 700,
              color: "#64748B",
              letterSpacing: 1.5,
            }}
          >
            <span>{spec.citation}</span>
            <span style={{ color: "#E2FF00" }}>● EMPIRICAL VERIFIED</span>
          </div>

          {/* Optional Forensic Stamp */}
          {spec.stampText && (
            <div
              style={{
                position: "absolute",
                top: 34,
                right: 34,
                border: `5px solid ${spec.stampColor || "#FF2A4B"}`,
                color: spec.stampColor || "#FF2A4B",
                padding: "8px 22px",
                fontSize: 28,
                fontWeight: 950,
                letterSpacing: 4,
                transform: "rotate(-8deg)",
                backgroundColor: "rgba(5, 8, 15, 0.9)",
                boxShadow: `0 0 30px ${spec.stampColor || "#FF2A4B"}66`,
              }}
            >
              {spec.stampText}
            </div>
          )}
        </div>

        {/* Right Column: Archival Image / Diagram OR Co-Host Dossier */}
        {spec.imageFile ? (
          <div
            style={{
              flex: 0.75,
              backgroundColor: "rgba(8, 13, 26, 0.88)",
              border: "2px solid rgba(255,255,255,0.2)",
              borderRadius: 24,
              padding: 22,
              display: "flex",
              flexDirection: "column",
              justifyContent: "space-between",
              boxShadow: "0 25px 70px rgba(0,0,0,0.85)",
            }}
          >
            <div
              style={{
                width: "100%",
                height: "84%",
                borderRadius: 16,
                overflow: "hidden",
                border: "1px solid rgba(255,255,255,0.15)",
                position: "relative",
                backgroundColor: "#050811",
              }}
            >
              <img
                src={staticFile(spec.imageFile)}
                alt={spec.imageCaption || "Archival Evidence"}
                style={{
                  width: "100%",
                  height: "100%",
                  objectFit: "cover",
                  filter: "contrast(1.1) brightness(0.96)",
                }}
              />
              <div
                style={{
                  position: "absolute",
                  top: 12,
                  left: 12,
                  backgroundColor: "rgba(0,0,0,0.8)",
                  border: `1px solid ${spec.badgeColor}`,
                  color: spec.badgeColor,
                  padding: "4px 12px",
                  borderRadius: 6,
                  fontSize: 12,
                  fontWeight: 900,
                  letterSpacing: 2,
                }}
              >
                ARCHIVAL PLATE
              </div>
            </div>
            <div
              style={{
                textAlign: "center",
                fontSize: 15,
                fontWeight: 800,
                color: "#CBD5E1",
                letterSpacing: 1.5,
                paddingTop: 10,
              }}
            >
              {spec.imageCaption}
            </div>
          </div>
        ) : (
          /* Co-Host Raptor Syndicate Visual Anchor Card (<=18% screen footprint) */
          <div
            style={{
              flex: 0.48,
              backgroundColor: "rgba(8, 13, 26, 0.86)",
              border: `2px solid ${hostAccent}66`,
              borderRadius: 24,
              padding: 24,
              display: "flex",
              flexDirection: "column",
              alignItems: "center",
              justifyContent: "center",
              boxShadow: "0 25px 70px rgba(0,0,0,0.85)",
              position: "relative",
            }}
          >
            <div
              style={{
                width: 240,
                height: 290,
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                marginBottom: 16,
              }}
            >
              <img
                src={hostSprite}
                alt={hostName}
                style={{
                  maxWidth: "100%",
                  maxHeight: "100%",
                  objectFit: "contain",
                  filter: `drop-shadow(0 12px 25px rgba(0,0,0,0.9))`,
                }}
              />
            </div>
            <div
              style={{
                fontSize: 22,
                fontWeight: 950,
                color: hostAccent,
                letterSpacing: 2,
                textAlign: "center",
              }}
            >
              {hostName}
            </div>
            <div
              style={{
                fontSize: 13,
                fontWeight: 800,
                color: "#94A3B8",
                letterSpacing: 2,
                marginTop: 4,
                textAlign: "center",
              }}
            >
              {hostRole}
            </div>
          </div>
        )}
      </div>
    </AbsoluteFill>
  );
};
