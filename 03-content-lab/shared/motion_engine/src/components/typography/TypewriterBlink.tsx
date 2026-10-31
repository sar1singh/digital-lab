import React from "react";
import { interpolate, useCurrentFrame } from "remotion";
import { THEME } from "../../styles/theme";

export interface TypewriterBlinkProps {
  badgeText?: string;
  text: string;
  subtext?: string;
  speed?: number; // characters per frame
}

export const TypewriterBlink: React.FC<TypewriterBlinkProps> = ({
  badgeText = "FORENSIC DISPATCH // TERMINAL LOG",
  text = "THE REVENUE MODEL WAS SECRETLY DESIGNED TO BLEED USERS DRY",
  subtext = "INTERNAL SLACK LOGS · MARCH 14, 2021",
  speed = 0.8,
}) => {
  const frame = useCurrentFrame();

  const charCount = Math.floor(Math.max(0, frame - 10) * speed);
  const displayedText = text.slice(0, charCount);

  // Blinking cursor (toggles every 8 frames)
  const showCursor = Math.floor(frame / 8) % 2 === 0;

  const cardOpacity = interpolate(frame, [0, 6], [0, 1], { extrapolateRight: "clamp" });

  return (
    <div
      style={{
        width: "100%",
        height: "100%",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        fontFamily: THEME.fonts.mono,
        backgroundColor: "transparent",
      }}
    >
      <div
        style={{
          width: "1400px",
          backgroundColor: THEME.colors.bgGlassDark,
          backdropFilter: "blur(24px)",
          borderRadius: "20px",
          border: `1px solid ${THEME.colors.borderAccent}`,
          boxShadow: `${THEME.shadows.glass}, ${THEME.shadows.glowLime}`,
          padding: "52px 64px",
          opacity: cardOpacity,
          display: "flex",
          flexDirection: "column",
          gap: "24px",
          position: "relative",
        }}
      >
        {/* Terminal Header */}
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", borderBottom: "1px solid rgba(255, 255, 255, 0.1)", paddingBottom: "16px" }}>
          <div style={{ display: "flex", alignItems: "center", gap: "10px" }}>
            <span style={{ width: "10px", height: "10px", borderRadius: "50%", backgroundColor: THEME.colors.acidLime, boxShadow: THEME.shadows.glowLime }} />
            <span style={{ fontSize: "13px", fontWeight: 700, color: THEME.colors.acidLime, letterSpacing: "0.2em" }}>
              {badgeText}
            </span>
          </div>
          <div style={{ fontSize: "12px", color: THEME.colors.textDim, letterSpacing: "0.15em" }}>
            SEC_LOG_MONITOR.sh
          </div>
        </div>

        {/* Big Typewriter Typography */}
        <div style={{ fontSize: "44px", fontWeight: 900, lineHeight: 1.25, color: THEME.colors.textWhite, letterSpacing: "-0.02em", minHeight: "120px" }}>
          <span>{displayedText}</span>
          <span
            style={{
              display: "inline-block",
              width: "18px",
              height: "44px",
              backgroundColor: THEME.colors.acidLime,
              marginLeft: "6px",
              verticalAlign: "middle",
              opacity: showCursor ? 1 : 0,
              boxShadow: THEME.shadows.glowLime,
            }}
          />
        </div>

        {/* Subtext */}
        {subtext && (
          <div style={{ fontSize: "15px", color: THEME.colors.textMuted, borderTop: "1px solid rgba(255, 255, 255, 0.08)", paddingTop: "14px", display: "flex", justifyContent: "space-between" }}>
            <span>{subtext}</span>
            <span style={{ color: THEME.colors.acidLime }}>[UNFILTERED]</span>
          </div>
        )}
      </div>
    </div>
  );
};
