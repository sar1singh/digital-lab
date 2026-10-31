import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { THEME } from "../../styles/theme";

export interface StrikethroughSlamProps {
  badgeText?: string;
  mythStatement?: string;
  strikeLabel?: string;
  truthStatement?: string;
}

export const StrikethroughSlam: React.FC<StrikethroughSlamProps> = ({
  badgeText = "CORPORATE MYTH DISPATCH",
  mythStatement = "“Cleaning fees are strictly passed along 100% to independent local cleaners.”",
  strikeLabel = "FALSE // SYSTEM AUDIT",
  truthStatement = "INTERNAL AUDIT: Over 70% of operators use automated outsourced software and pocket the spread.",
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const cardScale = spring({
    frame,
    fps,
    config: { damping: 14, mass: 0.8, stiffness: 100 },
  });

  const opacity = interpolate(frame, [0, 6], [0, 1], { extrapolateRight: "clamp" });

  // Strike bar sweeps across from frame 15 to 30
  const strikeProgress = interpolate(frame, [15, 30], [0, 100], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Truth stamp pops at frame 32
  const stampSpring = spring({
    frame: Math.max(0, frame - 32),
    fps,
    config: { damping: 10, mass: 0.5, stiffness: 170 },
  });

  return (
    <div
      style={{
        width: "100%",
        height: "100%",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        fontFamily: THEME.fonts.sans,
        backgroundColor: "transparent",
      }}
    >
      <div
        style={{
          width: "1380px",
          backgroundColor: THEME.colors.bgGlassDark,
          backdropFilter: "blur(24px)",
          borderRadius: "24px",
          border: `1px solid ${THEME.colors.borderCrimson}`,
          boxShadow: THEME.shadows.glass,
          padding: "52px 64px",
          transform: `scale(${cardScale})`,
          opacity,
          display: "flex",
          flexDirection: "column",
          gap: "24px",
          position: "relative",
          overflow: "hidden",
        }}
      >
        {/* Top Edge Bar */}
        <div style={{ position: "absolute", top: 0, left: 0, right: 0, height: "4px", backgroundColor: THEME.colors.crimsonRed }} />

        {/* Header */}
        <div style={{ display: "flex", justifyContent: "space-between", borderBottom: "1px solid rgba(255, 255, 255, 0.08)", paddingBottom: "14px" }}>
          <div style={{ fontFamily: THEME.fonts.mono, fontSize: "12px", fontWeight: 700, color: THEME.colors.crimsonRed, letterSpacing: "0.2em" }}>
            ● {badgeText}
          </div>
          <div style={{ fontFamily: THEME.fonts.mono, fontSize: "12px", color: THEME.colors.textDim, letterSpacing: "0.15em" }}>
            EXHIBIT // DEBUNKED
          </div>
        </div>

        {/* Myth Statement with Strikethrough */}
        <div style={{ position: "relative", margin: "12px 0" }}>
          <h2
            style={{
              fontSize: "38px",
              fontWeight: 800,
              lineHeight: 1.35,
              color: THEME.colors.textMuted,
              letterSpacing: "-0.02em",
              margin: 0,
              opacity: strikeProgress > 80 ? 0.45 : 0.9,
              transition: "opacity 0.2s ease",
            }}
          >
            {mythStatement}
          </h2>

          {/* Crimson Strikethrough Bar */}
          <div
            style={{
              position: "absolute",
              top: "50%",
              left: 0,
              width: `${strikeProgress}%`,
              height: "6px",
              backgroundColor: THEME.colors.crimsonRed,
              boxShadow: THEME.shadows.glowCrimson,
              transform: "translateY(-50%) rotate(-1.5deg)",
              borderRadius: "4px",
            }}
          />

          {/* Stamp Pop */}
          <div
            style={{
              position: "absolute",
              right: "40px",
              top: "50%",
              transform: `translateY(-50%) rotate(8deg) scale(${stampSpring})`,
              opacity: stampSpring,
              border: `3px solid ${THEME.colors.crimsonRed}`,
              borderRadius: "8px",
              padding: "6px 20px",
              fontFamily: THEME.fonts.mono,
              fontWeight: 900,
              fontSize: "16px",
              color: THEME.colors.crimsonRed,
              boxShadow: THEME.shadows.glowCrimson,
              backgroundColor: "rgba(10, 15, 26, 0.9)",
              letterSpacing: "0.18em",
            }}
          >
            {strikeLabel}
          </div>
        </div>

        {/* Truth Statement Box */}
        <div
          style={{
            backgroundColor: "rgba(226, 255, 0, 0.08)",
            borderLeft: `4px solid ${THEME.colors.acidLime}`,
            borderRadius: "0 12px 12px 0",
            padding: "20px 26px",
            fontSize: "20px",
            fontWeight: 600,
            color: THEME.colors.textWhite,
            lineHeight: 1.45,
          }}
        >
          {truthStatement}
        </div>
      </div>
    </div>
  );
};
