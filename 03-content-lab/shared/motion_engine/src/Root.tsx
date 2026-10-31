import React from "react";
import { Composition } from "remotion";

// Evidence & Data Suite
import { EvidenceGlassCard } from "./components/EvidenceGlassCard";
import { MetricCounterCard } from "./components/MetricCounterCard";
import { ComparisonSplitCard } from "./components/ComparisonSplitCard";
import { ForensicHeadlineCard } from "./components/ForensicHeadlineCard";
import { AnimatedBarChart } from "./components/evidence/AnimatedBarChart";
import { AnimatedLineChart } from "./components/evidence/AnimatedLineChart";
import { NewspaperSlider } from "./components/evidence/NewspaperSlider";
import { DocumentRedactionCard } from "./components/evidence/DocumentRedactionCard";
import { SocialCitationCard } from "./components/evidence/SocialCitationCard";
import { StatDonutGauge } from "./components/evidence/StatDonutGauge";
import { TornPaperReceipt } from "./components/evidence/TornPaperReceipt";
import { TerminalCodeBlock } from "./components/evidence/TerminalCodeBlock";
import { TimelineMilestoneFlow } from "./components/evidence/TimelineMilestoneFlow";
import { AudioWaveformCard } from "./components/evidence/AudioWaveformCard";
import { MapLocusRadar } from "./components/evidence/MapLocusRadar";
import { PhotoPolaroidPin } from "./components/evidence/PhotoPolaroidPin";
import { MagnifyingGlassDoc } from "./components/evidence/MagnifyingGlassDoc";
import { CharacterProfileCard } from "./components/evidence/CharacterProfileCard";
import { RankedListicleCard } from "./components/evidence/RankedListicleCard";
import { ConspiracyPinBoard } from "./components/evidence/ConspiracyPinBoard";
import { WatchMojoCountdown } from "./components/evidence/WatchMojoCountdown";
import { RoughSketchChart } from "./components/evidence/RoughSketchChart";
import { LottieAnimationCard } from "./components/evidence/LottieAnimationCard";

