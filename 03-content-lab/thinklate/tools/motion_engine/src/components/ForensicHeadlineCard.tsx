import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { THEME } from "../styles/theme";

export interface ForensicHeadlineCardProps {
  publication?: string;
  category?: string;
  headline: string;
  excerpt: string;
  highlightWords?: string;
  dateStr?: string;
  authorOrRef?: string;
}

export const ForensicHeadlineCard: React.FC<ForensicHeadlineCardProps> = ({
  publication = "THE WALL STREET JOURNAL",
  category = "INVESTIGATIVE DISPATCH",
  headline,
  excerpt,
  highlightWords,
  dateStr = "OCTOBER 2008",
  authorOrRef = "SPECIAL CORPORATE DOSSIER",
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Spring scale entrance
  const scale = spring({
    frame,
    fps,
    config: { damping: 14, mass: 0.85, stiffness: 100 },
  });

  const opacity = interpolate(frame, [0, 8], [0, 1], {
    extrapolateRight: "clamp",
  });

  // Highlighter sweep (frames 15 to 45)
  const highlightProgress = interpolate(frame, [15, 45], [0, 100], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Render excerpt with highlight
  const renderExcerpt = () => {
    if (!highlightWords || !excerpt.includes(highlightWords)) {
      return <span>{excerpt}</span>;
    }
    const [before, after] = excerpt.split(highlightWords);
    return (
      <span>
        {before}
        <span
          style={{
            position: "relative",
            display: "inline",
            color: "#05080F",
            fontWeight: 800,
            padding: "2px 8px",
            borderRadius: "4px",
            zIndex: 1,
          }}
        >
          <span
            style={{
              position: "absolute",
              top: 0,
              left: 0,
              bottom: 0,
              width: `${highlightProgress}%`,
              backgroundColor: THEME.colors.acidLime,
              zIndex: -1,
              borderRadius: "4px",
              boxShadow: THEME.shadows.glowLime,
            }}
          />
          {highlightWords}
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
          width: "1480px",
          backgroundColor: THEME.colors.bgGlassDark,
          backdropFilter: "blur(28px)",
          borderRadius: "20px",
          border: `1px solid ${THEME.colors.borderGlass}`,
          boxShadow: THEME.shadows.glass,
          padding: "52px 64px",
          transform: `scale(${scale})`,
          opacity,
          display: "flex",
          flexDirection: "column",
          gap: "24px",
          position: "relative",
          overflow: "hidden",
        }}
      >
        {/* Top Edge Accent */}
        <div
          style={{
            position: "absolute",
            top: 0,
            left: 0,
            right: 0,
            height: "4px",
            background: `linear-gradient(90deg, ${THEME.colors.acidLime}, ${THEME.colors.cyanElectric})`,
          }}
        />

        {/* Masthead Header */}
        <div
          style={{
            display: "flex",
            alignItems: "center",
            justifyContent: "space-between",
            borderBottom: `2px solid rgba(255, 255, 255, 0.12)`,
            paddingBottom: "18px",
          }}
        >
          <div style={{ display: "flex", alignItems: "baseline", gap: "16px" }}>
            <span
              style={{
                fontFamily: THEME.fonts.sans,
                fontSize: "24px",
                fontWeight: 900,
                letterSpacing: "0.08em",
                textTransform: "uppercase",
                color: THEME.colors.textWhite,
              }}
            >
              {publication}
            </span>
            <span
              style={{
                fontFamily: THEME.fonts.mono,
                fontSize: "12px",
                color: THEME.colors.acidLime,
                letterSpacing: "0.15em",
                textTransform: "uppercase",
              }}
            >
              // {category}
            </span>
          </div>
          <div
            style={{
              fontFamily: THEME.fonts.mono,
              fontSize: "13px",
              color: THEME.colors.textDim,
              letterSpacing: "0.1em",
            }}
          >
            {dateStr}
          </div>
        </div>

        {/* Big Editorial Headline */}
        <h1
          style={{
            fontSize: "46px",
            fontWeight: 900,
            lineHeight: 1.15,
            color: THEME.colors.textWhite,
            letterSpacing: "-0.025em",
            margin: "8px 0 0 0",
          }}
        >
          {headline}
        </h1>

        {/* Sub-quote / Forensic Excerpt Box */}
        <div
          style={{
            backgroundColor: "rgba(255, 255, 255, 0.04)",
            borderLeft: `4px solid ${THEME.colors.acidLime}`,
            borderRadius: "0 12px 12px 0",
            padding: "24px 28px",
            fontSize: "24px",
            lineHeight: 1.5,
            color: THEME.colors.textMuted,
            fontFamily: THEME.fonts.sans,
          }}
        >
          {renderExcerpt()}
        </div>

        {/* Masthead Footer */}
        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
            borderTop: `1px solid rgba(255, 255, 255, 0.08)`,
            paddingTop: "16px",
            fontFamily: THEME.fonts.mono,
            fontSize: "12px",
            color: THEME.colors.textDim,
            letterSpacing: "0.12em",
          }}
        >
          <span>ARCHIVAL PRESS REPOSITORY: {authorOrRef}</span>
          <span style={{ color: THEME.colors.acidLime }}>AUTHENTICATED SOURCE</span>
        </div>
      </div>
    </div>
  );
};
