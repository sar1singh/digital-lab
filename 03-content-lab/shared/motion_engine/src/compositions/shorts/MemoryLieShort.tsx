import React from "react";
import {
  AbsoluteFill,
  interpolate,
  OffthreadVideo,
  Sequence,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { MEMORY_LIE_WORDS, WordToken } from "./memory_lie_words";

// ============================================================================
// SUB-COMPONENTS: CINEMATIC ATMOSPHERE, FILM GRAIN & DUST PARTICLES
// ============================================================================

const CinematicAtmosphere: React.FC<{ frame: number; tintColor?: string }> = ({
  frame,
  tintColor = "rgba(0, 240, 255, 0.12)",
}) => {
  return (
    <AbsoluteFill style={{ pointerEvents: "none" }}>
      {/* Dynamic Chiaroscuro Lighting */}
      <div
        style={{
          position: "absolute",
          inset: 0,
          background: `radial-gradient(circle at 50% 30%, ${tintColor} 0%, transparent 65%)`,
        }}
      />
      {/* 35mm Heavy Cinematic Vignette */}
      <div
        style={{
          position: "absolute",
          inset: 0,
          background:
            "radial-gradient(circle at 50% 50%, transparent 30%, rgba(4, 7, 13, 0.75) 75%, rgba(2, 4, 8, 0.95) 100%)",
        }}
      />
      {/* Organic Floating Micro Dust Motes */}
      {Array.from({ length: 12 }).map((_, idx) => {
        const seed = (idx + 1) * 83;
        const x = (seed * 17 + frame * (0.35 + (idx % 3) * 0.2)) % 1080;
        const y = 1920 - ((seed * 29 + frame * (0.7 + (idx % 4) * 0.25)) % 1920);
        const size = 3 + (idx % 4) * 2;
        const opacity = 0.12 + (idx % 3) * 0.08;
        return (
          <div
            key={idx}
            style={{
              position: "absolute",
              left: x,
              top: y,
              width: size,
              height: size,
              borderRadius: "50%",
              backgroundColor: idx % 2 === 0 ? "#C5A059" : "#FFFFFF",
              opacity,
              filter: "blur(1px)",
            }}
          />
        );
      })}
    </AbsoluteFill>
  );
};

// ============================================================================
// MAIN 9:16 SHORT COMPOSITION (MAGNATES MEDIA / VOX DOCUMENTARY ENGINE)
// ============================================================================

export const MemoryLieShort: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const currentTime = frame / fps;

  // -------------------------------------------------------------
  // KINETIC SUBTITLE ENGINE (VOX / SWISS EDITORIAL ACTIVE HIGHLIGHT)
  // -------------------------------------------------------------
  const activeWordIdx = MEMORY_LIE_WORDS.findIndex(
    (w) => currentTime >= w.start && currentTime <= w.end
  );

  let chunkStartIndex = 0;
  if (activeWordIdx !== -1) {
    chunkStartIndex = Math.floor(activeWordIdx / 3) * 3;
  } else {
    const lastSpoken = MEMORY_LIE_WORDS.map((w, idx) => ({ w, idx })).filter(
      (item) => item.w.end <= currentTime
    );
    if (lastSpoken.length > 0) {
      chunkStartIndex = Math.floor(lastSpoken[lastSpoken.length - 1].idx / 3) * 3;
    }
  }

  const currentChunk = MEMORY_LIE_WORDS.slice(chunkStartIndex, chunkStartIndex + 3);

  // -------------------------------------------------------------
  // SCENE DYNAMICS (0 - 1122 Frames @ 30fps = 37.40s)
  // -------------------------------------------------------------
  const renderForensicCard = () => {
    // SCENE 1 (Frames 0 - 165 | 0.00s - 5.50s): Courtroom Sworn Affidavit
    if (frame < 165) {
      const enter = spring({ frame, fps, config: { damping: 15, stiffness: 110 } });
      const slowPush = interpolate(frame, [0, 165], [1.0, 1.05], { extrapolateRight: "clamp" });

      return (
        <div
          style={{
            transform: `scale(${enter * slowPush})`,
            opacity: enter,
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            width: "90%",
            maxWidth: 920,
          }}
        >
          {/* Historical Location Tag */}
          <div
            style={{
              padding: "10px 26px",
              backgroundColor: "rgba(197, 160, 89, 0.25)",
              border: "1px solid #C5A059",
              borderRadius: 30,
              color: "#C5A059",
              fontSize: 22,
              fontWeight: 800,
              letterSpacing: 4,
              marginBottom: 24,
              boxShadow: "0 4px 20px rgba(0,0,0,0.6)",
              backdropFilter: "blur(10px)",
            }}
          >
            🏛️ BURLINGTON, NORTH CAROLINA • 1984
          </div>

          {/* Tactile Court Docket Card */}
          <div
            style={{
              width: "100%",
              backgroundColor: "rgba(13, 19, 33, 0.88)",
              border: "2px solid rgba(197, 160, 89, 0.5)",
              borderRadius: 24,
              padding: "44px 38px",
              boxShadow: "0 30px 80px rgba(0,0,0,0.85), inset 0 1px 0 rgba(255,255,255,0.1)",
              backdropFilter: "blur(18px)",
            }}
          >
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
              <span style={{ color: "#94A3B8", fontSize: 20, fontWeight: 700, letterSpacing: 3 }}>
                SUPERIOR COURT OF JUSTICE // EXHIBIT A
              </span>
              <span
                style={{
                  color: "#00F0FF",
                  fontSize: 18,
                  fontWeight: 800,
                  backgroundColor: "rgba(0, 240, 255, 0.15)",
                  padding: "4px 12px",
                  borderRadius: 8,
                }}
              >
                SWORN TESTIMONY
              </span>
            </div>

            <div
              style={{
                color: "#FFFFFF",
                fontSize: 46,
                fontWeight: 900,
                marginTop: 20,
                lineHeight: 1.25,
                fontFamily: "Georgia, serif",
                fontStyle: "italic",
              }}
            >
              "I looked into his eyes... <br />
              <span style={{ color: "#E2FF00", fontStyle: "normal" }}>and I swore on the Bible."</span>
            </div>

            <div
              style={{
                marginTop: 30,
                display: "flex",
                alignItems: "center",
                gap: 20,
                borderTop: "1px solid rgba(255,255,255,0.12)",
                paddingTop: 22,
              }}
            >
              <div
                style={{
                  width: 58,
                  height: 58,
                  borderRadius: "50%",
                  backgroundColor: "#C5A059",
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "center",
                  fontSize: 28,
                  color: "#000",
                  boxShadow: "0 0 20px rgba(197, 160, 89, 0.5)",
                }}
              >
                ⚖️
              </div>
              <div>
                <div style={{ color: "#FFFFFF", fontSize: 26, fontWeight: 900 }}>JENNIFER THOMPSON</div>
                <div style={{ color: "#94A3B8", fontSize: 18, fontWeight: 600 }}>
                  22-YEAR-OLD COLLEGE STUDENT • EYEWITNESS
                </div>
              </div>
            </div>
          </div>
        </div>
      );
    }

    // SCENE 2 (Frames 165 - 345 | 5.50s - 11.50s): Historical Photo & 100% Certainty Reticle
    if (frame >= 165 && frame < 345) {
      const sceneFrame = frame - 165;
      const enter = spring({ frame: sceneFrame, fps, config: { damping: 14, stiffness: 120 } });
      const meterVal = interpolate(sceneFrame, [0, 55], [0, 100], { extrapolateRight: "clamp" });

      return (
        <div
          style={{
            transform: `scale(${enter})`,
            opacity: enter,
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            width: "90%",
            maxWidth: 920,
          }}
        >
          {/* Eyewitness Reticle Tag */}
          <div
            style={{
              padding: "10px 26px",
              backgroundColor: "rgba(0, 240, 255, 0.2)",
              border: "1px solid #00F0FF",
              borderRadius: 30,
              color: "#00F0FF",
              fontSize: 22,
              fontWeight: 800,
              letterSpacing: 3,
              marginBottom: 20,
              backdropFilter: "blur(12px)",
            }}
          >
            🎯 SUBJECTIVE CERTAINTY AUDIT
          </div>

          <div
            style={{
              width: "100%",
              backgroundColor: "rgba(10, 16, 30, 0.9)",
              border: "2px solid rgba(0, 240, 255, 0.5)",
              borderRadius: 24,
              padding: "36px 36px",
              boxShadow: "0 30px 80px rgba(0,0,0,0.85), 0 0 50px rgba(0, 240, 255, 0.25)",
              backdropFilter: "blur(20px)",
              display: "flex",
              flexDirection: "column",
              alignItems: "center",
            }}
          >
            {/* Real Archival Photo of Jennifer Thompson & Ronald Cotton */}
            <div
              style={{
                width: 280,
                height: 180,
                borderRadius: 16,
                overflow: "hidden",
                border: "2px solid rgba(255,255,255,0.25)",
                boxShadow: "0 15px 35px rgba(0,0,0,0.8)",
                marginBottom: 20,
                position: "relative",
              }}
            >
              <img
                src={staticFile("images/memory_lie/Jennifer_Thompson_Cannino_and_Ronald_Cot.jpg")}
                alt="Jennifer Thompson & Ronald Cotton Archival"
                style={{
                  width: "100%",
                  height: "100%",
                  objectFit: "cover",
                  filter: "contrast(1.15) brightness(0.95)",
                }}
              />
              <div
                style={{
                  position: "absolute",
                  bottom: 8,
                  left: 10,
                  backgroundColor: "rgba(0,0,0,0.75)",
                  padding: "3px 10px",
                  borderRadius: 6,
                  color: "#00F0FF",
                  fontSize: 14,
                  fontWeight: 800,
                }}
              >
                ARCHIVAL EVIDENCE
              </div>
            </div>

            <div style={{ color: "#94A3B8", fontSize: 22, fontWeight: 700, letterSpacing: 2 }}>
              WITNESS CONFIDENCE ON THE STAND
            </div>
            <div
              style={{
                fontSize: 92,
                fontWeight: 950,
                color: "#00F0FF",
                fontFamily: "monospace",
                margin: "4px 0",
                textShadow: "0 0 35px rgba(0,240,255,0.7)",
              }}
            >
              {meterVal.toFixed(1)}%
            </div>

            <div
              style={{
                width: "100%",
                height: 14,
                backgroundColor: "rgba(255,255,255,0.12)",
                borderRadius: 7,
                overflow: "hidden",
                margin: "12px 0 16px 0",
              }}
            >
              <div
                style={{
                  width: `${meterVal}%`,
                  height: "100%",
                  backgroundColor: "#00F0FF",
                  boxShadow: "0 0 20px #00F0FF",
                }}
              />
            </div>

            <div style={{ color: "#FFFFFF", fontSize: 28, fontWeight: 800, textAlign: "center" }}>
              "I STUDIED HIS FACE. I AM ONE HUNDRED PERCENT SURE."
            </div>
          </div>
        </div>
      );
    }

    // SCENE 3 (Frames 345 - 495 | 11.50s - 16.50s): Police Lineup & Guilty Verdict
    if (frame >= 345 && frame < 495) {
      const sceneFrame = frame - 345;
      const enter = spring({ frame: sceneFrame, fps, config: { damping: 14, stiffness: 120 } });
      const stampScale = interpolate(sceneFrame, [38, 48], [3.0, 1.0], { extrapolateRight: "clamp" });
      const stampOpacity = interpolate(sceneFrame, [38, 46], [0, 1], { extrapolateRight: "clamp" });
      const recoilShake =
        sceneFrame >= 48 && sceneFrame <= 56
          ? Math.sin((sceneFrame - 48) * 1.5) * 6
          : 0;

      return (
        <div
          style={{
            transform: `scale(${enter}) translateY(${recoilShake}px)`,
            opacity: enter,
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            width: "90%",
            maxWidth: 920,
          }}
        >
          <div
            style={{
              padding: "10px 26px",
              backgroundColor: "rgba(255, 42, 75, 0.25)",
              border: "1px solid #FF2A4B",
              borderRadius: 30,
              color: "#FF2A4B",
              fontSize: 22,
              fontWeight: 800,
              letterSpacing: 4,
              marginBottom: 24,
              backdropFilter: "blur(12px)",
            }}
          >
            🚨 POLICE PHOTO LINEUP • IDENTIFICATION
          </div>

          <div
            style={{
              position: "relative",
              width: "100%",
              backgroundColor: "rgba(15, 20, 32, 0.92)",
              border: "2px solid rgba(255, 42, 75, 0.5)",
              borderRadius: 24,
              padding: "48px 38px",
              textAlign: "center",
              overflow: "hidden",
              boxShadow: "0 30px 80px rgba(0,0,0,0.85), 0 0 50px rgba(255, 42, 75, 0.25)",
              backdropFilter: "blur(18px)",
            }}
          >
            <div style={{ color: "#94A3B8", fontSize: 22, fontWeight: 700, letterSpacing: 3 }}>
              DEFENDANT IDENTIFIED: SUSPECT #4
            </div>
            <div
              style={{
                color: "#FFFFFF",
                fontSize: 48,
                fontWeight: 950,
                margin: "18px 0",
                letterSpacing: 1,
              }}
            >
              RONALD COTTON
            </div>
            <div style={{ color: "#E2E8F0", fontSize: 26, fontWeight: 700 }}>
              VERDICT: SENTENCED TO LIFE IN PRISON + 54 YEARS
            </div>

            {sceneFrame >= 38 && (
              <div
                style={{
                  position: "absolute",
                  inset: 0,
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "center",
                  transform: `scale(${stampScale}) rotate(-10deg)`,
                  opacity: stampOpacity,
                }}
              >
                <div
                  style={{
                    border: "8px solid #FF2A4B",
                    color: "#FF2A4B",
                    fontSize: 58,
                    fontWeight: 950,
                    padding: "16px 44px",
                    letterSpacing: 8,
                    textTransform: "uppercase",
                    backgroundColor: "rgba(10, 15, 25, 0.9)",
                    boxShadow: "0 0 50px rgba(255, 42, 75, 0.8)",
                  }}
                >
                  GUILTY
                </div>
              </div>
            )}
          </div>
        </div>
      );
    }

    // SCENE 4 (Frames 495 - 660 | 16.50s - 22.00s): Real GelDoc DNA Exoneration
    if (frame >= 495 && frame < 660) {
      const sceneFrame = frame - 495;
      const enter = spring({ frame: sceneFrame, fps, config: { damping: 14, stiffness: 120 } });
      const stampScale = interpolate(sceneFrame, [35, 45], [3.0, 1.0], { extrapolateRight: "clamp" });
      const stampOpacity = interpolate(sceneFrame, [35, 43], [0, 1], { extrapolateRight: "clamp" });
      const recoilShake =
        sceneFrame >= 45 && sceneFrame <= 53
          ? Math.sin((sceneFrame - 45) * 1.5) * 6
          : 0;

      return (
        <div
          style={{
            transform: `scale(${enter}) translateY(${recoilShake}px)`,
            opacity: enter,
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            width: "90%",
            maxWidth: 920,
          }}
        >
          <div
            style={{
              padding: "10px 26px",
              backgroundColor: "rgba(16, 185, 129, 0.25)",
              border: "1px solid #10B981",
              borderRadius: 30,
              color: "#10B981",
              fontSize: 22,
              fontWeight: 800,
              letterSpacing: 4,
              marginBottom: 20,
              backdropFilter: "blur(12px)",
            }}
          >
            🧬 1995 • 11 YEARS LATER // DNA RE-ANALYSIS
          </div>

          <div
            style={{
              position: "relative",
              width: "100%",
              backgroundColor: "rgba(10, 22, 28, 0.92)",
              border: "2px solid rgba(16, 185, 129, 0.6)",
              borderRadius: 24,
              padding: "36px 36px",
              boxShadow: "0 30px 80px rgba(0,0,0,0.85), 0 0 50px rgba(16, 185, 129, 0.25)",
              backdropFilter: "blur(20px)",
              display: "flex",
              flexDirection: "column",
              alignItems: "center",
              overflow: "hidden",
            }}
          >
            {/* Real GelDoc DNA Electrophoresis Photo */}
            <div
              style={{
                width: 320,
                height: 150,
                borderRadius: 14,
                overflow: "hidden",
                border: "2px solid rgba(16, 185, 129, 0.4)",
                boxShadow: "0 10px 30px rgba(0,0,0,0.8)",
                marginBottom: 16,
                position: "relative",
              }}
            >
              <img
                src={staticFile("images/memory_lie/GelDoc_DNA_gel_electrophoresis_photograp.jpg")}
                alt="GelDoc DNA Electrophoresis"
                style={{
                  width: "100%",
                  height: "100%",
                  objectFit: "cover",
                  filter: "contrast(1.3) brightness(0.9)",
                }}
              />
              <div
                style={{
                  position: "absolute",
                  bottom: 6,
                  left: 8,
                  backgroundColor: "rgba(0,0,0,0.8)",
                  padding: "2px 8px",
                  borderRadius: 4,
                  color: "#10B981",
                  fontSize: 13,
                  fontWeight: 800,
                }}
              >
                GELDOC DNA BANDS // 100% EXCLUSION
              </div>
            </div>

            <div style={{ color: "#94A3B8", fontSize: 20, fontWeight: 700, letterSpacing: 2 }}>
              POST-CONVICTION MOLECULAR FORENSICS
            </div>
            <div style={{ color: "#FFFFFF", fontSize: 36, fontWeight: 900, margin: "8px 0" }}>
              MATCH CONFIRMED: BOBBY POOLE
            </div>
            <div style={{ color: "#10B981", fontSize: 24, fontWeight: 700 }}>
              RONALD COTTON WAS TOTALLY EXCLUDED
            </div>

            {sceneFrame >= 35 && (
              <div
                style={{
                  position: "absolute",
                  inset: 0,
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "center",
                  transform: `scale(${stampScale}) rotate(-8deg)`,
                  opacity: stampOpacity,
                }}
              >
                <div
                  style={{
                    border: "8px solid #10B981",
                    color: "#10B981",
                    fontSize: 54,
                    fontWeight: 950,
                    padding: "16px 40px",
                    letterSpacing: 6,
                    textTransform: "uppercase",
                    backgroundColor: "rgba(6, 18, 22, 0.92)",
                    boxShadow: "0 0 50px rgba(16, 185, 129, 0.8)",
                  }}
                >
                  100% INNOCENT
                </div>
              </div>
            )}
          </div>
        </div>
      );
    }

    // SCENE 5 (Frames 660 - 915 | 22.00s - 30.50s): The Innocence Project 70% Stat
    if (frame >= 660 && frame < 915) {
      const sceneFrame = frame - 660;
      const enter = spring({ frame: sceneFrame, fps, config: { damping: 14, stiffness: 120 } });
      const statVal = interpolate(sceneFrame, [0, 45], [0, 70], { extrapolateRight: "clamp" });

      return (
        <div
          style={{
            transform: `scale(${enter})`,
            opacity: enter,
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            width: "90%",
            maxWidth: 920,
          }}
        >
          <div
            style={{
              padding: "10px 26px",
              backgroundColor: "rgba(255, 42, 75, 0.25)",
              border: "1px solid #FF2A4B",
              borderRadius: 30,
              color: "#FF2A4B",
              fontSize: 22,
              fontWeight: 800,
              letterSpacing: 4,
              marginBottom: 20,
              backdropFilter: "blur(12px)",
            }}
          >
            ⚖️ THE INNOCENCE PROJECT • FORENSIC REPOSITORIES
          </div>

          <div
            style={{
              width: "100%",
              backgroundColor: "rgba(14, 20, 32, 0.92)",
              border: "2px solid rgba(255, 42, 75, 0.6)",
              borderRadius: 24,
              padding: "44px 38px",
              textAlign: "center",
              boxShadow: "0 30px 80px rgba(0,0,0,0.85), 0 0 60px rgba(255, 42, 75, 0.3)",
              backdropFilter: "blur(20px)",
            }}
          >
            <div style={{ color: "#94A3B8", fontSize: 24, fontWeight: 700, letterSpacing: 2 }}>
              OVERTURNED BY DNA FORENSICS
            </div>
            <div
              style={{
                fontSize: 120,
                fontWeight: 950,
                color: "#FF2A4B",
                fontFamily: "monospace",
                margin: "8px 0",
                textShadow: "0 0 45px rgba(255, 42, 75, 0.7)",
              }}
            >
              {Math.floor(statVal)}%
            </div>
            <div style={{ color: "#FFFFFF", fontSize: 34, fontWeight: 900 }}>
              CAUSED BY MISTAKEN EYEWITNESSES
            </div>
            <div
              style={{
                marginTop: 22,
                padding: "12px 24px",
                backgroundColor: "rgba(255, 255, 255, 0.08)",
                borderRadius: 14,
                color: "#E2FF00",
                fontSize: 24,
                fontWeight: 800,
                letterSpacing: 1,
              }}
            >
              TOTALLY CONFIDENT • PERFECTLY CALM • DEAD WRONG
            </div>
          </div>
        </div>
      );
    }

    // SCENE 6 (Frames 915 - 1122 | 30.50s - 37.40s): Living Brain Wetware & Circular Loop
    const sceneFrame = frame - 915;
    const enter = spring({ frame: sceneFrame, fps, config: { damping: 14, stiffness: 120 } });
    const glitchPulse = Math.sin(sceneFrame * 0.4) > 0.65;

    return (
      <div
        style={{
          transform: `scale(${enter})`,
          opacity: enter,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          width: "90%",
          maxWidth: 920,
        }}
      >
        <div
          style={{
            padding: "10px 26px",
            backgroundColor: "rgba(226, 255, 0, 0.2)",
            border: "1px solid #E2FF00",
            borderRadius: 30,
            color: "#E2FF00",
            fontSize: 22,
            fontWeight: 800,
            letterSpacing: 4,
            marginBottom: 20,
            backdropFilter: "blur(12px)",
          }}
        >
          🧠 HUMAN BIOLOGICAL WETWARE
        </div>

        <div
          style={{
            width: "100%",
            backgroundColor: "rgba(8, 14, 26, 0.92)",
            border: "2px solid #E2FF00",
            borderRadius: 24,
            padding: "44px 38px",
            textAlign: "center",
            boxShadow: "0 30px 80px rgba(0,0,0,0.85), 0 0 60px rgba(226, 255, 0, 0.3)",
            backdropFilter: "blur(20px)",
          }}
        >
          <div
            style={{
              fontSize: 50,
              fontWeight: 950,
              color: glitchPulse ? "#FF2A4B" : "#FFFFFF",
              marginBottom: 14,
              letterSpacing: 1,
            }}
          >
            YOUR SKULL HAS NO HARD DRIVE
          </div>
          <div style={{ color: "#94A3B8", fontSize: 24, fontWeight: 700 }}>
            ZERO VIDEO FILES • 20 WATTS METABOLIC POWER
          </div>
          <div
            style={{
              marginTop: 24,
              padding: "18px 26px",
              backgroundColor: "rgba(0,0,0,0.65)",
              borderRadius: 16,
              border: "1px dashed rgba(226, 255, 0, 0.5)",
              color: "#00F0FF",
              fontSize: 26,
              fontWeight: 800,
              lineHeight: 1.3,
            }}
          >
            EVERY SINGLE MEMORY IS A RE-CONSTRUCTED HALLUCINATION
          </div>
        </div>
      </div>
    );
  };

  return (
    <AbsoluteFill
      style={{
        backgroundColor: "#03060B",
        color: "#FFFFFF",
        fontFamily: "system-ui, -apple-system, sans-serif",
        overflow: "hidden",
      }}
    >
      {/* ============================================================== */}
      {/* LAYER 1: REAL 1080P DOCUMENTARY CINEMATOGRAPHY B-ROLL SPINE     */}
      {/* ============================================================== */}
      {/* Beat 1: Courtroom (0 - 165) */}
      <Sequence from={0} durationInFrames={165}>
        <AbsoluteFill>
          <OffthreadVideo
            src={staticFile("broll/courtroom.mp4")}
            muted
            style={{
              width: "100%",
              height: "100%",
              objectFit: "cover",
              filter: "brightness(0.65) contrast(1.2)",
              transform: `scale(${interpolate(frame, [0, 165], [1.05, 1.15], {
                extrapolateRight: "clamp",
              })})`,
            }}
          />
        </AbsoluteFill>
      </Sequence>

      {/* Beat 2: Eye / Lineup Reticle (165 - 345) */}
      <Sequence from={165} durationInFrames={180}>
        <AbsoluteFill>
          <OffthreadVideo
            src={staticFile("broll/courtroom.mp4")}
            muted
            style={{
              width: "100%",
              height: "100%",
              objectFit: "cover",
              filter: "brightness(0.5) contrast(1.25) saturate(0.8)",
              transform: `scale(${interpolate(frame, [165, 345], [1.15, 1.25], {
                extrapolateRight: "clamp",
              })})`,
            }}
          />
        </AbsoluteFill>
      </Sequence>

      {/* Beat 3: Prison Bars (345 - 495) */}
      <Sequence from={345} durationInFrames={150}>
        <AbsoluteFill>
          <OffthreadVideo
            src={staticFile("broll/prison_bars.mp4")}
            muted
            style={{
              width: "100%",
              height: "100%",
              objectFit: "cover",
              filter: "brightness(0.6) contrast(1.25)",
              transform: `scale(${interpolate(frame, [345, 495], [1.05, 1.18], {
                extrapolateRight: "clamp",
              })})`,
            }}
          />
        </AbsoluteFill>
      </Sequence>

      {/* Beat 4: DNA Laboratory (495 - 660) */}
      <Sequence from={495} durationInFrames={165}>
        <AbsoluteFill>
          <OffthreadVideo
            src={staticFile("broll/dna_lab.mp4")}
            muted
            style={{
              width: "100%",
              height: "100%",
              objectFit: "cover",
              filter: "brightness(0.65) contrast(1.2)",
              transform: `scale(${interpolate(frame, [495, 660], [1.05, 1.16], {
                extrapolateRight: "clamp",
              })})`,
            }}
          />
        </AbsoluteFill>
      </Sequence>

      {/* Beat 5: Legal Case Archives (660 - 915) */}
      <Sequence from={660} durationInFrames={255}>
        <AbsoluteFill>
          <OffthreadVideo
            src={staticFile("broll/archive_files.mp4")}
            muted
            style={{
              width: "100%",
              height: "100%",
              objectFit: "cover",
              filter: "brightness(0.55) contrast(1.2)",
              transform: `scale(${interpolate(frame, [660, 915], [1.05, 1.18], {
                extrapolateRight: "clamp",
              })})`,
            }}
          />
        </AbsoluteFill>
      </Sequence>

      {/* Beat 6: Brain Synapses (915 - 1122) */}
      <Sequence from={915} durationInFrames={207}>
        <AbsoluteFill>
          <OffthreadVideo
            src={staticFile("broll/brain_synapse.mp4")}
            muted
            style={{
              width: "100%",
              height: "100%",
              objectFit: "cover",
              filter: "brightness(0.7) contrast(1.3)",
              transform: `scale(${interpolate(frame, [915, 1122], [1.05, 1.2], {
                extrapolateRight: "clamp",
              })})`,
            }}
          />
        </AbsoluteFill>
      </Sequence>

      {/* ============================================================== */}
      {/* LAYER 2: 35MM FILM VIGNETTE & DUST MOTES (DEPTH & FOCUS)       */}
      {/* ============================================================== */}
      <CinematicAtmosphere frame={frame} />

      {/* ============================================================== */}
      {/* LAYER 3: TACTILE EVIDENCE CARDS & HISTORICAL ARCHIVES           */}
      {/* ============================================================== */}
      <div
        style={{
          position: "absolute",
          top: "16%",
          left: 0,
          right: 0,
          display: "flex",
          justifyContent: "center",
          zIndex: 10,
        }}
      >
        {renderForensicCard()}
      </div>

      {/* ============================================================== */}
      {/* LAYER 4: KINETIC SUBTITLES IN SAFE ZONE                        */}
      {/* ============================================================== */}
      <div
        style={{
          position: "absolute",
          bottom: "16%",
          left: "5%",
          right: "5%",
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          gap: 16,
          flexWrap: "wrap",
          zIndex: 20,
        }}
      >
        {currentChunk.map((token, idx) => {
          const isSpoken = currentTime >= token.start && currentTime <= token.end;
          return (
            <span
              key={idx}
              style={{
                fontSize: 54,
                fontWeight: 950,
                color: isSpoken ? "#E2FF00" : "#FFFFFF",
                textShadow: isSpoken
                  ? "0 0 30px rgba(226, 255, 0, 0.85), 0 4px 12px rgba(0,0,0,0.95)"
                  : "0 4px 14px rgba(0,0,0,0.95)",
                transform: isSpoken ? "scale(1.15)" : "scale(1.0)",
                transition: "transform 0.08s ease, color 0.08s ease",
                backgroundColor: isSpoken ? "rgba(0,0,0,0.75)" : "transparent",
                padding: "4px 14px",
                borderRadius: 14,
                letterSpacing: 1,
              }}
            >
              {token.word.toUpperCase()}
            </span>
          );
        })}
      </div>

      {/* ThinkLate Broadcast Badge at Top */}
      <div
        style={{
          position: "absolute",
          top: 60,
          left: 60,
          display: "flex",
          alignItems: "center",
          gap: 14,
          zIndex: 30,
        }}
      >
        <div
          style={{
            width: 14,
            height: 14,
            borderRadius: "50%",
            backgroundColor: "#E2FF00",
            boxShadow: "0 0 14px #E2FF00",
          }}
        />
        <span
          style={{
            fontSize: 22,
            fontWeight: 900,
            letterSpacing: 4,
            color: "#CBD5E1",
            textTransform: "uppercase",
            textShadow: "0 2px 8px rgba(0,0,0,0.9)",
          }}
        >
          THINKLATE // THE MEMORY LIE
        </span>
      </div>
    </AbsoluteFill>
  );
};
