import React, { useEffect, useRef } from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import rough from "roughjs";
import { ChannelId, getChannelTheme } from "../../styles/theme";

export interface RoughSketchChartProps {
  channel?: ChannelId;
  title?: string;
  subtitle?: string;
  leftLabel?: string;
  leftAmount?: string;
  leftHeightPercent?: number; // 0 to 100
  rightLabel?: string;
  rightAmount?: string;
  rightHeightPercent?: number; // 0 to 100
  handwrittenNote?: string;
}

export const RoughSketchChart: React.FC<RoughSketchChartProps> = ({
  channel = "thinklate",
  title = "THE ASSET OVERHEAD DISPARITY",
  subtitle = "PHYSICAL CONCRETE CAPITAL VS ZERO-ASSET CODEBASE",
  leftLabel = "MARRIOTT + HILTON (100 YEARS)",
  leftAmount = "$140 BILLION (DEBT + BUILDINGS)",
  leftHeightPercent = 85,
  rightLabel = "AIRBED & BREAKFAST (LINES OF CODE)",
  rightAmount = "$100 BILLION (ZERO PROPERTY)",
  rightHeightPercent = 65,
  handwrittenNote = "✦ 0 Physical Real Estate Owned. 100% Platform Margin.",
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const theme = getChannelTheme(channel);
  const accent = theme.colors.accent;
  const accentSecondary = theme.colors.accentSecondary;
  const canvasRef = useRef<HTMLCanvasElement>(null);

  // Entrance spring
  const scale = spring({
    frame,
    fps,
    config: { damping: 14, mass: 0.8, stiffness: 100 },
  });

  // Sketched bars growth animation (frames 15 to 65)
  const growth = interpolate(frame, [15, 65], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Draw rough sketchy elements on canvas
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const rc = rough.canvas(canvas);

    // Canvas dimensions: 1100 x 500
    const baseY = 420;

    // 1. Sketched Base Line
    rc.line(60, baseY, 1040, baseY, {
      stroke: "rgba(255, 255, 255, 0.4)",
      strokeWidth: 2,
      roughness: 1.5,
    });

    // 2. Sketched Bar 1 (Left - Legacy)
    const bar1MaxH = (leftHeightPercent / 100) * 300;
    const bar1H = bar1MaxH * growth;
    if (bar1H > 5) {
      rc.rectangle(200, baseY - bar1H, 180, bar1H, {
        fill: "rgba(239, 68, 68, 0.35)",
        fillStyle: "cross-hatch",
        stroke: "#EF4444",
        strokeWidth: 2.5,
        roughness: 2.0,
        hachureGap: 7,
      });
    }

    // 3. Sketched Bar 2 (Right - Arbitrage)
    const bar2MaxH = (rightHeightPercent / 100) * 300;
    const bar2H = bar2MaxH * growth;
    if (bar2H > 5) {
      rc.rectangle(660, baseY - bar2H, 180, bar2H, {
        fill: `${accent}45`,
        fillStyle: "zigzag",
        stroke: accent,
        strokeWidth: 2.8,
        roughness: 1.8,
        hachureGap: 6,
      });
    }

    // 4. Sketched Arrow connecting bars (frames 40+)
    if (frame > 40) {
      const arrowProgress = interpolate(frame, [40, 75], [0, 1], { extrapolateRight: "clamp" });
      const arrowEndX = 200 + 180 + (660 - 380) * arrowProgress;
      rc.line(380, 240, arrowEndX, 240, {
        stroke: accentSecondary,
        strokeWidth: 2.5,
        roughness: 1.8,
      });
      if (arrowProgress > 0.8) {
        // Arrow head
        rc.line(arrowEndX - 15, 225, arrowEndX, 240, { stroke: accentSecondary, strokeWidth: 2.5 });
        rc.line(arrowEndX - 15, 255, arrowEndX, 240, { stroke: accentSecondary, strokeWidth: 2.5 });
      }
    }

    // 5. Sketched hand-drawn rough circle around note (frames 60+)
    if (frame > 60) {
      rc.ellipse(550, 475, 520, 42, {
        stroke: accent,
        strokeWidth: 2,
        roughness: 2.2,
      });
    }
  }, [frame, growth, leftHeightPercent, rightHeightPercent, accent, accentSecondary]);

  return (
    <div
      style={{
        position: "absolute",
        top: "50%",
        left: "50%",
        transform: `translate(-50%, -50%) scale(${scale})`,
        width: 1200,
        backgroundColor: "rgba(10, 15, 26, 0.88)",
        backdropFilter: "blur(20px)",
        border: "1px solid rgba(255, 255, 255, 0.15)",
        borderRadius: 16,
        padding: "36px 48px",
        boxShadow: "0 25px 60px rgba(0, 0, 0, 0.6)",
        fontFamily: theme.fonts.mono,
        color: "#FFFFFF",
      }}
    >
      {/* Header */}
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", marginBottom: 12 }}>
        <div>
          <div
            style={{
              fontSize: 11,
              fontWeight: 800,
              color: accent,
              letterSpacing: 2,
              textTransform: "uppercase",
              marginBottom: 4,
            }}
          >
            VOX FORENSIC SKETCH // SYSTEM DIVERGENCE
          </div>
          <div
            style={{
              fontFamily: theme.fonts.display,
              fontSize: 28,
              fontWeight: 900,
              letterSpacing: 0.5,
            }}
          >
            {title}
          </div>
          <div style={{ fontSize: 13, color: "rgba(255,255,255,0.6)", marginTop: 2 }}>{subtitle}</div>
        </div>

        <div
          style={{
            fontSize: 10,
            fontWeight: 800,
            backgroundColor: "rgba(255, 255, 255, 0.08)",
            padding: "4px 10px",
            borderRadius: 6,
            border: "1px solid rgba(255, 255, 255, 0.15)",
            color: "rgba(255, 255, 255, 0.8)",
          }}
        >
          HAND-DRAWN EVIDENCE
        </div>
      </div>

      {/* Sketched Canvas */}
      <div style={{ position: "relative", width: 1100, height: 500, margin: "0 auto" }}>
        <canvas ref={canvasRef} width={1100} height={500} style={{ position: "absolute", top: 0, left: 0 }} />

        {/* Bar 1 Overlay Labels */}
        <div
          style={{
            position: "absolute",
            bottom: 90,
            left: 200,
            width: 180,
            textAlign: "center",
            pointerEvents: "none",
          }}
        >
          <div style={{ fontSize: 13, fontWeight: 900, color: "#EF4444", textShadow: "0 2px 8px rgba(0,0,0,0.8)" }}>
            {leftAmount}
          </div>
          <div style={{ fontSize: 10, fontWeight: 700, color: "rgba(255,255,255,0.7)", marginTop: 4 }}>
            {leftLabel}
          </div>
        </div>

        {/* Bar 2 Overlay Labels */}
        <div
          style={{
            position: "absolute",
            bottom: 90,
            left: 660,
            width: 180,
            textAlign: "center",
            pointerEvents: "none",
          }}
        >
          <div
            style={{
              fontSize: 13,
              fontWeight: 900,
              color: accent,
              textShadow: "0 2px 8px rgba(0,0,0,0.8)",
            }}
          >
            {rightAmount}
          </div>
          <div style={{ fontSize: 10, fontWeight: 700, color: "rgba(255,255,255,0.7)", marginTop: 4 }}>
            {rightLabel}
          </div>
        </div>

        {/* Handwritten Note at bottom */}
        <div
          style={{
            position: "absolute",
            bottom: 12,
            left: 0,
            right: 0,
            textAlign: "center",
            fontSize: 14,
            fontWeight: 700,
            color: accent,
            fontFamily: "monospace",
            letterSpacing: 0.5,
          }}
        >
          {handwrittenNote}
        </div>
      </div>
    </div>
  );
};
