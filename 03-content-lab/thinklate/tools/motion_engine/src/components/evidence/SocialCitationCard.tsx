import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { THEME } from "../../styles/theme";

export interface SocialCitationCardProps {
  authorName?: string;
  authorHandle?: string;
  avatarText?: string;
  avatarColor?: string;
  dateStr?: string;
  content: string;
  highlightWords?: string;
  reposts?: string;
  likes?: string;
  views?: string;
  footerNote?: string;
}

export const SocialCitationCard: React.FC<SocialCitationCardProps> = ({
  authorName = "Paul Graham",
  authorHandle = "@paulg",
  avatarText = "PG",
  avatarColor = "#F59E0B",
  dateStr = "11:42 PM · Nov 23, 2008",
  content = "We thought Airbnb was a terrible idea. Who wants to sleep on an air mattress in a stranger's apartment? But we funded them because we loved the founders.",
  highlightWords = "We thought Airbnb was a terrible idea",
  reposts = "14.2K",
  likes = "89.5K",
  views = "4.2M",
  footerNote = "VERIFIED FOUNDER TESTIMONY // PUBLIC CORRESPONDENCE",
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const cardScale = spring({
    frame,
    fps,
    config: { damping: 14, mass: 0.8, stiffness: 100 },
  });

  const opacity = interpolate(frame, [0, 8], [0, 1], { extrapolateRight: "clamp" });

  const highlightProgress = interpolate(frame, [15, 45], [0, 100], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const renderContent = () => {
    if (!highlightWords || !content.includes(highlightWords)) {
      return <span>{content}</span>;
    }
    const [before, after] = content.split(highlightWords);
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
          width: "1280px",
          backgroundColor: THEME.colors.bgGlass,
          backdropFilter: "blur(26px)",
          borderRadius: "24px",
          border: `1px solid rgba(255, 255, 255, 0.16)`,
          boxShadow: THEME.shadows.glass,
          padding: "44px 52px",
          transform: `scale(${cardScale})`,
          opacity,
          display: "flex",
          flexDirection: "column",
          gap: "22px",
          position: "relative",
          overflow: "hidden",
        }}
      >
        {/* Top edge accent */}
        <div style={{ position: "absolute", top: 0, left: "10%", right: "10%", height: "2px", background: `linear-gradient(90deg, transparent, #38BDF8, transparent)` }} />

        {/* User Author Header */}
        <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between" }}>
          <div style={{ display: "flex", alignItems: "center", gap: "16px" }}>
            <div
              style={{
                width: "56px",
                height: "56px",
                borderRadius: "50%",
                backgroundColor: avatarColor,
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                fontFamily: THEME.fonts.mono,
                fontWeight: 900,
                fontSize: "20px",
                color: "#FFFFFF",
                boxShadow: "0 4px 12px rgba(0,0,0,0.4)",
              }}
            >
              {avatarText}
            </div>
            <div>
              <div style={{ display: "flex", alignItems: "center", gap: "8px" }}>
                <span style={{ fontSize: "22px", fontWeight: 800, color: THEME.colors.textWhite }}>
                  {authorName}
                </span>
                {/* Verified badge */}
                <span style={{ color: "#38BDF8", fontSize: "18px" }}>✦</span>
              </div>
              <div style={{ fontFamily: THEME.fonts.mono, fontSize: "14px", color: THEME.colors.textDim }}>
                {authorHandle}
              </div>
            </div>
          </div>

          <div style={{ fontFamily: THEME.fonts.mono, fontSize: "22px", color: THEME.colors.textDim, fontWeight: 900 }}>
            𝕏
          </div>
        </div>

        {/* Tweet Body */}
        <div style={{ fontSize: "28px", lineHeight: 1.45, color: THEME.colors.textWhite, fontWeight: 500 }}>
          {renderContent()}
        </div>

        {/* Timestamp */}
        <div style={{ fontFamily: THEME.fonts.mono, fontSize: "14px", color: THEME.colors.textDim, borderBottom: "1px solid rgba(255, 255, 255, 0.08)", paddingBottom: "14px" }}>
          {dateStr}
        </div>

        {/* Metrics Row */}
        <div style={{ display: "flex", gap: "36px", fontFamily: THEME.fonts.mono, fontSize: "15px", color: THEME.colors.textMuted }}>
          <div><strong style={{ color: THEME.colors.textWhite }}>{reposts}</strong> Reposts</div>
          <div><strong style={{ color: THEME.colors.textWhite }}>{likes}</strong> Likes</div>
          <div><strong style={{ color: THEME.colors.textWhite }}>{views}</strong> Views</div>
        </div>

        {/* Footer */}
        {footerNote && (
          <div style={{ display: "flex", justifyContent: "space-between", fontFamily: THEME.fonts.mono, fontSize: "12px", color: THEME.colors.textDim, borderTop: "1px solid rgba(255, 255, 255, 0.08)", paddingTop: "12px" }}>
            <span>{footerNote}</span>
            <span style={{ color: "#38BDF8" }}>AUTHENTICATED POST</span>
          </div>
        )}
      </div>
    </div>
  );
};
