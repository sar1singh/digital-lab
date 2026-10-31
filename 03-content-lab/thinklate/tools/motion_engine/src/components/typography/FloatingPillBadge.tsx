import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { THEME } from "../../styles/theme";

export interface FloatingPillBadgeProps {
  icon?: string;
  pillText: string;
  subtext?: string;
  variant?: "lime" | "crimson" | "amber" | "cyan";
  position?: "center" | "bottom" | "top_right";
}

export const FloatingPillBadge: React.FC<FloatingPillBadgeProps> = ({
  icon = "✦",
  pillText = "$1,150 OVERDUE RENT // 72 HOURS TO EVICTION",
  subtext = "CRITICAL TURNING POINT",
  variant = "lime",
  position = "center",
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const entrance = spring({
    frame,
    fps,
    config: { damping: 12, mass: 0.6, stiffness: 140 },
  });

  const opacity = interpolate(frame, [0, 6], [0, 1], { extrapolateRight: "clamp" });

  // Continuous subtle vertical float (sine wave)
  const floatY = Math.sin((frame / fps) * Math.PI * 2) * 6;

  const colorMap = {
    lime: { color: THEME.colors.acidLime, border: THEME.colors.borderAccent, glow: THEME.shadows.glowLime },
    crimson: { color: THEME.colors.crimsonRed, border: THEME.colors.borderCrimson, glow: THEME.shadows.glowCrimson },
    amber: { color: THEME.colors.warmAmber, border: "rgba(245, 158, 11, 0.4)", glow: THEME.shadows.glowAmber },
    cyan: { color: THEME.colors.cyanElectric, border: "rgba(6, 182, 212, 0.4)", glow: "0 0 30px rgba(6, 182, 212, 0.3)" },
  };

  const currentTheme = colorMap[variant] || colorMap.lime;

  const alignmentStyle: React.CSSProperties =
    position === "bottom"
      ? { justifyContent: "center", alignItems: "flex-end", paddingBottom: "100px" }
      : position === "top_right"
      ? { justifyContent: "flex-end", alignItems: "flex-start", padding: "80px 100px" }
      : { justifyContent: "center", alignItems: "center" };

  return (
    <div
      style={{
        width: "100%",
        height: "100%",
        display: "flex",
        ...alignmentStyle,
        backgroundColor: "transparent",
        fontFamily: THEME.fonts.mono,
      }}
    >
      <div
        style={{
          transform: `scale(${entrance}) translateY(${floatY}px)`,
          opacity,
          backgroundColor: "rgba(10, 15, 26, 0.65)",
          backdropFilter: "blur(20px)",
          border: `1.5px solid ${currentTheme.border}`,
          borderRadius: "999px",
          padding: "16px 36px",
          display: "flex",
          alignItems: "center",
          gap: "16px",
          boxShadow: `${THEME.shadows.glass}, ${currentTheme.glow}`,
        }}
      >
        <span
          style={{
            fontSize: "20px",
            color: currentTheme.color,
          }}
        >
          {icon}
        </span>
        <div style={{ display: "flex", flexDirection: "column" }}>
          <span
            style={{
              fontSize: "24px",
              fontWeight: 900,
              letterSpacing: "0.06em",
              color: THEME.colors.textWhite,
              textTransform: "uppercase",
            }}
          >
            {pillText}
          </span>
          {subtext && (
            <span
              style={{
                fontSize: "12px",
                letterSpacing: "0.18em",
                color: currentTheme.color,
                fontWeight: 700,
                textTransform: "uppercase",
                marginTop: "2px",
              }}
            >
              {subtext}
            </span>
          )}
        </div>
      </div>
    </div>
  );
};
