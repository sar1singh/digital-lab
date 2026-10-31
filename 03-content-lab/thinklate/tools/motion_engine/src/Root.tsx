import React from "react";
import { Composition } from "remotion";
import { EvidenceGlassCard } from "./components/EvidenceGlassCard";
import { MetricCounterCard } from "./components/MetricCounterCard";
import { KineticTypographySlam } from "./components/KineticTypographySlam";
import { ComparisonSplitCard } from "./components/ComparisonSplitCard";
import { ForensicHeadlineCard } from "./components/ForensicHeadlineCard";

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

      <Composition
        id="ComparisonSplit"
        component={ComparisonSplitCard}
        durationInFrames={120}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          badgeText: "MARKET ARBITRAGE // EXPECTATION VS REALITY",
          leftTitle: "THE SAN FRANCISCO HOTEL CARTEL",
          leftSubtitle: "RIGID MONOPOLY PRICING",
          leftItems: [
            "$280/night standard room rate during design conference",
            "100% sold-out citywide capacity within 48 hours",
            "Mandatory $45 resort fees + parking overhead"
          ],
          rightTitle: "THE $80 AIRBED EXPERIMENT",
          rightSubtitle: "SOLO FOUNDER ARBITRAGE",
          rightItems: [
            "$80/night inflatable air mattress on living room floor",
            "Free WiFi + homemade breakfast pop-tarts included",
            "Zero hotel infrastructure, zero debt, instant cash flow"
          ],
          footerNote: "PRICE SPREAD: 71.4% DISCOUNT FOR ATTENDEES | $240 CASH REVENUE FOR FOUNDERS",
        }}
      />

      <Composition
        id="ForensicHeadline"
        component={ForensicHeadlineCard}
        durationInFrames={120}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          publication: "THE WALL STREET JOURNAL",
          category: "VENTURE CAPITAL FORENSICS",
          headline: "Silicon Valley Angels Reject Airbed Venture As 'Worst Idea We Have Ever Seen'",
          excerpt: "Top institutional investors passed on the 10% equity seed round for $150,000, citing stranger-danger liability and unscalable air mattress logistics.",
          highlightWords: "Worst Idea We Have Ever Seen",
          dateStr: "AUGUST 2008",
          authorOrRef: "TECH CRUCIBLE ARCHIVES // INVESTOR REJECTION DOSSIER",
        }}
      />
    </>
  );
};
