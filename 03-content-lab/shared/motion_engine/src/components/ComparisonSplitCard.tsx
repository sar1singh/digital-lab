import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { THEME } from "../styles/theme";

export interface ComparisonSplitCardProps {
  badgeText?: string;
  leftTag?: string;
  leftStat?: string;
  leftStatUnit?: string;
  leftTitle: string;
  leftItems: string[];
  rightTag?: string;
  rightStat?: string;
  rightStatUnit?: string;
  rightTitle: string;
  rightItems: string[];
  footerNote?: string;
}

// Utility to parse numeric value and formatting from a string like "$280" or "14.5x"
function parseStatString(statStr: string) {
  const match = statStr.match(/^([^0-9.-]*)([0-9,.]+)([^0-9.-]*)$/);
  if (!match) {
    return { prefix: "", num: 0, suffix: statStr, isNumeric: false };
  }
  const prefix = match[1] || "";
  const num = parseFloat(match[2].replace(/,/g, "")) || 0;
  const suffix = match[3] || "";
  return { prefix, num, suffix, isNumeric: true };
}

export const ComparisonSplitCard: React.FC<ComparisonSplitCardProps> = ({
  badgeText = "FORENSIC CONTRAST // THE REALITY GAP",
  leftTag = "RIGID MONOPOLY",
  leftStat = "$280",
  leftStatUnit = "/ night",
  leftTitle = "THE SAN FRANCISCO HOTEL CARTEL",
  leftItems = [
    "Standard room rate during design conference",
    "100% sold-out citywide capacity in 48 hours",
    "Mandatory $45 resort fees + parking overhead"
  ],
  rightTag = "SYSTEM ARBITRAGE",
  rightStat = "$80",
  rightStatUnit = "/ night",
  rightTitle = "THE $80 AIRBED EXPERIMENT",
  rightItems = [
    "Inflatable air mattress on living room rug",
    "Free Wi-Fi + homemade breakfast pop-tarts",
    "Zero hotel infrastructure, instant cash flow"
  ],
  footerNote = "PRICE SPREAD: 71.4% DISCOUNT FOR ATTENDEES  ✦  $240 CASH REVENUE FOR FOUNDERS",
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Entrance springs for the outer containers
  const leftSlide = spring({
    frame,
    fps,
    config: { damping: 15, mass: 0.8, stiffness: 110 },
  });

  const rightSlide = spring({
    frame: Math.max(0, frame - 4),
    fps,
    config: { damping: 15, mass: 0.8, stiffness: 110 },
  });

  const centerPop = spring({
    frame: Math.max(0, frame - 8),
    fps,
    config: { damping: 12, mass: 0.6, stiffness: 140 },
  });

  const opacity = interpolate(frame, [0, 10], [0, 1], {
    extrapolateRight: "clamp",
  });

  // Dynamic Numeric Count-Up Animations
  const leftParsed = parseStatString(leftStat);
  const leftCountSpring = spring({
    frame: Math.max(0, frame - 8),
    fps,
    config: { damping: 14, mass: 0.7, stiffness: 95 },
  });
  const currentLeftVal = leftParsed.isNumeric
    ? Math.round(leftCountSpring * leftParsed.num)
    : leftStat;

  const rightParsed = parseStatString(rightStat);
  const rightCountSpring = spring({
    frame: Math.max(0, frame - 12),
    fps,
    config: { damping: 14, mass: 0.7, stiffness: 95 },
  });
  const currentRightVal = rightParsed.isNumeric
    ? Math.round(rightCountSpring * rightParsed.num)
    : rightStat;

  // Bottom Footer Spread reveal at frame 46
  const footerSpring = spring({
    frame: Math.max(0, frame - 46),
    fps,
    config: { damping: 12, mass: 0.6, stiffness: 130 },
  });

  return (
    <div
      style={{
        width: "100%",
        height: "100%",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        fontFamily: THEME.fonts.sans,
        backgroundColor: "transparent",
        gap: "28px",
      }}
    >
      {/* Top Floating Category Badge */}
      <div
        style={{
          opacity,
          transform: `translateY(${(1 - opacity) * -15}px)`,
          backgroundColor: THEME.colors.bgGlass,
          backdropFilter: "blur(20px)",
          border: `1px solid ${THEME.colors.borderAccent}`,
          borderRadius: "999px",
          padding: "8px 24px",
          fontFamily: THEME.fonts.mono,
          fontSize: "12px",
          fontWeight: 700,
          letterSpacing: "0.22em",
          color: THEME.colors.acidLime,
          boxShadow: THEME.shadows.glowLime,
          display: "flex",
          alignItems: "center",
          gap: "10px",
          textTransform: "uppercase",
        }}
      >
        <span
          style={{
            width: "6px",
            height: "6px",
            borderRadius: "50%",
            backgroundColor: THEME.colors.acidLime,
          }}
        />
        {badgeText}
      </div>

      {/* Main 2-Card Split Deck */}
      <div
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          gap: "32px",
          width: "1580px",
          position: "relative",
        }}
      >
        {/* LEFT CARD: THE INCUMBENT / OLD MODEL */}
        <div
          style={{
            flex: 1,
            backgroundColor: THEME.colors.bgGlass,
            backdropFilter: "blur(24px)",
            borderRadius: "24px",
            border: `1px solid ${THEME.colors.borderCrimson}`,
            boxShadow: THEME.shadows.glass,
            padding: "40px 44px",
            transform: `translateX(${(1 - leftSlide) * -60}px)`,
            opacity: leftSlide,
            display: "flex",
            flexDirection: "column",
            gap: "20px",
            position: "relative",
            overflow: "hidden",
          }}
        >
          {/* Top subtle line */}
          <div
            style={{
              position: "absolute",
              top: 0,
              left: "15%",
              right: "15%",
              height: "2px",
              background: `linear-gradient(90deg, transparent, ${THEME.colors.crimsonRed}, transparent)`,
              opacity: 0.6,
            }}
          />

          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
            <span
              style={{
                fontFamily: THEME.fonts.mono,
                fontSize: "11px",
                fontWeight: 700,
                letterSpacing: "0.2em",
                color: THEME.colors.crimsonRed,
                backgroundColor: "rgba(239, 68, 68, 0.12)",
                padding: "4px 12px",
                borderRadius: "999px",
                border: "1px solid rgba(239, 68, 68, 0.25)",
              }}
            >
              ● {leftTag}
            </span>
          </div>

          <div>
            {/* Dynamic Animated Number */}
            <div style={{ display: "flex", alignItems: "baseline", gap: "8px", margin: "4px 0" }}>
              <span
                style={{
                  fontSize: "58px",
                  fontWeight: 900,
                  letterSpacing: "-0.04em",
                  color: THEME.colors.textWhite,
                  lineHeight: 1,
                  fontVariantNumeric: "tabular-nums",
                }}
              >
                {leftParsed.isNumeric
                  ? `${leftParsed.prefix}${currentLeftVal}${leftParsed.suffix}`
                  : leftStat}
              </span>
              <span
                style={{
                  fontFamily: THEME.fonts.mono,
                  fontSize: "18px",
                  color: THEME.colors.textDim,
                }}
              >
                {leftStatUnit}
              </span>
            </div>
            <h3
              style={{
                fontSize: "22px",
                fontWeight: 800,
                color: THEME.colors.textMuted,
                margin: "4px 0 0 0",
                letterSpacing: "-0.01em",
              }}
            >
              {leftTitle}
            </h3>
          </div>

          {/* Staggered Bullet Points (One after the other) */}
          <div style={{ display: "flex", flexDirection: "column", gap: "12px", marginTop: "8px" }}>
            {leftItems.map((item, idx) => {
              // Left bullets pop at frame 16, 26, 36
              const startF = 16 + idx * 10;
              const bSpring = spring({
                frame: Math.max(0, frame - startF),
                fps,
                config: { damping: 12, mass: 0.5, stiffness: 150 },
              });
              const bOpacity = interpolate(frame, [startF, startF + 5], [0, 1], {
                extrapolateLeft: "clamp",
                extrapolateRight: "clamp",
              });

              return (
                <div
                  key={idx}
                  style={{
                    display: "flex",
                    alignItems: "flex-start",
                    gap: "12px",
                    fontSize: "17px",
                    color: THEME.colors.textMuted,
                    lineHeight: 1.4,
                    transform: `translateX(${(1 - bSpring) * -18}px)`,
                    opacity: bOpacity,
                  }}
                >
                  <span
                    style={{
                      color: THEME.colors.crimsonRed,
                      fontWeight: 900,
                      fontSize: "16px",
                      marginTop: "2px",
                      transform: `scale(${bSpring})`,
                    }}
                  >
                    ✕
                  </span>
                  <span>{item}</span>
                </div>
              );
            })}
          </div>
        </div>

        {/* CENTER VS BADGE */}
        <div
          style={{
            position: "absolute",
            left: "50%",
            transform: `translate(-50%, -50%) scale(${centerPop})`,
            top: "50%",
            zIndex: 10,
            width: "56px",
            height: "56px",
            borderRadius: "50%",
            backgroundColor: "rgba(10, 15, 26, 0.85)",
            backdropFilter: "blur(20px)",
            border: `2px solid ${THEME.colors.acidLime}`,
            boxShadow: THEME.shadows.glowLime,
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            fontFamily: THEME.fonts.mono,
            fontWeight: 900,
            fontSize: "15px",
            color: THEME.colors.acidLime,
          }}
        >
          VS
        </div>

        {/* RIGHT CARD: SYSTEM ARBITRAGE / DISRUPTOR */}
        <div
          style={{
            flex: 1,
            backgroundColor: THEME.colors.bgGlass,
            backdropFilter: "blur(24px)",
            borderRadius: "24px",
            border: `1px solid ${THEME.colors.borderAccent}`,
            boxShadow: `${THEME.shadows.glass}, ${THEME.shadows.glowLime}`,
            padding: "40px 44px",
            transform: `translateX(${(1 - rightSlide) * 60}px)`,
            opacity: rightSlide,
            display: "flex",
            flexDirection: "column",
            gap: "20px",
            position: "relative",
            overflow: "hidden",
          }}
        >
          {/* Top Lime reflection line */}
          <div
            style={{
              position: "absolute",
              top: 0,
              left: "15%",
              right: "15%",
              height: "2px",
              background: `linear-gradient(90deg, transparent, ${THEME.colors.acidLime}, transparent)`,
              opacity: 0.9,
            }}
          />

          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
            <span
              style={{
                fontFamily: THEME.fonts.mono,
                fontSize: "11px",
                fontWeight: 700,
                letterSpacing: "0.2em",
                color: THEME.colors.acidLime,
                backgroundColor: "rgba(226, 255, 0, 0.12)",
                padding: "4px 12px",
                borderRadius: "999px",
                border: "1px solid rgba(226, 255, 0, 0.35)",
              }}
            >
              ✦ {rightTag}
            </span>
          </div>

          <div>
            {/* Dynamic Animated Number */}
            <div style={{ display: "flex", alignItems: "baseline", gap: "8px", margin: "4px 0" }}>
              <span
                style={{
                  fontSize: "58px",
                  fontWeight: 900,
                  letterSpacing: "-0.04em",
                  color: THEME.colors.acidLime,
                  textShadow: THEME.shadows.glowLime,
                  lineHeight: 1,
                  fontVariantNumeric: "tabular-nums",
                }}
              >
                {rightParsed.isNumeric
                  ? `${rightParsed.prefix}${currentRightVal}${rightParsed.suffix}`
                  : rightStat}
              </span>
              <span
                style={{
                  fontFamily: THEME.fonts.mono,
                  fontSize: "18px",
                  color: THEME.colors.textWhite,
                }}
              >
                {rightStatUnit}
              </span>
            </div>
            <h3
              style={{
                fontSize: "22px",
                fontWeight: 800,
                color: THEME.colors.textWhite,
                margin: "4px 0 0 0",
                letterSpacing: "-0.01em",
              }}
            >
              {rightTitle}
            </h3>
          </div>

          {/* Staggered Bullet Points (Ping-pong offset: frame 21, 31, 41) */}
          <div style={{ display: "flex", flexDirection: "column", gap: "12px", marginTop: "8px" }}>
            {rightItems.map((item, idx) => {
              // Right bullets pop at frame 21, 31, 41
              const startF = 21 + idx * 10;
              const bSpring = spring({
                frame: Math.max(0, frame - startF),
                fps,
                config: { damping: 12, mass: 0.5, stiffness: 150 },
              });
              const bOpacity = interpolate(frame, [startF, startF + 5], [0, 1], {
                extrapolateLeft: "clamp",
                extrapolateRight: "clamp",
              });

              return (
                <div
                  key={idx}
                  style={{
                    display: "flex",
                    alignItems: "flex-start",
                    gap: "12px",
                    fontSize: "17px",
                    color: THEME.colors.textWhite,
                    lineHeight: 1.4,
                    fontWeight: 500,
                    transform: `translateX(${(1 - bSpring) * 18}px)`,
                    opacity: bOpacity,
                  }}
                >
                  <span
                    style={{
                      color: THEME.colors.acidLime,
                      fontWeight: 900,
                      fontSize: "16px",
                      marginTop: "2px",
                      transform: `scale(${bSpring})`,
                    }}
                  >
                    ✓
                  </span>
                  <span>{item}</span>
                </div>
              );
            })}
          </div>
        </div>
      </div>

      {/* Bottom Floating Spread Banner (Reveals after bullets at frame 46) */}
      {footerNote && (
        <div
          style={{
            transform: `scale(${footerSpring}) translateY(${(1 - footerSpring) * 20}px)`,
            opacity: footerSpring,
            backgroundColor: THEME.colors.bgGlass,
            backdropFilter: "blur(20px)",
            border: `1px solid rgba(255, 255, 255, 0.14)`,
            borderRadius: "14px",
            padding: "12px 32px",
            fontFamily: THEME.fonts.mono,
            fontSize: "13px",
            fontWeight: 700,
            letterSpacing: "0.15em",
            color: THEME.colors.textMuted,
            display: "flex",
            alignItems: "center",
            gap: "12px",
            boxShadow: THEME.shadows.glass,
          }}
        >
          <span>{footerNote}</span>
        </div>
      )}
    </div>
  );
};
