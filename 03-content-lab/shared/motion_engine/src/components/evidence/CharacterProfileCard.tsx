import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { ChannelId, getChannelTheme } from "../../styles/theme";

export interface ProfileStat {
  label: string;
  value: string;
  color?: string;
}

export interface CharacterProfileCardProps {
  channel?: ChannelId;
  characterName?: string;
  designation?: string;
  photoUrl?: string;
  statusBadge?: string;
  stats?: ProfileStat[];
  stampTag?: string;
  quoteSnippet?: string;
}

export const CharacterProfileCard: React.FC<CharacterProfileCardProps> = ({
  channel = "thinklate",
  characterName = "BRIAN CHESKY",
  designation = "CO-FOUNDER & CEO // AIRBNB",
  photoUrl = "",
  statusBadge = "SUBJECT DOSSIER // ASYMMETRIC FOUNDER",
  stats = [
    { label: "OCTOBER 2007 RENT", value: "$1,150 (OVERDUE)", color: "#EF4444" },
    { label: "FIRST REVENUE", value: "$240 (3 AIRBEDS)", color: "#00F0FF" },
    { label: "CEREAL SEED CAPITAL", value: "$30,000 CASH", color: "#F59E0B" },
    { label: "PEAK VALUATION", value: "$100,000,000,000", color: "#10B981" },
  ],
  stampTag = "DISRUPTION PROVEN",
  quoteSnippet = "\"If we can't pay rent, we make rent our product.\"",
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const theme = getChannelTheme(channel);

  // Card entrance
  const cardScale = spring({
    frame,
    fps,
    config: { damping: 13, mass: 0.8, stiffness: 110 },
  });
  const opacity = interpolate(frame, [0, 8], [0, 1], { extrapolateRight: "clamp" });

  // Photo slide in from left
  const photoSlide = spring({
    frame: Math.max(0, frame - 5),
    fps,
    config: { damping: 11, mass: 0.6, stiffness: 130 },
  });

  // Stamp slam
  const stampSpring = spring({
    frame: Math.max(0, frame - 40),
    fps,
    config: { damping: 9, mass: 0.5, stiffness: 180 },
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
          width: "1400px",
          backgroundColor: theme.colors.bgGlassDark,
          backdropFilter: "blur(28px)",
          borderRadius: "20px",
          border: `1px solid ${theme.colors.borderGlass}`,
          boxShadow: theme.shadows.glass,
          padding: "44px 54px",
          transform: `scale(${cardScale})`,
          opacity,
          display: "grid",
          gridTemplateColumns: "360px 1fr",
          gap: "44px",
          alignItems: "center",
          position: "relative",
        }}
      >
        {/* Left Column: Portrait Cutout / ID Box */}
        <div
          style={{
            height: "460px",
            backgroundColor: "rgba(0, 0, 0, 0.4)",
            borderRadius: "14px",
            border: `2px solid ${theme.colors.borderAccent}`,
            overflow: "hidden",
            position: "relative",
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            justifyContent: "center",
            boxShadow: `0 20px 40px rgba(0,0,0,0.5), ${theme.shadows.glowAccent}`,
            transform: `translateX(${(1 - photoSlide) * -60}px)`,
          }}
        >
          {photoUrl ? (
            <img src={photoUrl} alt={characterName} style={{ width: "100%", height: "100%", objectFit: "cover" }} />
          ) : (
            <div style={{ textAlign: "center", padding: "20px" }}>
              <div style={{ fontSize: "72px", marginBottom: "16px" }}>👤</div>
              <div style={{ fontSize: "24px", fontWeight: 900, color: theme.colors.textWhite }}>{characterName}</div>
              <div style={{ fontSize: "12px", color: theme.colors.textDim, fontFamily: theme.fonts.mono, marginTop: "6px" }}>
                ARCHIVAL PHOTOGRAPH
              </div>
            </div>
          )}

          {/* Dossier Corner Ribbon */}
          <div
            style={{
              position: "absolute",
              top: "14px",
              left: "14px",
              padding: "4px 10px",
              backgroundColor: `${theme.colors.accent}22`,
              border: `1px solid ${theme.colors.borderAccent}`,
              borderRadius: "4px",
              fontSize: "11px",
              fontFamily: theme.fonts.mono,
              fontWeight: 800,
              color: theme.colors.accent,
            }}
          >
            FILE #08-FOUNDER
          </div>
        </div>

        {/* Right Column: Dossier Information & Financial Stats */}
        <div style={{ display: "flex", flexDirection: "column", gap: "20px" }}>
          <div>
            <div
              style={{
                display: "inline-flex",
                alignItems: "center",
                gap: "8px",
                padding: "6px 14px",
                borderRadius: "6px",
                backgroundColor: `${theme.colors.accent}15`,
                border: `1px solid ${theme.colors.borderAccent}`,
                fontSize: "12px",
                fontWeight: 800,
                letterSpacing: "0.1em",
                color: theme.colors.accent,
                marginBottom: "10px",
                fontFamily: theme.fonts.mono,
              }}
            >
              <span>●</span>
              <span>{statusBadge}</span>
            </div>

            <h1
              style={{
                fontSize: "44px",
                fontWeight: 900,
                color: theme.colors.textWhite,
                margin: 0,
                letterSpacing: "-0.02em",
              }}
            >
              {characterName}
            </h1>

            <div
              style={{
                fontSize: "18px",
                fontWeight: 700,
                color: theme.colors.accentSecondary,
                letterSpacing: "0.05em",
                fontFamily: theme.fonts.mono,
                marginTop: "4px",
              }}
            >
              {designation}
            </div>
          </div>

          {/* Quote Bar */}
          <div
            style={{
              padding: "16px 22px",
              backgroundColor: "rgba(255, 255, 255, 0.04)",
              borderLeft: `4px solid ${theme.colors.accent}`,
              borderRadius: "0 10px 10px 0",
              fontSize: "18px",
              fontStyle: "italic",
              color: theme.colors.textMuted,
            }}
          >
            {quoteSnippet}
          </div>

          {/* 4-Stat Metric Grid */}
          <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "16px" }}>
            {stats.map((st, idx) => {
              const rowFrame = 15 + idx * 8;
              const rowSpring = spring({
                frame: Math.max(0, frame - rowFrame),
                fps,
                config: { damping: 10, mass: 0.5, stiffness: 140 },
              });

              return (
                <div
                  key={idx}
                  style={{
                    backgroundColor: "rgba(0, 0, 0, 0.35)",
                    border: `1px solid rgba(255, 255, 255, 0.08)`,
                    borderRadius: "10px",
                    padding: "14px 18px",
                    transform: `translateY(${(1 - rowSpring) * 15}px)`,
                    opacity: interpolate(frame, [rowFrame, rowFrame + 6], [0, 1], { extrapolateRight: "clamp" }),
                  }}
                >
                  <div style={{ fontSize: "11px", color: theme.colors.textDim, fontFamily: theme.fonts.mono, letterSpacing: "0.08em" }}>
                    {st.label}
                  </div>
                  <div style={{ fontSize: "20px", fontWeight: 900, color: st.color || theme.colors.textWhite, marginTop: "4px" }}>
                    {st.value}
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* Rubber Stamp Slam in bottom right corner */}
        <div
          style={{
            position: "absolute",
            bottom: "32px",
            right: "42px",
            padding: "8px 22px",
            border: "4px solid #10B981",
            borderRadius: "8px",
            color: "#10B981",
            fontSize: "20px",
            fontWeight: 900,
            letterSpacing: "0.15em",
            textTransform: "uppercase",
            fontFamily: theme.fonts.mono,
            transform: `scale(${stampSpring}) rotate(-8deg)`,
            opacity: interpolate(frame, [40, 45], [0, 1], { extrapolateRight: "clamp" }),
            backgroundColor: "rgba(10, 20, 15, 0.85)",
            boxShadow: "0 8px 25px rgba(16, 185, 129, 0.35)",
            zIndex: 15,
          }}
        >
          {stampTag}
        </div>
      </div>
    </div>
  );
};

