import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { getChannelTheme } from "../styles/theme";

export interface KineticTypographySlamProps {
  channel?: string;
  line1?: string;
  line2?: string;
  line1Color?: string;
  line2Color?: string;
  subtext?: string;
}

export const KineticTypographySlam: React.FC<KineticTypographySlamProps> = ({
  channel = "thinklate",
  line1 = "OCTOBER 2007: $1,150 OVERDUE RENT",
  line2 = "3 AIRBEDS ON A LIVING ROOM RUG",
  line1Color,
  line2Color,
  subtext = "THE EMBARRASSING DESPERATE HUSTLE THAT HIJACKED AN INDUSTRY",
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const theme = getChannelTheme(channel);

  // Channel-adapted spring physics
  const impact = spring({
    frame,
    fps,
    config: {
      damping: theme.motion.damping,
      mass: theme.motion.mass,
      stiffness: theme.motion.stiffness,
    },
  });

  const scale = interpolate(impact, [0, 1], [1.35, 1]);
  const opacity = interpolate(impact, [0, 1], [0, 1]);

  const activeLine1Color = line1Color || theme.colors.textWhite;
  const activeLine2Color = line2Color || theme.colors.accent;

  return (
    <div
      style={{
        width: "100%",
        height: "100%",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        fontFamily: theme.fonts.sans,
        textAlign: "center",
        padding: "0 80px",
        boxSizing: "border-box",
        backgroundColor: "transparent",
      }}
    >
      <div
        style={{
          transform: `scale(${scale})`,
          opacity,
          display: "flex",
          flexDirection: "column",
          gap: "10px",
          alignItems: "center",
          backgroundColor: theme.colors.bgGlass,
          backdropFilter: "blur(24px)",
          border: `1.5px solid ${theme.colors.borderAccent}`,
          borderRadius: "28px",
          boxShadow: `${theme.shadows.glass}, ${theme.shadows.glowAccent}`,
          padding: "56px 72px",
          maxWidth: "1540px",
        }}
      >
        {/* Channel Indicator Badge */}
        <div
          style={{
            fontFamily: theme.fonts.mono,
            fontSize: "12px",
            fontWeight: 800,
            letterSpacing: "0.22em",
            color: theme.colors.accent,
            textTransform: "uppercase",
            marginBottom: "4px",
          }}
        >
          ✦ {theme.name}
        </div>

        {/* Line 1: Ultra-bold Primary Heading */}
        <div
          style={{
            fontSize: "64px",
            fontWeight: 900,
            lineHeight: 1.05,
            letterSpacing: "-0.03em",
            color: activeLine1Color,
            textTransform: "uppercase",
            textShadow: "0 10px 30px rgba(0, 0, 0, 0.8)",
          }}
        >
          {line1}
        </div>

        {/* Line 2: Brand Accent Punchline */}
        <div
          style={{
            fontSize: "76px",
            fontWeight: 900,
            lineHeight: 1.05,
            letterSpacing: "-0.03em",
            color: activeLine2Color,
            textTransform: "uppercase",
            textShadow: `0 10px 40px rgba(0, 0, 0, 0.9), ${theme.shadows.glowAccent}`,
          }}
        >
          {line2}
        </div>

        {/* Subtext */}
        {subtext && (
          <div
            style={{
              fontFamily: theme.fonts.mono,
              fontSize: "15px",
              fontWeight: 700,
              letterSpacing: "0.18em",
              color: theme.colors.textMuted,
              marginTop: "16px",
              textTransform: "uppercase",
              borderTop: `1px solid rgba(255, 255, 255, 0.12)`,
              paddingTop: "14px",
              width: "100%",
            }}
          >
            {subtext}
          </div>
        )}
      </div>
    </div>
  );
};
