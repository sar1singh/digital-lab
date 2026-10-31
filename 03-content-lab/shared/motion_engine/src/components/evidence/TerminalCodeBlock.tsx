import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { ChannelId, getChannelTheme } from "../../styles/theme";

export interface TerminalOutputLine {
  text: string;
  tag?: string;
  color?: string;
}

export interface TerminalCodeBlockProps {
  channel?: ChannelId;
  windowTitle?: string;
  commands?: string[];
  outputLines?: TerminalOutputLine[];
  statusText?: string;
  executionTime?: string;
}

export const TerminalCodeBlock: React.FC<TerminalCodeBlockProps> = ({
  channel = "thinklate",
  windowTitle = "root@hermes-daemon: /var/log/arbitrage_engine",
  commands = [
    "curl -X POST https://api.hotel-cartel.internal/v1/rates --data '{\"city\": \"SFO\", \"conference\": true}'",
    "grep -i 'surge_multiplier' >> surge_dump.json",
  ],
  outputLines = [
    { text: "[200 OK] Received 48,192 rate quotes across 412 properties", tag: "INFO", color: "#10B981" },
    { text: "WARNING: SFO occupancy exceeds 98.4%. Artificial bottleneck detected.", tag: "ALERT", color: "#F59E0B" },
    { text: "CRITICAL: Base price inflated from $120 to $480/night (+300% cartel spread)", tag: "SURGE", color: "#EF4444" },
    { text: "DISCOVERY: 3 Living room rugs registered on Airbedandbreakfast.com @ $80/night", tag: "ARBITRAGE", color: "#00F0FF" },
  ],
  statusText = "EXECUTION THREAD // RECORD VERIFIED",
  executionTime = "4.2ms",
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const theme = getChannelTheme(channel);

  // Layer 1: Window entrance spring
  const scale = spring({
    frame,
    fps,
    config: {
      damping: theme.motion.damping,
      mass: theme.motion.mass,
      stiffness: theme.motion.stiffness,
    },
  });
  const opacity = interpolate(frame, [0, 10], [0, 1], { extrapolateRight: "clamp" });

  // Layer 2: Ambient glow pulse
  const glowPulse = Math.sin(frame / 8) * 0.2 + 0.8;

  // Layer 3: Cursor blink
  const cursorBlink = Math.floor(frame / 15) % 2 === 0;

  return (
    <div
      style={{
        width: "100%",
        height: "100%",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        fontFamily: theme.fonts.mono,
        backgroundColor: "transparent",
      }}
    >
      <div
        style={{
          width: "1400px",
          backgroundColor: theme.colors.bgGlassDark,
          backdropFilter: "blur(28px)",
          borderRadius: "16px",
          border: `1px solid ${theme.colors.borderGlass}`,
          boxShadow: `${theme.shadows.glass}, 0 0 ${30 * glowPulse}px ${theme.colors.borderAccent}`,
          overflow: "hidden",
          transform: `scale(${scale})`,
          opacity,
        }}
      >
        {/* Terminal Title Bar */}
        <div
          style={{
            height: "46px",
            backgroundColor: "rgba(0, 0, 0, 0.45)",
            borderBottom: "1px solid rgba(255, 255, 255, 0.08)",
            display: "flex",
            alignItems: "center",
            padding: "0 20px",
            justifyContent: "space-between",
          }}
        >
          <div style={{ display: "flex", gap: "9px", alignItems: "center" }}>
            <div style={{ width: "12px", height: "12px", borderRadius: "50%", backgroundColor: "#EF4444" }} />
            <div style={{ width: "12px", height: "12px", borderRadius: "50%", backgroundColor: "#F59E0B" }} />
            <div style={{ width: "12px", height: "12px", borderRadius: "50%", backgroundColor: "#10B981" }} />
            <span
              style={{
                marginLeft: "14px",
                fontSize: "13px",
                color: theme.colors.textMuted,
                letterSpacing: "0.06em",
              }}
            >
              {windowTitle}
            </span>
          </div>

          <div
            style={{
              fontSize: "12px",
              color: theme.colors.accent,
              letterSpacing: "0.1em",
              fontWeight: 700,
            }}
          >
            {statusText}
          </div>
        </div>

        {/* Terminal Body */}
        <div style={{ padding: "34px 40px", display: "flex", flexDirection: "column", gap: "16px" }}>
          {/* Command Prompt */}
          {commands.map((cmd, idx) => {
            const startFrame = 8 + idx * 22;
            const cmdProgress = interpolate(frame, [startFrame, startFrame + 18], [0, cmd.length], {
              extrapolateLeft: "clamp",
              extrapolateRight: "clamp",
            });
            const typedText = cmd.slice(0, Math.round(cmdProgress));

            return (
              <div
                key={idx}
                style={{
                  fontSize: "19px",
                  color: theme.colors.textWhite,
                  display: "flex",
                  alignItems: "flex-start",
                  gap: "12px",
                }}
              >
                <span style={{ color: theme.colors.accent, fontWeight: 800 }}>❯</span>
                <span style={{ color: theme.colors.accentSecondary, fontWeight: 700 }}>sys::exec</span>
                <span style={{ color: theme.colors.textWhite }}>
                  {typedText}
                  {idx === commands.length - 1 && cursorBlink && (
                    <span style={{ color: theme.colors.accent, marginLeft: "2px" }}>▋</span>
                  )}
                </span>
              </div>
            );
          })}

          {/* Divider */}
          <div
            style={{
              height: "1px",
              backgroundColor: "rgba(255, 255, 255, 0.1)",
              margin: "8px 0",
            }}
          />

          {/* Output Lines with Ping-Pong Stagger Reveal */}
          <div style={{ display: "flex", flexDirection: "column", gap: "12px" }}>
            {outputLines.map((line, idx) => {
              const lineFrame = 55 + idx * 12;
              const lineSpring = spring({
                frame: Math.max(0, frame - lineFrame),
                fps,
                config: { damping: 12, mass: 0.5, stiffness: 140 },
              });
              const lineOpacity = interpolate(frame, [lineFrame, lineFrame + 6], [0, 1], {
                extrapolateRight: "clamp",
              });

              if (frame < lineFrame) return null;

              return (
                <div
                  key={idx}
                  style={{
                    display: "flex",
                    alignItems: "center",
                    gap: "14px",
                    transform: `translateX(${(1 - lineSpring) * -15}px)`,
                    opacity: lineOpacity,
                    fontSize: "17px",
                  }}
                >
                  {line.tag && (
                    <span
                      style={{
                        padding: "3px 9px",
                        borderRadius: "5px",
                        fontSize: "11px",
                        fontWeight: 900,
                        letterSpacing: "0.08em",
                        backgroundColor: line.color ? `${line.color}22` : "rgba(255,255,255,0.1)",
                        color: line.color || theme.colors.textWhite,
                        border: `1px solid ${line.color ? `${line.color}66` : "rgba(255,255,255,0.2)"}`,
                      }}
                    >
                      {line.tag}
                    </span>
                  )}
                  <span style={{ color: line.color || theme.colors.textMuted, letterSpacing: "0.02em" }}>
                    {line.text}
                  </span>
                </div>
              );
            })}
          </div>

          {/* Footer Status Bar */}
          <div
            style={{
              marginTop: "16px",
              paddingTop: "14px",
              borderTop: "1px dashed rgba(255, 255, 255, 0.12)",
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
              fontSize: "12px",
              color: theme.colors.textDim,
            }}
          >
            <span>STATUS: 200 SUCCESS ✦ PIPELINE: DAEMON_PID#8102</span>
            <span style={{ color: theme.colors.accent, fontWeight: 700 }}>LATENCY: {executionTime}</span>
          </div>
        </div>
      </div>
    </div>
  );
};
