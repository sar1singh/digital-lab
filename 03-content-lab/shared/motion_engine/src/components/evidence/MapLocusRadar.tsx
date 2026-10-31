import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { ChannelId, getChannelTheme } from "../../styles/theme";

export interface POIItem {
  name: string;
  distance: string;
  status: string;
  alert?: boolean;
}

export interface MapLocusRadarProps {
  channel?: ChannelId;
  targetTitle?: string;
  coordinates?: string;
  radiusMiles?: string;
  locationName?: string;
  poiList?: POIItem[];
  footerNote?: string;
}

export const MapLocusRadar: React.FC<MapLocusRadarProps> = ({
  channel = "thinklate",
  targetTitle = "GEOGRAPHIC MONOPOLY ANALYSIS // SAN FRANCISCO",
  coordinates = "LAT 37.7749° N, LON 122.4194° W",
  radiusMiles = "2.4 MILE RADIUS // MOSCONE CENTER",
  locationName = "SAN FRANCISCO DOWNTOWN HOTEL CLUSTER",
  poiList = [
    { name: "Moscone Convention Center", distance: "0.2 mi", status: "SOLD OUT (100%)", alert: true },
    { name: "Union Square Luxury Hotels", distance: "0.5 mi", status: "SURGE: $450/NT", alert: true },
    { name: "Rucker Living Room (Airbed HQ)", distance: "1.1 mi", status: "ONLINE ($80/NT)", alert: false },
    { name: "SFO Airport Perimeter Hotels", distance: "11.4 mi", status: "COMMUTE: 65 MIN", alert: false },
  ],
  footerNote = "SOURCE: SF TRAVEL ASSOCIATION & MUNICIPAL HOTEL OCCUPANCY RECORDS",
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const theme = getChannelTheme(channel);

  // Card spring
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

  // Radar sweep continuous rotation
  const sweepAngle = (frame * 3.5) % 360;

  // Expanding radar pulse waves
  const pulse1 = (frame * 0.03) % 1;
  const pulse2 = ((frame * 0.03) + 0.5) % 1;

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
          width: "1440px",
          backgroundColor: theme.colors.bgGlassDark,
          backdropFilter: "blur(28px)",
          borderRadius: "20px",
          border: `1px solid ${theme.colors.borderGlass}`,
          boxShadow: `${theme.shadows.glass}, 0 0 35px ${theme.colors.borderAccent}`,
          padding: "44px 54px",
          transform: `scale(${cardScale})`,
          opacity,
          display: "flex",
          flexDirection: "column",
          gap: "28px",
        }}
      >
        {/* Header Bar */}
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
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
                marginBottom: "12px",
                fontFamily: theme.fonts.mono,
              }}
            >
              <span>◈ RADAR SCAN</span>
              <span>{targetTitle}</span>
            </div>
            <h2
              style={{
                fontSize: "30px",
                fontWeight: 900,
                color: theme.colors.textWhite,
                margin: 0,
                letterSpacing: "-0.01em",
              }}
            >
              {locationName}
            </h2>
          </div>

          <div
            style={{
              padding: "10px 18px",
              backgroundColor: "rgba(0, 0, 0, 0.4)",
              border: "1px solid rgba(255, 255, 255, 0.12)",
              borderRadius: "8px",
              fontSize: "13px",
              fontFamily: theme.fonts.mono,
              color: theme.colors.accentSecondary,
              textAlign: "right",
            }}
          >
            <div>{coordinates}</div>
            <div style={{ fontSize: "11px", color: theme.colors.textDim, marginTop: "4px" }}>
              {radiusMiles}
            </div>
          </div>
        </div>

        {/* Tactical Radar Display & POI Grid */}
        <div style={{ display: "grid", gridTemplateColumns: "360px 1fr", gap: "36px", alignItems: "center" }}>
          {/* Radar Screen Visualizer */}
          <div
            style={{
              width: "360px",
              height: "360px",
              borderRadius: "50%",
              backgroundColor: "rgba(0, 0, 0, 0.6)",
              border: `2px solid ${theme.colors.borderGlass}`,
              position: "relative",
              overflow: "hidden",
              boxShadow: `inset 0 0 40px rgba(0,0,0,0.8), 0 0 25px ${theme.colors.borderAccent}`,
            }}
          >
            {/* Concentric rings */}
            <div
              style={{
                position: "absolute",
                top: "15%",
                left: "15%",
                width: "70%",
                height: "70%",
                borderRadius: "50%",
                border: "1px dashed rgba(255,255,255,0.18)",
              }}
            />
            <div
              style={{
                position: "absolute",
                top: "32%",
                left: "32%",
                width: "36%",
                height: "36%",
                borderRadius: "50%",
                border: "1px solid rgba(255,255,255,0.25)",
              }}
            />

            {/* Crosshairs */}
            <div
              style={{
                position: "absolute",
                top: 0,
                bottom: 0,
                left: "50%",
                width: "1px",
                backgroundColor: "rgba(255,255,255,0.2)",
              }}
            />
            <div
              style={{
                position: "absolute",
                left: 0,
                right: 0,
                top: "50%",
                height: "1px",
                backgroundColor: "rgba(255,255,255,0.2)",
              }}
            />

            {/* Expanding pulse wave */}
            <div
              style={{
                position: "absolute",
                top: `${50 - (pulse1 * 50)}%`,
                left: `${50 - (pulse1 * 50)}%`,
                width: `${pulse1 * 100}%`,
                height: `${pulse1 * 100}%`,
                borderRadius: "50%",
                border: `1px solid ${theme.colors.accent}`,
                opacity: 1 - pulse1,
              }}
            />

            {/* Rotating radar sweep cone */}
            <div
              style={{
                position: "absolute",
                top: 0,
                left: 0,
                width: "100%",
                height: "100%",
                transform: `rotate(${sweepAngle}deg)`,
                transformOrigin: "50% 50%",
                background: `conic-gradient(from 0deg at 50% 50%, rgba(0,0,0,0) 0deg, rgba(0,0,0,0) 300deg, ${theme.colors.accent}33 345deg, ${theme.colors.accent}88 360deg)`,
              }}
            />

            {/* Center target dot */}
            <div
              style={{
                position: "absolute",
                top: "calc(50% - 6px)",
                left: "calc(50% - 6px)",
                width: "12px",
                height: "12px",
                borderRadius: "50%",
                backgroundColor: theme.colors.accent,
                boxShadow: theme.shadows.glowAccent,
              }}
            />

            {/* Blinking Target Dot (Founders Rug) */}
            <div
              style={{
                position: "absolute",
                top: "65%",
                left: "70%",
                width: "10px",
                height: "10px",
                borderRadius: "50%",
                backgroundColor: theme.colors.accentSecondary,
                boxShadow: theme.shadows.glowSecondary,
                opacity: Math.sin(frame / 4) > 0 ? 1 : 0.3,
              }}
            />
          </div>

          {/* POI Table */}
          <div style={{ display: "flex", flexDirection: "column", gap: "12px" }}>
            {poiList.map((poi, idx) => {
              const rowFrame = 15 + idx * 8;
              const rowSpring = spring({
                frame: Math.max(0, frame - rowFrame),
                fps,
                config: { damping: 12, mass: 0.5, stiffness: 140 },
              });

              return (
                <div
                  key={idx}
                  style={{
                    backgroundColor: "rgba(0, 0, 0, 0.35)",
                    border: `1px solid ${poi.alert ? "rgba(239, 68, 68, 0.35)" : "rgba(255, 255, 255, 0.08)"}`,
                    borderRadius: "10px",
                    padding: "16px 22px",
                    display: "flex",
                    justifyContent: "space-between",
                    alignItems: "center",
                    transform: `translateX(${(1 - rowSpring) * 20}px)`,
                    opacity: interpolate(frame, [rowFrame, rowFrame + 6], [0, 1], { extrapolateRight: "clamp" }),
                  }}
                >
                  <div>
                    <div style={{ fontSize: "16px", fontWeight: 800, color: theme.colors.textWhite }}>
                      {poi.name}
                    </div>
                    <div style={{ fontSize: "13px", color: theme.colors.textDim, marginTop: "2px", fontFamily: theme.fonts.mono }}>
                      DISTANCE: {poi.distance}
                    </div>
                  </div>

                  <div
                    style={{
                      padding: "6px 14px",
                      borderRadius: "6px",
                      fontSize: "12px",
                      fontWeight: 800,
                      fontFamily: theme.fonts.mono,
                      backgroundColor: poi.alert ? "rgba(239, 68, 68, 0.18)" : `${theme.colors.accent}18`,
                      color: poi.alert ? "#EF4444" : theme.colors.accent,
                      border: `1px solid ${poi.alert ? "rgba(239, 68, 68, 0.45)" : theme.colors.borderAccent}`,
                    }}
                  >
                    {poi.status}
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* Footer */}
        <div
          style={{
            borderTop: "1px solid rgba(255, 255, 255, 0.08)",
            paddingTop: "14px",
            fontSize: "12px",
            fontFamily: theme.fonts.mono,
            color: theme.colors.textDim,
          }}
        >
          {footerNote}
        </div>
      </div>
    </div>
  );
};
