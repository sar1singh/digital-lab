import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { THEME } from "../../styles/theme";

export interface ReceiptLineItem {
  name: string;
  amount: string;
  isJunkFee?: boolean;
}

export interface TornPaperReceiptProps {
  receiptTitle?: string;
  storeLocation?: string;
  dateStr?: string;
  lineItems?: ReceiptLineItem[];
  subtotal?: string;
  total?: string;
  stampText?: string;
  footerMessage?: string;
}

export const TornPaperReceipt: React.FC<TornPaperReceiptProps> = ({
  receiptTitle = "THE INVOICE ANATOMY",
  storeLocation = "AIRBED & BREAKFAST PLATFORM RECEIPT",
  dateStr = "OCTOBER 14, 2023 // 14:22:09",
  lineItems = [
    { name: "2 Nights Living Room Stay", amount: "$160.00", isJunkFee: false },
    { name: "Mandatory Platform Service Fee", amount: "$38.40", isJunkFee: true },
    { name: "Standard Cleaning Fee", amount: "$110.00", isJunkFee: true },
    { name: "Host Chore Checklist Penalty", amount: "$50.00", isJunkFee: true },
    { name: "Local Occupancy Tax", amount: "$28.10", isJunkFee: false },
  ],
  subtotal = "$160.00",
  total = "$386.50",
  stampText = "141% JUNK FEE MARKUP",
  footerMessage = "ORIGINAL RATE: $80/NIGHT  ✦  FINAL CHECKOUT: $193.25/NIGHT",
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Motion 1: Receipt drops in with physical paper bounce & slight rotation
  const dropSpring = spring({
    frame,
    fps,
    config: { damping: 13, mass: 0.9, stiffness: 110 },
  });

  const opacity = interpolate(frame, [0, 8], [0, 1], { extrapolateRight: "clamp" });

  // Motion 4: Stamp slams at frame 28
  const stampSpring = spring({
    frame: Math.max(0, frame - 28),
    fps,
    config: { damping: 10, mass: 0.5, stiffness: 170 },
  });

  return (
    <div
      style={{
        width: "100%",
        height: "100%",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        fontFamily: THEME.fonts.mono,
        backgroundColor: "transparent",
      }}
    >
      <div
        style={{
          width: "980px",
          backgroundColor: "#FDFBF7",
          color: "#0F172A",
          boxShadow: "0 30px 80px rgba(0, 0, 0, 0.75), 0 0 0 1px rgba(255, 255, 255, 0.2)",
          padding: "54px 64px",
          transform: `translateY(${(1 - dropSpring) * -60}px) rotate(${(1 - dropSpring) * -4 - 1.5}deg) scale(${dropSpring})`,
          opacity,
          position: "relative",
          clipPath:
            "polygon(0% 12px, 4% 0px, 8% 12px, 12% 0px, 16% 12px, 20% 0px, 24% 12px, 28% 0px, 32% 12px, 36% 0px, 40% 12px, 44% 0px, 48% 12px, 52% 0px, 56% 12px, 60% 0px, 64% 12px, 68% 0px, 72% 12px, 76% 0px, 80% 12px, 84% 0px, 88% 12px, 92% 0px, 96% 12px, 100% 0px, 100% calc(100% - 12px), 96% 100%, 92% calc(100% - 12px), 88% 100%, 84% calc(100% - 12px), 80% 100%, 76% calc(100% - 12px), 72% 100%, 68% calc(100% - 12px), 64% 100%, 60% calc(100% - 12px), 56% 100%, 52% calc(100% - 12px), 48% 100%, 44% calc(100% - 12px), 40% 100%, 36% calc(100% - 12px), 32% 100%, 28% calc(100% - 12px), 24% 100%, 20% calc(100% - 12px), 16% 100%, 12% calc(100% - 12px), 8% 100%, 4% calc(100% - 12px), 0% 100%)",
        }}
      >
        {/* Receipt Header */}
        <div style={{ textAlign: "center", borderBottom: "2px dashed #94A3B8", paddingBottom: "20px", marginBottom: "24px" }}>
          <h2 style={{ fontSize: "34px", fontWeight: 900, letterSpacing: "0.08em", margin: "0 0 8px 0", textTransform: "uppercase" }}>
            {receiptTitle}
          </h2>
          <div style={{ fontSize: "16px", color: "#475569", fontWeight: 700, letterSpacing: "0.12em" }}>{storeLocation}</div>
          <div style={{ fontSize: "14px", color: "#64748B", marginTop: "6px", fontFamily: THEME.fonts.mono }}>{dateStr}</div>
        </div>

        {/* Motion 2: Staggered Line Items (One after the other) */}
        <div style={{ display: "flex", flexDirection: "column", gap: "14px", marginBottom: "26px" }}>
          {lineItems.map((item, idx) => {
            const itemStart = 10 + idx * 5;
            const itemSpring = spring({
              frame: Math.max(0, frame - itemStart),
              fps,
              config: { damping: 12, mass: 0.5, stiffness: 150 },
            });
            const itemOpacity = interpolate(frame, [itemStart, itemStart + 4], [0, 1], {
              extrapolateLeft: "clamp",
              extrapolateRight: "clamp",
            });

            return (
              <div
                key={idx}
                style={{
                  display: "flex",
                  justifyContent: "space-between",
                  fontSize: "22px",
                  color: item.isJunkFee ? "#DC2626" : "#0F172A",
                  fontWeight: item.isJunkFee ? 900 : 700,
                  transform: `translateX(${(1 - itemSpring) * -16}px)`,
                  opacity: itemOpacity,
                }}
              >
                <span>{item.isJunkFee ? `⚠️ ${item.name}` : item.name}</span>
                <span style={{ fontVariantNumeric: "tabular-nums" }}>{item.amount}</span>
              </div>
            );
          })}
        </div>

        {/* Subtotal & Total */}
        <div style={{ borderTop: "2px dashed #94A3B8", paddingTop: "18px", display: "flex", flexDirection: "column", gap: "8px" }}>
          <div style={{ display: "flex", justifyContent: "space-between", fontSize: "18px", fontWeight: 700, color: "#475569" }}>
            <span>BASE ADVERTISED RATE</span>
            <span style={{ fontVariantNumeric: "tabular-nums" }}>{subtotal}</span>
          </div>
          <div style={{ display: "flex", justifyContent: "space-between", fontSize: "38px", fontWeight: 900, color: "#0F172A", borderTop: "2px solid #CBD5E1", paddingTop: "10px" }}>
            <span>FINAL CHECKOUT TOTAL</span>
            <span style={{ color: "#DC2626", fontVariantNumeric: "tabular-nums" }}>{total}</span>
          </div>
        </div>

        {/* Footer */}
        <div style={{ textAlign: "center", marginTop: "24px", fontSize: "15px", fontWeight: 700, color: "#475569", borderTop: "1px dashed #CBD5E1", paddingTop: "14px" }}>
          {footerMessage}
        </div>

        {/* Motion 4: Physical Ink Stamp */}
        <div
          style={{
            position: "absolute",
            top: "45%",
            right: "32px",
            transform: `translateY(-50%) rotate(-12deg) scale(${stampSpring})`,
            opacity: stampSpring,
            border: "5px solid #DC2626",
            borderRadius: "12px",
            padding: "12px 28px",
            fontFamily: THEME.fonts.mono,
            fontWeight: 900,
            fontSize: "24px",
            letterSpacing: "0.15em",
            color: "#DC2626",
            textTransform: "uppercase",
            boxShadow: "0 0 25px rgba(220, 38, 38, 0.45)",
            pointerEvents: "none",
          }}
        >
          {stampText}
        </div>
      </div>
    </div>
  );
};
