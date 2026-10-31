import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { THEME } from "../../styles/theme";

export interface DocumentRedactionCardProps {
  docketNumber?: string;
  classification?: string;
  title: string;
  clausePreamble: string;
  redactedPhrase: string;
  clausePostamble: string;
  revealText?: string;
  footerNote?: string;
}

export const DocumentRedactionCard: React.FC<DocumentRedactionCardProps> = ({
  docketNumber = "CASE #08-CV-94021 // U.S. DISTRICT COURT",
  classification = "DECLASSIFIED EXHIBIT",
  title = "CONFIDENTIAL INTERNAL VC CORRESPONDENCE",
  clausePreamble = "The partners agreed that while the founders are remarkably persistent, ",
  redactedPhrase = "the core business model has no sustainable moat and will likely collapse within six months",
  clausePostamble = ", therefore recommending an immediate pass on the Series Seed round.",
  revealText = "EXHIBIT B: SAN FRANCISCO HOUSING COMM. DEPOSITION",
  footerNote = "UNREDACTED PRIMARY RECORD // FREEDOM OF INFORMATION ACT DOCKET",
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const cardScale = spring({
    frame,
    fps,
    config: { damping: 14, mass: 0.8, stiffness: 100 },
  });

  const opacity = interpolate(frame, [0, 8], [0, 1], { extrapolateRight: "clamp" });

  // Stamp entrance
  const stampPop = spring({
    frame: Math.max(0, frame - 8),
    fps,
    config: { damping: 10, mass: 0.5, stiffness: 160 },
  });

  // Redaction bar peel / lift (frame 25 to 50 reveals the secret underneath!)
  const peelProgress = interpolate(frame, [25, 50], [100, 0], {
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
        fontFamily: THEME.fonts.sans,
        backgroundColor: "transparent",
      }}
    >
      <div
        style={{
          width: "1360px",
          backgroundColor: THEME.colors.bgGlassDark,
          backdropFilter: "blur(26px)",
          borderRadius: "20px",
          border: `1px solid rgba(255, 255, 255, 0.15)`,
          boxShadow: THEME.shadows.glass,
          padding: "48px 60px",
          transform: `scale(${cardScale})`,
          opacity,
          display: "flex",
          flexDirection: "column",
          gap: "24px",
          position: "relative",
          overflow: "hidden",
        }}
      >
        {/* Top Edge Bar */}
        <div style={{ position: "absolute", top: 0, left: 0, right: 0, height: "4px", backgroundColor: THEME.colors.crimsonRed }} />

        {/* Header & Stamp */}
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", borderBottom: "1px solid rgba(255, 255, 255, 0.1)", paddingBottom: "18px" }}>
          <div>
            <div style={{ fontFamily: THEME.fonts.mono, fontSize: "12px", color: THEME.colors.crimsonRed, fontWeight: 700, letterSpacing: "0.2em", textTransform: "uppercase" }}>
              ● {docketNumber}
            </div>
            <h2 style={{ fontSize: "28px", fontWeight: 900, color: THEME.colors.textWhite, margin: "6px 0 0 0", letterSpacing: "-0.01em" }}>
              {title}
            </h2>
          </div>

          {/* Red Stamp */}
          <div
            style={{
              transform: `scale(${stampPop}) rotate(-6deg)`,
              opacity: stampPop,
              border: `3px solid ${THEME.colors.crimsonRed}`,
              borderRadius: "8px",
              padding: "6px 18px",
              fontFamily: THEME.fonts.mono,
              fontWeight: 900,
              fontSize: "14px",
              letterSpacing: "0.22em",
              color: THEME.colors.crimsonRed,
              textTransform: "uppercase",
              boxShadow: THEME.shadows.glowCrimson,
            }}
          >
            {classification}
          </div>
        </div>

        {/* Official Document Body */}
        <div
          style={{
            backgroundColor: "rgba(255, 255, 255, 0.03)",
            borderLeft: `4px solid ${THEME.colors.crimsonRed}`,
            padding: "28px 32px",
            borderRadius: "0 14px 14px 0",
            fontSize: "24px",
            lineHeight: 1.6,
            color: THEME.colors.textWhite,
            fontFamily: "Georgia, serif",
          }}
        >
          <span>{clausePreamble}</span>

          {/* Redacted / Revealed Zone */}
          <span
            style={{
              position: "relative",
              display: "inline",
              backgroundColor: "rgba(226, 255, 0, 0.15)",
              color: THEME.colors.acidLime,
              fontWeight: 900,
              padding: "2px 8px",
              borderRadius: "4px",
            }}
          >
            {/* The Black Redaction Tape that pulls back */}
            <span
              style={{
                position: "absolute",
                top: 0,
                bottom: 0,
                right: 0,
                width: `${peelProgress}%`,
                backgroundColor: "#05080F",
                border: "1px solid rgba(255,255,255,0.2)",
                zIndex: 2,
              }}
            />
            {redactedPhrase}
          </span>

          <span>{clausePostamble}</span>
        </div>

        {/* Footer */}
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", borderTop: "1px solid rgba(255, 255, 255, 0.08)", paddingTop: "14px", fontFamily: THEME.fonts.mono, fontSize: "12px", color: THEME.colors.textDim }}>
          <span>{revealText}</span>
          <span style={{ color: THEME.colors.crimsonRed }}>{footerNote}</span>
        </div>
      </div>
    </div>
  );
};
