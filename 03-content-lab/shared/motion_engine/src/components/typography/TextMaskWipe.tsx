import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { ChannelId, getChannelTheme } from "../../styles/theme";

export interface TextMaskWipeProps {
  channel?: ChannelId;
  topLine?: string;
  mainText?: string;
  subText?: string;
  accentWord?: string;
  fontFamily?: string;
}

export const TextMaskWipe: React.FC<TextMaskWipeProps> = ({
  channel = "thinklate",
  topLine = "THE UNCOMFORTABLE REALITY",
  mainText = "SYSTEMIC ARBITRAGE",
  subText = "HOW FOUNDERS EXPLOIT MONOPOLY BOTTLENECKS",
  accentWord = "ARBITRAGE",
  fontFamily = '"Cabinet Grotesk", "Clash Display", "Impact", "Arial Black", sans-serif',
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const theme = getChannelTheme(channel);

  // Layer 1: Mask wipe horizontal line animation (frames 0 to 22)
  const wipeBarWidth = interpolate(frame, [0, 18, 32], [0, 100, 0], {
    extrapolateRight: "clamp",
  });
  const barLeft = interpolate(frame, [0, 18, 32], [0, 0, 100], {
    extrapolateRight: "clamp",
  });

  // Layer 2: Main text rising up through the matte mask window
  const textRise = spring({
    frame: Math.max(0, frame - 10),
    fps,
    config: {
      damping: theme.motion.damping,
      mass: theme.motion.mass,
      stiffness: theme.motion.stiffness,
    },
  });
  const translateY = (1 - textRise) * 110;

  // Layer 3: Top line and Subtext staggered reveal
  const topOpacity = interpolate(frame, [5, 15], [0, 1], { extrapolateRight: "clamp" });
  const subSpring = spring({
    frame: Math.max(0, frame - 22),
    fps,
    config: { damping: 12, mass: 0.6, stiffness: 130 },
  });

  // Split main text to highlight the accent word
  const words = mainText.split(" ");

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
        fontFamily: theme.fonts.sans,
      }}
    >
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          textAlign: "center",
          maxWidth: "1600px",
        }}
      >
        {/* Top Tagline */}
        <div
          style={{
            fontSize: "20px",
            fontWeight: 800,
            letterSpacing: "0.25em",
            textTransform: "uppercase",
            color: theme.colors.accent,
            fontFamily: theme.fonts.mono,
            opacity: topOpacity,
            marginBottom: "16px",
            textShadow: theme.shadows.glowAccent,
          }}
        >
          {topLine}
        </div>

        {/* Masked Main Typography Container */}
        <div
          style={{
            position: "relative",
            overflow: "hidden",
            padding: "8px 24px",
          }}
        >
          {/* Main Text Sliding from bottom mask */}
          <h1
            style={{
              margin: 0,
              fontSize: "108px",
              fontWeight: 900,
              letterSpacing: "-0.03em",
              textTransform: "uppercase",
              fontFamily,
              lineHeight: 1.05,
              transform: `translateY(${translateY}%)`,
              display: "flex",
              gap: "28px",
              justifyContent: "center",
            }}
          >
            {words.map((w, idx) => {
              const isAccent = w.toLowerCase().includes(accentWord.toLowerCase());
              return (
                <span
                  key={idx}
                  style={{
                    color: isAccent ? theme.colors.accent : theme.colors.textWhite,
                    textShadow: isAccent
                      ? `${theme.shadows.glowAccent}, 0 0 60px ${theme.colors.accent}`
                      : "0 10px 40px rgba(0, 0, 0, 0.7)",
                  }}
                >
                  {w}
                </span>
              );
            })}
          </h1>

          {/* Shooting wipe bar overlay */}
          <div
            style={{
              position: "absolute",
              bottom: 0,
              left: `${barLeft}%`,
              width: `${wipeBarWidth}%`,
              height: "6px",
              backgroundColor: theme.colors.accent,
              boxShadow: theme.shadows.glowAccent,
            }}
          />
        </div>

        {/* Subtext with tracking expansion */}
        <div
          style={{
            marginTop: "24px",
            fontSize: "26px",
            fontWeight: 700,
            color: theme.colors.textMuted,
            letterSpacing: `${interpolate(frame, [22, 60], [0.02, 0.12], { extrapolateRight: "clamp" })}em`,
            opacity: interpolate(frame, [22, 32], [0, 1], { extrapolateRight: "clamp" }),
            transform: `translateY(${(1 - subSpring) * 20}px)`,
            fontFamily: theme.fonts.sans,
            textShadow: "0 4px 20px rgba(0, 0, 0, 0.8)",
          }}
        >
          {subText}
        </div>
      </div>
    </div>
  );
};
