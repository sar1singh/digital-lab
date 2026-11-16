import React from "react";
import { ChannelId, getChannelTheme } from "../../styles/theme";
import { SVG_CONCEPT_A, SVG_CONCEPT_B, SVG_CONCEPT_C } from "./thumbnailVectors";

export interface ThumbnailStudioProps {
  conceptPreset?: "concept_a_center_focal_point" | "concept_b_asymmetric_rule_of_thirds" | "concept_c_minimalist_hero_object" | "custom";
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
  conceptPreset = "custom",
  channel = "thinklate",
  style = "nitish_drama",
  headlineTop = "THE $300",
  headlineBottom = "CHORE",
  headlineTopColor = "#FFFFFF",
  headlineBottomColor,
  badgeText = "VACATION EXPOSÉ",
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
  // If a preset vector concept is selected, render it directly
  if (conceptPreset === "concept_a_center_focal_point") {
    return (
      <div
        style={{ width: 1920, height: 1080, overflow: "hidden", backgroundColor: "#060910" }}
        dangerouslySetInnerHTML={{ __html: SVG_CONCEPT_A }}
      />
    );
  }

  if (conceptPreset === "concept_b_asymmetric_rule_of_thirds") {
    return (
      <div
        style={{ width: 1920, height: 1080, overflow: "hidden", backgroundColor: "#060910" }}
        dangerouslySetInnerHTML={{ __html: SVG_CONCEPT_B }}
      />
    );
  }

  if (conceptPreset === "concept_c_minimalist_hero_object") {
    return (
      <div
        style={{ width: 1920, height: 1080, overflow: "hidden", backgroundColor: "#060910" }}
        dangerouslySetInnerHTML={{ __html: SVG_CONCEPT_C }}
      />
    );
  }

  const theme = getChannelTheme(channel);
  const bottomColor = headlineBottomColor || theme.colors.accent;

  // Background styling (1920x1080)
  const defaultGradient = style === "magnates_brand"
    ? "radial-gradient(circle at 65% 50%, #B50543 0%, #4D011B 70%, #0A0206 100%)"
    : style === "vox_forensic"
    ? "radial-gradient(circle at 50% 50%, #1E293B 0%, #0F172A 70%, #04060B 100%)"
    : "radial-gradient(circle at 25% 40%, #7F1D1D 0%, #200407 60%, #060910 100%)";

  const effectiveBg = bgImageUrl
    ? `linear-gradient(rgba(10, 15, 26, 0.4), rgba(10, 15, 26, 0.85)), url(${bgImageUrl}) center/cover no-repeat`
    : (bgGradient || defaultGradient);

