import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { THEME } from "../../styles/theme";

export interface WordByWordPopProps {
  phrase: string;
  subtext?: string;
  framesPerWord?: number;
}

export const WordByWordPop: React.FC<WordByWordPopProps> = ({
  phrase = "YOU CANNOT OUT-SPEND A BILLION-DOLLAR CARTEL · YOU HAVE TO OUT-THINK THEM",
  subtext = "THE ASYMMETRIC ADVANTAGE",
  framesPerWord = 4,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const words = phrase.split(" ");
  const cardOpacity = interpolate(frame, [0, 6], [0, 1], { extrapolateRight: "clamp" });

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
          width: "1420px",
          backgroundColor: THEME.colors.bgGlass,
          backdropFilter: "blur(24px)",
          borderRadius: "24px",
          border: `1px solid ${THEME.colors.borderGlass}`,
          boxShadow: THEME.shadows.glass,
          padding: "56px 64px",
          opacity: cardOpacity,
          display: "flex",
          flexDirection: "column",
          gap: "24px",
          alignItems: "center",
          textAlign: "center",
        }}
      >
        {/* Words wrap */}
        <div style={{ display: "flex", flexWrap: "wrap", justifyContent: "center", gap: "14px 18px", maxWidth: "1280px" }}>
          {words.map((word, idx) => {
            const wordStartFrame = 10 + idx * framesPerWord;
            const wordSpring = spring({
              frame: Math.max(0, frame - wordStartFrame),
              fps,
              config: { damping: 12, mass: 0.5, stiffness: 160 },
            });

            const isActive = frame >= wordStartFrame;
            const isLatest = frame >= wordStartFrame && frame < wordStartFrame + framesPerWord;

            return (
              <span
                key={idx}
                style={{
                  fontSize: "44px",
                  fontWeight: 900,
                  letterSpacing: "-0.02em",
                  color: isLatest
                    ? THEME.colors.acidLime
                    : isActive
                    ? THEME.colors.textWhite
                    : THEME.colors.textDim,
                  transform: `scale(${isLatest ? 1.15 : wordSpring})`,
                  opacity: isActive ? 1 : 0.25,
                  textShadow: isLatest ? THEME.shadows.glowLime : "none",
                  display: "inline-block",
                  transition: "color 0.1s ease",
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
              color: THEME.colors.acidLime,
              letterSpacing: "0.22em",
              borderTop: "1px solid rgba(255, 255, 255, 0.1)",
              paddingTop: "16px",
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
