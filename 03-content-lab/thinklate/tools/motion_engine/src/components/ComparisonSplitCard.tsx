import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { THEME } from "../styles/theme";

export interface ComparisonSplitCardProps {
  badgeText?: string;
  leftTitle: string;
  leftSubtitle?: string;
  leftItems: string[];
  rightTitle: string;
  rightSubtitle?: string;
  rightItems: string[];
  footerNote?: string;
}

export const ComparisonSplitCard: React.FC<ComparisonSplitCardProps> = ({
  badgeText = "FORENSIC CONTRAST // THE REALITY GAP",
  leftTitle,
  leftSubtitle,
  leftItems,
  rightTitle,
  rightSubtitle,
  rightItems,
  footerNote,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Entrance spring
  const scale = spring({
    frame,
    fps,
    config: { damping: 14, mass: 0.8, stiffness: 100 },
  });

  const opacity = interpolate(frame, [0, 10], [0, 1], {
    extrapolateRight: "clamp",
  });

  // Staggered columns
  const leftSlide = spring({
    frame: Math.max(0, frame - 5),
    fps,
    config: { damping: 15, mass: 0.7, stiffness: 120 },
  });

  const rightSlide = spring({
    frame: Math.max(0, frame - 12),
    fps,
    config: { damping: 15, mass: 0.7, stiffness: 120 },
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
          width: "1560px",
          backgroundColor: THEME.colors.bgGlass,
          backdropFilter: "blur(24px)",
          borderRadius: "24px",
          border: `1px solid ${THEME.colors.borderGlass}`,
          boxShadow: THEME.shadows.glass,
          padding: "48px 56px",
          transform: `scale(${scale})`,
          opacity,
          display: "flex",
          flexDirection: "column",
          gap: "28px",
          position: "relative",
          overflow: "hidden",
        }}
      >
        {/* Top reflection line */}
        <div
          style={{
            position: "absolute",
            top: 0,
            left: "10%",
            right: "10%",
            height: "2px",
            background: `linear-gradient(90deg, transparent, ${THEME.colors.acidLime}, transparent)`,
            opacity: 0.8,
          }}
        />

        {/* Header badge */}
        <div
          style={{
            display: "flex",
            alignItems: "center",
            justifyContent: "space-between",
            borderBottom: `1px solid rgba(255, 255, 255, 0.08)`,
            paddingBottom: "18px",
          }}
        >
          <div
            style={{
              fontFamily: THEME.fonts.mono,
              fontSize: "13px",
              fontWeight: 700,
              letterSpacing: "0.22em",
              textTransform: "uppercase",
              color: THEME.colors.acidLime,
              display: "flex",
              alignItems: "center",
              gap: "10px",
            }}
          >
            <span
              style={{
                width: "8px",
                height: "8px",
                borderRadius: "50%",
                backgroundColor: THEME.colors.acidLime,
                boxShadow: THEME.shadows.glowLime,
              }}
            />
            {badgeText}
          </div>
          <div
            style={{
              fontFamily: THEME.fonts.mono,
              fontSize: "12px",
              color: THEME.colors.textDim,
              letterSpacing: "0.15em",
            }}
          >
            AUDIT BENCHMARK
          </div>
        </div>

        {/* 2-Column Split Content */}
        <div
          style={{
            display: "grid",
            gridTemplateColumns: "1fr 1fr",
            gap: "36px",
            position: "relative",
          }}
        >
          {/* Vertical Divider Line */}
          <div
            style={{
              position: "absolute",
              top: 0,
              bottom: 0,
              left: "50%",
              width: "1px",
              backgroundColor: "rgba(255, 255, 255, 0.1)",
              transform: "translateX(-50%)",
            }}
          />

          {/* Left Column (Old World / Corporate / Problem) */}
          <div
            style={{
              transform: `translateY(${(1 - leftSlide) * 20}px)`,
              opacity: leftSlide,
              display: "flex",
              flexDirection: "column",
              gap: "20px",
              paddingRight: "20px",
            }}
          >
            <div>
              <div
                style={{
                  fontFamily: THEME.fonts.mono,
                  fontSize: "12px",
                  fontWeight: 700,
                  color: THEME.colors.crimsonRed,
                  letterSpacing: "0.18em",
                  marginBottom: "6px",
                  textTransform: "uppercase",
                }}
              >
                ● {leftSubtitle || "ESTABLISHED INCUMBENT"}
              </div>
              <h3
                style={{
                  fontSize: "30px",
                  fontWeight: 900,
                  color: THEME.colors.textWhite,
                  letterSpacing: "-0.02em",
                  margin: 0,
                }}
              >
                {leftTitle}
              </h3>
            </div>

            <div style={{ display: "flex", flexDirection: "column", gap: "12px" }}>
              {leftItems.map((item, idx) => (
                <div
                  key={idx}
                  style={{
                    backgroundColor: "rgba(239, 68, 68, 0.08)",
                    borderLeft: `3px solid ${THEME.colors.crimsonRed}`,
                    padding: "14px 18px",
                    borderRadius: "0 10px 10px 0",
                    fontSize: "18px",
                    color: THEME.colors.textMuted,
                    lineHeight: 1.4,
                  }}
                >
                  {item}
                </div>
              ))}
            </div>
          </div>

          {/* Right Column (Disruption / Reality / Winning Play) */}
          <div
            style={{
              transform: `translateY(${(1 - rightSlide) * 20}px)`,
              opacity: rightSlide,
              display: "flex",
              flexDirection: "column",
              gap: "20px",
              paddingLeft: "20px",
            }}
          >
            <div>
              <div
                style={{
                  fontFamily: THEME.fonts.mono,
                  fontSize: "12px",
                  fontWeight: 700,
                  color: THEME.colors.acidLime,
                  letterSpacing: "0.18em",
                  marginBottom: "6px",
                  textTransform: "uppercase",
                }}
              >
                ✦ {rightSubtitle || "SYSTEM ARBITRAGE"}
              </div>
              <h3
                style={{
                  fontSize: "30px",
                  fontWeight: 900,
                  color: THEME.colors.acidLime,
                  letterSpacing: "-0.02em",
                  margin: 0,
                  textShadow: THEME.shadows.glowLime,
                }}
              >
                {rightTitle}
              </h3>
            </div>

            <div style={{ display: "flex", flexDirection: "column", gap: "12px" }}>
              {rightItems.map((item, idx) => (
                <div
                  key={idx}
                  style={{
                    backgroundColor: "rgba(226, 255, 0, 0.08)",
                    borderLeft: `3px solid ${THEME.colors.acidLime}`,
                    padding: "14px 18px",
                    borderRadius: "0 10px 10px 0",
                    fontSize: "18px",
                    fontWeight: 600,
                    color: THEME.colors.textWhite,
                    lineHeight: 1.4,
                  }}
                >
                  {item}
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* Footer Note */}
        {footerNote && (
          <div
            style={{
              borderTop: `1px solid rgba(255, 255, 255, 0.08)`,
              paddingTop: "16px",
              fontFamily: THEME.fonts.mono,
              fontSize: "13px",
              color: THEME.colors.textDim,
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
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
