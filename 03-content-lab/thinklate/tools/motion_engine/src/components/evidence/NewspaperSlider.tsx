import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { THEME } from "../../styles/theme";

export interface NewspaperSliderProps {
  badgeText?: string;
  beforeMasthead?: string;
  beforeDate?: string;
  beforeHeadline?: string;
  beforeExcerpt?: string;
  afterMasthead?: string;
  afterDate?: string;
  afterHeadline?: string;
  afterExcerpt?: string;
  footerNote?: string;
}

export const NewspaperSlider: React.FC<NewspaperSliderProps> = ({
  badgeText = "HISTORICAL FORENSICS // ARCHIVE SLIDER",
  beforeMasthead = "THE SAN FRANCISCO CHRONICLE",
  beforeDate = "OCTOBER 1999",
  beforeHeadline = "Hotels Lock In Record High Rates As Room Capacity Hits Complete Drought",
  beforeExcerpt = "City officials warn tourists and convention attendees that standard lodging is completely exhausted, leaving zero alternatives for travelers.",
  afterMasthead = "THE WALL STREET JOURNAL",
  afterDate = "DECEMBER 2020",
  afterHeadline = "Airbnb Hits $100 Billion Valuation in Blockbuster Public Market Debut",
  afterExcerpt = "A pair of broke art school roommates who rented three air mattresses on their living room floor now control a platform larger than the top three hotel chains combined.",
  footerNote = "CHRONICLED TRANSFORMATION // 2007-2024 REGULATORY ARCHIVE",
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const cardScale = spring({
    frame,
    fps,
    config: { damping: 14, mass: 0.8, stiffness: 100 },
  });

  const opacity = interpolate(frame, [0, 8], [0, 1], { extrapolateRight: "clamp" });

  // Slider animation: sweeps from 25% to 75% then settles at 50%
  const sliderSpring = spring({
    frame: Math.max(0, frame - 15),
    fps,
    config: { damping: 14, mass: 0.9, stiffness: 90 },
  });

  const sliderPct = interpolate(sliderSpring, [0, 1], [20, 50]);

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
          width: "1440px",
          height: "640px",
          backgroundColor: THEME.colors.bgGlassDark,
          backdropFilter: "blur(26px)",
          borderRadius: "24px",
          border: `1px solid ${THEME.colors.borderGlass}`,
          boxShadow: THEME.shadows.glass,
          transform: `scale(${cardScale})`,
          opacity,
          position: "relative",
          overflow: "hidden",
          display: "flex",
          flexDirection: "column",
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
            background: `linear-gradient(90deg, ${THEME.colors.crimsonRed}, ${THEME.colors.acidLime})`,
            zIndex: 20,
          }}
        />

        {/* Floating Top Badge */}
        <div
          style={{
            padding: "20px 36px 12px 36px",
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
            borderBottom: "1px solid rgba(255, 255, 255, 0.08)",
            zIndex: 15,
          }}
        >
          <div style={{ fontFamily: THEME.fonts.mono, fontSize: "12px", fontWeight: 700, color: THEME.colors.acidLime, letterSpacing: "0.2em" }}>
            ✦ {badgeText}
          </div>
          <div style={{ fontFamily: THEME.fonts.mono, fontSize: "12px", color: THEME.colors.textDim, letterSpacing: "0.15em" }}>
            BEFORE // AFTER SLIDER
          </div>
        </div>

        {/* Slider Body Container */}
        <div style={{ position: "relative", flex: 1, overflow: "hidden" }}>
          
          {/* ================= AFTER LAYER (Full right side / underneath) ================= */}
          <div
            style={{
              position: "absolute",
              top: 0,
              left: 0,
              right: 0,
              bottom: 0,
              padding: "36px 56px",
              display: "flex",
              flexDirection: "column",
              justifyContent: "space-between",
              backgroundColor: "rgba(10, 15, 26, 0.75)",
            }}
          >
            <div>
              <div style={{ display: "flex", justifyContent: "space-between", borderBottom: `2px solid ${THEME.colors.acidLime}`, paddingBottom: "10px", marginBottom: "16px" }}>
                <span style={{ fontFamily: "Georgia, serif", fontSize: "20px", fontWeight: 900, letterSpacing: "0.08em", color: THEME.colors.textWhite }}>
                  {afterMasthead}
                </span>
                <span style={{ fontFamily: THEME.fonts.mono, fontSize: "12px", color: THEME.colors.acidLime, fontWeight: 700 }}>
                  AFTER: {afterDate}
                </span>
              </div>
              <h1 style={{ fontFamily: "Georgia, serif", fontSize: "38px", fontWeight: 900, lineHeight: 1.18, color: THEME.colors.acidLime, margin: "0 0 16px 0", letterSpacing: "-0.02em" }}>
                {afterHeadline}
              </h1>
              <p style={{ fontSize: "18px", lineHeight: 1.5, color: THEME.colors.textMuted, margin: 0 }}>
                {afterExcerpt}
              </p>
            </div>
            <div style={{ fontFamily: THEME.fonts.mono, fontSize: "12px", color: THEME.colors.textDim, borderTop: "1px solid rgba(255,255,255,0.08)", paddingTop: "10px" }}>
              DISRUPTION REALIZED ✦ GLOBAL REPOSITORY ARCHIVE
            </div>
          </div>

          {/* ================= BEFORE LAYER (Clipped via Slider width) ================= */}
          <div
            style={{
              position: "absolute",
              top: 0,
              left: 0,
              bottom: 0,
              width: `${sliderPct}%`,
              overflow: "hidden",
              borderRight: `3px solid ${THEME.colors.acidLime}`,
              backgroundColor: "rgba(18, 10, 14, 0.92)",
              zIndex: 10,
              boxShadow: "10px 0 30px rgba(0,0,0,0.8)",
            }}
          >
            {/* Inner container forced to exact card width so layout never distorts */}
            <div
              style={{
                width: "1440px",
                height: "100%",
                padding: "36px 56px",
                display: "flex",
                flexDirection: "column",
                justifyContent: "space-between",
              }}
            >
              <div>
                <div style={{ display: "flex", justifyContent: "space-between", width: "1328px", borderBottom: `2px solid ${THEME.colors.crimsonRed}`, paddingBottom: "10px", marginBottom: "16px" }}>
                  <span style={{ fontFamily: "Georgia, serif", fontSize: "20px", fontWeight: 900, letterSpacing: "0.08em", color: THEME.colors.textWhite }}>
                    {beforeMasthead}
                  </span>
                  <span style={{ fontFamily: THEME.fonts.mono, fontSize: "12px", color: THEME.colors.crimsonRed, fontWeight: 700 }}>
                    BEFORE: {beforeDate}
                  </span>
                </div>
                <h1 style={{ fontFamily: "Georgia, serif", fontSize: "38px", fontWeight: 900, lineHeight: 1.18, color: "#E2E8F0", margin: "0 0 16px 0", letterSpacing: "-0.02em", width: "1300px" }}>
                  {beforeHeadline}
                </h1>
                <p style={{ fontSize: "18px", lineHeight: 1.5, color: THEME.colors.textDim, margin: 0, width: "1250px" }}>
                  {beforeExcerpt}
                </p>
              </div>
              <div style={{ fontFamily: THEME.fonts.mono, fontSize: "12px", color: THEME.colors.textDim, borderTop: "1px solid rgba(255,255,255,0.08)", paddingTop: "10px", width: "1328px" }}>
                LEGACY MONOPOLY ARCHIVE ✦ HISTORICAL EVIDENCE
              </div>
            </div>
          </div>

          {/* ================= SLIDER HANDLE BUTTON ================= */}
          <div
            style={{
              position: "absolute",
              top: 0,
              bottom: 0,
              left: `${sliderPct}%`,
              transform: "translateX(-50%)",
              zIndex: 15,
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              pointerEvents: "none",
            }}
          >
            <div
              style={{
                width: "44px",
                height: "44px",
                borderRadius: "50%",
                backgroundColor: THEME.colors.acidLime,
                color: "#05080F",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                fontWeight: 900,
                fontSize: "18px",
                boxShadow: THEME.shadows.glowLime,
              }}
            >
              ↔
            </div>
          </div>

        </div>

        {/* Footer */}
        {footerNote && (
          <div
            style={{
              padding: "12px 36px",
              borderTop: "1px solid rgba(255, 255, 255, 0.08)",
              fontFamily: THEME.fonts.mono,
              fontSize: "12px",
              color: THEME.colors.textDim,
              display: "flex",
              justifyContent: "space-between",
              zIndex: 15,
            }}
          >
            <span>{footerNote}</span>
            <span style={{ color: THEME.colors.acidLime }}>VERIFIED TIMELINE</span>
          </div>
        )}
      </div>
    </div>
  );
};
