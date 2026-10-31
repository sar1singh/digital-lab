import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { ChannelId, getChannelTheme } from "../../styles/theme";

export interface MagnifyingGlassDocProps {
  channel?: ChannelId;
  documentTitle?: string;
  docketNo?: string;
  preambleText?: string;
  magnifiedText?: string;
  postambleText?: string;
  stampText?: string;
  footerNote?: string;
}

export const MagnifyingGlassDoc: React.FC<MagnifyingGlassDocProps> = ({
  channel = "thinklate",
  documentTitle = "MUNICIPAL HOUSING REGULATION // SECTION 402(B)",
  docketNo = "SAN FRANCISCO HOUSING AUTHORITY // DOCKET #07-8891",
  preambleText = "It is strictly unlawful for any tenant to sublease residential space without written consent, and specifically, ",
  magnifiedText = "charging nightly accommodation fees without a commercial hotel license constitutes an immediate misdemeanor",
  postambleText = ", subjecting all primary occupants to emergency eviction within seventy-two hours of notice.",
  stampText = "REGULATORY VIOLATION",
  footerNote = "OFFICIAL RECORD // CITY & COUNTY OF SAN FRANCISCO HOUSING CODE",
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const theme = getChannelTheme(channel);

  // Card entrance spring
  const cardScale = spring({
    frame,
    fps,
    config: { damping: 14, mass: 0.8, stiffness: 110 },
  });
  const opacity = interpolate(frame, [0, 8], [0, 1], { extrapolateRight: "clamp" });

  // Magnifying glass horizontal sweep (frames 15 to 70)
  const lensProgress = interpolate(frame, [15, 70], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const lensX = interpolate(lensProgress, [0, 1], [-180, 240]);
  const lensY = Math.sin(frame / 10) * 8;

  // Yellow highlighter sweep under magnified text (frames 20 to 65)
  const highlightWidth = interpolate(frame, [20, 65], [0, 100], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Forensic stamp slam at frame 55
  const stampSpring = spring({
    frame: Math.max(0, frame - 55),
    fps,
    config: { damping: 9, mass: 0.5, stiffness: 180 },
  });
  const stampOpacity = interpolate(frame, [55, 60], [0, 1], { extrapolateRight: "clamp" });

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
          width: "1420px",
          backgroundColor: theme.colors.bgGlassDark,
          backdropFilter: "blur(28px)",
          borderRadius: "20px",
          border: `1px solid ${theme.colors.borderGlass}`,
          boxShadow: theme.shadows.glass,
          padding: "48px 64px",
          transform: `scale(${cardScale})`,
          opacity,
          position: "relative",
          overflow: "hidden",
        }}
      >
        {/* Document Header */}
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", marginBottom: "28px" }}>
          <div>
            <div
              style={{
                display: "inline-flex",
                alignItems: "center",
                gap: "8px",
                padding: "6px 14px",
                borderRadius: "6px",
                backgroundColor: "rgba(239, 68, 68, 0.15)",
                border: "1px solid rgba(239, 68, 68, 0.45)",
                fontSize: "12px",
                fontWeight: 800,
                letterSpacing: "0.1em",
                color: "#EF4444",
                marginBottom: "10px",
                fontFamily: theme.fonts.mono,
              }}
            >
              <span>🔍 FORENSIC INSPECTION</span>
              <span>{docketNo}</span>
            </div>
            <h2
              style={{
                fontSize: "28px",
                fontWeight: 900,
                color: theme.colors.textWhite,
                margin: 0,
                letterSpacing: "-0.01em",
              }}
            >
              {documentTitle}
            </h2>
          </div>

          <div
            style={{
              padding: "8px 16px",
              backgroundColor: "rgba(255, 255, 255, 0.06)",
              border: "1px solid rgba(255, 255, 255, 0.1)",
              borderRadius: "8px",
              fontSize: "12px",
              fontFamily: theme.fonts.mono,
              color: theme.colors.accent,
            }}
          >
            EXHIBIT // AUDIT VERIFIED
          </div>
        </div>

        {/* Legal Document Content Plate */}
        <div
          style={{
            backgroundColor: "rgba(255, 255, 255, 0.03)",
            border: "1px solid rgba(255, 255, 255, 0.08)",
            borderRadius: "14px",
            padding: "36px 42px",
            fontSize: "23px",
            lineHeight: 1.65,
            color: theme.colors.textMuted,
            position: "relative",
          }}
        >
          <span>{preambleText}</span>

          {/* Target Highlighted Phrase with Neon Sweep */}
          <span
            style={{
              position: "relative",
              display: "inline",
              color: frame > 25 ? "#FFFFFF" : theme.colors.textMuted,
              fontWeight: frame > 25 ? 800 : 500,
              zIndex: 2,
            }}
          >
            <span
              style={{
                position: "absolute",
                left: 0,
                top: "15%",
                bottom: "10%",
                width: `${highlightWidth}%`,
                backgroundColor: "rgba(250, 204, 21, 0.38)", // Signature Nitish Rajput Yellow Marker
                boxShadow: "0 0 20px rgba(250, 204, 21, 0.4)",
                borderRadius: "4px",
                zIndex: -1,
              }}
            />
            {magnifiedText}
          </span>

          <span>{postambleText}</span>

          {/* Magnifying Glass Animated Element */}
          <div
            style={{
              position: "absolute",
              top: "42%",
              left: "48%",
              transform: `translate(${lensX}px, ${lensY}px)`,
              pointerEvents: "none",
              zIndex: 10,
            }}
          >
            {/* Glass Lens Circle */}
            <div
              style={{
                width: "150px",
                height: "150px",
                borderRadius: "50%",
                border: `4px solid ${theme.colors.accent}`,
                boxShadow: `0 15px 35px rgba(0, 0, 0, 0.6), inset 0 0 25px rgba(255, 255, 255, 0.25), ${theme.shadows.glowAccent}`,
                backdropFilter: "contrast(125%) brightness(115%)",
                position: "relative",
                background: "radial-gradient(circle at 35% 35%, rgba(255,255,255,0.2) 0%, rgba(255,255,255,0.02) 60%, rgba(0,0,0,0.2) 100%)",
              }}
            >
              {/* Internal Crosshairs */}
              <div
                style={{
                  position: "absolute",
                  top: "50%",
                  left: "20%",
                  right: "20%",
                  height: "1px",
                  backgroundColor: "rgba(255, 255, 255, 0.35)",
                }}
              />
              <div
                style={{
                  position: "absolute",
                  left: "50%",
                  top: "20%",
                  bottom: "20%",
                  width: "1px",
                  backgroundColor: "rgba(255, 255, 255, 0.35)",
                }}
              />
            </div>

            {/* Lens Handle */}
            <div
              style={{
                position: "absolute",
                top: "125px",
                left: "125px",
                width: "90px",
                height: "12px",
                borderRadius: "6px",
                background: "linear-gradient(90deg, #334155, #0F172A)",
                border: "1px solid rgba(255,255,255,0.2)",
                boxShadow: "0 8px 15px rgba(0,0,0,0.5)",
                transform: "rotate(45deg)",
                transformOrigin: "0% 0%",
              }}
            />
          </div>

          {/* Forensic Red Rubber Stamp Slam */}
          <div
            style={{
              position: "absolute",
              bottom: "24px",
              right: "40px",
              padding: "10px 24px",
              border: "4px solid #DC2626",
              borderRadius: "8px",
              color: "#DC2626",
              fontSize: "22px",
              fontWeight: 900,
              letterSpacing: "0.15em",
              textTransform: "uppercase",
              fontFamily: theme.fonts.mono,
              transform: `scale(${stampSpring}) rotate(-12deg)`,
              opacity: stampOpacity,
              backgroundColor: "rgba(255, 255, 255, 0.9)",
              boxShadow: "0 8px 25px rgba(220, 38, 38, 0.35)",
              zIndex: 15,
            }}
          >
            {stampText}
          </div>
        </div>

        {/* Footer */}
        <div
          style={{
            marginTop: "20px",
            fontSize: "12px",
            fontFamily: theme.fonts.mono,
            color: theme.colors.textDim,
            display: "flex",
            justifyContent: "space-between",
          }}
        >
          <span>{footerNote}</span>
          <span style={{ color: theme.colors.accent }}>PAGE 14 OF 82 // PRIMARY EVIDENCE</span>
        </div>
      </div>
    </div>
  );
};

