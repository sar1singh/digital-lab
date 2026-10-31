import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { ChannelId, getChannelTheme } from "../../styles/theme";

export interface TextTrailOutlineProps {
  channel?: ChannelId;
  text?: string;
  subtitle?: string;
  fontFamily?: string;
}

export const TextTrailOutline: React.FC<TextTrailOutlineProps> = ({
  channel = "thinklate",
  text = "DISRUPTION",
  subtitle = "WHEN THE OLD RULES CEASE TO FUNCTION",
  fontFamily = '"Cabinet Grotesk", "Impact", "Arial Black", sans-serif',
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const theme = getChannelTheme(channel);

  // Staggered springs for 3 outline trail layers + 1 solid foreground
  const trail1 = spring({ frame, fps, config: { damping: 12, mass: 0.6, stiffness: 120 } });
  const trail2 = spring({ frame: Math.max(0, frame - 5), fps, config: { damping: 12, mass: 0.6, stiffness: 120 } });
  const trail3 = spring({ frame: Math.max(0, frame - 10), fps, config: { damping: 12, mass: 0.6, stiffness: 120 } });
  const solidSpring = spring({ frame: Math.max(0, frame - 16), fps, config: { damping: 9, mass: 0.5, stiffness: 160 } });

  // Floating drift
  const driftY = Math.sin(frame / 12) * 8;

  return (
    <div
      style={{
        width: "100%",
        height: "100%",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        backgroundColor: "transparent",
        fontFamily: theme.fonts.sans,
        position: "relative",
      }}
    >
      <div
        style={{
          position: "relative",
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          transform: `translateY(${driftY}px)`,
        }}
      >
        {/* Trail 3 (Deepest) */}
        <div
          style={{
            position: "absolute",
            fontFamily,
            fontSize: "136px",
            fontWeight: 900,
            letterSpacing: "-0.03em",
            textTransform: "uppercase",
            color: "transparent",
            WebkitTextStroke: `2px rgba(255, 255, 255, 0.15)`,
            transform: `translateY(${(1 - trail1) * 80 + 45}px) scale(${0.88 + trail1 * 0.12})`,
            opacity: interpolate(frame, [0, 8], [0, 0.4], { extrapolateRight: "clamp" }),
            pointerEvents: "none",
          }}
        >
          {text}
        </div>

        {/* Trail 2 */}
        <div
          style={{
            position: "absolute",
            fontFamily,
            fontSize: "136px",
            fontWeight: 900,
            letterSpacing: "-0.03em",
            textTransform: "uppercase",
            color: "transparent",
            WebkitTextStroke: `2px ${theme.colors.accentSecondary}88`,
            transform: `translateY(${(1 - trail2) * 60 + 25}px) scale(${0.92 + trail2 * 0.08})`,
            opacity: interpolate(frame, [5, 14], [0, 0.7], { extrapolateRight: "clamp" }),
            pointerEvents: "none",
          }}
        >
          {text}
        </div>

        {/* Trail 1 */}
        <div
          style={{
            position: "absolute",
            fontFamily,
            fontSize: "136px",
            fontWeight: 900,
            letterSpacing: "-0.03em",
            textTransform: "uppercase",
            color: "transparent",
            WebkitTextStroke: `2px ${theme.colors.accent}`,
            transform: `translateY(${(1 - trail3) * 40 + 10}px) scale(${0.96 + trail3 * 0.04})`,
            opacity: interpolate(frame, [10, 18], [0, 0.9], { extrapolateRight: "clamp" }),
            pointerEvents: "none",
          }}
        >
          {text}
        </div>

        {/* Solid Foreground Hero Word */}
        <div
          style={{
            fontFamily,
            fontSize: "136px",
            fontWeight: 900,
            letterSpacing: "-0.03em",
            textTransform: "uppercase",
            color: theme.colors.textWhite,
            textShadow: `${theme.shadows.glowAccent}, 0 10px 40px rgba(0, 0, 0, 0.9)`,
            transform: `scale(${solidSpring})`,
            opacity: interpolate(frame, [16, 22], [0, 1], { extrapolateRight: "clamp" }),
            position: "relative",
            zIndex: 5,
          }}
        >
          {text}
        </div>
      </div>

      {/* Subtitle */}
      <div
        style={{
          marginTop: "30px",
          fontSize: "22px",
          fontWeight: 800,
          letterSpacing: "0.2em",
          color: theme.colors.accent,
          fontFamily: theme.fonts.mono,
          opacity: interpolate(frame, [24, 34], [0, 1], { extrapolateRight: "clamp" }),
          textShadow: theme.shadows.glowAccent,
        }}
      >
        // {subtitle} //
      </div>
    </div>
  );
};
