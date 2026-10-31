import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { ChannelId, getChannelTheme } from "../../styles/theme";

export interface CurtainSwipeRevealProps {
  channel?: ChannelId;
  heading?: string;
  punchline?: string;
  categoryTag?: string;
}

export const CurtainSwipeReveal: React.FC<CurtainSwipeRevealProps> = ({
  channel = "thinklate",
  heading = "THE FOUNDERS DIDN'T RAISE VC MONEY.",
  punchline = "THEY SOLD BREAKFAST CEREAL.",
  categoryTag = "UNCONVENTIONAL EXECUTION",
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const theme = getChannelTheme(channel);

  // Curtain wipe progress (frames 0 to 22)
  const curtainProgress = interpolate(frame, [0, 22], [0, 100], {
    extrapolateRight: "clamp",
  });

  // Second curtain trailing (frames 4 to 28)
  const curtain2Progress = interpolate(frame, [4, 28], [0, 100], {
    extrapolateRight: "clamp",
  });

  // Typography entrance spring after curtain clears (frame 18)
  const textSpring = spring({
    frame: Math.max(0, frame - 16),
    fps,
    config: {
      damping: theme.motion.damping,
      mass: theme.motion.mass,
      stiffness: theme.motion.stiffness,
    },
  });

  const punchlinePulse = Math.sin(frame / 6) * 0.05 + 1.0;

  return (
    <div
      style={{
        width: "100%",
        height: "100%",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        backgroundColor: "transparent",
        position: "relative",
        overflow: "hidden",
        fontFamily: theme.fonts.sans,
      }}
    >
      {/* Wipe Curtain Layer 1 (Accent Color) */}
      <div
        style={{
          position: "absolute",
          top: 0,
          left: 0,
          bottom: 0,
          width: `${curtainProgress}%`,
          backgroundColor: theme.colors.accent,
          zIndex: 20,
          clipPath: "polygon(0 0, 100% 0, 85% 100%, 0% 100%)",
          display: curtainProgress >= 100 ? "none" : "block",
        }}
      />

      {/* Wipe Curtain Layer 2 (Dark Obsidian Glass) */}
      <div
        style={{
          position: "absolute",
          top: 0,
          left: 0,
          bottom: 0,
          width: `${curtain2Progress}%`,
          backgroundColor: "#0A0F1A",
          zIndex: 19,
          clipPath: "polygon(0 0, 100% 0, 85% 100%, 0% 100%)",
          display: curtain2Progress >= 100 ? "none" : "block",
        }}
      />

      {/* Hero Typography Content */}
      <div
        style={{
          maxWidth: "1400px",
          textAlign: "center",
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          gap: "20px",
          transform: `scale(${textSpring})`,
          opacity: interpolate(frame, [14, 20], [0, 1], { extrapolateRight: "clamp" }),
          zIndex: 10,
        }}
      >
        <div
          style={{
            fontSize: "18px",
            fontWeight: 800,
            letterSpacing: "0.2em",
            textTransform: "uppercase",
            color: theme.colors.accentSecondary,
            fontFamily: theme.fonts.mono,
          }}
        >
          // {categoryTag} //
        </div>

        <div
          style={{
            fontSize: "44px",
            fontWeight: 700,
            color: theme.colors.textMuted,
            letterSpacing: "-0.01em",
            lineHeight: 1.2,
          }}
        >
          {heading}
        </div>

        <h1
          style={{
            fontSize: "96px",
            fontWeight: 900,
            letterSpacing: "-0.03em",
            textTransform: "uppercase",
            color: theme.colors.accent,
            fontFamily: '"Cabinet Grotesk", "Impact", "Arial Black", sans-serif',
            margin: 0,
            lineHeight: 1.05,
            textShadow: `${theme.shadows.glowAccent}, 0 10px 40px rgba(0, 0, 0, 0.9)`,
            transform: `scale(${punchlinePulse})`,
          }}
        >
          {punchline}
        </h1>
      </div>
    </div>
  );
};
