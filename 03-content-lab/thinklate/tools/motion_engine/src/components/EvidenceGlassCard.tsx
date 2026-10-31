import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { THEME } from "../styles/theme";

export interface EvidenceGlassCardProps {
  badgeText?: string;
  badgeType?: "warning" | "verified" | "danger";
  title?: string;
  quote?: string;
  highlightWords?: string;
  sourceDoc?: string;
  dateStr?: string;
}

export const EvidenceGlassCard: React.FC<EvidenceGlassCardProps> = ({
  badgeText = "PRIMARY EVIDENCE // EVICTION NOTICE",
  badgeType = "warning",
  title = "OCTOBER 2007: 72 HOURS FROM STREET",
  quote = "Your rent is $1,150. You have three days before your landlord kicks you out and your bank account is empty.",
  highlightWords = "three days before your landlord kicks you out",
  sourceDoc = "SAN FRANCISCO RESIDENTIAL TENANCY RECORD #4092",
  dateStr = "OCTOBER 14, 2007",
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Entrance spring animation (smooth slide and fade from right)
  const entrance = spring({
    frame,
    fps,
    config: {
      damping: 16,
      mass: 0.8,
      stiffness: 120,
    },
  });

  const translateY = interpolate(entrance, [0, 1], [40, 0]);
  const opacity = interpolate(entrance, [0, 1], [0, 1]);
  const scale = interpolate(entrance, [0, 1], [0.94, 1]);

  // Highlighter sweep progress (starts after card lands at frame 15)
  const highlightProgress = interpolate(frame, [18, 48], [0, 100], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const getBadgeColors = () => {
    switch (badgeType) {
      case "danger":
        return { bg: "rgba(239, 68, 68, 0.18)", border: THEME.colors.crimsonRed, text: "#FFA4A4" };
      case "verified":
        return { bg: "rgba(6, 182, 212, 0.18)", border: THEME.colors.cyanElectric, text: "#A5F3FC" };
      case "warning":
      default:
        return { bg: "rgba(245, 158, 11, 0.18)", border: THEME.colors.warmAmber, text: "#FDE68A" };
    }
  };

  const badgeStyle = getBadgeColors();

  return (
    <div
      style={{
        width: "100%",
        height: "100%",
        display: "flex",
        alignItems: "center",
        justifyContent: "flex-end",
        paddingRight: "100px",
        fontFamily: THEME.fonts.sans,
        boxSizing: "border-box",
      }}
    >
      <div
        style={{
          width: "780px",
          backgroundColor: THEME.colors.bgGlass,
          backdropFilter: "blur(24px)",
          borderRadius: "24px",
          border: `1px solid ${THEME.colors.borderGlass}`,
          boxShadow: THEME.shadows.glass,
          padding: "44px 50px",
          transform: `translateY(${translateY}px) scale(${scale})`,
          opacity,
          display: "flex",
          flexDirection: "column",
          gap: "24px",
          position: "relative",
          overflow: "hidden",
        }}
      >
        {/* Top subtle highlight reflection line */}
        <div
          style={{
            position: "absolute",
            top: 0,
            left: "15%",
            right: "15%",
            height: "1px",
            background: "linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent)",
          }}
        />

        {/* Top Badge & Date Header */}
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
          <div
            style={{
              padding: "6px 14px",
              borderRadius: "8px",
              backgroundColor: badgeStyle.bg,
              border: `1px solid ${badgeStyle.border}`,
              color: badgeStyle.text,
              fontSize: "13px",
              fontWeight: 700,
              letterSpacing: "1.2px",
              fontFamily: THEME.fonts.mono,
              display: "flex",
              alignItems: "center",
              gap: "8px",
            }}
          >
            <span
              style={{
                width: "8px",
                height: "8px",
                borderRadius: "50%",
                backgroundColor: badgeStyle.border,
                display: "inline-block",
              }}
            />
            {badgeText}
          </div>

          <div
            style={{
              fontFamily: THEME.fonts.mono,
              fontSize: "13px",
              color: THEME.colors.textMuted,
              letterSpacing: "1px",
            }}
          >
            {dateStr}
          </div>
        </div>

        {/* Headline Title */}
        <div
          style={{
            fontSize: "24px",
            fontWeight: 800,
            color: THEME.colors.textWhite,
            letterSpacing: "-0.5px",
            lineHeight: 1.25,
            textTransform: "uppercase",
          }}
        >
          {title}
        </div>

        {/* Quote Content with Highlighter Sweep */}
        <div
          style={{
            fontSize: "30px",
            fontWeight: 600,
            color: THEME.colors.textWhite,
            lineHeight: 1.45,
            position: "relative",
          }}
        >
          <span>&ldquo;</span>
          {quote.includes(highlightWords) ? (
            <>
              {quote.split(highlightWords)[0]}
              <span
                style={{
                  position: "relative",
                  display: "inline-block",
                  color: "#FFFFFF",
                  fontWeight: 700,
                  zIndex: 1,
                  padding: "0 4px",
                }}
              >
                <span
                  style={{
                    position: "absolute",
                    left: 0,
                    bottom: "2px",
                    height: "36%",
                    width: `${highlightProgress}%`,
                    backgroundColor: "rgba(226, 255, 0, 0.45)",
                    borderBottom: `2px solid ${THEME.colors.acidLime}`,
                    zIndex: -1,
                    borderRadius: "2px",
                    boxShadow: "0 0 15px rgba(226, 255, 0, 0.3)",
                  }}
                />
                {highlightWords}
              </span>
              {quote.split(highlightWords)[1]}
            </>
          ) : (
            quote
          )}
          <span>&rdquo;</span>
        </div>

        {/* Bottom Verification Docket Footer */}
        <div
          style={{
            marginTop: "8px",
            paddingTop: "20px",
            borderTop: "1px solid rgba(255, 255, 255, 0.08)",
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
            fontSize: "12px",
            color: THEME.colors.textDim,
            fontFamily: THEME.fonts.mono,
            letterSpacing: "0.8px",
          }}
        >
          <span>SRC: {sourceDoc}</span>
          <span style={{ color: THEME.colors.acidLime, fontWeight: 700 }}>VERIFIED RECORD ✓</span>
        </div>
      </div>
    </div>
  );
};
