import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { THEME } from "../../styles/theme";

export interface StatDonutGaugeProps {
  badgeText?: string;
  targetPercent: number;
  label: string;
  title: string;
  description: string;
  subStatLabel?: string;
  subStatValue?: string;
  footerNote?: string;
}

export const StatDonutGauge: React.FC<StatDonutGaugeProps> = ({
  badgeText = "MARKET CONCENTRATION // ANTITRUST METRIC",
  targetPercent = 78.5,
  label = "URBAN MARKET SHARE",
  title = "THE DE FACTO SHORT-TERM MONOPOLY",
  description = "Across top 25 metropolitan areas, a single platform controls over three-quarters of all active short-term rental listings, dwarfing legacy hotel supply.",
  subStatLabel = "INDEPENDENT SUPPLY",
  subStatValue = "21.5%",
  footerNote = "SOURCE: U.S. BUREAU OF ECONOMIC ANALYSIS & AIRDNA ARCHIVE",
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const cardScale = spring({
    frame,
    fps,
    config: { damping: 14, mass: 0.8, stiffness: 100 },
  });

  const opacity = interpolate(frame, [0, 8], [0, 1], { extrapolateRight: "clamp" });

  const progressSpring = spring({
    frame: Math.max(0, frame - 10),
    fps,
    config: { damping: 15, mass: 0.8, stiffness: 90 },
  });

  const currentPercent = progressSpring * targetPercent;

  // Donut SVG geometry
  const size = 260;
  const strokeWidth = 24;
  const radius = (size - strokeWidth) / 2;
  const circumference = 2 * Math.PI * radius;
  const strokeDashoffset = circumference - (currentPercent / 100) * circumference;

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
          width: "1360px",
          backgroundColor: THEME.colors.bgGlass,
          backdropFilter: "blur(26px)",
          borderRadius: "24px",
          border: `1px solid ${THEME.colors.borderGlass}`,
          boxShadow: THEME.shadows.glass,
          padding: "48px 56px",
          transform: `scale(${cardScale})`,
          opacity,
          display: "flex",
          flexDirection: "column",
          gap: "28px",
          position: "relative",
          overflow: "hidden",
        }}
      >
        {/* Top lime line */}
        <div style={{ position: "absolute", top: 0, left: "10%", right: "10%", height: "2px", background: `linear-gradient(90deg, transparent, ${THEME.colors.acidLime}, transparent)` }} />

        {/* Header */}
        <div style={{ display: "flex", justifyContent: "space-between", borderBottom: "1px solid rgba(255, 255, 255, 0.08)", paddingBottom: "16px" }}>
          <div style={{ fontFamily: THEME.fonts.mono, fontSize: "12px", fontWeight: 700, color: THEME.colors.acidLime, letterSpacing: "0.2em" }}>
            ✦ {badgeText}
          </div>
          <div style={{ fontFamily: THEME.fonts.mono, fontSize: "12px", color: THEME.colors.textDim, letterSpacing: "0.15em" }}>
            HERFINDAHL-HIRSCHMAN INDEX
          </div>
        </div>

        {/* Main Body: Donut Meter + Content */}
        <div style={{ display: "flex", alignItems: "center", gap: "64px" }}>
          
          {/* Radial Donut SVG */}
          <div style={{ position: "relative", width: `${size}px`, height: `${size}px`, flexShrink: 0 }}>
            <svg width={size} height={size} style={{ transform: "rotate(-90deg)" }}>
              {/* Background Track */}
              <circle
                cx={size / 2}
                cy={size / 2}
                r={radius}
                fill="transparent"
                stroke="rgba(255, 255, 255, 0.08)"
                strokeWidth={strokeWidth}
              />
              {/* Progress Arc */}
              <circle
                cx={size / 2}
                cy={size / 2}
                r={radius}
                fill="transparent"
                stroke={THEME.colors.acidLime}
                strokeWidth={strokeWidth}
                strokeDasharray={circumference}
                strokeDashoffset={strokeDashoffset}
                strokeLinecap="round"
                style={{ filter: "drop-shadow(0 0 12px rgba(226, 255, 0, 0.45))" }}
              />
            </svg>

            {/* Center Percentage Display */}
            <div
              style={{
                position: "absolute",
                top: 0,
                left: 0,
                right: 0,
                bottom: 0,
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                justifyContent: "center",
              }}
            >
              <span style={{ fontSize: "44px", fontWeight: 900, color: THEME.colors.textWhite, letterSpacing: "-0.03em", lineHeight: 1 }}>
                {currentPercent.toFixed(1)}%
              </span>
              <span style={{ fontFamily: THEME.fonts.mono, fontSize: "11px", fontWeight: 700, color: THEME.colors.acidLime, letterSpacing: "0.12em", marginTop: "6px" }}>
                {label}
              </span>
            </div>
          </div>

          {/* Right Text Dossier */}
          <div style={{ display: "flex", flexDirection: "column", gap: "16px", flex: 1 }}>
            <h2 style={{ fontSize: "36px", fontWeight: 900, color: THEME.colors.textWhite, margin: 0, letterSpacing: "-0.02em" }}>
              {title}
            </h2>
            <p style={{ fontSize: "20px", lineHeight: 1.5, color: THEME.colors.textMuted, margin: 0 }}>
              {description}
            </p>

            {/* Sub-stat pill */}
            <div style={{ display: "flex", gap: "20px", marginTop: "6px" }}>
              <div style={{ backgroundColor: "rgba(255, 255, 255, 0.05)", borderLeft: `3px solid ${THEME.colors.textDim}`, padding: "10px 18px", borderRadius: "0 8px 8px 0" }}>
                <div style={{ fontFamily: THEME.fonts.mono, fontSize: "11px", color: THEME.colors.textDim }}>{subStatLabel}</div>
                <div style={{ fontSize: "20px", fontWeight: 800, color: THEME.colors.textWhite }}>{subStatValue}</div>
              </div>
            </div>
          </div>

        </div>

        {/* Footer */}
        {footerNote && (
          <div style={{ display: "flex", justifyContent: "space-between", borderTop: "1px solid rgba(255, 255, 255, 0.08)", paddingTop: "14px", fontFamily: THEME.fonts.mono, fontSize: "12px", color: THEME.colors.textDim }}>
            <span>{footerNote}</span>
            <span style={{ color: THEME.colors.acidLime }}>REGULATORY VERIFIED</span>
          </div>
        )}
      </div>
    </div>
  );
};
