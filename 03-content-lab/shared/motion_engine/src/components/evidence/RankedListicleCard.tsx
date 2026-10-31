import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { ChannelId, getChannelTheme } from "../../styles/theme";

export interface RankedListicleCardProps {
  channel?: ChannelId;
  rankNumber?: string;
  categoryTag?: string;
  headline?: string;
  subExplanation?: string;
  footerMetric?: string;
}

export const RankedListicleCard: React.FC<RankedListicleCardProps> = ({
  channel = "thinklate",
  rankNumber = "01",
  categoryTag = "RULE #01 // THE SYSTEM ARBITRAGE",
  headline = "THE ASSET-LIGHT ADVANTAGE",
  subExplanation = "Traditional hotel empires spent $100M per tower on concrete, staff, and debt. Airbnb scaled to 100,000 rooms with $0 spent on physical real estate.",
  footerMetric = "CAPITAL EFFICIENCY RATIO: 416X MULTIPLIER",
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const theme = getChannelTheme(channel);

  // Big number entrance spring
  const numSpring = spring({
    frame,
    fps,
    config: { damping: 11, mass: 0.7, stiffness: 130 },
  });

  // Laser line draw animation (frames 10 to 45)
  const lineWidth = interpolate(frame, [10, 45], [0, 100], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Content fade & slide up
  const contentSlide = spring({
    frame: Math.max(0, frame - 18),
    fps,
    config: { damping: 12, mass: 0.6, stiffness: 120 },
  });

  // Subtle metallic glint sweep across the number
  const glintPos = interpolate(frame, [25, 75], [-100, 200], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
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
          width: "1360px",
          backgroundColor: theme.colors.bgGlassDark,
          backdropFilter: "blur(30px)",
          borderRadius: "24px",
          border: `1px solid ${theme.colors.borderGlass}`,
          boxShadow: `${theme.shadows.glass}, 0 0 50px rgba(0,0,0,0.8)`,
          padding: "54px 72px",
          display: "flex",
          flexDirection: "column",
          gap: "28px",
          position: "relative",
          overflow: "hidden",
        }}
      >
        {/* Top Header Tag */}
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
          <div
            style={{
              fontSize: "14px",
              fontWeight: 800,
              letterSpacing: "0.2em",
              color: theme.colors.accent,
              fontFamily: theme.fonts.mono,
              textTransform: "uppercase",
            }}
          >
            ✦ {categoryTag} ✦
          </div>

          <div
            style={{
              fontSize: "12px",
              fontFamily: theme.fonts.mono,
              color: theme.colors.textDim,
              letterSpacing: "0.1em",
            }}
          >
            DOCUMENTARY CHAPTER
          </div>
        </div>

        {/* Main Hero Row: Giant Numeral + Headline */}
        <div style={{ display: "flex", alignItems: "center", gap: "48px" }}>
          {/* Giant Alux-Style Number */}
          <div
            style={{
              fontSize: "150px",
              fontWeight: 900,
              fontFamily: '"Cabinet Grotesk", "Impact", "Arial Black", sans-serif',
              lineHeight: 1,
              color: theme.colors.accent,
              textShadow: `${theme.shadows.glowAccent}, 0 10px 40px rgba(0, 0, 0, 0.9)`,
              transform: `scale(${numSpring})`,
              position: "relative",
              userSelect: "none",
            }}
          >
            {rankNumber}
          </div>

          {/* Headline & Category */}
          <div style={{ flex: 1, transform: `translateY(${(1 - contentSlide) * 25}px)` }}>
            <h1
              style={{
                fontSize: "52px",
                fontWeight: 900,
                color: theme.colors.textWhite,
                margin: 0,
                letterSpacing: "-0.02em",
                lineHeight: 1.15,
                textTransform: "uppercase",
              }}
            >
              {headline}
            </h1>
          </div>
        </div>

        {/* Laser Accent Drawing Line */}
        <div
          style={{
            width: "100%",
            height: "3px",
            backgroundColor: "rgba(255, 255, 255, 0.12)",
            borderRadius: "2px",
            position: "relative",
            overflow: "hidden",
          }}
        >
          <div
            style={{
              position: "absolute",
              top: 0,
              left: 0,
              height: "100%",
              width: `${lineWidth}%`,
              background: `linear-gradient(90deg, ${theme.colors.accentSecondary}, ${theme.colors.accent})`,
              boxShadow: theme.shadows.glowAccent,
            }}
          />
        </div>

        {/* Sub-Explanation Paragraph */}
        <div
          style={{
            fontSize: "24px",
            lineHeight: 1.55,
            color: theme.colors.textMuted,
            maxWidth: "1150px",
            transform: `translateY(${(1 - contentSlide) * 20}px)`,
            opacity: interpolate(frame, [20, 32], [0, 1], { extrapolateRight: "clamp" }),
          }}
        >
          {subExplanation}
        </div>

        {/* Footer Metric Callout Bar */}
        <div
          style={{
            marginTop: "10px",
            padding: "16px 24px",
            backgroundColor: "rgba(0, 0, 0, 0.45)",
            border: `1px solid rgba(255, 255, 255, 0.08)`,
            borderRadius: "12px",
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
            fontSize: "14px",
            fontFamily: theme.fonts.mono,
            color: theme.colors.accentSecondary,
            fontWeight: 700,
          }}
        >
          <span>{footerMetric}</span>
          <span style={{ color: theme.colors.accent }}>KEY NARRATIVE TAKEAWAY</span>
        </div>
      </div>
    </div>
  );
};

