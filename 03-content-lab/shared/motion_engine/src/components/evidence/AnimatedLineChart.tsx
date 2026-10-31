import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { THEME } from "../../styles/theme";

export interface DataPoint {
  xLabel: string;
  yValue: number;
}

export interface AnimatedLineChartProps {
  badgeText?: string;
  title: string;
  subtitle?: string;
  points?: DataPoint[];
  milestoneText?: string;
  milestoneSubtext?: string;
  footerNote?: string;
}

export const AnimatedLineChart: React.FC<AnimatedLineChartProps> = ({
  badgeText = "FORENSIC TRAJECTORY // CAPITAL MARKET RUNWAY",
  title = "VALUATION SPIKE COLLAPSE",
  subtitle = "Capital market valuation trajectory ($ Billions)",
  points = [
    { xLabel: "2008", yValue: 0.1 },
    { xLabel: "2011", yValue: 1.0 },
    { xLabel: "2015", yValue: 25.5 },
    { xLabel: "2019", yValue: 38.0 },
    { xLabel: "2020", yValue: 18.0 },
    { xLabel: "2021", yValue: 100.0 },
    { xLabel: "2024", yValue: 85.0 },
  ],
  milestoneText = "DEC 2020: $100B IPO SPIKE",
  milestoneSubtext = "From $80 airbeds on a living room rug to larger than Marriott + Hilton combined",
  footerNote = "SOURCE: S&P CAPITAL IQ // NASDAQ ARCHIVES",
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const cardScale = spring({
    frame,
    fps,
    config: { damping: 14, mass: 0.8, stiffness: 100 },
  });

  const opacity = interpolate(frame, [0, 8], [0, 1], { extrapolateRight: "clamp" });

  // Line draw progress (frames 10 to 60)
  const drawProgress = interpolate(frame, [10, 55], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const milestonePop = spring({
    frame: Math.max(0, frame - 40),
    fps,
    config: { damping: 12, mass: 0.6, stiffness: 130 },
  });

  // Calculate SVG path
  const svgWidth = 1100;
  const svgHeight = 280;
  const paddingX = 40;
  const paddingY = 30;

  const maxY = Math.max(...points.map((p) => p.yValue));
  const minY = Math.min(...points.map((p) => p.yValue));

  const coords = points.map((p, idx) => {
    const x = paddingX + (idx / (points.length - 1)) * (svgWidth - paddingX * 2);
    const y = svgHeight - paddingY - ((p.yValue - minY) / (maxY - minY || 1)) * (svgHeight - paddingY * 2);
    return { x, y, ...p };
  });

  const pathD = coords.reduce((acc, pt, i) => `${acc} ${i === 0 ? "M" : "L"} ${pt.x} ${pt.y}`, "");
  const areaD = `${pathD} L ${coords[coords.length - 1].x} ${svgHeight} L ${coords[0].x} ${svgHeight} Z`;

  // Peak point index for milestone
  const peakIdx = coords.reduce((maxI, pt, i, arr) => (pt.yValue > arr[maxI].yValue ? i : maxI), 0);
  const peakPt = coords[peakIdx];

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
          width: "1380px",
          backgroundColor: THEME.colors.bgGlass,
          backdropFilter: "blur(24px)",
          borderRadius: "24px",
          border: `1px solid ${THEME.colors.borderGlass}`,
          boxShadow: THEME.shadows.glass,
          padding: "44px 56px",
          transform: `scale(${cardScale})`,
          opacity,
          display: "flex",
          flexDirection: "column",
          gap: "20px",
          position: "relative",
          overflow: "hidden",
        }}
      >
        {/* Top lime gradient highlight */}
        <div
          style={{
            position: "absolute",
            top: 0,
            left: "10%",
            right: "10%",
            height: "2px",
            background: `linear-gradient(90deg, transparent, ${THEME.colors.acidLime}, transparent)`,
          }}
        />

        {/* Header */}
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", borderBottom: `1px solid rgba(255, 255, 255, 0.08)`, paddingBottom: "16px" }}>
          <div>
            <div
              style={{
                fontFamily: THEME.fonts.mono,
                fontSize: "12px",
                fontWeight: 700,
                letterSpacing: "0.2em",
                color: THEME.colors.acidLime,
                marginBottom: "6px",
                textTransform: "uppercase",
              }}
            >
              ✦ {badgeText}
            </div>
            <h2 style={{ fontSize: "32px", fontWeight: 900, color: THEME.colors.textWhite, margin: 0, letterSpacing: "-0.02em" }}>
              {title}
            </h2>
            {subtitle && <p style={{ fontSize: "16px", color: THEME.colors.textMuted, margin: "4px 0 0 0" }}>{subtitle}</p>}
          </div>
          <div style={{ fontFamily: THEME.fonts.mono, fontSize: "12px", color: THEME.colors.textDim, letterSpacing: "0.15em" }}>
            MARKET DOCKET
          </div>
        </div>

        {/* Line Chart Area */}
        <div style={{ position: "relative", width: "100%", height: "300px" }}>
          <svg width="100%" height="100%" viewBox={`0 0 ${svgWidth} ${svgHeight}`} style={{ overflow: "visible" }}>
            <defs>
              <linearGradient id="lineGrad" x1="0" y1="0" x2="0" y2="1">
                <stop offset="0%" stopColor={THEME.colors.acidLime} stopOpacity="0.35" />
                <stop offset="100%" stopColor={THEME.colors.acidLime} stopOpacity="0.0" />
              </linearGradient>
            </defs>

            {/* Subtle horizontal grid */}
            <line x1={paddingX} y1={paddingY} x2={svgWidth - paddingX} y2={paddingY} stroke="rgba(255,255,255,0.06)" strokeDasharray="4 4" />
            <line x1={paddingX} y1={svgHeight / 2} x2={svgWidth - paddingX} y2={svgHeight / 2} stroke="rgba(255,255,255,0.06)" strokeDasharray="4 4" />
            <line x1={paddingX} y1={svgHeight - paddingY} x2={svgWidth - paddingX} y2={svgHeight - paddingY} stroke="rgba(255,255,255,0.15)" />

            {/* Gradient Area */}
            <path d={areaD} fill="url(#lineGrad)" opacity={drawProgress} />

            {/* Animated Stroke Path */}
            <path
              d={pathD}
              fill="none"
              stroke={THEME.colors.acidLime}
              strokeWidth="4"
              strokeLinecap="round"
              strokeDasharray={2000}
              strokeDashoffset={(1 - drawProgress) * 2000}
              style={{ filter: "drop-shadow(0 0 10px rgba(226, 255, 0, 0.4))" }}
            />

            {/* Points & Labels */}
            {coords.map((pt, i) => {
              const ptAppears = drawProgress >= (i / (coords.length - 1)) * 0.9;
              return (
                <g key={i} opacity={ptAppears ? 1 : 0}>
                  <circle cx={pt.x} cy={pt.y} r={pt.yValue === maxY ? 7 : 4} fill={THEME.colors.textWhite} stroke={THEME.colors.acidLime} strokeWidth="3" />
                  <text x={pt.x} y={svgHeight - 6} fill={THEME.colors.textDim} fontSize="14" fontFamily={THEME.fonts.mono} textAnchor="middle">
                    {pt.xLabel}
                  </text>
                </g>
              );
            })}
          </svg>

          {/* Floating Peak Milestone Box */}
          {peakPt && (
            <div
              style={{
                position: "absolute",
                left: `${(peakPt.x / svgWidth) * 100}%`,
                top: `${(peakPt.y / svgHeight) * 100}%`,
                transform: `translate(-50%, -125%) scale(${milestonePop})`,
                opacity: milestonePop,
                backgroundColor: "rgba(10, 15, 26, 0.88)",
                backdropFilter: "blur(16px)",
                border: `1px solid ${THEME.colors.acidLime}`,
                boxShadow: THEME.shadows.glowLime,
                borderRadius: "12px",
                padding: "12px 18px",
                whiteSpace: "nowrap",
                zIndex: 10,
              }}
            >
              <div style={{ fontFamily: THEME.fonts.mono, fontSize: "14px", fontWeight: 900, color: THEME.colors.acidLime }}>
                ✦ {milestoneText}
              </div>
              {milestoneSubtext && (
                <div style={{ fontFamily: THEME.fonts.sans, fontSize: "12px", color: THEME.colors.textMuted, marginTop: "2px" }}>
                  {milestoneSubtext}
                </div>
              )}
            </div>
          )}
        </div>

        {/* Footer */}
        {footerNote && (
          <div
            style={{
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
              fontFamily: THEME.fonts.mono,
              fontSize: "12px",
              color: THEME.colors.textDim,
              letterSpacing: "0.12em",
              paddingTop: "6px",
            }}
          >
            <span>{footerNote}</span>
            <span style={{ color: THEME.colors.acidLime }}>SEC VERIFIED</span>
          </div>
        )}
      </div>
    </div>
  );
};
