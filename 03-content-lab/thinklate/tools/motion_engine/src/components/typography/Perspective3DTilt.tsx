import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { THEME } from "../../styles/theme";

export interface Perspective3DTiltProps {
  category?: string;
  headlineLine1?: string;
  headlineLine2?: string;
  subtext?: string;
}

export const Perspective3DTilt: React.FC<Perspective3DTiltProps> = ({
  category = "THE SYSTEMIC QUESTION",
  headlineLine1 = "HOW AN $80 AIRBED",
  headlineLine2 = "HIJACKED A $100B INDUSTRY",
  subtext = "THE ANATOMY OF A SILICON VALLEY SYSTEM ARBITRAGE",
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Slow smooth 3D push-in
  const pushProgress = interpolate(frame, [0, 90], [0.95, 1.05], {
    extrapolateRight: "clamp",
  });

  const cardOpacity = interpolate(frame, [0, 10], [0, 1], { extrapolateRight: "clamp" });

  const entrance = spring({
    frame,
    fps,
    config: { damping: 14, mass: 0.8, stiffness: 100 },
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
        perspective: "1200px",
      }}
    >
      <div
        style={{
          transform: `scale(${entrance * pushProgress}) rotateX(14deg) rotateY(-8deg)`,
          opacity: cardOpacity,
          transformStyle: "preserve-3d",
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          textAlign: "center",
          gap: "16px",
        }}
      >
        {/* Category Tag */}
        <div
          style={{
            fontFamily: THEME.fonts.mono,
            fontSize: "14px",
            fontWeight: 800,
            letterSpacing: "0.25em",
            color: THEME.colors.acidLime,
            backgroundColor: "rgba(10, 15, 26, 0.75)",
            backdropFilter: "blur(16px)",
            padding: "8px 24px",
            borderRadius: "999px",
            border: `1px solid ${THEME.colors.borderAccent}`,
            boxShadow: THEME.shadows.glowLime,
            textTransform: "uppercase",
          }}
        >
          ✦ {category}
        </div>

        {/* Big 3D Typography */}
        <div style={{ display: "flex", flexDirection: "column", gap: "4px" }}>
          <h1
            style={{
              fontSize: "76px",
              fontWeight: 900,
              lineHeight: 1.05,
              color: THEME.colors.textWhite,
              letterSpacing: "-0.04em",
              margin: 0,
              textShadow: "0 10px 30px rgba(0, 0, 0, 0.8), 0 0 40px rgba(255, 255, 255, 0.2)",
            }}
          >
            {headlineLine1}
          </h1>
          <h1
            style={{
              fontSize: "84px",
              fontWeight: 900,
              lineHeight: 1.05,
              color: THEME.colors.acidLime,
              letterSpacing: "-0.04em",
              margin: 0,
              textShadow: "0 15px 40px rgba(0, 0, 0, 0.9), 0 0 50px rgba(226, 255, 0, 0.4)",
            }}
          >
            {headlineLine2}
          </h1>
        </div>

        {/* Subtext */}
        {subtext && (
          <div
            style={{
              fontFamily: THEME.fonts.mono,
              fontSize: "16px",
              fontWeight: 700,
              letterSpacing: "0.18em",
              color: THEME.colors.textMuted,
              marginTop: "8px",
              textShadow: "0 4px 12px rgba(0,0,0,0.8)",
            }}
          >
            {subtext}
          </div>
        )}
      </div>
    </div>
  );
};
