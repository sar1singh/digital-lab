import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { Lottie, LottieAnimationData } from "@remotion/lottie";
import { ChannelId, getChannelTheme } from "../../styles/theme";

// Standard lightweight vector pulse/check Lottie animation
const DEFAULT_LOTTIE_DATA: any = {
  v: "5.5.7",
  fr: 30,
  ip: 0,
  op: 60,
  w: 200,
  h: 200,
  nm: "Success Pulse",
  ddd: 0,
  assets: [],
  layers: [
    {
      ddd: 0,
      ind: 1,
      ty: 4,
      nm: "Ring Pulse",
      sr: 1,
      ks: {
        o: { a: 1, k: [{ i: { x: [0.833], y: [0.833] }, o: { x: [0.167], y: [0.167] }, t: 0, s: [100] }, { t: 50, s: [0] }] },
        r: { a: 0, k: 0 },
        p: { a: 0, k: [100, 100, 0] },
        a: { a: 0, k: [0, 0, 0] },
        s: { a: 1, k: [{ i: { x: [0.667, 0.667, 0.667], y: [1, 1, 1] }, o: { x: [0.167, 0.167, 0.167], y: [0.167, 0.167, 0.167] }, t: 0, s: [40, 40, 100] }, { t: 50, s: [140, 140, 100] }] }
      },
      shapes: [
        {
          ty: "el",
          d: 1,
          p: { a: 0, k: [0, 0] },
          s: { a: 0, k: [100, 100] }
        },
        {
          ty: "st",
          c: { a: 0, k: [0.88, 1, 0, 1] },
          o: { a: 0, k: 100 },
          w: { a: 0, k: 4 },
          lc: 1,
          lj: 1
        }
      ]
    },
    {
      ddd: 0,
      ind: 2,
      ty: 4,
      nm: "Core Circle",
      sr: 1,
      ks: {
        o: { a: 0, k: 100 },
        r: { a: 0, k: 0 },
        p: { a: 0, k: [100, 100, 0] },
        a: { a: 0, k: [0, 0, 0] },
        s: { a: 1, k: [{ i: { x: [0.667, 0.667, 0.667], y: [1, 1, 1] }, o: { x: [0.167, 0.167, 0.167], y: [0.167, 0.167, 0.167] }, t: 0, s: [0, 0, 100] }, { t: 20, s: [100, 100, 100] }] }
      },
      shapes: [
        {
          ty: "el",
          d: 1,
          p: { a: 0, k: [0, 0] },
          s: { a: 0, k: [70, 70] }
        },
        {
          ty: "fl",
          c: { a: 0, k: [0, 0.94, 1, 1] },
          o: { a: 0, k: 90 }
        }
      ]
    }
  ]
};

export interface LottieAnimationCardProps {
  channel?: ChannelId;
  badgeText?: string;
  headline?: string;
  explanation?: string;
  statValue?: string;
  statLabel?: string;
  animationData?: any;
}

export const LottieAnimationCard: React.FC<LottieAnimationCardProps> = ({
  channel = "thinklate",
  badgeText = "VECTOR MOTION GRAPHIC // SYSTEM RESOLUTION",
  headline = "THE ASYMMETRIC FLYWHEEL ACTIVATED",
  explanation = "When supply acquisition cost drops to near zero, growth compounds without physical friction.",
  statValue = "0% CAPITAL DEBT",
  statLabel = "PHYSICAL PROPERTY RATIO",
  animationData = DEFAULT_LOTTIE_DATA,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const theme = getChannelTheme(channel);
  const accent = theme.colors.accent;
  const accentSecondary = theme.colors.accentSecondary;

  const cardScale = spring({
    frame,
    fps,
    config: { damping: 13, mass: 0.8, stiffness: 110 },
  });

  const contentFade = interpolate(frame, [10, 25], [0, 1], { extrapolateRight: "clamp" });

  return (
    <div
      style={{
        position: "absolute",
        top: "50%",
        left: "50%",
        transform: `translate(-50%, -50%) scale(${cardScale})`,
        width: 1050,
        backgroundColor: "rgba(10, 15, 26, 0.90)",
        backdropFilter: "blur(20px)",
        border: `1px solid rgba(255, 255, 255, 0.18)`,
        borderLeft: `4px solid ${accent}`,
        borderRadius: 14,
        padding: "36px 42px",
        boxShadow: "0 25px 60px rgba(0, 0, 0, 0.65)",
        fontFamily: theme.fonts.mono,
        color: "#FFFFFF",
        display: "flex",
        alignItems: "center",
        gap: 36,
      }}
    >
      {/* Lottie Vector Graphic Box */}
      <div
        style={{
          width: 200,
          height: 200,
          backgroundColor: "rgba(255, 255, 255, 0.04)",
          borderRadius: 12,
          border: "1px solid rgba(255, 255, 255, 0.1)",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          flexShrink: 0,
          boxShadow: `inset 0 0 25px ${accent}15`,
        }}
      >
        <Lottie animationData={animationData} style={{ width: 180, height: 180 }} />
      </div>

      {/* Narrative & Metric Content */}
      <div style={{ flex: 1, opacity: contentFade }}>
        <div
          style={{
            fontSize: 10,
            fontWeight: 800,
            letterSpacing: 2,
            color: accent,
            marginBottom: 6,
          }}
        >
          {badgeText}
        </div>

        <div
          style={{
            fontFamily: theme.fonts.display,
            fontSize: 30,
            fontWeight: 900,
            letterSpacing: 0.5,
            lineHeight: 1.2,
            marginBottom: 10,
          }}
        >
          {headline}
        </div>

        <div
          style={{
            fontSize: 13,
            lineHeight: 1.5,
            color: "rgba(255, 255, 255, 0.7)",
            marginBottom: 18,
          }}
        >
          {explanation}
        </div>

        {/* Highlighted Stat Footer */}
        <div
          style={{
            display: "inline-flex",
            alignItems: "center",
            gap: 12,
            backgroundColor: "rgba(255, 255, 255, 0.06)",
            border: `1px solid ${accentSecondary}40`,
            borderRadius: 6,
            padding: "6px 14px",
          }}
        >
          <span style={{ fontSize: 16, fontWeight: 900, color: accentSecondary }}>{statValue}</span>
          <span style={{ fontSize: 10, fontWeight: 700, color: "rgba(255, 255, 255, 0.6)", letterSpacing: 1 }}>
            {statLabel}
          </span>
        </div>
      </div>
    </div>
  );
};
