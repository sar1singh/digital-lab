import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { THEME } from "../../styles/theme";

export interface StaggeredWaveTextProps {
  badgeText?: string;
  punchline: string;
  highlightWords?: string[];
  subtext?: string;
}

export const StaggeredWaveText: React.FC<StaggeredWaveTextProps> = ({
  badgeText = "ROAST & REVEAL // THE BITTER TRUTH",
  punchline = "THEY DID NOT INVENT A NEW MARKET · THEY MONETIZED DESPERATION",
  highlightWords = ["MONETIZED", "DESPERATION"],
  subtext = "WHEN AIR MATTRESSES BECOME A $100B ASYMMETRIC WEAPON",
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const words = punchline.split(" ");
  const cardOpacity = interpolate(frame, [0, 8], [0, 1], { extrapolateRight: "clamp" });

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
          width: "1440px",
          backgroundColor: THEME.colors.bgGlass,
          backdropFilter: "blur(24px)",
          borderRadius: "24px",
          border: `1px solid ${THEME.colors.borderGlass}`,
          boxShadow: THEME.shadows.glass,
          padding: "56px 68px",
          opacity: cardOpacity,
          display: "flex",
          flexDirection: "column",
          gap: "28px",
          alignItems: "center",
          textAlign: "center",
        }}
      >
        {/* Header Badge */}
        <div
          style={{
            fontFamily: THEME.fonts.mono,
            fontSize: "12px",
            fontWeight: 700,
            letterSpacing: "0.22em",
            color: THEME.colors.acidLime,
            textTransform: "uppercase",
            display: "flex",
            alignItems: "center",
            gap: "10px",
          }}
        >
          <span style={{ width: "8px", height: "8px", borderRadius: "50%", backgroundColor: THEME.colors.acidLime, boxShadow: THEME.shadows.glowLime }} />
          {badgeText}
        </div>

        {/* Wavy Words Container */}
        <div style={{ display: "flex", flexWrap: "wrap", justifyContent: "center", gap: "16px 20px", maxWidth: "1320px" }}>
          {words.map((word, idx) => {
            const wordSpring = spring({
              frame: Math.max(0, frame - 8 - idx * 3),
              fps,
              config: { damping: 11, mass: 0.5, stiffness: 150 },
            });

            const cleanWord = word.replace(/[^A-Za-z0-9]/g, "");
            const isHighlight = highlightWords.includes(cleanWord);

            return (
              <span
                key={idx}
                style={{
                  fontSize: "50px",
                  fontWeight: 900,
                  letterSpacing: "-0.03em",
                  color: isHighlight ? THEME.colors.acidLime : THEME.colors.textWhite,
                  textShadow: isHighlight ? THEME.shadows.glowLime : "none",
                  transform: `translateY(${(1 - wordSpring) * 40}px) scale(${wordSpring})`,
                  opacity: wordSpring,
                  display: "inline-block",
                }}
              >
                {word}
              </span>
            );
          })}
        </div>

        {/* Subtext */}
        {subtext && (
          <div
            style={{
              fontFamily: THEME.fonts.mono,
              fontSize: "13px",
              fontWeight: 700,
              letterSpacing: "0.2em",
              color: THEME.colors.textDim,
              borderTop: "1px solid rgba(255, 255, 255, 0.08)",
              paddingTop: "18px",
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
