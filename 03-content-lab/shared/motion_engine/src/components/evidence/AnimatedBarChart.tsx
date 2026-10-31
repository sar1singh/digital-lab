import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { THEME } from "../../styles/theme";

export interface BarItem {
  label: string;
  value: number;
  suffix?: string;
  prefix?: string;
  highlight?: boolean;
  color?: string;
}

export interface AnimatedBarChartProps {
  badgeText?: string;
  title: string;
  subtitle?: string;
  bars: BarItem[];
  footerNote?: string;
}

export const AnimatedBarChart: React.FC<AnimatedBarChartProps> = ({
  badgeText = "MARKET ARBITRAGE // EMPIRICAL DATA",
  title = "VALUATION REVENUE MULTIPLES",
  subtitle = "Public Hotel Operators vs Solo Airbed Platform",
  bars = [
    { label: "Marriott Int.", value: 1.8, suffix: "x", highlight: false },
    { label: "Hilton Worldwide", value: 2.1, suffix: "x", highlight: false },
    { label: "Hyatt Hotels", value: 1.5, suffix: "x", highlight: false },
    { label: "Airbnb (Peak)", value: 14.5, suffix: "x", highlight: true, color: THEME.colors.acidLime },
  ],
  footerNote = "SOURCE: SEC FORM 10-K & BLOOMBERG MARKET BENCHMARKS",
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Motion 1: Master card entrance
  const cardScale = spring({
    frame,
    fps,
    config: { damping: 14, mass: 0.8, stiffness: 100 },
  });

  const opacity = interpolate(frame, [0, 8], [0, 1], { extrapolateRight: "clamp" });

  const maxValue = Math.max(...bars.map((b) => b.value), 1);

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
          backgroundColor: THEME.colors.bgGlass,
          backdropFilter: "blur(24px)",
          borderRadius: "24px",
          border: `1px solid ${THEME.colors.borderGlass}`,
          boxShadow: THEME.shadows.glass,
          padding: "44px 56px",
          transform: `scale(${cardScale})`,
          opacity,
          display: "flex",
          flexDirection: "column",
          gap: "24px",
          position: "relative",
          overflow: "hidden",
        }}
      >
        {/* Top lime gradient highlight */}
        <div
          style={{
            position: "absolute",
            top: 0,
            left: "10%",
            right: "10%",
            height: "2px",
            background: `linear-gradient(90deg, transparent, ${THEME.colors.acidLime}, transparent)`,
          }}
        />

        {/* Header */}
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", borderBottom: `1px solid rgba(255, 255, 255, 0.08)`, paddingBottom: "16px" }}>
          <div>
            <div
              style={{
                fontFamily: THEME.fonts.mono,
                fontSize: "12px",
                fontWeight: 700,
                letterSpacing: "0.2em",
                color: THEME.colors.acidLime,
                marginBottom: "6px",
                textTransform: "uppercase",
              }}
            >
              ✦ {badgeText}
            </div>
            <h2 style={{ fontSize: "32px", fontWeight: 900, color: THEME.colors.textWhite, margin: 0, letterSpacing: "-0.02em" }}>
              {title}
            </h2>
            {subtitle && <p style={{ fontSize: "16px", color: THEME.colors.textMuted, margin: "4px 0 0 0" }}>{subtitle}</p>}
          </div>
          <div style={{ fontFamily: THEME.fonts.mono, fontSize: "12px", color: THEME.colors.textDim, letterSpacing: "0.15em" }}>
            INDEX METRIC
          </div>
        </div>

        {/* Bar Chart Area */}
        <div
          style={{
            height: "320px",
            display: "flex",
            alignItems: "flex-end",
            justifyContent: "space-around",
            padding: "20px 20px 0 20px",
            position: "relative",
            borderBottom: `2px solid rgba(255, 255, 255, 0.15)`,
          }}
        >
          {/* Subtle horizontal grid lines */}
          <div style={{ position: "absolute", top: "25%", left: 0, right: 0, height: "1px", backgroundColor: "rgba(255, 255, 255, 0.05)" }} />
          <div style={{ position: "absolute", top: "50%", left: 0, right: 0, height: "1px", backgroundColor: "rgba(255, 255, 255, 0.05)" }} />
          <div style={{ position: "absolute", top: "75%", left: 0, right: 0, height: "1px", backgroundColor: "rgba(255, 255, 255, 0.05)" }} />

          {bars.map((bar, idx) => {
            // Motion 2: Staggered bar rise
            const barStart = 10 + idx * 5;
            const barSpring = spring({
              frame: Math.max(0, frame - barStart),
              fps,
              config: { damping: 14, mass: 0.6, stiffness: 120 },
            });

            // Motion 3: Dynamic numeric roll-up
            const currentVal = (barSpring * bar.value).toFixed(1);

            const targetHeightPct = (bar.value / maxValue) * 100;
            const currentHeight = targetHeightPct * barSpring;
            const isHighlight = bar.highlight;
            const barColor = isHighlight ? (bar.color || THEME.colors.acidLime) : "rgba(255, 255, 255, 0.25)";

            // Motion 4: Ambient glow pulse on the highlight bar
            const glowPulse = isHighlight ? 1 + Math.sin((frame / fps) * 4) * 0.15 : 1;

            return (
              <div
                key={idx}
                style={{
                  display: "flex",
                  flexDirection: "column",
                  alignItems: "center",
                  justifyContent: "flex-end",
                  width: "140px",
                  height: "100%",
                }}
              >
                {/* Dynamic Value Label above bar */}
                <div
                  style={{
                    opacity: barSpring,
                    transform: `translateY(${(1 - barSpring) * 15}px) scale(${isHighlight ? glowPulse : 1})`,
                    marginBottom: "12px",
                    fontFamily: THEME.fonts.mono,
                    fontSize: isHighlight ? "26px" : "18px",
                    fontWeight: 900,
                    color: isHighlight ? THEME.colors.acidLime : THEME.colors.textWhite,
                    textShadow: isHighlight ? THEME.shadows.glowLime : "none",
                    fontVariantNumeric: "tabular-nums",
                  }}
                >
                  {bar.prefix || ""}{currentVal}{bar.suffix || "x"}
                </div>

                {/* The Bar Pillar */}
                <div
                  style={{
                    width: "100%",
                    height: `${currentHeight}%`,
                    backgroundColor: barColor,
                    borderRadius: "8px 8px 0 0",
                    boxShadow: isHighlight ? THEME.shadows.glowLime : "none",
                    position: "relative",
                  }}
                >
                  {/* Top edge gleam */}
                  <div
                    style={{
                      position: "absolute",
                      top: 0,
                      left: 0,
                      right: 0,
                      height: "3px",
                      backgroundColor: "rgba(255, 255, 255, 0.6)",
                      borderRadius: "8px 8px 0 0",
                    }}
                  />
                </div>

                {/* Bar Label below baseline */}
                <div
                  style={{
                    marginTop: "14px",
                    fontFamily: THEME.fonts.sans,
                    fontSize: "15px",
                    fontWeight: isHighlight ? 800 : 600,
                    color: isHighlight ? THEME.colors.textWhite : THEME.colors.textDim,
                    textAlign: "center",
                    whiteSpace: "nowrap",
                  }}
                >
                  {bar.label}
                </div>
              </div>
            );
          })}
        </div>

        {/* Footer */}
        {footerNote && (
          <div
            style={{
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
              fontFamily: THEME.fonts.mono,
              fontSize: "12px",
              color: THEME.colors.textDim,
              letterSpacing: "0.12em",
              paddingTop: "8px",
            }}
          >
            <span>{footerNote}</span>
            <span style={{ color: THEME.colors.acidLime }}>VERIFIED SPREAD</span>
          </div>
        )}
      </div>
    </div>
  );
};
