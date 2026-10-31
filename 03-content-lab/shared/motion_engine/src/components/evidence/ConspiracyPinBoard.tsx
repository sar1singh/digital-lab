import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { ChannelId, getChannelTheme } from "../../styles/theme";

export interface BoardEntity {
  name: string;
  tag: string;
  detail?: string;
  icon?: string;
}

export interface ConspiracyPinBoardProps {
  channel?: ChannelId;
  boardTitle?: string;
  leftEntity?: BoardEntity;
  rightEntity?: BoardEntity;
  connectionLabel?: string;
  evidenceNote?: string;
}

export const ConspiracyPinBoard: React.FC<ConspiracyPinBoardProps> = ({
  channel = "thinklate",
  boardTitle = "FORENSIC CONNECTION // ASYMMETRIC VALUE TRAIL",
  leftEntity = {
    name: "THE $80 AIRBED RUG",
    tag: "BOOTSTRAP PROTOTYPE // SFO",
    detail: "3 Living room mattresses funded founder rent in October 2007",
    icon: "🛏️",
  },
  rightEntity = {
    name: "HILTON & MARRIOTT CARTEL",
    tag: "LEGACY MONOPOLY // $140B",
    detail: "Overpriced room rates during SFO design conference created artificial bottleneck",
    icon: "🏨",
  },
  connectionLabel = "71.4% VALUE ARBITRAGE EXPLOITED",
  evidenceNote = "EVIDENCE CORRELATION: DIRECT SYSTEM ARBITRAGE CONFIRMED BY TRANSACTION MANIFEST",
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const theme = getChannelTheme(channel);

  // Board entrance
  const boardScale = spring({
    frame,
    fps,
    config: { damping: 14, mass: 0.8, stiffness: 100 },
  });
  const opacity = interpolate(frame, [0, 8], [0, 1], { extrapolateRight: "clamp" });

  // Left card slam at frame 10
  const leftSlam = spring({
    frame: Math.max(0, frame - 8),
    fps,
    config: { damping: 10, mass: 0.5, stiffness: 160 },
  });

  // Right card slam at frame 20
  const rightSlam = spring({
    frame: Math.max(0, frame - 18),
    fps,
    config: { damping: 10, mass: 0.5, stiffness: 160 },
  });

  // Red string drawing progress between left and right pins (frames 26 to 52)
  const threadProgress = interpolate(frame, [26, 52], [0, 100], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Center connection label pop at frame 48
  const centerPop = spring({
    frame: Math.max(0, frame - 46),
    fps,
    config: { damping: 9, mass: 0.5, stiffness: 180 },
  });

  return (
    <div
      style={{
        width: "100%",
        height: "100%",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        fontFamily: theme.fonts.sans,
        backgroundColor: "transparent",
      }}
    >
      <div
        style={{
          width: "1440px",
          backgroundColor: "rgba(15, 17, 26, 0.72)",
          backdropFilter: "blur(32px)",
          borderRadius: "24px",
          border: `1px solid rgba(255, 255, 255, 0.16)`,
          boxShadow: `0 30px 80px rgba(0, 0, 0, 0.7), inset 0 0 40px rgba(0, 0, 0, 0.5)`,
          padding: "46px 64px",
          transform: `scale(${boardScale})`,
          opacity,
          position: "relative",
          overflow: "hidden",
        }}
      >
        {/* Header Bar */}
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "36px" }}>
          <div
            style={{
              display: "inline-flex",
              alignItems: "center",
              gap: "8px",
              padding: "6px 16px",
              borderRadius: "6px",
              backgroundColor: "rgba(239, 68, 68, 0.15)",
              border: "1px solid rgba(239, 68, 68, 0.45)",
              fontSize: "12px",
              fontWeight: 800,
              letterSpacing: "0.12em",
              color: "#EF4444",
              fontFamily: theme.fonts.mono,
            }}
          >
            <span>📌 DETECTIVE CORKBOARD</span>
            <span>{boardTitle}</span>
          </div>

          <div
            style={{
              fontSize: "12px",
              fontFamily: theme.fonts.mono,
              color: theme.colors.textDim,
            }}
          >
            CASE EXHIBIT // THREAD #42
          </div>
        </div>

        {/* Investigative Board Stage with 2 Entities and Red Thread */}
        <div
          style={{
            height: "360px",
            position: "relative",
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
            padding: "0 40px",
          }}
        >
          {/* Animated Red String SVG Layer */}
          <svg
            style={{
              position: "absolute",
              top: 0,
              left: 0,
              width: "100%",
              height: "100%",
              pointerEvents: "none",
              zIndex: 5,
            }}
          >
            {/* Red Thread Line */}
            <line
              x1="320"
              y1="180"
              x2={`${320 + (threadProgress / 100) * (1440 - 128 - 640)}`}
              y2="180"
              stroke="#EF4444"
              strokeWidth="4"
              strokeDasharray="6 4"
              style={{
                filter: "drop-shadow(0 0 8px rgba(239, 68, 68, 0.8))",
              }}
            />
          </svg>

          {/* Left Pinned Entity */}
          <div
            style={{
              width: "380px",
              backgroundColor: "rgba(255, 255, 255, 0.05)",
              border: `2px solid ${theme.colors.borderAccent}`,
              borderRadius: "14px",
              padding: "24px 28px",
              position: "relative",
              transform: `scale(${leftSlam}) rotate(-3deg)`,
              boxShadow: "0 15px 35px rgba(0, 0, 0, 0.5)",
              zIndex: 6,
            }}
          >
            {/* Red Pushpin Graphic at Top Center */}
            <div
              style={{
                position: "absolute",
                top: "-14px",
                left: "calc(50% - 10px)",
                width: "20px",
                height: "20px",
                borderRadius: "50%",
                backgroundColor: "#EF4444",
                boxShadow: "0 4px 10px rgba(0,0,0,0.6), 0 0 10px #EF4444",
                border: "2px solid #FFFFFF",
              }}
            />

            <div style={{ fontSize: "36px", marginBottom: "8px" }}>{leftEntity.icon}</div>
            <div style={{ fontSize: "11px", color: theme.colors.accent, fontFamily: theme.fonts.mono, letterSpacing: "0.1em", fontWeight: 800 }}>
              {leftEntity.tag}
            </div>
            <div style={{ fontSize: "22px", fontWeight: 900, color: theme.colors.textWhite, marginTop: "4px", marginBottom: "8px" }}>
              {leftEntity.name}
            </div>
            <div style={{ fontSize: "13px", color: theme.colors.textMuted, lineHeight: 1.4 }}>
              {leftEntity.detail}
            </div>
          </div>

          {/* Center Connection Label Badge */}
          <div
            style={{
              position: "absolute",
              top: "calc(50% - 30px)",
              left: "calc(50% - 170px)",
              width: "340px",
              padding: "12px 20px",
              backgroundColor: "#EF4444",
              borderRadius: "8px",
              textAlign: "center",
              boxShadow: "0 10px 30px rgba(239, 68, 68, 0.4), 0 4px 15px rgba(0,0,0,0.6)",
              transform: `scale(${centerPop})`,
              opacity: interpolate(frame, [46, 50], [0, 1], { extrapolateRight: "clamp" }),
              zIndex: 10,
            }}
          >
            <div style={{ fontSize: "11px", fontWeight: 900, letterSpacing: "0.15em", color: "#FFFFFF", fontFamily: theme.fonts.mono }}>
              CORRELATED VECTOR
            </div>
            <div style={{ fontSize: "16px", fontWeight: 900, color: "#FFFFFF", marginTop: "2px" }}>
              {connectionLabel}
            </div>
          </div>

          {/* Right Pinned Entity */}
          <div
            style={{
              width: "380px",
              backgroundColor: "rgba(255, 255, 255, 0.05)",
              border: `2px solid rgba(255, 255, 255, 0.18)`,
              borderRadius: "14px",
              padding: "24px 28px",
              position: "relative",
              transform: `scale(${rightSlam}) rotate(3.5deg)`,
              boxShadow: "0 15px 35px rgba(0, 0, 0, 0.5)",
              zIndex: 6,
            }}
          >
            {/* Red Pushpin Graphic at Top Center */}
            <div
              style={{
                position: "absolute",
                top: "-14px",
                left: "calc(50% - 10px)",
                width: "20px",
                height: "20px",
                borderRadius: "50%",
                backgroundColor: "#EF4444",
                boxShadow: "0 4px 10px rgba(0,0,0,0.6), 0 0 10px #EF4444",
                border: "2px solid #FFFFFF",
              }}
            />

            <div style={{ fontSize: "36px", marginBottom: "8px" }}>{rightEntity.icon}</div>
            <div style={{ fontSize: "11px", color: theme.colors.accentSecondary, fontFamily: theme.fonts.mono, letterSpacing: "0.1em", fontWeight: 800 }}>
              {rightEntity.tag}
            </div>
            <div style={{ fontSize: "22px", fontWeight: 900, color: theme.colors.textWhite, marginTop: "4px", marginBottom: "8px" }}>
              {rightEntity.name}
            </div>
            <div style={{ fontSize: "13px", color: theme.colors.textMuted, lineHeight: 1.4 }}>
              {rightEntity.detail}
            </div>
          </div>
        </div>

        {/* Footer */}
        <div
          style={{
            borderTop: "1px solid rgba(255, 255, 255, 0.08)",
            paddingTop: "16px",
            fontSize: "12px",
            fontFamily: theme.fonts.mono,
            color: theme.colors.textDim,
            display: "flex",
            justifyContent: "space-between",
          }}
        >
          <span>{evidenceNote}</span>
          <span style={{ color: "#EF4444" }}>● TIE VERIFIED</span>
        </div>
      </div>
    </div>
  );
};

