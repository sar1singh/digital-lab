import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { ChannelId, getChannelTheme } from "../../styles/theme";

export interface TypographyBackgroundWallProps {
  channel?: ChannelId;
  wallText?: string;
  centerBadgeText?: string;
  centerStatement?: string;
  subNote?: string;
}

export const TypographyBackgroundWall: React.FC<TypographyBackgroundWallProps> = ({
  channel = "thinklate",
  wallText = "DISRUPT MONOPOLY SCALE ARBITRAGE BOOTSTRAP CASHFLOW",
  centerBadgeText = "UNFAIR ADVANTAGE DETECTED",
  centerStatement = "ZERO ASSET OVERHEAD",
  subNote = "Traditional hotels own $100M concrete assets. Airbnb owns lines of code.",
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const theme = getChannelTheme(channel);

  // Background wall parallax speeds
  const offsetRow1 = (frame * 2.5) % 1800;
  const offsetRow2 = -(frame * 3.2) % 1800;
  const offsetRow3 = (frame * 2.8) % 1800;

  // Foreground card spring
  const cardScale = spring({
    frame: Math.max(0, frame - 10),
    fps,
    config: {
      damping: theme.motion.damping,
      mass: theme.motion.mass,
      stiffness: theme.motion.stiffness,
    },
  });
  const cardOpacity = interpolate(frame, [10, 18], [0, 1], { extrapolateRight: "clamp" });

  // Neon pulse
  const glowPulse = Math.sin(frame / 7) * 0.25 + 0.85;

  const repeatedString = `${wallText} • ${wallText} • ${wallText} • ${wallText}`;

  return (
    <div
      style={{
        width: "100%",
        height: "100%",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        backgroundColor: "transparent",
        position: "relative",
        overflow: "hidden",
        fontFamily: theme.fonts.sans,
      }}
    >
      {/* Background Kinetic Wall (3 Rows) */}
      <div
        style={{
          position: "absolute",
          top: 0,
          left: 0,
          right: 0,
          bottom: 0,
          display: "flex",
          flexDirection: "column",
          justifyContent: "space-around",
          opacity: 0.18,
          pointerEvents: "none",
        }}
      >
        <div
          style={{
            whiteSpace: "nowrap",
            fontFamily: '"Cabinet Grotesk", "Impact", "Arial Black", sans-serif',
            fontSize: "120px",
            fontWeight: 900,
            color: theme.colors.textWhite,
            transform: `translateX(-${offsetRow1}px)`,
          }}
        >
          {repeatedString}
        </div>

        <div
          style={{
            whiteSpace: "nowrap",
            fontFamily: '"Cabinet Grotesk", "Impact", "Arial Black", sans-serif',
            fontSize: "120px",
            fontWeight: 900,
            color: theme.colors.accent,
            transform: `translateX(${offsetRow2}px)`,
          }}
        >
          {repeatedString}
        </div>

        <div
          style={{
            whiteSpace: "nowrap",
            fontFamily: '"Cabinet Grotesk", "Impact", "Arial Black", sans-serif',
            fontSize: "120px",
            fontWeight: 900,
            color: theme.colors.textWhite,
            transform: `translateX(-${offsetRow3}px)`,
          }}
        >
          {repeatedString}
        </div>
      </div>

      {/* Foreground Hero Focus Glass Badge */}
      <div
        style={{
          backgroundColor: theme.colors.bgGlassDark,
          backdropFilter: "blur(30px)",
          border: `2px solid ${theme.colors.borderAccent}`,
          borderRadius: "20px",
          padding: "48px 64px",
          boxShadow: `${theme.shadows.glass}, 0 0 ${40 * glowPulse}px ${theme.colors.borderAccent}`,
          transform: `scale(${cardScale})`,
          opacity: cardOpacity,
          textAlign: "center",
          maxWidth: "1000px",
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          gap: "18px",
          zIndex: 10,
        }}
      >
        <div
          style={{
            display: "inline-flex",
            alignItems: "center",
            gap: "8px",
            padding: "6px 16px",
            borderRadius: "6px",
            backgroundColor: `${theme.colors.accent}18`,
            border: `1px solid ${theme.colors.borderAccent}`,
            fontSize: "13px",
            fontWeight: 800,
            letterSpacing: "0.15em",
            color: theme.colors.accent,
            fontFamily: theme.fonts.mono,
          }}
        >
          <span>●</span>
          <span>{centerBadgeText}</span>
        </div>

        <h1
          style={{
            fontSize: "76px",
            fontWeight: 900,
            color: theme.colors.textWhite,
            letterSpacing: "-0.03em",
            margin: 0,
            textTransform: "uppercase",
            fontFamily: '"Cabinet Grotesk", "Impact", sans-serif',
            textShadow: "0 6px 30px rgba(0, 0, 0, 0.9)",
          }}
        >
          {centerStatement}
        </h1>

        <div
          style={{
            fontSize: "20px",
            color: theme.colors.textMuted,
            maxWidth: "760px",
            lineHeight: 1.5,
          }}
        >
          {subNote}
        </div>
      </div>
    </div>
  );
};