  return (
    <div
      style={{
        position: "relative",
        width: 1920,
        height: 1080,
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
          border: `6px solid ${theme.colors.accent}`,
          boxShadow: `inset 0 0 60px rgba(0,0,0,0.85), 0 0 40px ${theme.colors.accent}60`,
          pointerEvents: "none",
          zIndex: 50,
        }}
      />

      {/* 2. Top Banner Headline (Rule 15 Compliant - Top Center) */}
      <div
        style={{
          position: "absolute",
          top: 45,
          left: 0,
          right: 0,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          gap: 12,
          zIndex: 40,
        }}
      >
        {badgeText && (
          <div
            style={{
              backgroundColor: badgeColor,
              color: "#FFFFFF",
              fontSize: 22,
              fontWeight: 900,
              letterSpacing: "3px",
              padding: "10px 32px",
              borderRadius: 8,
              textTransform: "uppercase",
              boxShadow: "0 8px 24px rgba(0,0,0,0.7)",
              border: "2px solid #000000",
            }}
          >
            {badgeText}
          </div>
        )}

        <div
          style={{
            display: "flex",
            flexDirection: "row",
            gap: 20,
            textTransform: "uppercase",
            fontFamily: "'Montserrat', 'Impact', 'Arial Black', sans-serif",
            letterSpacing: "-1px",
            lineHeight: 1,
          }}
        >
          <span
            style={{
              fontSize: 124,
              fontWeight: 900,
              color: headlineTopColor,
              textShadow: "0 14px 0 #000000, 0 24px 40px rgba(0,0,0,0.95)",
              WebkitTextStroke: "4px #000000",
            }}
          >
            {headlineTop}
          </span>
          <span
            style={{
              fontSize: 124,
              fontWeight: 900,
              color: bottomColor,
              textShadow: "0 14px 0 #000000, 0 24px 40px rgba(0,0,0,0.95)",
              WebkitTextStroke: "4px #000000",
            }}
          >
            {headlineBottom}
          </span>
        </div>
      </div>

      {/* 3. Style-Specific Visual Layout */}
      {/* MAGNATES STYLE */}
      {style === "magnates_brand" && (
        <>
          <div
            style={{
              position: "absolute",
              right: 120,
              top: 240,
              width: 580,
              height: 580,
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              filter: `drop-shadow(0 30px 60px rgba(0,0,0,0.8)) drop-shadow(0 0 80px ${theme.colors.accent}70)`,
              zIndex: 10,
            }}
          >
            {brandLogoType === "airbnb" && (
              <svg viewBox="0 0 100 115" width="500" height="550" fill="none" stroke="#FFFFFF" strokeWidth="9" strokeLinecap="round" strokeLinejoin="round">
                <path d="M50 8 C38 8 28 20 28 35 C28 60 12 75 8 92 C4 105 15 110 28 110 C38 110 46 102 50 92 C54 102 62 110 72 110 C85 110 96 105 92 92 C88 75 72 60 72 35 C72 20 62 8 50 8 Z" />
                <circle cx="50" cy="48" r="14" stroke="#FFFFFF" strokeWidth="8" />
              </svg>
            )}
            {brandLogoType === "dollar" && (
              <div style={{ fontSize: 440, fontWeight: 900, color: "#FFFFFF", textShadow: "0 15px 50px rgba(0,0,0,0.95)" }}>
                $
              </div>
            )}
          </div>

          <div
            style={{
              position: "absolute",
              bottom: 60,
              left: 100,
              display: "flex",
              gap: 28,
              zIndex: 20,
            }}
          >
            {statPins.map((pin, i) => (
              <div
                key={i}
                style={{
                  backgroundColor: "#FFFFFF",
                  color: "#080C14",
                  padding: "16px 32px",
                  borderRadius: 28,
                  boxShadow: "0 16px 35px rgba(0,0,0,0.7)",
                  display: "flex",
                  flexDirection: "column",
                  alignItems: "center",
                  border: "3px solid #000000",
                }}
              >
                <span style={{ fontSize: 16, fontWeight: 800, letterSpacing: "1.5px", color: "#64748B" }}>
                  {pin.label}
                </span>
                <span style={{ fontSize: 36, fontWeight: 900, color: "#DC2626" }}>
                  {pin.value}
                </span>
              </div>
            ))}
          </div>
        </>
      )}

      {/* NITISH / DRAMA STYLE */}
      {style === "nitish_drama" && (
        <div
          style={{
            position: "absolute",
            right: 80,
            bottom: 0,
            width: 720,
            height: 840,
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
                filter: `drop-shadow(0 0 35px ${subjectRimColor}) drop-shadow(0 25px 50px rgba(0,0,0,0.95)) contrast(1.15) brightness(1.05)`,
              }}
            />
          ) : (
            <div
              style={{
                width: 580,
                height: 720,
                background: `linear-gradient(180deg, ${subjectRimColor}40 0%, #0F172A 100%)`,
                borderRadius: "260px 260px 0 0",
                border: `6px solid ${subjectRimColor}`,
                boxShadow: `0 0 60px ${subjectRimColor}60, 0 40px 80px rgba(0,0,0,0.9)`,
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                justifyContent: "center",
                padding: 40,
                boxSizing: "border-box",
              }}
            >
              <span style={{ fontSize: 24, fontWeight: 900, color: subjectRimColor, letterSpacing: 2, marginBottom: 16 }}>
                2D VECTOR SUBJECT
              </span>
              <span style={{ fontSize: 16, color: "#94A3B8", textAlign: "center" }}>
                (Infographics Show 2.0 / Kurzgesagt Flat Cel-Shaded)
              </span>
            </div>
          )}
        </div>
      )}

      {accentStamp && (
        <div
          style={{
            position: "absolute",
            left: 100,
            bottom: 120,
            border: "6px solid #EF4444",
            color: "#EF4444",
            fontSize: 42,
            fontWeight: 900,
            padding: "8px 28px",
            borderRadius: 10,
            textTransform: "uppercase",
            letterSpacing: 4,
            transform: "rotate(-6deg)",
            backgroundColor: "rgba(0,0,0,0.7)",
            boxShadow: "0 8px 30px rgba(239, 68, 68, 0.5)",
            WebkitTextStroke: "2px #000000",
            zIndex: 35,
          }}
        >
          {accentStamp}
        </div>
      )}
    </div>
  );
};
