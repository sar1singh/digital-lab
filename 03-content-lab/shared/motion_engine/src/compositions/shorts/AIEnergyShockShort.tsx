import React from "react";
import {
  AbsoluteFill,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { WORDS_DATA, WordToken } from "./words_data";

export const AIEnergyShockShort: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();
  const currentTime = frame / fps;

  // -------------------------------------------------------------
  // 1. AMBIENT BACKGROUND & 3D PERSPECTIVE GRID (ZERO GAMEPLAY)
  // -------------------------------------------------------------
  const gridOffsetY = (frame * 1.5) % 60;
  const pulseOpacity = interpolate(
    Math.sin(frame * 0.08),
    [-1, 1],
    [0.15, 0.35]
  );

  // -------------------------------------------------------------
  // 2. KINETIC SUBTITLE ENGINE (HORMOZI / VOX ACTIVE PILL POP)
  // -------------------------------------------------------------
  // Find current active word index
  const activeWordIdx = WORDS_DATA.findIndex(
    (w) => currentTime >= w.start && currentTime <= w.end
  );

  // Determine current display chunk (2 to 3 words around active word)
  let chunkStartIndex = 0;
  if (activeWordIdx !== -1) {
    chunkStartIndex = Math.floor(activeWordIdx / 3) * 3;
  } else {
    // If between words, find last spoken word
    const lastSpoken = WORDS_DATA.map((w, idx) => ({ w, idx })).filter(
      (item) => item.w.end <= currentTime
    );
    if (lastSpoken.length > 0) {
      chunkStartIndex = Math.floor(lastSpoken[lastSpoken.length - 1].idx / 3) * 3;
    }
  }

  const currentChunk = WORDS_DATA.slice(chunkStartIndex, chunkStartIndex + 3);

  // -------------------------------------------------------------
  // 3. SCENE TIMING & COMPONENT SWITCHING
  // -------------------------------------------------------------
  // Scene 1: Frames 0 - 165 (0.00s - 5.50s) | The $20 Rate Hike
  // Scene 2: Frames 166 - 390 (5.50s - 13.00s) | The $1.5T Capex vs Grid
  // Scene 3: Frames 391 - 685 (13.00s - 22.80s) | PJM +800% Capacity Spike
  // Scene 4: Frames 686 - 1035 (22.80s - 34.50s) | PUCO Rate Socialization Docket
  // Scene 5: Frames 1036 - 1380 (34.50s - 46.00s) | Nov 3, 2026 Ballot Revolt
  // Scene 6: Frames 1381 - 1635 (46.00s - 54.50s) | Prompt vs Transformer Reality
  // Scene 7: Frames 1636 - 1788 (54.50s - 59.58s) | Climax: YOUR PAYCHECK

  return (
    <AbsoluteFill
      style={{
        backgroundColor: "#06080E",
        color: "#FFFFFF",
        fontFamily: "system-ui, -apple-system, sans-serif",
        overflow: "hidden",
      }}
    >
      {/* ========================================================= */}
      {/* LAYER 1: 3D PERSPECTIVE GRID & AMBIENT COLOR GRADIENTS     */}
      {/* ========================================================= */}
      <div
        style={{
          position: "absolute",
          inset: 0,
          background:
            "radial-gradient(circle at 50% 30%, rgba(20, 30, 55, 0.6) 0%, rgba(6, 8, 14, 0.95) 80%)",
        }}
      />

      {/* Moving Perspective Floor */}
      <div
        style={{
          position: "absolute",
          bottom: 0,
          left: "-50%",
          width: "200%",
          height: "65%",
          transform: "perspective(500px) rotateX(65deg)",
          transformOrigin: "bottom center",
          backgroundImage: `
            linear-gradient(to right, rgba(226, 255, 0, 0.12) 1px, transparent 1px),
            linear-gradient(to bottom, rgba(226, 255, 0, 0.12) 1px, transparent 1px)
          `,
          backgroundSize: "60px 60px",
          backgroundPosition: `0px ${gridOffsetY}px`,
          opacity: pulseOpacity,
          maskImage: "linear-gradient(to top, rgba(0,0,0,1) 20%, transparent 80%)",
          WebkitMaskImage:
            "linear-gradient(to top, rgba(0,0,0,1) 20%, transparent 80%)",
        }}
      />

      {/* Atmospheric Vignette & Film Noise Simulation */}
      <div
        style={{
          position: "absolute",
          inset: 0,
          boxShadow: "inset 0 0 160px rgba(0,0,0,0.85)",
          pointerEvents: "none",
        }}
      />

      {/* ========================================================= */}
      {/* LAYER 2: TOP TECHNICAL HUD / REGULATORY BANNER            */}
      {/* ========================================================= */}
      <div
        style={{
          position: "absolute",
          top: 100,
          left: 60,
          right: 60,
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          borderBottom: "1px solid rgba(255, 255, 255, 0.12)",
          paddingBottom: 16,
          zIndex: 30,
        }}
      >
        <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
          <div
            style={{
              width: 10,
              height: 10,
              borderRadius: "50%",
              backgroundColor: "#FF2A4B",
              boxShadow: "0 0 12px #FF2A4B",
            }}
          />
          <span
            style={{
              fontFamily: "monospace",
              fontSize: 20,
              letterSpacing: "0.15em",
              color: "#94A3B8",
              fontWeight: 700,
            }}
          >
            GRID STABILITY AUDIT // 2026
          </span>
        </div>
        <span
          style={{
            fontFamily: "monospace",
            fontSize: 20,
            color: "#E2FF00",
            fontWeight: 800,
            letterSpacing: "0.1em",
          }}
        >
          MIDTERMS: NOV 03
        </span>
      </div>

      {/* ========================================================= */}
      {/* LAYER 3: DYNAMIC 3D EVIDENCE PLATES (SCENE-BY-SCENE)       */}
      {/* ========================================================= */}
      <div
        style={{
          position: "absolute",
          top: 260,
          left: 60,
          right: 60,
          height: 900,
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          zIndex: 20,
        }}
      >
        {/* SCENE 1 (0 - 165): THE $20/MO UTILITY SURCHARGE COUNTER */}
        {frame < 166 && (
          <Scene1RateHike frame={frame} fps={fps} />
        )}

        {/* SCENE 2 (166 - 390): $1.5 TRILLION AI CAPEX VS 125 GW GRID */}
        {frame >= 166 && frame < 391 && (
          <Scene2CapexSplit frame={frame - 166} fps={fps} />
        )}

        {/* SCENE 3 (391 - 685): PJM WHOLESALE CAPACITY +800% LINE CHART */}
        {frame >= 391 && frame < 686 && (
          <Scene3CapacityChart frame={frame - 391} fps={fps} />
        )}

        {/* SCENE 4 (686 - 1035): PUCO DOCKET & REDACTION SOCIALIZATION */}
        {frame >= 686 && frame < 1036 && (
          <Scene4DocketRedaction frame={frame - 686} fps={fps} />
        )}

        {/* SCENE 5 (1036 - 1380): NOV 3 ELECTION DAY BALLOT REVOLT */}
        {frame >= 1036 && frame < 1381 && (
          <Scene5ElectionBallot frame={frame - 1036} fps={fps} />
        )}

        {/* SCENE 6 (1381 - 1635): AI PROMPT VS POWER TRANSFORMER REALITY */}
        {frame >= 1381 && frame < 1636 && (
          <Scene6PromptVsTransformer frame={frame - 1381} fps={fps} />
        )}

        {/* SCENE 7 (1636 - 1788): CLIMAX SLAM: YOUR PAYCHECK */}
        {frame >= 1636 && (
          <Scene7ClimaxSlam frame={frame - 1636} fps={fps} />
        )}
      </div>

      {/* ========================================================= */}
      {/* LAYER 4: WORD-BY-WORD KINETIC CAPTIONS (HORMOZI / VOX)     */}
      {/* ========================================================= */}
      <div
        style={{
          position: "absolute",
          bottom: 240,
          left: 60,
          right: 60,
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          gap: 16,
          zIndex: 40,
        }}
      >
        {currentChunk.map((token, i) => {
          const isCurrent =
            currentTime >= token.start && currentTime <= token.end;
          const isSpecial =
            token.word.includes("$") ||
            token.word.toLowerCase().includes("trillion") ||
            token.word.toLowerCase().includes("800") ||
            token.word.toLowerCase().includes("paycheck") ||
            token.word.toLowerCase().includes("billions");

          const enterFrame = token.start * fps;
          const wordSpring = spring({
            frame: frame - enterFrame,
            fps,
            config: { damping: 12, mass: 0.5, stiffness: 180 },
          });

          const scale = isCurrent ? interpolate(wordSpring, [0, 1], [0.8, 1.15]) : 1.0;

          return (
            <div
              key={`${token.start}-${i}`}
              style={{
                display: "inline-flex",
                alignItems: "center",
                padding: isCurrent ? "10px 22px" : "8px 12px",
                borderRadius: 14,
                backgroundColor: isCurrent
                  ? isSpecial
                    ? "#FF2A4B"
                    : "#E2FF00"
                  : "transparent",
                color: isCurrent ? "#000000" : "#FFFFFF",
                fontSize: isCurrent ? 52 : 46,
                fontWeight: 900,
                letterSpacing: "-0.02em",
                transform: `scale(${scale})`,
                boxShadow: isCurrent
                  ? isSpecial
                    ? "0 0 35px rgba(255, 42, 75, 0.6)"
                    : "0 0 35px rgba(226, 255, 0, 0.6)"
                  : "none",
                transition: "all 0.06s ease-out",
                textShadow: isCurrent ? "none" : "0 4px 12px rgba(0,0,0,0.8)",
              }}
            >
              {token.word}
            </div>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};

// =====================================================================
// SCENE 1: RATE HIKE PENALTY LIVE SPRING COUNTER
// =====================================================================
const Scene1RateHike: React.FC<{ frame: number; fps: number }> = ({ frame, fps }) => {
  const cardSpring = spring({
    frame,
    fps,
    config: { damping: 14, mass: 0.8, stiffness: 120 },
  });
  const cardScale = interpolate(cardSpring, [0, 1], [0.85, 1.0]);
  const cardY = interpolate(cardSpring, [0, 1], [60, 0]);

  // Live Counter Animation (0 -> 20.00)
  const counterProgress = spring({
    frame: frame - 12,
    fps,
    config: { damping: 20, mass: 1, stiffness: 80 },
  });
  const currentVal = (interpolate(counterProgress, [0, 1], [0, 20])).toFixed(2);

  // Red Stamp Slam at Frame 60
  const stampSpring = spring({
    frame: frame - 45,
    fps,
    config: { damping: 10, mass: 0.6, stiffness: 220 },
  });
  const stampScale = interpolate(stampSpring, [0, 1], [2.4, 1.0]);
  const stampOpacity = interpolate(stampSpring, [0, 1], [0, 1]);

  return (
    <div
      style={{
        width: "100%",
        maxWidth: 960,
        backgroundColor: "rgba(13, 18, 31, 0.88)",
        backdropFilter: "blur(28px)",
        WebkitBackdropFilter: "blur(28px)",
        borderRadius: 36,
        border: "2px solid rgba(226, 255, 0, 0.35)",
        boxShadow: "0 25px 60px rgba(0, 0, 0, 0.7), 0 0 40px rgba(226, 255, 0, 0.15)",
        padding: "50px 60px",
        transform: `translateY(${cardY}px) scale(${cardScale})`,
        position: "relative",
        overflow: "hidden",
      }}
    >
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <span
          style={{
            fontFamily: "monospace",
            fontSize: 22,
            fontWeight: 800,
            color: "#FF2A4B",
            letterSpacing: "0.15em",
            backgroundColor: "rgba(255, 42, 75, 0.15)",
            padding: "8px 18px",
            borderRadius: 10,
            border: "1px solid rgba(255, 42, 75, 0.4)",
          }}
        >
          RATEPAYER SURCHARGE
        </span>
        <span style={{ fontFamily: "monospace", fontSize: 20, color: "#64748B" }}>
          PJM CAPACITY AUCTION
        </span>
      </div>

      <div style={{ textAlign: "center", margin: "45px 0" }}>
        <div style={{ fontSize: 24, letterSpacing: "0.2em", color: "#94A3B8", fontWeight: 700 }}>
          AVERAGE RESIDENTIAL MONTHLY HIKE
        </div>
        <div
          style={{
            fontSize: 120,
            fontWeight: 900,
            color: "#E2FF00",
            fontFamily: "monospace",
            letterSpacing: "-0.04em",
            margin: "15px 0",
            textShadow: "0 0 45px rgba(226, 255, 0, 0.45)",
          }}
        >
          +${currentVal}
          <span style={{ fontSize: 36, color: "#94A3B8" }}> / mo</span>
        </div>
        <div style={{ fontSize: 24, color: "#CBD5E1", maxWidth: 700, margin: "0 auto", lineHeight: 1.4 }}>
          Direct transmission charge added to household bills to power corporate AI data centers.
        </div>
      </div>

      {/* Red Rubber Stamp Slam */}
      {frame >= 45 && (
        <div
          style={{
            position: "absolute",
            bottom: 40,
            right: 60,
            transform: `scale(${stampScale}) rotate(-14deg)`,
            opacity: stampOpacity,
            border: "5px solid #FF2A4B",
            color: "#FF2A4B",
            padding: "12px 28px",
            fontSize: 34,
            fontWeight: 900,
            letterSpacing: "0.15em",
            borderRadius: 16,
            backgroundColor: "rgba(255, 42, 75, 0.15)",
            boxShadow: "0 0 35px rgba(255, 42, 75, 0.5)",
          }}
        >
          GRID LEVY APPLIED
        </div>
      )}
    </div>
  );
};

// =====================================================================
// SCENE 2: $1.5 TRILLION AI CAPEX VS 125 GW POWER CRISIS
// =====================================================================
const Scene2CapexSplit: React.FC<{ frame: number; fps: number }> = ({ frame, fps }) => {
  const s = spring({ frame, fps, config: { damping: 14, mass: 0.8, stiffness: 120 } });
  const scale = interpolate(s, [0, 1], [0.9, 1.0]);

  return (
    <div
      style={{
        width: "100%",
        maxWidth: 960,
        display: "grid",
        gridTemplateColumns: "1fr 1fr",
        gap: 30,
        transform: `scale(${scale})`,
      }}
    >
      {/* Left: Big Tech Capex */}
      <div
        style={{
          backgroundColor: "rgba(13, 18, 31, 0.9)",
          borderRadius: 32,
          padding: 45,
          border: "2px solid rgba(6, 182, 212, 0.4)",
          boxShadow: "0 20px 50px rgba(0,0,0,0.6)",
        }}
      >
        <div style={{ color: "#06B6D4", fontFamily: "monospace", fontSize: 20, fontWeight: 800 }}>
          HYPERSCALER SPEND
        </div>
        <div style={{ fontSize: 76, fontWeight: 900, color: "#06B6D4", margin: "20px 0", fontFamily: "monospace" }}>
          $1.5T
        </div>
        <div style={{ fontSize: 22, color: "#94A3B8", lineHeight: 1.4 }}>
          Amazon, Google, Meta, & Microsoft AI data center commitments.
        </div>
      </div>

      {/* Right: Grid Power Crisis */}
      <div
        style={{
          backgroundColor: "rgba(13, 18, 31, 0.9)",
          borderRadius: 32,
          padding: 45,
          border: "2px solid rgba(255, 42, 75, 0.4)",
          boxShadow: "0 20px 50px rgba(0,0,0,0.6)",
        }}
      >
        <div style={{ color: "#FF2A4B", fontFamily: "monospace", fontSize: 20, fontWeight: 800 }}>
          PUBLIC GRID DRAW
        </div>
        <div style={{ fontSize: 76, fontWeight: 900, color: "#FF2A4B", margin: "20px 0", fontFamily: "monospace" }}>
          125 GW
        </div>
        <div style={{ fontSize: 22, color: "#94A3B8", lineHeight: 1.4 }}>
          Projected load by 2030 (Each gigawatt = 750,000 American homes).
        </div>
      </div>
    </div>
  );
};

// =====================================================================
// SCENE 3: PJM CAPACITY SPIKE (DRAWING SVG TRAJECTORY LINE)
// =====================================================================
const Scene3CapacityChart: React.FC<{ frame: number; fps: number }> = ({ frame, fps }) => {
  const lineProgress = interpolate(frame, [10, 80], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <div
      style={{
        width: "100%",
        maxWidth: 960,
        backgroundColor: "rgba(13, 18, 31, 0.92)",
        borderRadius: 36,
        padding: "45px 55px",
        border: "2px solid rgba(226, 255, 0, 0.3)",
      }}
    >
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <div>
          <div style={{ fontSize: 20, color: "#E2FF00", fontFamily: "monospace", fontWeight: 800 }}>
            WHOLESALE CAPACITY EXPLOSION
          </div>
          <div style={{ fontSize: 32, fontWeight: 900, color: "#FFFFFF", marginTop: 6 }}>
            PJM Interconnection Clearing Price
          </div>
        </div>
        <div
          style={{
            backgroundColor: "rgba(255, 42, 75, 0.2)",
            border: "2px solid #FF2A4B",
            color: "#FF2A4B",
            fontWeight: 900,
            fontSize: 28,
            padding: "8px 20px",
            borderRadius: 14,
          }}
        >
          +800% SPIKE
        </div>
      </div>

      {/* SVG Chart with Live Drawing Line */}
      <div style={{ margin: "40px 0 20px 0" }}>
        <svg viewBox="0 0 800 280" style={{ width: "100%", height: 260, overflow: "visible" }}>
          <defs>
            <linearGradient id="areaGrad" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stop-color="#E2FF00" stop-opacity="0.45" />
              <stop offset="100%" stop-color="#E2FF00" stop-opacity="0.0" />
            </linearGradient>
          </defs>

          {/* Grid lines */}
          <line x1="0" y1="240" x2="800" y2="240" stroke="rgba(255,255,255,0.1)" strokeWidth="2" />
          <line x1="0" y1="140" x2="800" y2="140" stroke="rgba(255,255,255,0.1)" strokeWidth="2" />
          <line x1="0" y1="40" x2="800" y2="40" stroke="rgba(255,255,255,0.1)" strokeWidth="2" />

          {/* Trajectory Path */}
          <path
            d="M 50,230 Q 250,220 450,90 T 750,30"
            fill="none"
            stroke="#E2FF00"
            strokeWidth="8"
            strokeLinecap="round"
            strokeDasharray={900}
            strokeDashoffset={900 * (1 - lineProgress)}
          />

          {/* Peak Value Indicator */}
          {lineProgress > 0.85 && (
            <>
              <circle cx="750" cy="30" r="14" fill="#E2FF00" />
              <circle cx="750" cy="30" r="8" fill="#FFFFFF" />
              <text x="630" y="15" fill="#E2FF00" fontSize="32" fontWeight="900" fontFamily="monospace">
                $333.60
              </text>
            </>
          )}

          {/* Baseline Indicator */}
          <circle cx="50" cy="230" r="10" fill="#64748B" />
          <text x="50" y="270" fill="#94A3B8" fontSize="22" fontFamily="monospace">
            2023: $28.92
          </text>
          <text x="700" y="270" fill="#E2FF00" fontSize="22" fontFamily="monospace" fontWeight="bold">
            2026: $333.60
          </text>
        </svg>
      </div>

      <div style={{ fontSize: 20, color: "#94A3B8", textAlign: "center" }}>
        Independent Market Monitor: <strong>63% of increase caused by data center queues.</strong>
      </div>
    </div>
  );
};

// =====================================================================
// SCENE 4: PUCO DOCKET & REDACTION REVEAL
// =====================================================================
const Scene4DocketRedaction: React.FC<{ frame: number; fps: number }> = ({ frame, fps }) => {
  const stampSpring = spring({ frame: frame - 40, fps, config: { damping: 12, mass: 0.7, stiffness: 200 } });
  const stampScale = interpolate(stampSpring, [0, 1], [2.2, 1.0]);

  // Highlighter wipe
  const highlightWidth = interpolate(frame, [15, 65], [0, 100], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <div
      style={{
        width: "100%",
        maxWidth: 960,
        backgroundColor: "rgba(13, 18, 31, 0.94)",
        borderRadius: 36,
        padding: "50px 60px",
        border: "2px solid rgba(255, 255, 255, 0.2)",
        position: "relative",
      }}
    >
      <div style={{ borderBottom: "2px solid rgba(255,255,255,0.1)", paddingBottom: 20 }}>
        <div style={{ color: "#E2FF00", fontFamily: "monospace", fontSize: 20, fontWeight: 800 }}>
          PUBLIC UTILITIES COMMISSION OF OHIO // DOCKET 24-508
        </div>
        <div style={{ fontSize: 32, fontWeight: 900, color: "#FFFFFF", marginTop: 8 }}>
          AEP Ohio Data Center Tariff Investigation
        </div>
      </div>

      <div style={{ margin: "40px 0", fontSize: 28, lineHeight: 1.6, color: "#E2E8F0" }}>
        "Utilities requested authorization to allocate multi-billion-dollar transmission buildouts{" "}
        <span style={{ position: "relative", display: "inline-block", color: "#000000", fontWeight: 800 }}>
          <span
            style={{
              position: "absolute",
              inset: "-2px -6px",
              backgroundColor: "#FFE600",
              zIndex: -1,
              width: `${highlightWidth}%`,
              borderRadius: 6,
            }}
          />
          directly onto ordinary households
        </span>{" "}
        under general distribution rate bases."
      </div>

      {frame >= 40 && (
        <div
          style={{
            position: "absolute",
            bottom: 35,
            right: 60,
            transform: `scale(${stampScale}) rotate(-12deg)`,
            border: "6px solid #FF2A4B",
            color: "#FF2A4B",
            padding: "12px 32px",
            fontSize: 38,
            fontWeight: 900,
            letterSpacing: "0.15em",
            backgroundColor: "rgba(255, 42, 75, 0.2)",
            boxShadow: "0 0 40px rgba(255, 42, 75, 0.6)",
          }}
        >
          SOCIALIZED DEBT
        </div>
      )}
    </div>
  );
};

// =====================================================================
// SCENE 5: ELECTION DAY 2026 BALLOT CLASH
// =====================================================================
const Scene5ElectionBallot: React.FC<{ frame: number; fps: number }> = ({ frame, fps }) => {
  const stampSpring = spring({ frame: frame - 35, fps, config: { damping: 10, mass: 0.6, stiffness: 220 } });
  const stampScale = interpolate(stampSpring, [0, 1], [2.5, 1.0]);

  return (
    <div
      style={{
        width: "100%",
        maxWidth: 960,
        backgroundColor: "rgba(13, 18, 31, 0.94)",
        borderRadius: 36,
        padding: "50px 60px",
        border: "2px solid rgba(255, 42, 75, 0.4)",
        position: "relative",
      }}
    >
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <span style={{ fontFamily: "monospace", fontSize: 22, color: "#FFAA00", fontWeight: 800 }}>
          US MIDTERMS: NOV 03, 2026
        </span>
        <span style={{ backgroundColor: "#FF2A4B", color: "#FFF", padding: "6px 16px", borderRadius: 8, fontSize: 18, fontWeight: 900 }}>
          LOCAL BALLOT MEASURE
        </span>
      </div>

      <div style={{ margin: "40px 0" }}>
        <div style={{ fontSize: 24, color: "#94A3B8", letterSpacing: "0.1em" }}>OHIO & VIRGINIA REFERENDUMS</div>
        <div style={{ fontSize: 44, fontWeight: 900, color: "#FFFFFF", margin: "12px 0 24px 0", lineHeight: 1.2 }}>
          EMERGENCY DATA CENTER MORATORIUM & UTILITY BOARD ELECTIONS
        </div>
        <div style={{ fontSize: 24, color: "#CBD5E1", lineHeight: 1.5 }}>
          Furious voters demand binding bans on new server hookups until tech monopolies pay 100% of grid upgrades.
        </div>
      </div>

      {frame >= 35 && (
        <div
          style={{
            position: "absolute",
            bottom: 40,
            right: 60,
            transform: `scale(${stampScale}) rotate(-10deg)`,
            border: "6px solid #FF2A4B",
            color: "#FF2A4B",
            padding: "14px 34px",
            fontSize: 42,
            fontWeight: 900,
            letterSpacing: "0.15em",
            backgroundColor: "rgba(255, 42, 75, 0.25)",
            boxShadow: "0 0 50px rgba(255, 42, 75, 0.7)",
          }}
        >
          VOTER REVOLT
        </div>
      )}
    </div>
  );
};

// =====================================================================
// SCENE 6: AI PROMPT VS POWER TRANSFORMER REALITY
// =====================================================================
const Scene6PromptVsTransformer: React.FC<{ frame: number; fps: number }> = ({ frame, fps }) => {
  return (
    <div
      style={{
        width: "100%",
        maxWidth: 960,
        backgroundColor: "rgba(13, 18, 31, 0.92)",
        borderRadius: 36,
        padding: 50,
        border: "2px solid rgba(255, 255, 255, 0.2)",
      }}
    >
      <div style={{ textAlign: "center", marginBottom: 35 }}>
        <div style={{ color: "#E2FF00", fontFamily: "monospace", fontSize: 22, fontWeight: 800 }}>
          THE PHYSICAL CEILING
        </div>
        <div style={{ fontSize: 38, fontWeight: 900, color: "#FFFFFF", marginTop: 8 }}>
          Software Promises vs Thermodynamic Reality
        </div>
      </div>

      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 30 }}>
        <div style={{ backgroundColor: "rgba(255,255,255,0.04)", padding: 30, borderRadius: 24 }}>
          <div style={{ color: "#06B6D4", fontFamily: "monospace", fontSize: 20 }}>AI QUERY PROMISE</div>
          <div style={{ fontSize: 48, fontWeight: 900, color: "#FFFFFF", margin: "15px 0" }}>$0.002</div>
          <div style={{ color: "#94A3B8", fontSize: 20 }}>"Infinite digital efficiency."</div>
        </div>
        <div style={{ backgroundColor: "rgba(255,255,255,0.04)", padding: 30, borderRadius: 24, border: "2px solid #FF2A4B" }}>
          <div style={{ color: "#FF2A4B", fontFamily: "monospace", fontSize: 20 }}>GRID REALITY</div>
          <div style={{ fontSize: 48, fontWeight: 900, color: "#FF2A4B", margin: "15px 0" }}>5-7 YEARS</div>
          <div style={{ color: "#94A3B8", fontSize: 20 }}>Lead time to build one substation.</div>
        </div>
      </div>
    </div>
  );
};

// =====================================================================
// SCENE 7: CLIMAX TYPOGRAPHY SLAM (YOUR PAYCHECK)
// =====================================================================
const Scene7ClimaxSlam: React.FC<{ frame: number; fps: number }> = ({ frame, fps }) => {
  const slamSpring = spring({ frame, fps, config: { damping: 10, mass: 0.5, stiffness: 220 } });
  const slamScale = interpolate(slamSpring, [0, 1], [1.8, 1.0]);

  return (
    <div style={{ textAlign: "center", transform: `scale(${slamScale})` }}>
      <div
        style={{
          fontSize: 100,
          fontWeight: 900,
          color: "#FF2A4B",
          fontFamily: "monospace",
          letterSpacing: "-0.03em",
          textShadow: "0 0 60px rgba(255, 42, 75, 0.8)",
        }}
      >
        YOUR PAYCHECK.
      </div>
      <div style={{ fontSize: 32, fontWeight: 700, color: "#FFFFFF", marginTop: 20, letterSpacing: "0.05em" }}>
        EVERY SINGLE AI PROMPT IS RUNNING ON YOUR ELECTRIC BILL.
      </div>
    </div>
  );
};

