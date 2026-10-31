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

  // Receipt drops in with physical paper bounce & slight rotation
  const dropSpring = spring({
    frame,
    fps,
    config: { damping: 13, mass: 0.9, stiffness: 110 },
  });

  const opacity = interpolate(frame, [0, 8], [0, 1], { extrapolateRight: "clamp" });

  const stampSpring = spring({
    frame: Math.max(0, frame - 16),
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
          width: "720px",
          backgroundColor: "#FDFBF7",
          color: "#0F172A",
          boxShadow: "0 30px 80px rgba(0, 0, 0, 0.75), 0 0 0 1px rgba(255, 255, 255, 0.2)",
          padding: "48px 52px",
          transform: `translateY(${(1 - dropSpring) * -60}px) rotate(${(1 - dropSpring) * -6 - 2}deg) scale(${dropSpring})`,
          opacity,
          position: "relative",
          clipPath:
            "polygon(0% 12px, 4% 0px, 8% 12px, 12% 0px, 16% 12px, 20% 0px, 24% 12px, 28% 0px, 32% 12px, 36% 0px, 40% 12px, 44% 0px, 48% 12px, 52% 0px, 56% 12px, 60% 0px, 64% 12px, 68% 0px, 72% 12px, 76% 0px, 80% 12px, 84% 0px, 88% 12px, 92% 0px, 96% 12px, 100% 0px, 100% calc(100% - 12px), 96% 100%, 92% calc(100% - 12px), 88% 100%, 84% calc(100% - 12px), 80% 100%, 76% calc(100% - 12px), 72% 100%, 68% calc(100% - 12px), 64% 100%, 60% calc(100% - 12px), 56% 100%, 52% calc(100% - 12px), 48% 100%, 44% calc(100% - 12px), 40% 100%, 36% calc(100% - 12px), 32% 100%, 28% calc(100% - 12px), 24% 100%, 20% calc(100% - 12px), 16% 100%, 12% calc(100% - 12px), 8% 100%, 4% calc(100% - 12px), 0% 100%)",
        }}
      >
        {/* Receipt Header */}
        <div style={{ textAlign: "center", borderBottom: "2px dashed #94A3B8", paddingBottom: "18px", marginBottom: "20px" }}>
          <h2 style={{ fontSize: "24px", fontWeight: 900, letterSpacing: "0.1em", margin: "0 0 6px 0", textTransform: "uppercase" }}>
            {receiptTitle}
          </h2>
          <div style={{ fontSize: "12px", color: "#64748B", letterSpacing: "0.15em" }}>{storeLocation}</div>
          <div style={{ fontSize: "11px", color: "#94A3B8", marginTop: "4px" }}>{dateStr}</div>
        </div>

        {/* Line Items */}
        <div style={{ display: "flex", flexDirection: "column", gap: "10px", marginBottom: "20px" }}>
          {lineItems.map((item, idx) => (
            <div
              key={idx}
              style={{
                display: "flex",
                justifyContent: "space-between",
                fontSize: "15px",
                color: item.isJunkFee ? "#DC2626" : "#1E293B",
                fontWeight: item.isJunkFee ? 800 : 500,
              }}
            >
              <span>{item.isJunkFee ? `⚠️ ${item.name}` : item.name}</span>
              <span>{item.amount}</span>
            </div>
          ))}
        </div>

        {/* Subtotal & Total */}
        <div style={{ borderTop: "2px dashed #94A3B8", paddingTop: "14px", display: "flex", flexDirection: "column", gap: "6px" }}>
          <div style={{ display: "flex", justifyContent: "space-between", fontSize: "14px", color: "#64748B" }}>
            <span>BASE ADVERTISED RATE</span>
            <span>{subtotal}</span>
          </div>
          <div style={{ display: "flex", justifyContent: "space-between", fontSize: "28px", fontWeight: 900, color: "#0F172A", borderTop: "1px solid #CBD5E1", paddingTop: "8px" }}>
            <span>FINAL TOTAL</span>
            <span style={{ color: "#DC2626" }}>{total}</span>
          </div>
        </div>

        {/* Footer */}
        <div style={{ textAlign: "center", marginTop: "24px", fontSize: "11px", color: "#64748B", borderTop: "1px dashed #CBD5E1", paddingTop: "12px" }}>
          {footerMessage}
        </div>

        {/* Physical Ink Stamp */}
        <div
          style={{
            position: "absolute",
            top: "45%",
            right: "24px",
            transform: `translateY(-50%) rotate(-14deg) scale(${stampSpring})`,
            opacity: stampSpring,
            border: "4px solid #DC2626",
            borderRadius: "10px",
            padding: "8px 20px",
            fontFamily: THEME.fonts.mono,
            fontWeight: 900,
            fontSize: "18px",
            letterSpacing: "0.15em",
            color: "#DC2626",
            textTransform: "uppercase",
            boxShadow: "0 0 20px rgba(220, 38, 38, 0.4)",
            pointerEvents: "none",
          }}
        >
          {stampText}
        </div>
      </div>
    </div>
  );
};
