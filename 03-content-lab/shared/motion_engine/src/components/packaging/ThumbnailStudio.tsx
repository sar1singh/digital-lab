import React from "react";
import { ChannelId, getChannelTheme } from "../../styles/theme";

export interface ThumbnailStudioProps {
  channel?: ChannelId;
  style?: "nitish_drama" | "magnates_brand" | "alux_minimal" | "vox_forensic";
  headlineTop?: string;
  headlineBottom?: string;
  headlineTopColor?: string;
  headlineBottomColor?: string;
  badgeText?: string;
  badgeColor?: string;
  bgGradient?: string;
  bgImageUrl?: string;
  subjectImageUrl?: string;
  subjectRimColor?: string;
  brandLogoType?: "airbnb" | "hazard" | "dollar" | "skull" | "none";
  statPins?: Array<{ label: string; value: string }>;
  accentStamp?: string;
}

export const ThumbnailStudio: React.FC<ThumbnailStudioProps> = ({
  channel = "thinklate",
  style = "nitish_drama",
  headlineTop = "THE INSANE",
  headlineBottom = "HEIST OF $100B",
  headlineTopColor = "#FFFFFF",
  headlineBottomColor,
  badgeText = "CRIMINAL EXPOSE",
  badgeColor = "#FF2A4B",
  bgGradient,
  bgImageUrl,
  subjectImageUrl,
  subjectRimColor = "#00F0FF",
  brandLogoType = "airbnb",
  statPins = [
    { label: "CLEANING FEE", value: "$300" },
    { label: "CHORE LIST", value: "8 TASKS" },
    { label: "HOTEL SAVINGS", value: "$0" }
  ],
  accentStamp = "EXPOSED"
}) => {
  const theme = getChannelTheme(channel);
  const bottomColor = headlineBottomColor || theme.colors.accent;

  // Background styling
  const defaultGradient = style === "magnates_brand"
    ? "radial-gradient(circle at 65% 50%, #B50543 0%, #4D011B 70%, #1A0009 100%)"
    : style === "vox_forensic"
    ? "radial-gradient(circle at 50% 50%, #1E293B 0%, #0F172A 70%, #050811 100%)"
    : "radial-gradient(circle at 25% 40%, #7F1D1D 0%, #200407 60%, #080C14 100%)";

  const effectiveBg = bgImageUrl
    ? `linear-gradient(rgba(10, 15, 26, 0.4), rgba(10, 15, 26, 0.85)), url(${bgImageUrl}) center/cover no-repeat`
    : (bgGradient || defaultGradient);

  return (
    <div
      style={{
        position: "relative",
        width: 1280,
        height: 720,
        background: effectiveBg,
        overflow: "hidden",
        fontFamily: "'Inter', system-ui, -apple-system, sans-serif",
        boxSizing: "border-box",
      }}
    >
      {/* 1. Subtle High-Contrast Outer Glow Border to Prevent Dark Mode #0F0F0F Blending */}
      <div
        style={{
          position: "absolute",
          top: 0,
          left: 0,
          right: 0,
          bottom: 0,
          border: `4px solid ${theme.colors.accent}`,
          boxShadow: `inset 0 0 40px rgba(0,0,0,0.8), 0 0 30px ${theme.colors.accent}40`,
          pointerEvents: "none",
          zIndex: 50,
        }}
      />

      {/* 2. Style-Specific Visual Layout */}

      {/* A. MAGNATES STYLE: Giant Brand Logo on Right, 3D pins on Bottom */}
      {style === "magnates_brand" && (
        <>
          {/* Giant Brand Logo Right */}
          <div
            style={{
              position: "absolute",
              right: 60,
              top: 80,
              width: 440,
              height: 440,
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              filter: `drop-shadow(0 20px 40px rgba(0,0,0,0.7)) drop-shadow(0 0 60px ${theme.colors.accent}60)`,
              zIndex: 10,
            }}
          >
            {brandLogoType === "airbnb" && (
              <svg viewBox="0 0 100 115" width="380" height="420" fill="none" stroke="#FFFFFF" strokeWidth="9" strokeLinecap="round" strokeLinejoin="round">
                <path d="M50 8 C38 8 28 20 28 35 C28 60 12 75 8 92 C4 105 15 110 28 110 C38 110 46 102 50 92 C54 102 62 110 72 110 C85 110 96 105 92 92 C88 75 72 60 72 35 C72 20 62 8 50 8 Z" />
                <circle cx="50" cy="48" r="14" stroke="#FFFFFF" strokeWidth="8" />
              </svg>
            )}
            {brandLogoType === "dollar" && (
              <div style={{ fontSize: 320, fontWeight: 900, color: "#FFFFFF", textShadow: "0 10px 40px rgba(0,0,0,0.9)" }}>
                $
              </div>
            )}
          </div>

          {/* Bottom Skyline / Stat Chips */}
          <div
            style={{
              position: "absolute",
              bottom: 40,
              left: 60,
              display: "flex",
              gap: 20,
              zIndex: 20,
            }}
          >
            {statPins.map((pin, i) => (
              <div
                key={i}
                style={{
                  backgroundColor: "#FFFFFF",
                  color: "#080C14",
                  padding: "10px 22px",
                  borderRadius: 24,
                  boxShadow: "0 12px 25px rgba(0,0,0,0.6)",
                  display: "flex",
                  flexDirection: "column",
                  alignItems: "center",
                  border: "2px solid #000000",
                }}
              >
                <span style={{ fontSize: 13, fontWeight: 800, letterSpacing: "1px", color: "#64748B" }}>
                  {pin.label}
                </span>
                <span style={{ fontSize: 26, fontWeight: 900, color: "#DC2626" }}>
                  {pin.value}
                </span>
              </div>
            ))}
          </div>
        </>
      )}

      {/* B. NITISH / DRAMA STYLE: Subject Cutout with Neon Rim Light on Right */}
      {style === "nitish_drama" && (
        <>
          {/* Host / Subject Cutout Container */}
          <div
            style={{
              position: "absolute",
              right: 20,
              bottom: 0,
              width: 520,
              height: 680,
              display: "flex",
              alignItems: "flex-end",
              justifyContent: "center",
              zIndex: 15,
            }}
          >
            {subjectImageUrl ? (
              <img
                src={subjectImageUrl}
                alt="Subject"
                style={{
                  maxHeight: "100%",
                  maxWidth: "100%",
                  objectFit: "contain",
                  filter: `drop-shadow(0 0 25px ${subjectRimColor}) drop-shadow(0 20px 40px rgba(0,0,0,0.95)) contrast(1.15) brightness(1.05)`,
                }}
              />
            ) : (
              // High-impact graphic placeholder silhouette if no photo cutout provided
              <div
                style={{
                  width: 440,
                  height: 600,
                  background: `linear-gradient(180deg, ${subjectRimColor}40 0%, #0F172A 100%)`,
                  borderRadius: "200px 200px 0 0",
                  border: `4px solid ${subjectRimColor}`,
                  boxShadow: `0 0 50px ${subjectRimColor}60, 0 30px 60px rgba(0,0,0,0.9)`,
                  display: "flex",
                  flexDirection: "column",
                  alignItems: "center",
                  justifyContent: "center",
                  padding: 30,
                  boxSizing: "border-box",
                }}
              >
                <span style={{ fontSize: 18, fontWeight: 800, color: subjectRimColor, letterSpacing: 2, marginBottom: 12 }}>
                  SUBJECT CUTOUT
                </span>
                <span style={{ fontSize: 14, color: "#94A3B8", textAlign: "center" }}>
                  (Pass cutout PNG via subjectImageUrl for Nitish-grade host presence)
                </span>
              </div>
            )}
          </div>

          {/* Red Alert Threat Accent on Midground */}
          <div
            style={{
              position: "absolute",
              left: 480,
              top: 140,
              backgroundColor: "rgba(239, 68, 68, 0.25)",
              border: "2px solid #EF4444",
              color: "#FCA5A5",
              padding: "8px 18px",
              borderRadius: 8,
              fontSize: 14,
              fontWeight: 800,
              letterSpacing: 2,
              transform: "rotate(-6deg)",
              boxShadow: "0 0 30px rgba(239, 68, 68, 0.5)",
              zIndex: 12,
            }}
          >
            ⚠️ HIGH CONFLICT
          </div>
        </>
      )}

      {/* 3. The Swiss Brutalist Typography Stack (Left Half, Top-Tier Mobile Readability) */}
      <div
        style={{
          position: "absolute",
          top: 65,
          left: 65,
          width: 720,
          display: "flex",
          flexDirection: "column",
          gap: 16,
          zIndex: 30,
        }}
      >
        {/* Category Pill / High-Voltage Badge */}
        {badgeText && (
          <div
            style={{
              alignSelf: "flex-start",
              backgroundColor: badgeColor,
              color: "#FFFFFF",
              fontSize: 18,
              fontWeight: 900,
              letterSpacing: "2.5px",
              padding: "10px 24px",
              borderRadius: 6,
              textTransform: "uppercase",
              boxShadow: "0 8px 24px rgba(0,0,0,0.6)",
              border: "1px solid rgba(255,255,255,0.3)",
            }}
          >
            {badgeText}
          </div>
        )}

        {/* Headline Stack - Massive 110px-130px Architectural Condensed Font */}
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            lineHeight: 0.88,
            textTransform: "uppercase",
            fontFamily: "'Impact', 'Arial Black', 'Montserrat ExtraBold', sans-serif",
            letterSpacing: "-1px",
          }}
        >
          {/* Top Line (Chalk White) */}
          <span
            style={{
              fontSize: 115,
              color: headlineTopColor,
              textShadow: "0 8px 0 #000000, 0 16px 30px rgba(0,0,0,0.9)",
              WebkitTextStroke: "3px #000000",
            }}
          >
            {headlineTop}
          </span>

          {/* Bottom Line (Acid Lime / High-Voltage Accent) */}
          <span
            style={{
              fontSize: 130,
              color: bottomColor,
              textShadow: "0 8px 0 #000000, 0 20px 40px rgba(0,0,0,0.95)",
              WebkitTextStroke: "4px #000000",
            }}
          >
            {headlineBottom}
          </span>
        </div>

        {/* Rubber Stamp Slam Overlay */}
        {accentStamp && (
          <div
            style={{
              alignSelf: "flex-start",
              marginTop: 10,
              border: "5px solid #EF4444",
              color: "#EF4444",
              fontSize: 32,
              fontWeight: 900,
              padding: "6px 20px",
              borderRadius: 8,
              textTransform: "uppercase",
              letterSpacing: 4,
              transform: "rotate(-4deg)",
              backgroundColor: "rgba(0,0,0,0.5)",
              boxShadow: "0 6px 20px rgba(239, 68, 68, 0.4)",
              WebkitTextStroke: "1px #000000",
            }}
          >
            {accentStamp}
          </div>
        )}
      </div>
    </div>
  );
};

