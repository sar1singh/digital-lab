import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { ChannelId, getChannelTheme } from "../../styles/theme";

export interface AudioWaveformCardProps {
  channel?: ChannelId;
  speakerTag?: string;
  speakerName?: string;
  audioTitle?: string;
  durationStr?: string;
  transcriptSnippet?: string;
  highlightWords?: string;
  barsCount?: number;
}

export const AudioWaveformCard: React.FC<AudioWaveformCardProps> = ({
  channel = "thinklate",
  speakerTag = "LEAKED BOARDROOM AUDIO // SAN FRANCISCO",
  speakerName = "INVESTOR / HOTEL LOBBYIST RECORDING",
  audioTitle = "WIRETAP #891: 'NOBODY WANTS TO SLEEP ON AN AIRBED'",
  durationStr = "00:14 / 01:30",
  transcriptSnippet = "They think they can replace a Hilton with a $20 air mattress? Let them burn through their seed money. It will die in six weeks.",
  highlightWords = "Let them burn through their seed money",
  barsCount = 38,
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

  // Playhead scrubber progress (0% to 100% across 120 frames)
  const scrubberProgress = interpolate(frame, [10, 110], [0, 100], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Split transcript words for progressive reveal
  const words = transcriptSnippet.split(" ");
  const activeWordIndex = Math.min(
    words.length - 1,
    Math.floor(interpolate(frame, [15, 105], [0, words.length], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }))
  );

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
          width: "1380px",
          backgroundColor: theme.colors.bgGlassDark,
          backdropFilter: "blur(28px)",
          borderRadius: "20px",
          border: `1px solid ${theme.colors.borderGlass}`,
          boxShadow: `${theme.shadows.glass}, 0 0 35px ${theme.colors.borderAccent}`,
          padding: "44px 56px",
          transform: `scale(${cardScale})`,
          opacity,
          display: "flex",
          flexDirection: "column",
          gap: "24px",
        }}
      >
        {/* Header & Speaker Info */}
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
          <div>
            <div
              style={{
                display: "inline-flex",
                alignItems: "center",
                gap: "8px",
                padding: "5px 12px",
                borderRadius: "6px",
                backgroundColor: "rgba(239, 68, 68, 0.15)",
                border: "1px solid rgba(239, 68, 68, 0.45)",
                fontSize: "12px",
                fontWeight: 800,
                letterSpacing: "0.08em",
                color: "#EF4444",
                marginBottom: "10px",
                fontFamily: theme.fonts.mono,
              }}
            >
              <span style={{ animation: "pulse 1s infinite" }}>● REC</span>
              <span>{speakerTag}</span>
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
              {audioTitle}
            </h2>
            <div style={{ fontSize: "14px", color: theme.colors.textDim, marginTop: "4px" }}>
              {speakerName}
            </div>
          </div>

          <div
            style={{
              padding: "10px 18px",
              backgroundColor: "rgba(255, 255, 255, 0.06)",
              border: "1px solid rgba(255, 255, 255, 0.12)",
              borderRadius: "8px",
              fontSize: "14px",
              fontFamily: theme.fonts.mono,
              color: theme.colors.accent,
              fontWeight: 700,
            }}
          >
            {durationStr}
          </div>
        </div>

        {/* Live Dynamic Waveform Visualizer */}
        <div
          style={{
            height: "90px",
            backgroundColor: "rgba(0, 0, 0, 0.35)",
            borderRadius: "12px",
            border: "1px solid rgba(255, 255, 255, 0.08)",
            padding: "0 24px",
            display: "flex",
            alignItems: "center",
            justifyContent: "space-between",
            position: "relative",
            overflow: "hidden",
          }}
        >
          {/* Scrubber vertical bar */}
          <div
            style={{
              position: "absolute",
              top: 0,
              bottom: 0,
              left: `${scrubberProgress}%`,
              width: "2px",
              backgroundColor: theme.colors.textWhite,
              boxShadow: `0 0 10px ${theme.colors.accent}`,
              zIndex: 10,
            }}
          />

          {Array.from({ length: barsCount }).map((_, i) => {
            // Harmonic sine calculation for organic voice fluctuating wave
            const barFraction = i / barsCount;
            const isPast = barFraction * 100 <= scrubberProgress;
            const wave1 = Math.sin(frame * 0.28 + i * 0.45);
            const wave2 = Math.cos(frame * 0.18 + i * 0.25);
            const amplitude = Math.abs(wave1 * 0.6 + wave2 * 0.4);
            const barHeight = Math.max(12, Math.round(amplitude * 65));

            return (
              <div
                key={i}
                style={{
                  width: "12px",
                  height: `${barHeight}px`,
                  borderRadius: "6px",
                  backgroundColor: isPast ? theme.colors.accent : "rgba(255, 255, 255, 0.22)",
                  boxShadow: isPast ? theme.shadows.glowAccent : "none",
                  transition: "height 0.05s ease",
                }}
              />
            );
          })}
        </div>

        {/* Live Synchronized Transcript Box */}
        <div
          style={{
            backgroundColor: "rgba(0, 0, 0, 0.25)",
            border: `1px solid rgba(255, 255, 255, 0.08)`,
            borderRadius: "12px",
            padding: "22px 28px",
            fontSize: "22px",
            lineHeight: 1.5,
            color: theme.colors.textMuted,
          }}
        >
          <span style={{ color: theme.colors.accentSecondary, fontWeight: 800, marginRight: "12px" }}>
            TRANSCRIPTION:
          </span>
          {words.map((word, wIdx) => {
            const isSpoken = wIdx <= activeWordIndex;
            const cleanWord = word.replace(/[^a-zA-Z]/g, "").toLowerCase();
            const isTargetHighlight = highlightWords.toLowerCase().includes(cleanWord);

            return (
              <span
                key={wIdx}
                style={{
                  marginRight: "7px",
                  color: isSpoken
                    ? isTargetHighlight
                      ? theme.colors.accent
                      : theme.colors.textWhite
                    : "rgba(255, 255, 255, 0.28)",
                  fontWeight: isTargetHighlight && isSpoken ? 800 : 500,
                  textDecoration: isTargetHighlight && isSpoken ? "underline" : "none",
                  textDecorationColor: theme.colors.accent,
                  transition: "color 0.1s ease",
                }}
              >
                {word}
              </span>
            );
          })}
        </div>
      </div>
    </div>
  );
};
