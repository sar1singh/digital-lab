import React from "react";
import { Composition } from "remotion";
import { EvidenceGlassCard } from "./components/EvidenceGlassCard";
import { MetricCounterCard } from "./components/MetricCounterCard";
import { KineticTypographySlam } from "./components/KineticTypographySlam";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="EvidenceCard"
        component={EvidenceGlassCard}
        durationInFrames={120}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          badgeText: "PRIMARY EVIDENCE // EVICTION NOTICE",
          badgeType: "warning",
          title: "OCTOBER 2007: 72 HOURS FROM STREET",
          quote: "Your rent is $1,150. You have three days before your landlord kicks you out and your bank account is empty.",
          highlightWords: "three days before your landlord kicks you out",
          sourceDoc: "SAN FRANCISCO RESIDENTIAL TENANCY RECORD #4092",
          dateStr: "OCTOBER 14, 2007",
        }}
      />

      <Composition
        id="MetricCounter"
        component={MetricCounterCard}
        durationInFrames={120}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          badgeText: "FINANCIAL METRIC ARBITRAGE",
          startVal: 0,
          endVal: 30000,
          prefix: "$",
          suffix: "",
          label: "CEREAL BOX BOOTSTRAP CAPITAL",
          subtext: "1,000 custom election cereal boxes sold at $40/each to fund 3 months of runway",
        }}
      />

      <Composition
        id="TypographySlam"
        component={KineticTypographySlam}
        durationInFrames={90}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          line1: "OCTOBER 2007: $1,150 OVERDUE RENT",
          line2: "3 AIRBEDS ON A LIVING ROOM RUG",
          subtext: "THE EMBARRASSING DESPERATE HUSTLE THAT HIJACKED AN INDUSTRY",
        }}
      />
    </>
  );
};
