import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { ChannelId, getChannelTheme } from "../../styles/theme";

export interface PhotoPolaroidPinProps {
  channel?: ChannelId;
  photoUrl?: string;
  exhibitBadge?: string;
  title?: string;
  handwrittenNote?: string;
  dateStr?: string;
  stampText?: string;
  tiltDeg?: number;
}

export const PhotoPolaroidPin: React.FC<PhotoPolaroidPinProps> = ({
  channel = "thinklate",
  photoUrl = "",
  exhibitBadge = "EVIDENCE ARCHIVE // EXHIBIT #104",
  title = "THE ORIGINAL 3 AIR MATTRESSES ON LIVING ROOM RUG",
  handwrittenNote = "\"Took photo before first 3 design conference guests arrived. $80 cash in envelope.\" - Joe",
  dateStr = "OCTOBER 19, 2007",
  stampText = "AUTHENTICATED RECORD",
  tiltDeg = -2.5,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const theme = getChannelTheme(channel);

  // Layer 1: Polaroid drop spring
  const dropSpring = spring({
    frame,
    fps,
    config: { damping: 11, mass: 0.9, stiffness: 95 },
  });
  const translateY = (1 - dropSpring) * -120;
  const currentTilt = tiltDeg + Math.sin(frame / 14) * 0.4;

  // Layer 2: Tape / pin slam
  const tapeSlam = spring({
    frame: Math.max(0, frame - 8),
    fps,
    config: { damping: 8, mass: 0.4, stiffness: 180 },
  });

  // Layer 3: Forensic Stamp slam at frame 26
  const stampSpring = spring({
    frame: Math.max(0, frame - 26),
    fps,
    config: { damping: 9, mass: 0.5, stiffness: 200 },
  });
  const stampOpacity = interpolate(frame, [26, 30], [0, 1], { extrapolateRight: "clamp" });

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
          width: "920px",
          backgroundColor: "#F8FAFC",
          borderRadius: "8px",
          padding: "26px 26px 36px 26px",
          boxShadow: "0 30px 80px rgba(0, 0, 0, 0.65), 0 0 0 1px rgba(0, 0, 0, 0.1)",
          transform: `translateY(${translateY}px) rotate(${currentTilt}deg) scale(${dropSpring})`,
          position: "relative",
        }}
      >
        {/* Scotch Tape Graphic at Top */}
        <div
          style={{
            position: "absolute",
            top: "-18px",
            left: "calc(50% - 70px)",
            width: "140px",
            height: "36px",
            backgroundColor: "rgba(255, 255, 230, 0.72)",
            border: "1px dashed rgba(200, 200, 150, 0.5)",
            boxShadow: "0 4px 10px rgba(0, 0, 0, 0.15)",
            transform: `scale(${tapeSlam}) rotate(1.2deg)`,
            zIndex: 20,
          }}
        />

        {/* Photo Container */}
        <div
          style={{
            width: "100%",
            height: "480px",
            backgroundColor: "#0B0F19",
            borderRadius: "4px",
            overflow: "hidden",
            position: "relative",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            border: "1px solid rgba(0, 0, 0, 0.15)",
          }}
        >
          {photoUrl ? (
            <img
              src={photoUrl}
              alt={title}
              style={{ width: "100%", height: "100%", objectFit: "cover" }}
            />
          ) : (
            <div
              style={{
                width: "100%",
                height: "100%",
                background: "linear-gradient(135deg, #111827 0%, #1F2937 50%, #0F172A 100%)",
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                justifyContent: "center",
                gap: "14px",
                padding: "30px",
                textAlign: "center",
              }}
            >
              <div
                style={{
                  fontSize: "48px",
                  color: theme.colors.accent,
                }}
              >
                📸
              </div>
              <div
                style={{
                  fontSize: "20px",
                  fontWeight: 800,
                  color: "#F8FAFC",
                  letterSpacing: "-0.01em",
                }}
              >
                {title}
              </div>
              <div
                style={{
                  fontSize: "13px",
                  color: "#94A3B8",
                  fontFamily: theme.fonts.mono,
                  letterSpacing: "0.08em",
                }}
              >
                {exhibitBadge}
              </div>
            </div>
          )}

          {/* Red Forensic Stamp Slammed Over Image */}
          <div
            style={{
              position: "absolute",
              bottom: "24px",
              right: "32px",
              padding: "8px 20px",
              border: "4px solid #DC2626",
              borderRadius: "8px",
              color: "#DC2626",
              fontSize: "18px",
              fontWeight: 900,
              letterSpacing: "0.15em",
              textTransform: "uppercase",
              fontFamily: theme.fonts.mono,
              transform: `scale(${stampSpring}) rotate(-12deg)`,
              opacity: stampOpacity,
              backgroundColor: "rgba(255, 255, 255, 0.85)",
              boxShadow: "0 6px 15px rgba(220, 38, 38, 0.25)",
              zIndex: 15,
            }}
          >
            {stampText}
          </div>
        </div>

        {/* Polaroid Handwritten Caption Bottom Area */}
        <div
          style={{
            padding: "24px 10px 0 10px",
            display: "flex",
            justifyContent: "space-between",
            alignItems: "flex-end",
          }}
        >
          <div style={{ maxWidth: "680px" }}>
            <div
              style={{
                fontFamily: '"Caveat", "Comic Sans MS", "Bradley Hand", cursive, sans-serif',
                fontSize: "24px",
                color: "#1E293B",
                fontWeight: 600,
                lineHeight: 1.3,
              }}
            >
              {handwrittenNote}
            </div>
            <div
              style={{
                fontSize: "11px",
                fontFamily: theme.fonts.mono,
                color: "#64748B",
                marginTop: "8px",
                letterSpacing: "0.05em",
              }}
            >
              {exhibitBadge}
            </div>
          </div>

          <div
            style={{
              fontSize: "13px",
              fontWeight: 800,
              fontFamily: theme.fonts.mono,
              color: "#0F172A",
              letterSpacing: "0.08em",
              padding: "6px 12px",
              backgroundColor: "rgba(0, 0, 0, 0.05)",
              borderRadius: "4px",
            }}
          >
            {dateStr}
          </div>
        </div>
      </div>
    </div>
  );
};
