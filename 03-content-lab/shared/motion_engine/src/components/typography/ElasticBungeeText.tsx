import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { ChannelId, getChannelTheme } from "../../styles/theme";

export interface ElasticBungeeTextProps {
  channel?: ChannelId;
  text?: string;
  subtitle?: string;
  highlightWord?: string;
  fontFamily?: string;
}

export const ElasticBungeeText: React.FC<ElasticBungeeTextProps> = ({
  channel = "thinklate",
  text = "100% ILLEGAL",
  subtitle = "ACCORDING TO MUNICIPAL HOTEL REGULATIONS",
  highlightWord = "ILLEGAL",
  fontFamily = '"Cabinet Grotesk", "Impact", "Arial Black", sans-serif',
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const theme = getChannelTheme(channel);

  // Elastic bungee entrance spring
  const fallProgress = spring({
    frame,
    fps,
    config: { damping: 7, mass: 1.1, stiffness: 180 },
  });

  // Calculate squash and stretch dynamically from impact timing
  const translateY = (1 - fallProgress) * -450;
  const stretchY = interpolate(frame, [0, 10, 14, 19, 28], [1.4, 1.3, 0.75, 1.08, 1.0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const stretchX = 2 - stretchY; // conserve volume

  // Impact frame shockwave (hits around frame 14)
  const impactFrame = 12;
  const shockwaveScale = interpolate(frame, [impactFrame, impactFrame + 20], [0.3, 2.8], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const shockwaveOpacity = interpolate(frame, [impactFrame, impactFrame + 20], [0.8, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Screen impact micro-shake
  const shake = frame >= impactFrame && frame < impactFrame + 10
    ? Math.sin((frame - impactFrame) * 1.5) * (impactFrame + 10 - frame) * 1.2
    : 0;

  const words = text.split(" ");

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
        transform: `translateY(${shake}px)`,
        position: "relative",
      }}
    >
      {/* Floor Shockwave Ring */}
      <div
        style={{
          position: "absolute",
          width: "500px",
          height: "140px",
          borderRadius: "50%",
          border: `3px solid ${theme.colors.accent}`,
          boxShadow: theme.shadows.glowAccent,
          transform: `scale(${shockwaveScale})`,
          opacity: shockwaveOpacity,
          pointerEvents: "none",
        }}
      />

      {/* Main Elastic Bungee Typography */}
      <div
        style={{
          transform: `translateY(${translateY}px) scale(${stretchX}, ${stretchY})`,
          transformOrigin: "center bottom",
          textAlign: "center",
          display: "flex",
          gap: "24px",
          justifyContent: "center",
        }}
      >
        {words.map((w, idx) => {
          const isHighlight = w.toLowerCase().includes(highlightWord.toLowerCase());
          return (
            <span
              key={idx}
              style={{
                fontFamily,
                fontSize: "128px",
                fontWeight: 900,
                letterSpacing: "-0.03em",
                textTransform: "uppercase",
                color: isHighlight ? theme.colors.accent : theme.colors.textWhite,
                textShadow: isHighlight
                  ? `${theme.shadows.glowAccent}, 0 0 60px ${theme.colors.accent}`
                  : "0 10px 40px rgba(0, 0, 0, 0.8)",
              }}
            >
              {w}
            </span>
          );
        })}
      </div>

      {/* Subtitle tag with delayed spring */}
      <div
        style={{
          marginTop: "20px",
          fontSize: "24px",
          fontWeight: 800,
          letterSpacing: "0.15em",
          color: theme.colors.textMuted,
          fontFamily: theme.fonts.mono,
          opacity: interpolate(frame, [18, 28], [0, 1], { extrapolateRight: "clamp" }),
          textShadow: "0 4px 15px rgba(0, 0, 0, 0.8)",
        }}
      >
        {subtitle}
      </div>
    </div>
  );
};
