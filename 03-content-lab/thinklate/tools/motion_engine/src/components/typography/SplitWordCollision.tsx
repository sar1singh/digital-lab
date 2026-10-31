import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { THEME } from "../../styles/theme";

export interface SplitWordCollisionProps {
  leftWord?: string;
  rightWord?: string;
  centerBadge?: string;
  subtext?: string;
}

export const SplitWordCollision: React.FC<SplitWordCollisionProps> = ({
  leftWord = "THE PROMISE",
  rightWord = "THE REALITY",
  centerBadge = "VS",
  subtext = "WHAT THEY PITCHED INVESTORS VS WHAT THEY ACTUALLY DELIVERED",
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Violent spring crash from left (-500px -> 0) and right (+500px -> 0)
  const leftSlide = spring({
    frame,
    fps,
    config: { damping: 11, mass: 0.6, stiffness: 180 },
  });

  const rightSlide = spring({
    frame,
    fps,
    config: { damping: 11, mass: 0.6, stiffness: 180 },
  });

  // Impact flash (frames 6 to 12)
  const flash = interpolate(frame, [5, 7, 14], [0, 0.8, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const cardOpacity = interpolate(frame, [0, 4], [0, 1], { extrapolateRight: "clamp" });

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
        position: "relative",
      }}
    >
      {/* Impact flash overlay */}
      <div
        style={{
          position: "absolute",
          top: 0,
          left: 0,
          right: 0,
          bottom: 0,
          backgroundColor: THEME.colors.acidLime,
          opacity: flash,
          pointerEvents: "none",
          zIndex: 30,
        }}
      />

      <div
        style={{
          width: "1520px",
          backgroundColor: THEME.colors.bgGlass,
          backdropFilter: "blur(24px)",
          borderRadius: "24px",
          border: `1px solid ${THEME.colors.borderGlass}`,
          boxShadow: THEME.shadows.glass,
          padding: "64px 72px",
          opacity: cardOpacity,
          display: "flex",
          flexDirection: "column",
          gap: "28px",
          alignItems: "center",
          position: "relative",
          overflow: "hidden",
        }}
      >
        {/* The Two Crashing Words */}
        <div style={{ display: "flex", alignItems: "center", justifyContent: "center", gap: "40px", width: "100%" }}>
          {/* Left Word */}
          <div
            style={{
              flex: 1,
              textAlign: "right",
              fontSize: "64px",
              fontWeight: 900,
              letterSpacing: "-0.04em",
              color: THEME.colors.textWhite,
              transform: `translateX(${(1 - leftSlide) * -400}px)`,
            }}
          >
            {leftWord}
          </div>

          {/* Center VS pill */}
          <div
            style={{
              width: "60px",
              height: "60px",
              borderRadius: "50%",
              backgroundColor: THEME.colors.bgGlassDark,
              border: `2px solid ${THEME.colors.acidLime}`,
              boxShadow: THEME.shadows.glowLime,
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              fontFamily: THEME.fonts.mono,
              fontWeight: 900,
              fontSize: "18px",
              color: THEME.colors.acidLime,
              flexShrink: 0,
            }}
          >
            {centerBadge}
          </div>

          {/* Right Word */}
          <div
            style={{
              flex: 1,
              textAlign: "left",
              fontSize: "64px",
              fontWeight: 900,
              letterSpacing: "-0.04em",
              color: THEME.colors.acidLime,
              textShadow: THEME.shadows.glowLime,
              transform: `translateX(${(1 - rightSlide) * 400}px)`,
            }}
          >
            {rightWord}
          </div>
        </div>

        {/* Subtext */}
        {subtext && (
          <div
            style={{
              fontFamily: THEME.fonts.mono,
              fontSize: "13px",
              fontWeight: 700,
              color: THEME.colors.textDim,
              letterSpacing: "0.2em",
              borderTop: "1px solid rgba(255, 255, 255, 0.1)",
              paddingTop: "20px",
              textAlign: "center",
              width: "100%",
            }}
          >
            ✦ {subtext}
          </div>
        )}
      </div>
    </div>
  );
};
