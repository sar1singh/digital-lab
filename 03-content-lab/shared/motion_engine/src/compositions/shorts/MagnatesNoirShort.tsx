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
import { BEATS_TIMING } from "./words_data";

// ============================================================================
// SUB-COMPONENTS: 2.5D PARALLAX NOIR SILHOUETTES & ATMOSPHERE
// ============================================================================

const FilmGrainAndVignette: React.FC<{ accentColor: string; frame: number }> = ({
  accentColor,
  frame,
}) => {
  const lightShiftX = Math.sin(frame * 0.03) * 120;
  const lightShiftY = Math.cos(frame * 0.02) * 80;

  return (
    <AbsoluteFill style={{ pointerEvents: "none" }}>
      <div
        style={{
          position: "absolute",
          inset: -200,
          background: `radial-gradient(circle at ${50 + lightShiftX * 0.1}% ${
            35 + lightShiftY * 0.1
          }%, ${accentColor}33 0%, transparent 62%)`,
        }}
      />
      <div
        style={{
          position: "absolute",
          inset: 0,
          background:
            "radial-gradient(circle at 50% 50%, transparent 35%, rgba(4, 7, 13, 0.85) 85%, #04070D 100%)",
        }}
      />
      {Array.from({ length: 14 }).map((_, idx) => {
        const seed = (idx + 1) * 73;
        const x = (seed * 19 + frame * (0.4 + (idx % 3) * 0.25)) % 1080;
        const y = 1920 - ((seed * 31 + frame * (0.8 + (idx % 4) * 0.3)) % 1920);
        const size = 3 + (idx % 5) * 2;
        const opacity = 0.15 + (idx % 4) * 0.08;
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
              backgroundColor: idx % 2 === 0 ? accentColor : "#FFFFFF",
              opacity,
              filter: "blur(1px)",
            }}
          />
        );
      })}
    </AbsoluteFill>
  );
};