// Kinetic Typography Suite
import { KineticTypographySlam } from "./components/KineticTypographySlam";
import { TypewriterBlink } from "./components/typography/TypewriterBlink";
import { GlitchDecoder } from "./components/typography/GlitchDecoder";
import { HighlighterWipeText } from "./components/typography/HighlighterWipeText";
import { WordByWordPop } from "./components/typography/WordByWordPop";
import { SplitWordCollision } from "./components/typography/SplitWordCollision";
import { StrikethroughSlam } from "./components/typography/StrikethroughSlam";
import { FloatingPillBadge } from "./components/typography/FloatingPillBadge";
import { Perspective3DTilt } from "./components/typography/Perspective3DTilt";
import { StaggeredWaveText } from "./components/typography/StaggeredWaveText";
import { TextMaskWipe } from "./components/typography/TextMaskWipe";
import { KineticScrollLadder } from "./components/typography/KineticScrollLadder";
import { ElasticBungeeText } from "./components/typography/ElasticBungeeText";
import { TextTrailOutline } from "./components/typography/TextTrailOutline";
import { TypographyBackgroundWall } from "./components/typography/TypographyBackgroundWall";
import { CurtainSwipeReveal } from "./components/typography/CurtainSwipeReveal";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      {/* ============================================================== */}
      {/* 1. EVIDENCE & DATA SUITE (11 Broadcast Forensic Templates)      */}
      {/* ============================================================== */}
      <Composition
        id="EvidenceCard"
        component={EvidenceGlassCard as any}
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
        component={MetricCounterCard as any}
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
        id="ComparisonSplit"
        component={ComparisonSplitCard as any}
        durationInFrames={120}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          badgeText: "MARKET ARBITRAGE // EXPECTATION VS REALITY",
          leftTag: "RIGID MONOPOLY",
          leftStat: "$280",
          leftStatUnit: "/ night",
          leftTitle: "THE SAN FRANCISCO HOTEL CARTEL",
          leftItems: [
            "Standard room rate during design conference",
            "100% sold-out citywide capacity in 48 hours",
            "Mandatory $45 resort fees + parking overhead"
          ],
          rightTag: "SYSTEM ARBITRAGE",
          rightStat: "$80",
          rightStatUnit: "/ night",
          rightTitle: "THE $80 AIRBED EXPERIMENT",
          rightItems: [
            "Inflatable air mattress on living room rug",
            "Free Wi-Fi + homemade breakfast pop-tarts",
            "Zero hotel infrastructure, instant cash flow"
          ],
          footerNote: "PRICE SPREAD: 71.4% DISCOUNT FOR ATTENDEES  ✦  $240 CASH REVENUE FOR FOUNDERS",
        }}
      />

      <Composition
        id="ForensicHeadline"
        component={ForensicHeadlineCard as any}
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

      <Composition
        id="AnimatedBarChart"
        component={AnimatedBarChart as any}
        durationInFrames={120}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          badgeText: "MARKET ARBITRAGE // EMPIRICAL DATA",
          title: "VALUATION REVENUE MULTIPLES",
          subtitle: "Public Hotel Operators vs Solo Airbed Platform",
          bars: [
            { label: "Marriott Int.", value: 1.8, displayValue: "1.8x", highlight: false },
            { label: "Hilton Worldwide", value: 2.1, displayValue: "2.1x", highlight: false },
            { label: "Hyatt Hotels", value: 1.5, displayValue: "1.5x", highlight: false },
            { label: "Airbnb (Peak)", value: 14.5, displayValue: "14.5x", highlight: true },
          ],
          footerNote: "SOURCE: SEC FORM 10-K & BLOOMBERG MARKET BENCHMARKS",
        }}
      />

      <Composition
        id="AnimatedLineChart"
        component={AnimatedLineChart as any}
        durationInFrames={120}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          badgeText: "FORENSIC TRAJECTORY // CAPITAL MARKET RUNWAY",
          title: "VALUATION SPIKE COLLAPSE",
          subtitle: "Capital market valuation trajectory ($ Billions)",
          points: [
            { xLabel: "2008", yValue: 0.1 },
            { xLabel: "2011", yValue: 1.0 },
            { xLabel: "2015", yValue: 25.5 },
            { xLabel: "2019", yValue: 38.0 },
            { xLabel: "2020", yValue: 18.0 },
            { xLabel: "2021", yValue: 100.0 },
            { xLabel: "2024", yValue: 85.0 },
          ],
          milestoneText: "DEC 2020: $100B IPO SPIKE",
          milestoneSubtext: "From $80 airbeds on a living room rug to larger than Marriott + Hilton combined",
          footerNote: "SOURCE: S&P CAPITAL IQ // NASDAQ ARCHIVES",
        }}
      />

      <Composition
        id="NewspaperSlider"
        component={NewspaperSlider as any}
        durationInFrames={120}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          badgeText: "HISTORICAL FORENSICS // ARCHIVE SLIDER",
          beforeMasthead: "THE SAN FRANCISCO CHRONICLE",
          beforeDate: "OCTOBER 1999",
          beforeHeadline: "Hotels Lock In Record High Rates As Room Capacity Hits Complete Drought",
          beforeExcerpt: "City officials warn tourists and convention attendees that standard lodging is completely exhausted, leaving zero alternatives for travelers.",
          afterMasthead: "THE WALL STREET JOURNAL",
          afterDate: "DECEMBER 2020",
          afterHeadline: "Airbnb Hits $100 Billion Valuation in Blockbuster Public Market Debut",
          afterExcerpt: "A pair of broke art school roommates who rented three air mattresses on their living room floor now control a platform larger than the top three hotel chains combined.",
          footerNote: "CHRONICLED TRANSFORMATION // 2007-2024 REGULATORY ARCHIVE",
        }}
      />

      <Composition
        id="DocumentRedaction"
        component={DocumentRedactionCard as any}
        durationInFrames={120}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          docketNumber: "CASE #08-CV-94021 // U.S. DISTRICT COURT",
          classification: "DECLASSIFIED EXHIBIT",
          title: "CONFIDENTIAL INTERNAL VC CORRESPONDENCE",
          clausePreamble: "The partners agreed that while the founders are remarkably persistent, ",
          redactedPhrase: "the core business model has no sustainable moat and will likely collapse within six months",
          clausePostamble: ", therefore recommending an immediate pass on the Series Seed round.",
          revealText: "EXHIBIT B: SAN FRANCISCO HOUSING COMM. DEPOSITION",
          footerNote: "UNREDACTED PRIMARY RECORD // FREEDOM OF INFORMATION ACT DOCKET",
        }}
      />

      <Composition
        id="SocialCitation"
        component={SocialCitationCard as any}
        durationInFrames={120}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          authorName: "Paul Graham",
          authorHandle: "@paulg",
          avatarText: "PG",
          avatarColor: "#F59E0B",
          dateStr: "11:42 PM · Nov 23, 2008",
          content: "We thought Airbnb was a terrible idea. Who wants to sleep on an air mattress in a stranger's apartment? But we funded them because we loved the founders.",
          highlightWords: "We thought Airbnb was a terrible idea",
          reposts: "14.2K",
          likes: "89.5K",
          views: "4.2M",
          footerNote: "VERIFIED FOUNDER TESTIMONY // PUBLIC CORRESPONDENCE",
        }}
      />

      <Composition
        id="StatDonutGauge"
        component={StatDonutGauge as any}
        durationInFrames={120}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          badgeText: "MARKET CONCENTRATION // ANTITRUST METRIC",
          targetPercent: 78.5,
          label: "URBAN MARKET SHARE",
          title: "THE DE FACTO SHORT-TERM MONOPOLY",
          description: "Across top 25 metropolitan areas, a single platform controls over three-quarters of all active short-term rental listings, dwarfing legacy hotel supply.",
          subStatLabel: "INDEPENDENT SUPPLY",
          subStatValue: "21.5%",
          footerNote: "SOURCE: U.S. BUREAU OF ECONOMIC ANALYSIS & AIRDNA ARCHIVE",
        }}
      />

      <Composition
        id="TornPaperReceipt"
        component={TornPaperReceipt as any}
        durationInFrames={120}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          receiptTitle: "THE INVOICE ANATOMY",
          storeLocation: "AIRBED & BREAKFAST PLATFORM RECEIPT",
          dateStr: "OCTOBER 14, 2023 // 14:22:09",
          lineItems: [
            { name: "2 Nights Living Room Stay", amount: "$160.00", isJunkFee: false },
            { name: "Mandatory Platform Service Fee", amount: "$38.40", isJunkFee: true },
            { name: "Standard Cleaning Fee", amount: "$110.00", isJunkFee: true },
            { name: "Host Chore Checklist Penalty", amount: "$50.00", isJunkFee: true },
            { name: "Local Occupancy Tax", amount: "$28.10", isJunkFee: false },
          ],
          subtotal: "$160.00",
          total: "$386.50",
          stampText: "141% JUNK FEE MARKUP",
          footerMessage: "ORIGINAL RATE: $80/NIGHT  ✦  FINAL CHECKOUT: $193.25/NIGHT",
        }}
      />

      {/* ============================================================== */}
      {/* 2. KINETIC TYPOGRAPHY SUITE (10 Visual Narrative Templates)    */}
      {/* ============================================================== */}
      <Composition
        id="TypographySlam"
        component={KineticTypographySlam as any}
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
        id="TypewriterBlink"
        component={TypewriterBlink as any}
        durationInFrames={90}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          badgeText: "FORENSIC DISPATCH // TERMINAL LOG",
          text: "THE REVENUE MODEL WAS SECRETLY DESIGNED TO BLEED USERS DRY",
          subtext: "INTERNAL SLACK LOGS · MARCH 14, 2021",
          speed: 0.8,
        }}
      />

      <Composition
        id="GlitchDecoder"
        component={GlitchDecoder as any}
        durationInFrames={90}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          badgeText: "FORENSIC DECRYPTION // SYSTEM REVEAL",
          decodedPhrase: "THE ANATOMY OF A LEGAL CARTEL",
          subtext: "RECOVERED FROM DELETED EXECUTIVE ARCHIVES",
        }}
      />

      <Composition
        id="HighlighterWipe"
        component={HighlighterWipeText as any}
        durationInFrames={90}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          badgeText: "KEY FORENSIC TAKEAWAY",
          statement: "When an industry gets completely closed off, the winning move is never playing by their rules.",
          highlightedPhrase: "never playing by their rules",
          subtext: "THE REASON AIRBEDS BEAT 100-YEAR-OLD HOTEL CARTELS",
        }}
      />

      <Composition
        id="WordByWordPop"
        component={WordByWordPop as any}
        durationInFrames={90}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          phrase: "YOU CANNOT OUT-SPEND A BILLION-DOLLAR CARTEL · YOU HAVE TO OUT-THINK THEM",
          subtext: "THE ASYMMETRIC ADVANTAGE",
          framesPerWord: 4,
        }}
      />

      <Composition
        id="SplitWordCollision"
        component={SplitWordCollision as any}
        durationInFrames={90}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          leftWord: "THE PROMISE",
          rightWord: "THE REALITY",
          centerBadge: "VS",
          subtext: "WHAT THEY PITCHED INVESTORS VS WHAT THEY ACTUALLY DELIVERED",
        }}
      />

      <Composition
        id="StrikethroughSlam"
        component={StrikethroughSlam as any}
        durationInFrames={90}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          badgeText: "CORPORATE MYTH DISPATCH",
          mythStatement: "“Cleaning fees are strictly passed along 100% to independent local cleaners.”",
          strikeLabel: "FALSE // SYSTEM AUDIT",
          truthStatement: "INTERNAL AUDIT: Over 70% of operators use automated outsourced software and pocket the spread.",
        }}
      />

      <Composition
        id="FloatingPillBadge"
        component={FloatingPillBadge as any}
        durationInFrames={90}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          icon: "✦",
          pillText: "$1,150 OVERDUE RENT // 72 HOURS TO EVICTION",
          subtext: "CRITICAL TURNING POINT",
          variant: "lime",
          position: "center",
        }}
      />

      <Composition
        id="Perspective3DTilt"
        component={Perspective3DTilt as any}
        durationInFrames={90}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          category: "THE SYSTEMIC QUESTION",
          headlineLine1: "HOW AN $80 AIRBED",
          headlineLine2: "HIJACKED A $100B INDUSTRY",
          subtext: "THE ANATOMY OF A SILICON VALLEY SYSTEM ARBITRAGE",
        }}
      />

      <Composition
        id="StaggeredWave"
        component={StaggeredWaveText as any}
        durationInFrames={90}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          badgeText: "ROAST & REVEAL // THE BITTER TRUTH",
          punchline: "THEY DID NOT INVENT A NEW MARKET · THEY MONETIZED DESPERATION",
          highlightWords: ["MONETIZED", "DESPERATION"],
          subtext: "WHEN AIR MATTRESSES BECOME A $100B ASYMMETRIC WEAPON",
        }}
      />

      {/* New Evidence & Forensic Compositions (32+ Expansion) */}
      <Composition
        id="TerminalCodeBlock"
        component={TerminalCodeBlock as any}
        durationInFrames={120}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          channel: "thinklate",
          windowTitle: "root@hermes-daemon: /var/log/arbitrage_engine",
          commands: [
            "curl -X POST https://api.hotel-cartel.internal/v1/rates --data '{\"city\": \"SFO\", \"conference\": true}'",
            "grep -i 'surge_multiplier' >> surge_dump.json",
          ],
          outputLines: [
            { text: "[200 OK] Received 48,192 rate quotes across 412 properties", tag: "INFO", color: "#10B981" },
            { text: "WARNING: SFO occupancy exceeds 98.4%. Artificial bottleneck detected.", tag: "ALERT", color: "#F59E0B" },
            { text: "CRITICAL: Base price inflated from $120 to $480/night (+300% cartel spread)", tag: "SURGE", color: "#EF4444" },
            { text: "DISCOVERY: 3 Living room rugs registered on Airbedandbreakfast.com @ $80/night", tag: "ARBITRAGE", color: "#00F0FF" },
          ],
          statusText: "EXECUTION THREAD // RECORD VERIFIED",
          executionTime: "4.2ms",
        }}
      />

      <Composition
        id="TimelineMilestoneFlow"
        component={TimelineMilestoneFlow as any}
        durationInFrames={120}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          channel: "thinklate",
          badgeText: "HISTORICAL SEQUENCE // CRITICAL TURNING POINTS",
          title: "THE 4-STAGE BOOTSTRAP TO UNICORN VELOCITY",
          milestones: [
            { date: "OCT 2007", title: "THE $80 AIRBED", desc: "3 air mattresses on living room floor pays $1,150 rent.", active: false },
            { date: "AUG 2008", title: "OBAMA O'S CEREAL", desc: "$30K election cereal boxes bootstrap 3 months runway.", active: false },
            { date: "JAN 2009", title: "Y COMBINATOR RESCUE", desc: "Paul Graham: 'If you can sell $40 cereal, you won't die.'", active: true },
            { date: "NOV 2011", title: "$1B VALUATION", desc: "Global disruption of the legacy hotel cartel finalized.", active: false },
          ],
          footerNote: "SOURCE: FOUNDER DEPOSITIONS ✦ Y COMBINATOR ARCHIVES W09",
        }}
      />

      <Composition
        id="AudioWaveformCard"
        component={AudioWaveformCard as any}
        durationInFrames={120}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          channel: "thinklate",
          speakerTag: "LEAKED BOARDROOM AUDIO // SAN FRANCISCO",
          speakerName: "INVESTOR / HOTEL LOBBYIST RECORDING",
          audioTitle: "WIRETAP #891: 'NOBODY WANTS TO SLEEP ON AN AIRBED'",
          durationStr: "00:14 / 01:30",
          transcriptSnippet: "They think they can replace a Hilton with a $20 air mattress? Let them burn through their seed money. It will die in six weeks.",
          highlightWords: "Let them burn through their seed money",
          barsCount: 38,
        }}
      />

      <Composition
        id="MapLocusRadar"
        component={MapLocusRadar as any}
        durationInFrames={120}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          channel: "thinklate",
          targetTitle: "GEOGRAPHIC MONOPOLY ANALYSIS // SAN FRANCISCO",
          coordinates: "LAT 37.7749° N, LON 122.4194° W",
          radiusMiles: "2.4 MILE RADIUS // MOSCONE CENTER",
          locationName: "SAN FRANCISCO DOWNTOWN HOTEL CLUSTER",
          poiList: [
            { name: "Moscone Convention Center", distance: "0.2 mi", status: "SOLD OUT (100%)", alert: true },
            { name: "Union Square Luxury Hotels", distance: "0.5 mi", status: "SURGE: $450/NT", alert: true },
            { name: "Rucker Living Room (Airbed HQ)", distance: "1.1 mi", status: "ONLINE ($80/NT)", alert: false },
            { name: "SFO Airport Perimeter Hotels", distance: "11.4 mi", status: "COMMUTE: 65 MIN", alert: false },
          ],
          footerNote: "SOURCE: SF TRAVEL ASSOCIATION & MUNICIPAL HOTEL OCCUPANCY RECORDS",
        }}
      />

      <Composition
        id="PhotoPolaroidPin"
        component={PhotoPolaroidPin as any}
        durationInFrames={120}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          channel: "thinklate",
          exhibitBadge: "EVIDENCE ARCHIVE // EXHIBIT #104",
          title: "THE ORIGINAL 3 AIR MATTRESSES ON LIVING ROOM RUG",
          handwrittenNote: "\"Took photo before first 3 design conference guests arrived. $80 cash in envelope.\" - Joe",
          dateStr: "OCTOBER 19, 2007",
          stampText: "AUTHENTICATED RECORD",
          tiltDeg: -2.5,
        }}
      />

      {/* Documentary & Elite Explainer Compositions (Nitish Rajput, Alux, Vox, Infographics) */}
      <Composition
        id="MagnifyingGlassDoc"
        component={MagnifyingGlassDoc as any}
        durationInFrames={120}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          channel: "thinklate",
          documentTitle: "MUNICIPAL HOUSING REGULATION // SECTION 402(B)",
          docketNo: "SAN FRANCISCO HOUSING AUTHORITY // DOCKET #07-8891",
          preambleText: "It is strictly unlawful for any tenant to sublease residential space without written consent, and specifically, ",
          magnifiedText: "charging nightly accommodation fees without a commercial hotel license constitutes an immediate misdemeanor",
          postambleText: ", subjecting all primary occupants to emergency eviction within seventy-two hours of notice.",
          stampText: "REGULATORY VIOLATION",
          footerNote: "OFFICIAL RECORD // CITY & COUNTY OF SAN FRANCISCO HOUSING CODE",
        }}
      />

      <Composition
        id="CharacterProfileCard"
        component={CharacterProfileCard as any}
        durationInFrames={120}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          channel: "thinklate",
          characterName: "BRIAN CHESKY",
          designation: "CO-FOUNDER & CEO // AIRBNB",
          photoUrl: "",
          statusBadge: "SUBJECT DOSSIER // ASYMMETRIC FOUNDER",
          stats: [
            { label: "OCTOBER 2007 RENT", value: "$1,150 (OVERDUE)", color: "#EF4444" },
            { label: "FIRST REVENUE", value: "$240 (3 AIRBEDS)", color: "#00F0FF" },
            { label: "CEREAL SEED CAPITAL", value: "$30,000 CASH", color: "#F59E0B" },
            { label: "PEAK VALUATION", value: "$100,000,000,000", color: "#10B981" },
          ],
          stampTag: "DISRUPTION PROVEN",
          quoteSnippet: "\"If we can't pay rent, we make rent our product.\"",
        }}
      />

      <Composition
        id="RankedListicleCard"
        component={RankedListicleCard as any}
        durationInFrames={120}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          channel: "thinklate",
          rankNumber: "01",
          categoryTag: "RULE #01 // THE SYSTEM ARBITRAGE",
          headline: "THE ASSET-LIGHT ADVANTAGE",
          subExplanation: "Traditional hotel empires spent $100M per tower on concrete, staff, and debt. Airbnb scaled to 100,000 rooms with $0 spent on physical real estate.",
          footerMetric: "CAPITAL EFFICIENCY RATIO: 416X MULTIPLIER",
        }}
      />

      <Composition
        id="ConspiracyPinBoard"
        component={ConspiracyPinBoard as any}
        durationInFrames={120}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          channel: "thinklate",
          boardTitle: "FORENSIC CONNECTION // ASYMMETRIC VALUE TRAIL",
          leftEntity: {
            name: "THE $80 AIRBED RUG",
            tag: "BOOTSTRAP PROTOTYPE // SFO",
            detail: "3 Living room mattresses funded founder rent in October 2007",
            icon: "🛏️",
          },
          rightEntity: {
            name: "HILTON & MARRIOTT CARTEL",
            tag: "LEGACY MONOPOLY // $140B",
            detail: "Overpriced room rates during SFO design conference created artificial bottleneck",
            icon: "🏨",
          },
          connectionLabel: "71.4% VALUE ARBITRAGE EXPLOITED",
          evidenceNote: "EVIDENCE CORRELATION: DIRECT SYSTEM ARBITRAGE CONFIRMED BY TRANSACTION MANIFEST",
        }}
      />

      <Composition
        id="WatchMojoCountdown"
        component={WatchMojoCountdown as any}
        durationInFrames={120}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          channel: "thinklate",
          rank: "#01",
          title: "THE ASSET-LIGHT ARBITRAGE",
          subtitle: "AIRBNB DEFEATS THE 100-YEAR HOTEL CARTEL",
          category: "GREATEST MARKET DISRUPTIONS OF ALL TIME",
          iconName: "trophy",
          statHighlight: "416X CAPITAL EFFICIENCY",
        }}
      />

      <Composition
        id="RoughSketchChart"
        component={RoughSketchChart as any}
        durationInFrames={120}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          channel: "thinklate",
          title: "THE ASSET OVERHEAD DISPARITY",
          subtitle: "PHYSICAL CONCRETE CAPITAL VS ZERO-ASSET CODEBASE",
          leftLabel: "MARRIOTT + HILTON (100 YEARS)",
          leftAmount: "$140 BILLION (DEBT + BUILDINGS)",
          leftHeightPercent: 85,
          rightLabel: "AIRBED & BREAKFAST (LINES OF CODE)",
          rightAmount: "$100 BILLION (ZERO PROPERTY)",
          rightHeightPercent: 65,
          handwrittenNote: "✦ 0 Physical Real Estate Owned. 100% Platform Margin.",
        }}
      />

      <Composition
        id="LottieAnimationCard"
        component={LottieAnimationCard as any}
        durationInFrames={120}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          channel: "thinklate",
          badgeText: "VECTOR MOTION GRAPHIC // SYSTEM RESOLUTION",
          headline: "THE ASYMMETRIC FLYWHEEL ACTIVATED",
          explanation: "When supply acquisition cost drops to near zero, growth compounds without physical friction.",
          statValue: "0% CAPITAL DEBT",
          statLabel: "PHYSICAL PROPERTY RATIO",
        }}
      />

      {/* New Kinetic Typography Compositions */}
      <Composition
        id="TextMaskWipe"
        component={TextMaskWipe as any}
        durationInFrames={90}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          channel: "thinklate",
          topLine: "THE UNCOMFORTABLE REALITY",
          mainText: "SYSTEMIC ARBITRAGE",
          subText: "HOW FOUNDERS EXPLOIT MONOPOLY BOTTLENECKS",
          accentWord: "ARBITRAGE",
        }}
      />

      <Composition
        id="KineticScrollLadder"
        component={KineticScrollLadder as any}
        durationInFrames={90}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          channel: "thinklate",
          items: [
            "$450 LUXURY HOTEL ROOM",
            "$320 AIRPORT MOTEL SUITE",
            "$180 OVERPRICED HOSTEL",
            "$80 AIRBED ON A LIVING ROOM RUG",
          ],
          selectedIndex: 3,
          subtitle: "THE WINNING VALUE EQUATION",
        }}
      />

      <Composition
        id="ElasticBungeeText"
        component={ElasticBungeeText as any}
        durationInFrames={90}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          channel: "thinklate",
          text: "100% ILLEGAL",
          subtitle: "ACCORDING TO MUNICIPAL HOTEL REGULATIONS",
          highlightWord: "ILLEGAL",
        }}
      />

      <Composition
        id="TextTrailOutline"
        component={TextTrailOutline as any}
        durationInFrames={90}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          channel: "thinklate",
          text: "DISRUPTION",
          subtitle: "WHEN THE OLD RULES CEASE TO FUNCTION",
        }}
      />

      <Composition
        id="TypographyBackgroundWall"
        component={TypographyBackgroundWall as any}
        durationInFrames={90}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          channel: "thinklate",
          wallText: "DISRUPT MONOPOLY SCALE ARBITRAGE BOOTSTRAP CASHFLOW",
          centerBadgeText: "UNFAIR ADVANTAGE DETECTED",
          centerStatement: "ZERO ASSET OVERHEAD",
          subNote: "Traditional hotels own $100M concrete assets. Airbnb owns lines of code.",
        }}
      />

      <Composition
        id="CurtainSwipeReveal"
        component={CurtainSwipeReveal as any}
        durationInFrames={90}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          channel: "thinklate",
          heading: "THE FOUNDERS DIDN'T RAISE VC MONEY.",
          punchline: "THEY SOLD BREAKFAST CEREAL.",
          categoryTag: "UNCONVENTIONAL EXECUTION",
        }}
      />
    </>
  );
};
