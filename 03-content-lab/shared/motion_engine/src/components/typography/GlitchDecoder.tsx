import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { THEME } from "../../styles/theme";

export interface GlitchDecoderProps {
  badgeText?: string;
  decodedPhrase: string;
  subtext?: string;
}

const GLYPHS = "!@#$%^&*()_+-=[]{}|;:,.<>?/0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";

export const GlitchDecoder: React.FC<GlitchDecoderProps> = ({
  badgeText = "FORENSIC DECRYPTION // SYSTEM REVEAL",
  decodedPhrase = "THE ANATOMY OF A LEGAL CARTEL",
  subtext = "RECOVERED FROM DELETED EXECUTIVE ARCHIVES",
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const cardScale = spring({
    frame,
    fps,
    config: { damping: 14, mass: 0.8, stiffness: 110 },
  });

  const opacity = interpolate(frame, [0, 6], [0, 1], { extrapolateRight: "clamp" });

  // Letter by letter resolution (each letter resolves over 2-3 frames)
  const resolvedCount = Math.floor(interpolate(frame, [10, 45], [0, decodedPhrase.length], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }));

  // Render scrambled vs resolved text
  const renderedChars = decodedPhrase.split("").map((targetChar, idx) => {
    if (idx < resolvedCount) {
      return (
        <span key={idx} style={{ color: THEME.colors.acidLime, textShadow: THEME.shadows.glowLime }}>
          {targetChar}
        </span>
      );
    }
    if (targetChar === " ") return " ";
    // Pick pseudo-random glyph based on frame and index
    const glyphIdx = (frame * 7 + idx * 13) % GLYPHS.length;
    return (
      <span key={idx} style={{ color: THEME.colors.textDim, opacity: 0.6 }}>
        {GLYPHS[glyphIdx]}
      </span>
    );
  });

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
          width: "1360px",
          backgroundColor: THEME.colors.bgGlassDark,
          backdropFilter: "blur(24px)",
          borderRadius: "20px",
          border: `1px solid ${THEME.colors.borderAccent}`,
          boxShadow: `${THEME.shadows.glass}, ${THEME.shadows.glowLime}`,
          padding: "52px 64px",
          transform: `scale(${cardScale})`,
          opacity,
          display: "flex",
          flexDirection: "column",
          gap: "24px",
          position: "relative",
        }}
      >
        {/* Header */}
        <div style={{ display: "flex", justifyContent: "space-between", borderBottom: "1px solid rgba(255, 255, 255, 0.1)", paddingBottom: "16px" }}>
          <div style={{ fontSize: "13px", fontWeight: 700, color: THEME.colors.acidLime, letterSpacing: "0.2em" }}>
            ✦ {badgeText}
          </div>
          <div style={{ fontSize: "12px", color: THEME.colors.textDim, letterSpacing: "0.15em" }}>
            HASH_KEY // 0x7F2B
          </div>
        </div>

        {/* Decoded Typography */}
        <h1 style={{ fontSize: "52px", fontWeight: 900, lineHeight: 1.15, letterSpacing: "-0.01em", margin: "12px 0" }}>
          {renderedChars}
        </h1>

        {/* Subtext */}
        {subtext && (
          <div style={{ fontSize: "15px", color: THEME.colors.textMuted, borderTop: "1px solid rgba(255, 255, 255, 0.08)", paddingTop: "14px", display: "flex", justifyContent: "space-between" }}>
            <span>{subtext}</span>
            <span style={{ color: THEME.colors.acidLime }}>DECRYPTED</span>
          </div>
        )}
      </div>
    </div>
  );
};
