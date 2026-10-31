import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { THEME } from "../styles/theme";

export interface MetricCounterCardProps {
  badgeText?: string;
  startVal?: number;
  endVal?: number;
  prefix?: string;
  suffix?: string;
  label?: string;
  subtext?: string;
  accentColor?: string;
}

export const MetricCounterCard: React.FC<MetricCounterCardProps> = ({
  badgeText = "FINANCIAL METRIC ARBITRAGE",
  startVal = 0,
  endVal = 30000,
  prefix = "$",
  suffix = "",
  label = "CEREAL BOX BOOTSTRAP CAPITAL",
  subtext = "1,000 custom election cereal boxes sold at $40/each to fund 3 months of survival",
  accentColor = THEME.colors.acidLime,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const entrance = spring({
    frame,
    fps,
    config: { damping: 14, mass: 0.9, stiffness: 100 },
  });

  const cardY = interpolate(entrance, [0, 1], [50, 0]);
  const cardOpacity = interpolate(entrance, [0, 1], [0, 1]);

  // Counting spring animation (runs over ~45 frames)
  const countProgress = spring({
    frame: frame - 10,
    fps,
    config: { damping: 20, mass: 1, stiffness: 80 },
  });

  const currentNumber = Math.round(interpolate(countProgress, [0, 1], [startVal, endVal]));

  return (
    <div
      style={{
        width: "100%",
        height: "100%",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        fontFamily: THEME.fonts.sans,
      }}
    >
      <div
        style={{
          width: "720px",
          backgroundColor: THEME.colors.bgGlass,
          backdropFilter: "blur(24px)",
          borderRadius: "28px",
          border: `1px solid ${THEME.colors.borderGlass}`,
          boxShadow: THEME.shadows.glass,
          padding: "50px 60px",
          transform: `translateY(${cardY}px)`,
          opacity: cardOpacity,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          textAlign: "center",
          gap: "20px",
          position: "relative",
        }}
      >
        {/* Subtle accent glow behind the card */}
        <div
          style={{
            position: "absolute",
            top: "20%",
            left: "25%",
            width: "50%",
            height: "40%",
            background: accentColor,
            opacity: 0.12,
            filter: "blur(60px)",
            zIndex: -1,
          }}
        />

        {/* Badge Pill */}
        <div
          style={{
            padding: "6px 16px",
            borderRadius: "20px",
            backgroundColor: "rgba(255, 255, 255, 0.08)",
            border: `1px solid ${THEME.colors.borderGlass}`,
            color: THEME.colors.textMuted,
            fontSize: "12px",
            fontWeight: 700,
            letterSpacing: "1.5px",
            fontFamily: THEME.fonts.mono,
            textTransform: "uppercase",
          }}
        >
          {badgeText}
        </div>

        {/* Big Counter Value */}
        <div
          style={{
            fontSize: "84px",
            fontWeight: 900,
            color: accentColor,
            fontFamily: THEME.fonts.mono,
            letterSpacing: "-2px",
            lineHeight: 1,
            textShadow: `0 0 35px ${accentColor}40`,
          }}
        >
          {prefix}
          {currentNumber.toLocaleString()}
          {suffix}
        </div>

        {/* Label */}
        <div
          style={{
            fontSize: "22px",
            fontWeight: 800,
            color: THEME.colors.textWhite,
            letterSpacing: "0.5px",
            textTransform: "uppercase",
          }}
        >
          {label}
        </div>

        {/* Subtitle / Context */}
        <div
          style={{
            fontSize: "16px",
            color: THEME.colors.textMuted,
            lineHeight: 1.5,
            maxWidth: "540px",
          }}
        >
          {subtext}
        </div>
      </div>
    </div>
  );
};
