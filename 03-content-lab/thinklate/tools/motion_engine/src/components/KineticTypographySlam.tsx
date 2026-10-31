import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { THEME } from "../styles/theme";

export interface KineticTypographySlamProps {
  line1?: string;
  line2?: string;
  line1Color?: string;
  line2Color?: string;
  subtext?: string;
}

export const KineticTypographySlam: React.FC<KineticTypographySlamProps> = ({
  line1 = "OCTOBER 2007: $1,150 OVERDUE RENT",
  line2 = "3 AIRBEDS ON A LIVING ROOM RUG",
  line1Color = THEME.colors.textWhite,
  line2Color = THEME.colors.acidLime,
  subtext = "THE EMBARRASSING DESPERATE HUSTLE THAT HIJACKED AN INDUSTRY",
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Violent, punchy spring impact (0 to 1 in ~8 frames)
  const impact = spring({
    frame,
    fps,
    config: { damping: 12, mass: 0.5, stiffness: 180 },
  });

  const scale = interpolate(impact, [0, 1], [1.3, 1]);
  const opacity = interpolate(impact, [0, 1], [0, 1]);

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
        textAlign: "center",
        padding: "0 80px",
        boxSizing: "border-box",
      }}
    >
      <div
        style={{
          transform: `scale(${scale})`,
          opacity,
          display: "flex",
          flexDirection: "column",
          gap: "8px",
          alignItems: "center",
        }}
      >
        {/* Line 1: Ultra-bold Chalk White */}
        <div
          style={{
            fontSize: "64px",
            fontWeight: 900,
            color: line1Color,
            letterSpacing: "-1px",
            lineHeight: 1.1,
            textTransform: "uppercase",
            textShadow: "0 10px 30px rgba(0,0,0,0.8)",
          }}
        >
          {line1}
        </div>

        {/* Line 2: High-Voltage Acid Lime */}
        <div
          style={{
            fontSize: "72px",
            fontWeight: 900,
            color: line2Color,
            letterSpacing: "-1.5px",
            lineHeight: 1.1,
            textTransform: "uppercase",
            textShadow: `0 10px 30px rgba(0,0,0,0.8), 0 0 40px ${line2Color}40`,
          }}
        >
          {line2}
        </div>

        {/* Supporting Subtext Pill */}
        {subtext && (
          <div
            style={{
              marginTop: "24px",
              padding: "10px 24px",
              borderRadius: "100px",
              backgroundColor: "rgba(10, 15, 26, 0.75)",
              backdropFilter: "blur(16px)",
              border: `1px solid ${THEME.colors.borderGlass}`,
              color: THEME.colors.textMuted,
              fontSize: "15px",
              fontWeight: 700,
              letterSpacing: "1.5px",
              fontFamily: THEME.fonts.mono,
              textTransform: "uppercase",
            }}
          >
            {subtext}
          </div>
        )}
      </div>
    </div>
  );
};
