import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { THEME } from "../../styles/theme";

export interface HighlighterWipeTextProps {
  badgeText?: string;
  statement: string;
  highlightedPhrase: string;
  subtext?: string;
}

export const HighlighterWipeText: React.FC<HighlighterWipeTextProps> = ({
  badgeText = "KEY FORENSIC TAKEAWAY",
  statement = "When an industry gets completely closed off, the winning move is never playing by their rules.",
  highlightedPhrase = "never playing by their rules",
  subtext = "THE REASON AIRBEDS BEAT 100-YEAR-OLD HOTEL CARTELS",
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const cardScale = spring({
    frame,
    fps,
    config: { damping: 14, mass: 0.8, stiffness: 100 },
  });

  const opacity = interpolate(frame, [0, 8], [0, 1], { extrapolateRight: "clamp" });

  // Highlighter sweep (frames 15 to 45)
  const sweepProgress = interpolate(frame, [15, 45], [0, 100], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const renderStatement = () => {
    if (!statement.includes(highlightedPhrase)) {
      return <span>{statement}</span>;
    }
    const [before, after] = statement.split(highlightedPhrase);
    return (
      <span>
        {before}
        <span
          style={{
            position: "relative",
            display: "inline",
            color: sweepProgress > 50 ? "#05080F" : THEME.colors.textWhite,
            fontWeight: 900,
            padding: "2px 8px",
            borderRadius: "4px",
            zIndex: 1,
            transition: "color 0.2s ease",
          }}
        >
          <span
            style={{
              position: "absolute",
              top: 0,
              left: 0,
              bottom: 0,
              width: `${sweepProgress}%`,
              backgroundColor: THEME.colors.acidLime,
              zIndex: -1,
              borderRadius: "4px",
              boxShadow: THEME.shadows.glowLime,
            }}
          />
          {highlightedPhrase}
        </span>
        {after}
      </span>
    );
  };

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
          backdropFilter: "blur(24px)",
          borderRadius: "24px",
          border: `1px solid ${THEME.colors.borderGlass}`,
          boxShadow: THEME.shadows.glass,
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
        <div style={{ display: "flex", justifyContent: "space-between", borderBottom: "1px solid rgba(255, 255, 255, 0.08)", paddingBottom: "16px" }}>
          <div style={{ fontFamily: THEME.fonts.mono, fontSize: "12px", fontWeight: 700, color: THEME.colors.acidLime, letterSpacing: "0.2em" }}>
            ✦ {badgeText}
          </div>
          <div style={{ fontFamily: THEME.fonts.mono, fontSize: "12px", color: THEME.colors.textDim, letterSpacing: "0.15em" }}>
            RULE OF ARBITRAGE
          </div>
        </div>

        {/* Big Statement */}
        <h1 style={{ fontSize: "44px", fontWeight: 800, lineHeight: 1.35, color: THEME.colors.textWhite, letterSpacing: "-0.02em", margin: "8px 0" }}>
          {renderStatement()}
        </h1>

        {/* Subtext */}
        {subtext && (
          <div style={{ fontFamily: THEME.fonts.mono, fontSize: "13px", color: THEME.colors.textDim, borderTop: "1px solid rgba(255, 255, 255, 0.08)", paddingTop: "14px", display: "flex", justifyContent: "space-between" }}>
            <span>{subtext}</span>
            <span style={{ color: THEME.colors.acidLime }}>VERIFIED PLAYBOOK</span>
          </div>
        )}
      </div>
    </div>
  );
};