// Alternative A: 2.5D Graphic Noir Investigator Silhouette Anchor
const NoirInvestigatorParallax: React.FC<{
  frame: number;
  fps: number;
  mode: "window_bunkers" | "climax_return";
}> = ({ frame, fps, mode }) => {
  const pushBg = interpolate(frame, [0, 210], [1.0, 1.08], {
    extrapolateRight: "clamp",
  });
  const pushMid = interpolate(frame, [0, 210], [1.0, 1.15], {
    extrapolateRight: "clamp",
  });
  const pushFg = interpolate(frame, [0, 210], [1.0, 1.26], {
    extrapolateRight: "clamp",
  });
  const panX = interpolate(frame, [0, 210], [-18, 18], {
    extrapolateRight: "clamp",
  });

  const rimColor = mode === "window_bunkers" ? "#06B6D4" : "#FF2A4B";

  return (
    <AbsoluteFill
      style={{
        perspective: "1200px",
        overflow: "hidden",
      }}
    >
      {/* Z-PLANE -100: Distant Glowing Data Center Bunkers */}
      <div
        style={{
          position: "absolute",
          inset: -60,
          transform: `translate3d(${-panX * 0.5}px, 0px, -100px) scale(${pushBg})`,
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <div
          style={{
            position: "absolute",
            top: 420,
            display: "flex",
            gap: 28,
            alignItems: "flex-end",
          }}
        >
          {[0, 1, 2].map((bunkerIdx) => {
            const pulse = 0.6 + 0.4 * Math.sin(frame * 0.15 + bunkerIdx * 1.5);
            return (
              <div
                key={bunkerIdx}
                style={{
                  width: 260,
                  height: bunkerIdx === 1 ? 220 : 185,
                  background: "linear-gradient(180deg, #0D1526 0%, #050811 100%)",
                  border: `2px solid ${rimColor}`,
                  boxShadow: `0 0 45px ${rimColor}${Math.round(pulse * 90)
                    .toString(16)
                    .padStart(2, "0")}`,
                  position: "relative",
                  display: "flex",
                  flexDirection: "column",
                  justifyContent: "space-between",
                  padding: 18,
                }}
              >
                <div
                  style={{
                    fontFamily: "Montserrat, sans-serif",
                    fontWeight: 800,
                    fontSize: 16,
                    color: rimColor,
                    letterSpacing: 2,
                  }}
                >
                  HYPERSCALE BUNKER 0{bunkerIdx + 1}
                </div>
                <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
                  {[0, 1, 2].map((r) => (
                    <div
                      key={r}
                      style={{
                        height: 8,
                        background: rimColor,
                        opacity: 0.4 + 0.5 * ((r + bunkerIdx) % 2),
                        boxShadow: `0 0 12px ${rimColor}`,
                      }}
                    />
                  ))}
                </div>
                <div
                  style={{
                    fontFamily: "monospace",
                    fontSize: 18,
                    fontWeight: 700,
                    color: "#E2FF00",
                  }}
                >
                  LOAD: 320 MW
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Z-PLANE +20: High-Rise Window Mullions */}
      <div
        style={{
          position: "absolute",
          inset: 0,
          transform: `translate3d(${panX * 0.3}px, 0px, 20px) scale(${pushMid})`,
          pointerEvents: "none",
        }}
      >
        <div
          style={{
            position: "absolute",
            left: 190,
            top: 0,
            bottom: 0,
            width: 14,
            background: "linear-gradient(90deg, #05070B, #1E293B, #05070B)",
            opacity: 0.75,
          }}
        />
        <div
          style={{
            position: "absolute",
            right: 190,
            top: 0,
            bottom: 0,
            width: 14,
            background: "linear-gradient(90deg, #05070B, #1E293B, #05070B)",
            opacity: 0.75,
          }}
        />
      </div>

      {/* Z-PLANE +95: Alternative A — 2.5D Noir Investigator Cutout Silhouette */}
      <div
        style={{
          position: "absolute",
          bottom: -60,
          left: "50%",
          width: 780,
          height: 980,
          marginLeft: -390,
          transform: `translate3d(${panX}px, 0px, 95px) scale(${pushFg})`,
          display: "flex",
          justifyContent: "center",
          alignItems: "flex-end",
          filter: `drop-shadow(0px -8px 28px ${rimColor}88)`,
        }}
      >
        <svg viewBox="0 0 600 750" width="100%" height="100%">
          <defs>
            <linearGradient id="noirCoat" x1="0" y1="0" x2="1" y2="1">
              <stop offset="0%" stopColor="#0F172A" />
              <stop offset="40%" stopColor="#060911" />
              <stop offset="100%" stopColor="#020408" />
            </linearGradient>
            <linearGradient id="cyanRim" x1="0" y1="0" x2="1" y2="0">
              <stop offset="0%" stopColor={rimColor} stopOpacity="0.95" />
              <stop offset="15%" stopColor={rimColor} stopOpacity="0.0" />
              <stop offset="85%" stopColor="#E2FF00" stopOpacity="0.0" />
              <stop offset="100%" stopColor="#E2FF00" stopOpacity="0.85" />
            </linearGradient>
          </defs>
          <path
            d="M 70 750 L 110 470 C 125 410 175 380 235 365 L 215 310 L 385 310 L 365 365 C 425 380 475 410 490 470 L 530 750 Z"
            fill="url(#noirCoat)"
            stroke="url(#cyanRim)"
            strokeWidth="5"
          />
          <path
            d="M 210 375 L 185 280 L 255 315 L 300 395 L 345 315 L 415 280 L 390 375 Z"
            fill="#090D16"
            stroke={rimColor}
            strokeWidth="3"
          />
          <path
            d="M 235 205 C 235 125 365 125 365 205 C 365 265 350 315 300 325 C 250 315 235 265 235 205 Z"
            fill="#060911"
            stroke={rimColor}
            strokeWidth="4"
          />
          <rect
            x="252"
            y="198"
            width="38"
            height="12"
            rx="3"
            fill={rimColor}
            opacity="0.85"
          />
          <rect
            x="310"
            y="198"
            width="38"
            height="12"
            rx="3"
            fill={rimColor}
            opacity="0.85"
          />
        </svg>
      </div>
    </AbsoluteFill>
  );
};

// Layer 5: Tactile Forensic Document Inspection (PUCO Docket 24-508)
const ForensicDocketDesk: React.FC<{ localFrame: number; fps: number }> = ({
  localFrame,
  fps,
}) => {
  const slideIn = spring({
    frame: localFrame,
    fps,
    config: { damping: 14, stiffness: 95 },
  });

  const camZoom = interpolate(localFrame, [0, 260], [0.96, 1.14], {
    extrapolateRight: "clamp",
  });
  const camTiltX = interpolate(localFrame, [0, 260], [16, 6], {
    extrapolateRight: "clamp",
  });
  const camRotateZ = interpolate(localFrame, [0, 260], [-3.5, -0.5], {
    extrapolateRight: "clamp",
  });

  const highlightProgress = interpolate(localFrame, [55, 125], [0, 100], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const stampSpring = spring({
    frame: Math.max(0, localFrame - 145),
    fps,
    config: { damping: 10, stiffness: 180 },
  });
  const stampScale = interpolate(stampSpring, [0, 1], [2.8, 1.0]);
  const stampOpacity = localFrame >= 145 ? 1 : 0;

  return (
    <AbsoluteFill
      style={{
        perspective: "1400px",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <div
        style={{
          width: 920,
          minHeight: 1220,
          backgroundColor: "#F4F1EA",
          backgroundImage:
            "radial-gradient(#D8D2C5 1px, transparent 1px), linear-gradient(180deg, #FAF8F5 0%, #EAE4D7 100%)",
          backgroundSize: "24px 24px, 100% 100%",
          borderRadius: 12,
          padding: "56px 52px",
          boxShadow:
            "0 50px 100px rgba(0,0,0,0.95), 0 0 0 2px #C8C1B2, inset 0 0 60px rgba(139,119,101,0.18)",
          transform: `translateY(${(1 - slideIn) * 700}px) scale(${camZoom}) rotateX(${camTiltX}deg) rotateZ(${camRotateZ}deg)`,
          color: "#111827",
          fontFamily: "Georgia, serif",
          position: "relative",
        }}
      >
        <div
          style={{
            borderBottom: "4px solid #111827",
            paddingBottom: 22,
            marginBottom: 30,
            display: "flex",
            justifyContent: "space-between",
            alignItems: "flex-start",
          }}
        >
          <div>
            <div
              style={{
                fontFamily: "Montserrat, sans-serif",
                fontWeight: 900,
                fontSize: 24,
                letterSpacing: 3,
                color: "#991B1B",
              }}
            >
              PUBLIC UTILITIES COMMISSION OF OHIO
            </div>
            <div
              style={{
                fontFamily: "monospace",
                fontSize: 22,
                fontWeight: 700,
                color: "#374151",
                marginTop: 6,
              }}
            >
              DOCKET NO. 24-508-EL-ATA • AEP OHIO TARIFF
            </div>
          </div>
          <div
            style={{
              border: "3px solid #111827",
              padding: "8px 16px",
              fontFamily: "monospace",
              fontWeight: 900,
              fontSize: 20,
            }}
          >
            EXHIBIT B-4
          </div>
        </div>

        <div style={{ marginBottom: 34 }}>
          <div
            style={{
              fontFamily: "Montserrat, sans-serif",
              fontWeight: 800,
              fontSize: 22,
              color: "#4B5563",
              letterSpacing: 1.5,
              marginBottom: 10,
            }}
          >
            SECTION 4.1 — PRIVATE HYPERSCALE VOLUME AGREEMENT
          </div>
          <div
            style={{
              fontSize: 29,
              lineHeight: 1.45,
              color: "#1F2937",
            }}
          >
            Commercial AI compute facilities exceeding 100 MW load shall receive{" "}
            <span
              style={{
                backgroundColor: "#111827",
                color: "#E2FF00",
                padding: "2px 10px",
                fontFamily: "monospace",
                fontWeight: 800,
              }}
            >
              PREFERENTIAL BULK RATE
            </span>{" "}
            exemptions under special bilateral utility contracts.
          </div>
        </div>

        <div
          style={{
            backgroundColor: "#FFFFFF",
            border: "3px solid #111827",
            padding: 32,
            position: "relative",
            marginBottom: 36,
          }}
        >
          <div
            style={{
              fontFamily: "Montserrat, sans-serif",
              fontWeight: 900,
              fontSize: 24,
              color: "#991B1B",
              marginBottom: 14,
            }}
          >
            SECTION 4.2 — TRANSMISSION UPGRADE COST RECOVERY:
          </div>
          <div
            style={{
              position: "relative",
              fontSize: 36,
              fontWeight: 800,
              lineHeight: 1.42,
              fontFamily: "Montserrat, sans-serif",
              color: "#090D16",
              zIndex: 2,
            }}
          >
            <div
              style={{
                position: "absolute",
                left: -8,
                top: 4,
                bottom: 4,
                width: `${highlightProgress}%`,
                backgroundColor: "#FFE600",
                opacity: 0.82,
                zIndex: -1,
                borderRadius: 4,
              }}
            />
            "100% OF SUBSTATION & GRID EXPANSION COSTS ($1.5B+) SHALL BE
            RECOVERED DIRECTLY FROM RESIDENTIAL HOUSEHOLD METERS."
          </div>
        </div>

        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
            borderTop: "2px dashed #6B7280",
            paddingTop: 24,
            fontFamily: "monospace",
            fontSize: 24,
            fontWeight: 700,
          }}
        >
          <div>HYPERSCALER INFRASTRUCTURE TAB: $0.00</div>
          <div style={{ color: "#DC2626" }}>HOMEOWNER SURCHARGE: +$264/YR</div>
        </div>

        <div
          style={{
            position: "absolute",
            right: 48,
            bottom: 95,
            opacity: stampOpacity,
            transform: `scale(${stampScale}) rotate(-14deg)`,
            border: "10px solid #DC2626",
            borderRadius: 16,
            padding: "16px 36px",
            color: "#DC2626",
            fontFamily: "Montserrat, sans-serif",
            fontWeight: 900,
            fontSize: 52,
            letterSpacing: 4,
            textTransform: "uppercase",
            backgroundColor: "rgba(254, 242, 242, 0.92)",
            boxShadow: "0 12px 35px rgba(220, 38, 38, 0.35)",
            zIndex: 10,
          }}
        >
          DUMPED ON YOU
        </div>
      </div>
    </AbsoluteFill>
  );
};

// ============================================================================
// MAIN COMPOSITION: DYNAMICALLY SYNCED TO WHISPER BEATS_TIMING
// ============================================================================

export const MagnatesNoirShort: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;

  // Read exact Whisper-aligned beat boundaries dynamically
  const b1End = BEATS_TIMING[0]?.end ?? 9.37;
  const b2Start = BEATS_TIMING[1]?.start ?? 9.4;
  const b2End = BEATS_TIMING[1]?.end ?? 16.47;
  const b3Start = BEATS_TIMING[2]?.start ?? 16.5;
  const b3End = BEATS_TIMING[2]?.end ?? 29.21;
  const b4Start = BEATS_TIMING[3]?.start ?? 29.24;
  const b4End = BEATS_TIMING[3]?.end ?? 37.53;
  const b5Start = BEATS_TIMING[4]?.start ?? 37.98;
  const b5End = BEATS_TIMING[4]?.end ?? 46.71;
  const b6Start = BEATS_TIMING[5]?.start ?? 46.74;

  const isDeadAir = t >= b4End && t < b5Start;

  if (isDeadAir) {
    return <AbsoluteFill style={{ backgroundColor: "#030508" }} />;
  }

  let accentColor = "#FF2A4B";
  if (t >= b2Start && t < b3Start) accentColor = "#06B6D4";
  if (t >= b4Start && t < b4End) accentColor = "#F59E0B";
  if (t >= b5Start && t < b6Start) accentColor = "#E2FF00";

  const brollScale = 1.04 + ((frame % 300) / 300) * 0.09;

  const fB2Start = Math.round(b2Start * fps);
  const fB3Start = Math.round(b3Start * fps);
  const fB4Start = Math.round(b4Start * fps);
  const fB4End = Math.round(b4End * fps);
  const fB5Start = Math.round(b5Start * fps);

  return (
    <AbsoluteFill
      style={{
        backgroundColor: "#060911",
        fontFamily: "Montserrat, Inter, sans-serif",
        overflow: "hidden",
      }}
    >
      {/* LAYER 1: REAL CURATED DOCUMENTARY B-ROLL */}
      <Sequence from={0} durationInFrames={fB2Start}>
        <AbsoluteFill>
          <OffthreadVideo
            src={staticFile("broll/broll_power_lines.mp4")}
            muted
            style={{
              width: "100%",
              height: "100%",
              objectFit: "cover",
              transform: `scale(${brollScale})`,
              filter: "contrast(1.25) saturate(0.55) brightness(0.42) blur(3px)",
            }}
          />
        </AbsoluteFill>
      </Sequence>

      <Sequence from={fB2Start} durationInFrames={fB3Start - fB2Start}>
        <AbsoluteFill>
          <OffthreadVideo
            src={staticFile("broll/broll_city_grid.mp4")}
            muted
            style={{
              width: "100%",
              height: "100%",
              objectFit: "cover",
              transform: `scale(${brollScale})`,
              filter: "contrast(1.3) saturate(0.6) brightness(0.38) blur(4px)",
            }}
          />
        </AbsoluteFill>
      </Sequence>

      <Sequence from={fB3Start} durationInFrames={fB4Start - fB3Start}>
        <AbsoluteFill>
          <OffthreadVideo
            src={staticFile("broll/broll_servers.mp4")}
            muted
            style={{
              width: "100%",
              height: "100%",
              objectFit: "cover",
              transform: `scale(${brollScale})`,
              filter: "contrast(1.25) saturate(0.7) brightness(0.36) blur(5px)",
            }}
          />
        </AbsoluteFill>
      </Sequence>

      <Sequence from={fB4Start} durationInFrames={fB4End - fB4Start}>
        <AbsoluteFill>
          <OffthreadVideo
            src={staticFile("broll/broll_cooling_towers.mp4")}
            muted
            style={{
              width: "100%",
              height: "100%",
              objectFit: "cover",
              transform: `scale(${brollScale})`,
              filter: "contrast(1.3) saturate(0.6) brightness(0.42) blur(3px)",
            }}
          />
        </AbsoluteFill>
      </Sequence>

      <Sequence from={fB5Start} durationInFrames={500}>
        <AbsoluteFill>
          <OffthreadVideo
            src={staticFile("broll/broll_power_lines.mp4")}
            muted
            style={{
              width: "100%",
              height: "100%",
              objectFit: "cover",
              transform: `scale(${brollScale})`,
              filter: "contrast(1.3) saturate(0.5) brightness(0.35) blur(4px)",
            }}
          />
        </AbsoluteFill>
      </Sequence>

      {/* LAYER 2: ATMOSPHERIC FOCUS, VOLUMETRIC SPOTLIGHT & 35MM GRAIN */}
      <FilmGrainAndVignette accentColor={accentColor} frame={frame} />

      {/* SCENE 1: THE $22 ELECTRIC BILL SHOCK */}
      {t < b2Start && (
        <AbsoluteFill
          style={{
            justifyContent: "center",
            alignItems: "center",
            padding: "0 54px",
          }}
        >
          {t < 3.1 ? (
            (() => {
              const s = spring({
                frame,
                fps,
                config: { damping: 11, stiffness: 130 },
              });
              const billAmount = interpolate(frame, [0, 38], [0, 22], {
                extrapolateRight: "clamp",
              });
              return (
                <div
                  style={{
                    width: "100%",
                    transform: `scale(${interpolate(s, [0, 1], [0.7, 1])})`,
                    display: "flex",
                    flexDirection: "column",
                    alignItems: "center",
                    textAlign: "center",
                  }}
                >
                  <div
                    style={{
                      backgroundColor: "#FF2A4B",
                      color: "#FFFFFF",
                      fontSize: 34,
                      fontWeight: 900,
                      padding: "12px 32px",
                      letterSpacing: 6,
                      marginBottom: 28,
                      boxShadow: "0 14px 40px rgba(255,42,75,0.5)",
                    }}
                  >
                    RESIDENTIAL UTILITY NOTICE
                  </div>
                  <div
                    style={{
                      fontSize: 210,
                      fontWeight: 900,
                      color: "#E2FF00",
                      lineHeight: 0.95,
                      letterSpacing: -6,
                      textShadow: "0 20px 60px rgba(0,0,0,0.95)",
                    }}
                  >
                    +${Math.round(billAmount)}/MO
                  </div>
                  <div
                    style={{
                      fontSize: 78,
                      fontWeight: 900,
                      color: "#FFFFFF",
                      lineHeight: 1.05,
                      marginTop: 24,
                      textTransform: "uppercase",
                      textShadow: "0 12px 35px rgba(0,0,0,0.95)",
                    }}
                  >
                    ELECTRIC BILL
                    <br />
                    <span style={{ color: "#FF2A4B" }}>SHOCK</span>
                  </div>
                </div>
              );
            })()
          ) : (
            (() => {
              const localF = frame - Math.round(3.1 * fps);
              const s1 = spring({
                frame: localF,
                fps,
                config: { damping: 12, stiffness: 120 },
              });
              const strikeWidth = interpolate(localF, [35, 65], [0, 100], {
                extrapolateLeft: "clamp",
                extrapolateRight: "clamp",
              });
              const showBottom = localF >= 58;
              const s2 = spring({
                frame: Math.max(0, localF - 58),
                fps,
                config: { damping: 11, stiffness: 140 },
              });

              return (
                <div
                  style={{
                    width: "100%",
                    display: "flex",
                    flexDirection: "column",
                    gap: 44,
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{
                      transform: `translateY(${(1 - s1) * 80}px)`,
                      opacity: s1,
                      backgroundColor: "rgba(15, 23, 42, 0.85)",
                      borderLeft: "12px solid #06B6D4",
                      padding: "36px 42px",
                      position: "relative",
                    }}
                  >
                    <div
                      style={{
                        fontSize: 28,
                        fontWeight: 800,
                        color: "#06B6D4",
                        letterSpacing: 4,
                        marginBottom: 12,
                      }}
                    >
                      SILICON VALLEY'S PROMISE:
                    </div>
                    <div
                      style={{
                        fontSize: 76,
                        fontWeight: 900,
                        color: "#FFFFFF",
                        lineHeight: 1.05,
                        position: "relative",
                        display: "inline-block",
                      }}
                    >
                      "CURE CANCER &
                      <br />
                      DO YOUR TAXES"
                      <div
                        style={{
                          position: "absolute",
                          left: 0,
                          top: "52%",
                          height: 16,
                          width: `${strikeWidth}%`,
                          backgroundColor: "#FF2A4B",
                          transform: "rotate(-3deg)",
                          boxShadow: "0 0 25px #FF2A4B",
                        }}
                      />
                    </div>
                  </div>

                  {showBottom && (
                    <div
                      style={{
                        transform: `scale(${interpolate(s2, [0, 1], [1.35, 1])})`,
                        backgroundColor: "#FF2A4B",
                        padding: "42px 44px",
                        boxShadow: "0 30px 80px rgba(255, 42, 75, 0.45)",
                      }}
                    >
                      <div
                        style={{
                          fontSize: 28,
                          fontWeight: 900,
                          color: "#090D16",
                          letterSpacing: 4,
                          marginBottom: 10,
                        }}
                      >
                        WHAT AI ACTUALLY DID FIRST:
                      </div>
                      <div
                        style={{
                          fontSize: 82,
                          fontWeight: 900,
                          color: "#FFFFFF",
                          lineHeight: 1.0,
                          textTransform: "uppercase",
                        }}
                      >
                        MADE YOUR AC
                        <br />
                        <span style={{ color: "#E2FF00" }}>UNAFFORDABLE.</span>
                      </div>
                    </div>
                  )}
                </div>
              );
            })()
          )}
        </AbsoluteFill>
      )}

      {/* SCENE 2: ALTERNATIVE A — 2.5D NOIR INVESTIGATOR ANCHOR */}
      {t >= b2Start && t < b3Start && (
        <AbsoluteFill>
          <NoirInvestigatorParallax
            frame={frame - fB2Start}
            fps={fps}
            mode="window_bunkers"
          />
          <div
            style={{
              position: "absolute",
              top: 120,
              left: 54,
              right: 54,
              display: "flex",
              flexDirection: "column",
              alignItems: "center",
              textAlign: "center",
            }}
          >
            <div
              style={{
                fontSize: 66,
                fontWeight: 900,
                color: "#FFFFFF",
                lineHeight: 1.04,
                textTransform: "uppercase",
                textShadow: "0 16px 40px rgba(0,0,0,0.95)",
              }}
            >
              {t < b2Start + 2.8 ? (
                <>
                  NO HOT TUB.
                  <br />
                  <span style={{ color: "#06B6D4" }}>NO OVEN LEFT ON.</span>
                </>
              ) : (
                <>
                  <span style={{ color: "#E2FF00" }}>3 CONCRETE BUNKERS</span>
                  <br />
                  PLUGGED INTO YOUR TOWN
                </>
              )}
            </div>
          </div>
        </AbsoluteFill>
      )}

      {/* SCENE 3: THE CORPORATE HEIST & PUCO DOCKET */}
      {t >= b3Start && t < b4Start && (
        <AbsoluteFill>
          {t < b3Start + 3.8 ? (
            (() => {
              const localF = frame - fB3Start;
              const pop = spring({
                frame: localF,
                fps,
                config: { damping: 12, stiffness: 130 },
              });
              return (
                <AbsoluteFill
                  style={{
                    justifyContent: "center",
                    alignItems: "center",
                    padding: "0 50px",
                    textAlign: "center",
                  }}
                >
                  <div
                    style={{
                      transform: `scale(${interpolate(pop, [0, 1], [0.8, 1])})`,
                    }}
                  >
                    <div
                      style={{
                        fontSize: 34,
                        fontWeight: 800,
                        color: "#06B6D4",
                        letterSpacing: 6,
                        marginBottom: 20,
                      }}
                    >
                      INSIDE THE WINDOWLESS WALLS
                    </div>
                    <div
                      style={{
                        fontSize: 132,
                        fontWeight: 900,
                        color: "#E2FF00",
                        lineHeight: 0.95,
                        textShadow: "0 20px 50px rgba(0,0,0,0.95)",
                      }}
                    >
                      10,000+
                      <br />
                      <span style={{ color: "#FFFFFF", fontSize: 108 }}>
                        AI CHIPS
                      </span>
                    </div>
                    <div
                      style={{
                        marginTop: 32,
                        backgroundColor: "#FF2A4B",
                        color: "#FFFFFF",
                        fontSize: 52,
                        fontWeight: 900,
                        padding: "18px 36px",
                        display: "inline-block",
                      }}
                    >
                      BURNING A SMALL CITY'S POWER
                    </div>
                  </div>
                </AbsoluteFill>
              );
            })()
          ) : (
            <ForensicDocketDesk
              localFrame={frame - Math.round((b3Start + 3.8) * fps)}
              fps={fps}
            />
          )}
        </AbsoluteFill>
      )}

      {/* SCENE 4: THE PHYSICAL LIMIT & +800% SPIKE */}
      {t >= b4Start && t < b4End && (
        <AbsoluteFill
          style={{
            justifyContent: "center",
            alignItems: "center",
            padding: "0 54px",
          }}
        >
          {t < b4Start + 3.6 ? (
            <div style={{ width: "100%", textAlign: "left" }}>
              <div
                style={{
                  fontSize: 96,
                  fontWeight: 900,
                  color: "#FFFFFF",
                  lineHeight: 0.98,
                  textTransform: "uppercase",
                  marginBottom: 42,
                  textShadow: "0 18px 45px rgba(0,0,0,0.95)",
                }}
              >
                SOFTWARE
                <br />
                SCALES
                <br />
                <span style={{ color: "#06B6D4" }}>INFINITELY.</span>
              </div>
              <div
                style={{
                  backgroundColor: "#F59E0B",
                  color: "#060911",
                  padding: "34px 40px",
                  fontSize: 82,
                  fontWeight: 900,
                  lineHeight: 0.98,
                  textTransform: "uppercase",
                  boxShadow: "0 24px 60px rgba(245, 158, 11, 0.45)",
                }}
              >
                COPPER & COAL
                <br />
                DO NOT.
              </div>
            </div>
          ) : (
            (() => {
              const localF = frame - Math.round((b4Start + 3.6) * fps);
              const progress = interpolate(localF, [0, 58], [0, 1], {
                extrapolateRight: "clamp",
              });
              const mwPrice = interpolate(progress, [0, 1], [28.92, 333.6]);

              return (
                <div
                  style={{
                    width: "100%",
                    display: "flex",
                    flexDirection: "column",
                    alignItems: "center",
                    textAlign: "center",
                  }}
                >
                  <div
                    style={{
                      fontSize: 32,
                      fontWeight: 800,
                      color: "#F59E0B",
                      letterSpacing: 5,
                      marginBottom: 16,
                    }}
                  >
                    13-STATE PJM GRID AUCTION
                  </div>
                  <div
                    style={{
                      fontSize: 190,
                      fontWeight: 900,
                      color: "#FF2A4B",
                      lineHeight: 0.92,
                      letterSpacing: -5,
                      textShadow: "0 20px 60px rgba(255, 42, 75, 0.55)",
                    }}
                  >
                    +{Math.round(progress * 800)}%
                  </div>
                  <div
                    style={{
                      fontSize: 74,
                      fontWeight: 900,
                      color: "#FFFFFF",
                      marginTop: 12,
                      marginBottom: 38,
                    }}
                  >
                    OVERNIGHT SPIKE
                  </div>

                  <div
                    style={{
                      width: "100%",
                      height: 340,
                      backgroundColor: "rgba(9, 13, 22, 0.88)",
                      border: "3px solid rgba(255, 42, 75, 0.6)",
                      borderRadius: 20,
                      padding: 28,
                      position: "relative",
                      display: "flex",
                      flexDirection: "column",
                      justifyContent: "space-between",
                    }}
                  >
                    <div
                      style={{
                        display: "flex",
                        justifyContent: "space-between",
                        fontFamily: "monospace",
                        fontSize: 30,
                        fontWeight: 800,
                      }}
                    >
                      <span style={{ color: "#94A3B8" }}>BEFORE: $28.92</span>
                      <span style={{ color: "#E2FF00", fontSize: 38 }}>
                        NOW: ${mwPrice.toFixed(2)}/MW-DAY
                      </span>
                    </div>
                    <svg viewBox="0 0 800 180" width="100%" height="190">
                      <path
                        d="M 20 155 L 240 150 L 440 142 L 600 95 L 770 15"
                        fill="none"
                        stroke="#FF2A4B"
                        strokeWidth="14"
                        strokeLinecap="round"
                        strokeDasharray="1000"
                        strokeDashoffset={1000 * (1 - progress)}
                      />
                    </svg>
                  </div>
                </div>
              );
            })()
          )}
        </AbsoluteFill>
      )}

      {/* SCENE 5: BALLOT REBELLION CLIMAX */}
      {t >= b5Start && t < b6Start && (
        <AbsoluteFill
          style={{
            justifyContent: "center",
            alignItems: "center",
            padding: "0 50px",
          }}
        >
          {(() => {
            const localF = frame - fB5Start;
            const slam = spring({
              frame: localF,
              fps,
              config: { damping: 11, stiffness: 150 },
            });
            const showStamp = localF >= 120;
            const stampS = spring({
              frame: Math.max(0, localF - 120),
              fps,
              config: { damping: 9, stiffness: 180 },
            });

            return (
              <div
                style={{
                  width: "100%",
                  transform: `scale(${interpolate(slam, [0, 1], [1.3, 1])})`,
                  display: "flex",
                  flexDirection: "column",
                  alignItems: "center",
                  textAlign: "center",
                  position: "relative",
                }}
              >
                <div
                  style={{
                    backgroundColor: "#E2FF00",
                    color: "#060911",
                    fontSize: 32,
                    fontWeight: 900,
                    padding: "12px 30px",
                    letterSpacing: 5,
                    marginBottom: 26,
                  }}
                >
                  NOVEMBER 3, 2026 • ELECTION REVOLT
                </div>
                <div
                  style={{
                    fontSize: 114,
                    fontWeight: 900,
                    color: "#FFFFFF",
                    lineHeight: 0.96,
                    textTransform: "uppercase",
                    textShadow: "0 20px 55px rgba(0,0,0,0.95)",
                  }}
                >
                  DATA CENTERS
                  <br />
                  <span style={{ color: "#E2FF00" }}>ON THE BALLOT</span>
                </div>

                <div
                  style={{
                    display: "flex",
                    gap: 20,
                    marginTop: 42,
                    marginBottom: 42,
                  }}
                >
                  {["TEXAS", "GEORGIA", "VIRGINIA"].map((st) => (
                    <div
                      key={st}
                      style={{
                        backgroundColor: "rgba(15, 23, 42, 0.92)",
                        border: "3px solid #06B6D4",
                        color: "#FFFFFF",
                        padding: "18px 28px",
                        fontSize: 34,
                        fontWeight: 900,
                        letterSpacing: 2,
                      }}
                    >
                      {st}
                    </div>
                  ))}
                </div>

                <div
                  style={{
                    fontSize: 56,
                    fontWeight: 900,
                    color: "#CBD5E1",
                    lineHeight: 1.15,
                    textTransform: "uppercase",
                  }}
                >
                  VOTERS BLOCKING WALL STREET'S
                  <br />
                  <span style={{ color: "#FF2A4B", fontSize: 74 }}>
                    AI CASINO
                  </span>
                </div>

                {showStamp && (
                  <div
                    style={{
                      position: "absolute",
                      top: "38%",
                      transform: `scale(${interpolate(
                        stampS,
                        [0, 1],
                        [2.6, 1]
                      )}) rotate(-10deg)`,
                      backgroundColor: "#FF2A4B",
                      color: "#FFFFFF",
                      border: "8px solid #FFFFFF",
                      padding: "20px 54px",
                      fontSize: 84,
                      fontWeight: 900,
                      letterSpacing: 6,
                      boxShadow: "0 30px 90px rgba(0,0,0,0.95)",
                    }}
                  >
                    ZONING BANNED
                  </div>
                )}
              </div>
            );
          })()}
        </AbsoluteFill>
      )}

      {/* SCENE 6: THE MIC-DROP CLIMAX & NOIR RETURN */}
      {t >= b6Start && (
        <AbsoluteFill>
          <NoirInvestigatorParallax
            frame={frame - Math.round(b6Start * fps)}
            fps={fps}
            mode="climax_return"
          />
          <AbsoluteFill
            style={{
              justifyContent: "flex-start",
              alignItems: "center",
              padding: "110px 48px 0 48px",
              textAlign: "center",
            }}
          >
            {t < b6Start + 2.4 ? (
              <div
                style={{
                  backgroundColor: "rgba(6, 9, 17, 0.90)",
                  border: "4px solid #E2FF00",
                  padding: "42px 44px",
                  width: "100%",
                  boxShadow: "0 25px 70px rgba(0,0,0,0.95)",
                }}
              >
                <div
                  style={{
                    fontSize: 30,
                    fontWeight: 800,
                    color: "#06B6D4",
                    letterSpacing: 5,
                    marginBottom: 14,
                  }}
                >
                  THE TRILLION-DOLLAR REALITY
                </div>
                <div
                  style={{
                    fontSize: 82,
                    fontWeight: 900,
                    color: "#E2FF00",
                    lineHeight: 0.98,
                  }}
                >
                  BIG TECH POCKETS
                  <br />
                  <span style={{ color: "#FFFFFF" }}>THE TRILLIONS.</span>
                </div>
              </div>
            ) : (
              (() => {
                const localF = frame - Math.round((b6Start + 2.4) * fps);
                const climaxSlam = spring({
                  frame: localF,
                  fps,
                  config: { damping: 11, stiffness: 155 },
                });
                return (
                  <div
                    style={{
                      transform: `scale(${interpolate(
                        climaxSlam,
                        [0, 1],
                        [1.32, 1]
                      )})`,
                      backgroundColor: "rgba(6, 9, 17, 0.94)",
                      border: "6px solid #FF2A4B",
                      padding: "44px 42px",
                      width: "100%",
                      boxShadow: "0 35px 95px rgba(255, 42, 75, 0.55)",
                    }}
                  >
                    <div
                      style={{
                        fontSize: 68,
                        fontWeight: 900,
                        color: "#FFFFFF",
                        lineHeight: 1.02,
                        textTransform: "uppercase",
                      }}
                    >
                      EVERY AI PROMPT
                      <br />
                      RUNS ON YOUR
                    </div>
                    <div
                      style={{
                        fontSize: 124,
                        fontWeight: 900,
                        color: "#E2FF00",
                        lineHeight: 0.95,
                        marginTop: 14,
                        letterSpacing: -2,
                        textShadow: "0 14px 40px rgba(0,0,0,0.95)",
                      }}
                    >
                      PAYCHECK.
                    </div>
                  </div>
                );
              })()
            )}
          </AbsoluteFill>
        </AbsoluteFill>
      )}
    </AbsoluteFill>
  );
};
