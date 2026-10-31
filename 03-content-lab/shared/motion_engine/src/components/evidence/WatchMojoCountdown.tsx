import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { ChannelId, getChannelTheme } from "../../styles/theme";
import { Trophy, Flame, Zap, TrendingUp, AlertTriangle, Star } from "lucide-react";

export interface WatchMojoCountdownProps {
  channel?: ChannelId;
  rank?: string;
  title?: string;
  subtitle?: string;
  category?: string;
  iconName?: "trophy" | "flame" | "zap" | "trending" | "alert" | "star";
  statHighlight?: string;
}

export const WatchMojoCountdown: React.FC<WatchMojoCountdownProps> = ({
  channel = "thinklate",
  rank = "#01",
  title = "THE ASSET-LIGHT ARBITRAGE",
  subtitle = "AIRBNB DEFEATS THE 100-YEAR HOTEL CARTEL",
  category = "GREATEST MARKET DISRUPTIONS OF ALL TIME",
  iconName = "trophy",
  statHighlight = "416X CAPITAL EFFICIENCY",
}) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();
  const theme = getChannelTheme(channel);
  const accent = theme.colors.accent;
  const accentSecondary = theme.colors.accentSecondary;

  // Entrance spring for rank badge
  const badgeSpring = spring({
    frame,
    fps,
    config: { damping: 12, mass: 0.7, stiffness: 130 },
  });

  // Lower third width expansion (frames 10 to 35)
  const barExpansion = interpolate(frame, [10, 35], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Text fade-in after banner expands
  const textFade = interpolate(frame, [25, 42], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Countdown timer / progress bar across the entire duration
  const progressPercent = interpolate(frame, [0, durationInFrames], [100, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Render Lucide Icon
  const renderIcon = () => {
    const iconProps = { size: 28, color: accent, strokeWidth: 2.2 };
    switch (iconName) {
      case "flame":
        return <Flame {...iconProps} />;
      case "zap":
        return <Zap {...iconProps} />;
      case "trending":
        return <TrendingUp {...iconProps} />;
      case "alert":
        return <AlertTriangle {...iconProps} />;
      case "star":
        return <Star {...iconProps} />;
      case "trophy":
      default:
        return <Trophy {...iconProps} />;
    }
  };

  return (
    <div
      style={{
        position: "absolute",
        bottom: 80,
        left: 100,
        display: "flex",
        alignItems: "flex-end",
        fontFamily: theme.fonts.mono,
        zIndex: 50,
      }}
    >
      {/* 1. Large High-Voltage Rank Number Badge (Left Anchor) */}
      <div
        style={{
          transform: `scale(${badgeSpring})`,
          transformOrigin: "bottom left",
          backgroundColor: "#0A0D14",
          border: `3px solid ${accent}`,
          boxShadow: `0 0 35px ${accent}40`,
          borderRadius: 8,
          width: 140,
          height: 140,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
          position: "relative",
          zIndex: 2,
        }}
      >
        <div style={{ marginBottom: 4 }}>{renderIcon()}</div>
        <span
          style={{
            fontFamily: theme.fonts.display,
            fontSize: 54,
            fontWeight: 900,
            color: accent,
            lineHeight: 1,
            letterSpacing: -1,
          }}
        >
          {rank}
        </span>
        <div
          style={{
            fontSize: 9,
            fontWeight: 800,
            letterSpacing: 2,
            color: "rgba(255,255,255,0.7)",
            marginTop: 4,
          }}
        >
          RANKING
        </div>
      </div>

      {/* 2. Expanding Broadcast Lower-Third Content Banner */}
      <div
        style={{
          marginLeft: -10,
          width: `${barExpansion * 820}px`,
          height: 120,
          overflow: "hidden",
          backgroundColor: "rgba(10, 15, 26, 0.92)",
          backdropFilter: "blur(20px)",
          borderTop: "2px solid rgba(255, 255, 255, 0.15)",
          borderRight: `3px solid ${accentSecondary}`,
          borderBottom: "2px solid rgba(255, 255, 255, 0.15)",
          borderRadius: "0 10px 10px 0",
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          paddingLeft: 36,
          paddingRight: 28,
          position: "relative",
          boxShadow: "0 15px 35px rgba(0, 0, 0, 0.6)",
        }}
      >
        {/* Top Tag & Category */}
        <div
          style={{
            opacity: textFade,
            display: "flex",
            alignItems: "center",
            gap: 12,
            marginBottom: 6,
          }}
        >
          <span
            style={{
              fontSize: 10,
              fontWeight: 900,
              letterSpacing: 2,
              color: accent,
              textTransform: "uppercase",
            }}
          >
            {category}
          </span>
          {statHighlight && (
            <span
              style={{
                fontSize: 10,
                fontWeight: 800,
                backgroundColor: `${accentSecondary}25`,
                color: accentSecondary,
                padding: "2px 8px",
                borderRadius: 4,
                border: `1px solid ${accentSecondary}50`,
              }}
            >
              {statHighlight}
            </span>
          )}
        </div>

        {/* Big Bold Entry Title */}
        <div
          style={{
            opacity: textFade,
            fontFamily: theme.fonts.display,
            fontSize: 26,
            fontWeight: 900,
            color: "#FFFFFF",
            letterSpacing: 0.5,
            whiteSpace: "nowrap",
            overflow: "hidden",
            textOverflow: "ellipsis",
            textTransform: "uppercase",
          }}
        >
          {title}
        </div>

        {/* Subtitle / Context Note */}
        <div
          style={{
            opacity: textFade,
            fontSize: 12,
            fontWeight: 500,
            color: "rgba(255, 255, 255, 0.65)",
            letterSpacing: 0.2,
            whiteSpace: "nowrap",
            overflow: "hidden",
            textOverflow: "ellipsis",
            marginTop: 4,
          }}
        >
          {subtitle}
        </div>

        {/* Bottom Ticking Progress Bar */}
        <div
          style={{
            position: "absolute",
            bottom: 0,
            left: 0,
            height: 3,
            width: `${progressPercent}%`,
            backgroundColor: accent,
            boxShadow: `0 0 10px ${accent}`,
          }}
        />
      </div>
    </div>
  );
};
