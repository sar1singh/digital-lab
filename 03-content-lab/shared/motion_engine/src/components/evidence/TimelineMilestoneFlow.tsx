import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { ChannelId, getChannelTheme } from "../../styles/theme";

export interface MilestoneItem {
  date: string;
  title: string;
  desc: string;
  active?: boolean;
}

export interface TimelineMilestoneFlowProps {
  channel?: ChannelId;
  badgeText?: string;
  title?: string;
  milestones?: MilestoneItem[];
  footerNote?: string;
}

export const TimelineMilestoneFlow: React.FC<TimelineMilestoneFlowProps> = ({
  channel = "thinklate",
  badgeText = "HISTORICAL SEQUENCE // CRITICAL TURNING POINTS",
  title = "THE 4-STAGE BOOTSTRAP TO UNICORN VELOCITY",
  milestones = [
    {
      date: "OCT 2007",
      title: "THE $80 AIRBED",
      desc: "3 air mattresses on living room floor pays $1,150 rent.",
      active: false,
    },
    {
      date: "AUG 2008",
      title: "OBAMA O'S CEREAL",
      desc: "$30K election cereal boxes bootstrap 3 months runway.",
      active: false,
    },
    {
      date: "JAN 2009",
      title: "Y COMBINATOR RESCUE",
      desc: "Paul Graham: 'If you can sell $40 cereal, you won't die.'",
      active: true,
    },
    {
      date: "NOV 2011",
      title: "$1B VALUATION",
      desc: "Global disruption of the legacy hotel cartel finalized.",
      active: false,
    },
  ],
  footerNote = "SOURCE: FOUNDER DEPOSITIONS ✦ Y COMBINATOR ARCHIVES W09",
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const theme = getChannelTheme(channel);

  // Entrance spring
  const cardScale = spring({
    frame,
    fps,
    config: {
      damping: theme.motion.damping,
      mass: theme.motion.mass,
      stiffness: theme.motion.stiffness,
    },
  });
  const opacity = interpolate(frame, [0, 8], [0, 1], { extrapolateRight: "clamp" });

  // Progress line animation (frames 15 to 60)
  const lineProgress = interpolate(frame, [15, 60], [0, 100], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <div
      style={{
        width: "100%",
        height: "100%",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        fontFamily: theme.fonts.sans,
        backgroundColor: "transparent",
      }}
    >
      <div
        style={{
          width: "1480px",
          backgroundColor: theme.colors.bgGlassDark,
          backdropFilter: "blur(26px)",
          borderRadius: "20px",
          border: `1px solid ${theme.colors.borderGlass}`,
          boxShadow: theme.shadows.glass,
          padding: "44px 56px",
          transform: `scale(${cardScale})`,
          opacity,
          display: "flex",
          flexDirection: "column",
          gap: "28px",
        }}
      >
        {/* Header */}
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
          <div>
            <div
              style={{
                display: "inline-flex",
                alignItems: "center",
                gap: "8px",
                padding: "6px 14px",
                borderRadius: "6px",
                backgroundColor: `${theme.colors.accent}18`,
                border: `1px solid ${theme.colors.borderAccent}`,
                fontSize: "12px",
                fontWeight: 800,
                letterSpacing: "0.1em",
                color: theme.colors.accent,
                marginBottom: "12px",
                fontFamily: theme.fonts.mono,
              }}
            >
              <span>●</span>
              <span>{badgeText}</span>
            </div>
            <h2
              style={{
                fontSize: "32px",
                fontWeight: 900,
                color: theme.colors.textWhite,
                margin: 0,
                letterSpacing: "-0.02em",
              }}
            >
              {title}
            </h2>
          </div>

          <div
            style={{
              padding: "8px 16px",
              backgroundColor: "rgba(255, 255, 255, 0.05)",
              border: "1px solid rgba(255, 255, 255, 0.1)",
              borderRadius: "8px",
              fontSize: "12px",
              fontFamily: theme.fonts.mono,
              color: theme.colors.textMuted,
            }}
          >
            PROGRESSION: {Math.round(lineProgress)}%
          </div>
        </div>

        {/* Timeline Horizontal Track */}
        <div style={{ position: "relative", marginTop: "32px", marginBottom: "16px" }}>
          {/* Base Track */}
          <div
            style={{
              position: "absolute",
              top: "24px",
              left: "40px",
              right: "40px",
              height: "4px",
              backgroundColor: "rgba(255, 255, 255, 0.12)",
              borderRadius: "2px",
              zIndex: 1,
            }}
          />

          {/* Active Animated Track */}
          <div
            style={{
              position: "absolute",
              top: "24px",
              left: "40px",
              width: `calc(${lineProgress}% - 80px)`,
              height: "4px",
              background: `linear-gradient(90deg, ${theme.colors.accentSecondary}, ${theme.colors.accent})`,
              boxShadow: theme.shadows.glowAccent,
              borderRadius: "2px",
              zIndex: 2,
            }}
          />

          {/* Milestone Columns */}
          <div
            style={{
              display: "grid",
              gridTemplateColumns: `repeat(${milestones.length}, 1fr)`,
              gap: "24px",
              position: "relative",
              zIndex: 3,
            }}
          >
            {milestones.map((m, idx) => {
              const nodeFrame = 18 + idx * 12;
              const nodeSpring = spring({
                frame: Math.max(0, frame - nodeFrame),
                fps,
                config: { damping: 10, mass: 0.6, stiffness: 150 },
              });
              const nodeOpacity = interpolate(frame, [nodeFrame, nodeFrame + 6], [0, 1], {
                extrapolateRight: "clamp",
              });

              const isActive = m.active;
              const pulse = isActive ? Math.sin(frame / 6) * 0.25 + 0.95 : 1;

              return (
                <div
                  key={idx}
                  style={{
                    display: "flex",
                    flexDirection: "column",
                    alignItems: "flex-start",
                    opacity: nodeOpacity,
                    transform: `translateY(${(1 - nodeSpring) * 20}px)`,
                  }}
                >
                  {/* Node Dot / Badge */}
                  <div
                    style={{
                      width: "48px",
                      height: "48px",
                      borderRadius: "50%",
                      backgroundColor: isActive ? theme.colors.accent : "rgba(18, 24, 38, 0.9)",
                      border: `3px solid ${isActive ? theme.colors.textWhite : theme.colors.borderGlass}`,
                      display: "flex",
                      alignItems: "center",
                      justifyContent: "center",
                      fontSize: "14px",
                      fontWeight: 900,
                      color: isActive ? "#05080F" : theme.colors.textMuted,
                      boxShadow: isActive ? `${theme.shadows.glowAccent}, 0 0 20px ${theme.colors.accent}` : "none",
                      transform: `scale(${nodeSpring * pulse})`,
                      marginBottom: "18px",
                    }}
                  >
                    0{idx + 1}
                  </div>

                  {/* Date Pill */}
                  <div
                    style={{
                      fontSize: "12px",
                      fontWeight: 800,
                      color: isActive ? theme.colors.accent : theme.colors.textDim,
                      fontFamily: theme.fonts.mono,
                      letterSpacing: "0.08em",
                      marginBottom: "6px",
                    }}
                  >
                    {m.date}
                  </div>

                  {/* Milestone Title */}
                  <div
                    style={{
                      fontSize: "18px",
                      fontWeight: 800,
                      color: theme.colors.textWhite,
                      marginBottom: "8px",
                      lineHeight: 1.2,
                    }}
                  >
                    {m.title}
                  </div>

                  {/* Milestone Description */}
                  <div
                    style={{
                      fontSize: "14px",
                      color: theme.colors.textMuted,
                      lineHeight: 1.45,
                    }}
                  >
                    {m.desc}
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* Footer Note */}
        <div
          style={{
            borderTop: "1px solid rgba(255, 255, 255, 0.08)",
            paddingTop: "16px",
            fontSize: "12px",
            fontFamily: theme.fonts.mono,
            color: theme.colors.textDim,
            letterSpacing: "0.05em",
          }}
        >
          {footerNote}
        </div>
      </div>
    </div>
  );
};
