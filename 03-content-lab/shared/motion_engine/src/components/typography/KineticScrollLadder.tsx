import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { ChannelId, getChannelTheme } from "../../styles/theme";

export interface KineticScrollLadderProps {
  channel?: ChannelId;
  items?: string[];
  selectedIndex?: number;
  subtitle?: string;
  fontFamily?: string;
}

export const KineticScrollLadder: React.FC<KineticScrollLadderProps> = ({
  channel = "thinklate",
  items = [
    "$450 LUXURY HOTEL ROOM",
    "$320 AIRPORT MOTEL SUITE",
    "$180 OVERPRICED HOSTEL",
    "$80 AIRBED ON A LIVING ROOM RUG",
  ],
  selectedIndex = 3,
  subtitle = "THE WINNING VALUE EQUATION",
  fontFamily = '"Cabinet Grotesk", "Impact", "Arial Black", sans-serif',
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const theme = getChannelTheme(channel);

  const itemHeight = 110;

  // Rapid roll animation across frames 0 to 45
  const scrollProgress = interpolate(frame, [5, 45], [0, selectedIndex], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Elastic snap spring for the final index
  const snapSpring = spring({
    frame: Math.max(0, frame - 42),
    fps,
    config: { damping: 9, mass: 0.6, stiffness: 160 },
  });

  const currentY = -scrollProgress * itemHeight;

  // Background frame entrance
  const boxScale = spring({
    frame,
    fps,
    config: { damping: 14, mass: 0.8, stiffness: 120 },
  });

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
      }}
    >
      {/* Subtitle tag */}
      <div
        style={{
          fontSize: "18px",
          fontWeight: 800,
          letterSpacing: "0.2em",
          color: theme.colors.accent,
          fontFamily: theme.fonts.mono,
          marginBottom: "20px",
          textShadow: theme.shadows.glowAccent,
          opacity: interpolate(frame, [0, 10], [0, 1], { extrapolateRight: "clamp" }),
        }}
      >
        ▲ {subtitle} ▲
      </div>

      {/* Viewport Frame with Highlight Box */}
      <div
        style={{
          position: "relative",
          width: "1280px",
          height: `${itemHeight}px`,
          overflow: "hidden",
          borderRadius: "16px",
          boxShadow: theme.shadows.glass,
          transform: `scale(${boxScale})`,
        }}
      >
        {/* Active Center Target Highlight Glass Bar */}
        <div
          style={{
            position: "absolute",
            top: 0,
            left: 0,
            right: 0,
            bottom: 0,
            backgroundColor: theme.colors.bgGlassDark,
            border: `2px solid ${theme.colors.borderAccent}`,
            borderRadius: "16px",
            boxShadow: `${theme.shadows.glowAccent}, inset 0 0 25px rgba(226, 255, 0, 0.1)`,
            zIndex: 1,
            pointerEvents: "none",
          }}
        />

        {/* Scrolling Items Stream */}
        <div
          style={{
            transform: `translateY(${currentY}px)`,
            display: "flex",
            flexDirection: "column",
            zIndex: 2,
            position: "relative",
          }}
        >
          {items.map((item, idx) => {
            const isSelected = idx === selectedIndex;
            const distance = Math.abs(idx - scrollProgress);
            const itemOpacity = Math.max(0.2, 1 - distance * 0.7);

            return (
              <div
                key={idx}
                style={{
                  height: `${itemHeight}px`,
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "center",
                  padding: "0 30px",
                  textAlign: "center",
                  fontFamily,
                  fontSize: isSelected ? "48px" : "40px",
                  fontWeight: 900,
                  letterSpacing: "-0.02em",
                  color: isSelected && frame > 42 ? theme.colors.accent : theme.colors.textWhite,
                  opacity: itemOpacity,
                  transform: isSelected && frame > 42 ? `scale(${1 + (snapSpring - 1) * 0.08})` : "scale(1)",
                  textShadow: isSelected && frame > 42
                    ? `${theme.shadows.glowAccent}, 0 4px 30px rgba(0, 0, 0, 0.9)`
                    : "0 4px 20px rgba(0, 0, 0, 0.8)",
                  transition: "color 0.1s ease",
                }}
              >
                {item}
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};
