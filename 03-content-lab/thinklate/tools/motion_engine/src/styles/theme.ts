export type ChannelId = "thinklate" | "offscript" | "sarwanology" | "general";

export interface ChannelTheme {
  id: ChannelId;
  name: string;
  colors: {
    accent: string;
    accentSecondary: string;
    bgGlass: string;
    bgGlassDark: string;
    bgGlassLight: string;
    borderGlass: string;
    borderAccent: string;
    borderWarning: string;
    textWhite: string;
    textMuted: string;
    textDim: string;
    highlightInk: string;
  };
  shadows: {
    glass: string;
    glowAccent: string;
    glowSecondary: string;
    glowWarning: string;
  };
  fonts: {
    sans: string;
    mono: string;
    display: string;
  };
  motion: {
    damping: number;
    mass: number;
    stiffness: number;
    speedMultiplier: number;
  };
}

export const CHANNEL_THEMES: Record<ChannelId, ChannelTheme> = {
  // 1. ThinkLate: Conversational Infotainment, Tech & Solo-Founders
  thinklate: {
    id: "thinklate",
    name: "ThinkLate (@wethinklate)",
    colors: {
      accent: "#E2FF00", // Electric Acid Lime
      accentSecondary: "#06B6D4", // Electric Cyan
      bgGlass: "rgba(10, 15, 26, 0.48)", // Translucent Obsidian
      bgGlassDark: "rgba(8, 12, 22, 0.58)",
      bgGlassLight: "rgba(255, 255, 255, 0.05)",
      borderGlass: "rgba(255, 255, 255, 0.16)",
      borderAccent: "rgba(226, 255, 0, 0.45)",
      borderWarning: "rgba(239, 68, 68, 0.45)",
      textWhite: "#F8FAFC",
      textMuted: "#CBD5E1",
      textDim: "#94A3B8",
      highlightInk: "#05080F",
    },
    shadows: {
      glass: "0 20px 50px rgba(0, 0, 0, 0.45), 0 0 0 1px rgba(255, 255, 255, 0.12)",
      glowAccent: "0 0 35px rgba(226, 255, 0, 0.35)",
      glowSecondary: "0 0 35px rgba(6, 182, 212, 0.35)",
      glowWarning: "0 0 35px rgba(239, 68, 68, 0.4)",
    },
    fonts: {
      sans: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif',
      mono: 'ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace',
      display: '"Archivo Black", -apple-system, sans-serif',
    },
    motion: {
      damping: 14,
      mass: 0.8,
      stiffness: 105,
      speedMultiplier: 1.0,
    },
  },

  // 2. Off Script: High-Octane Unscripted Gaming Commentary, Satire & Roasts
  offscript: {
    id: "offscript",
    name: "Off Script (@OffScriptEddy)",
    colors: {
      accent: "#FF5500", // High-Voltage Flame Orange
      accentSecondary: "#00F0FF", // Cyber Neon Cyan
      bgGlass: "rgba(18, 18, 26, 0.52)", // Smoked Matte Carbon
      bgGlassDark: "rgba(12, 12, 18, 0.65)",
      bgGlassLight: "rgba(255, 255, 255, 0.07)",
      borderGlass: "rgba(255, 255, 255, 0.18)",
      borderAccent: "rgba(255, 85, 0, 0.55)",
      borderWarning: "rgba(255, 0, 85, 0.55)",
      textWhite: "#FFFFFF",
      textMuted: "#E2E8F0",
      textDim: "#A0AEC0",
      highlightInk: "#000000",
    },
    shadows: {
      glass: "0 20px 50px rgba(0, 0, 0, 0.6), 0 0 0 1px rgba(255, 255, 255, 0.15)",
      glowAccent: "0 0 40px rgba(255, 85, 0, 0.45)",
      glowSecondary: "0 0 40px rgba(0, 240, 255, 0.4)",
      glowWarning: "0 0 40px rgba(255, 0, 85, 0.5)",
    },
    fonts: {
      sans: '"Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif',
      mono: '"Space Mono", ui-monospace, Menlo, monospace',
      display: '"Impact", "Bebas Neue", sans-serif',
    },
    motion: {
      damping: 10, // Faster, violent snap
      mass: 0.55,
      stiffness: 160,
      speedMultiplier: 1.25, // Snappier for rapid gamer pacing
    },
  },

  // 3. Sarwanology: Systems Engineering, Deep Philosophy & Wealth Architecture
  sarwanology: {
    id: "sarwanology",
    name: "Sarwanology (Founder Architecture)",
    colors: {
      accent: "#6366F1", // Electric Indigo / Violet
      accentSecondary: "#10B981", // Emerald Matrix
      bgGlass: "rgba(15, 23, 42, 0.45)", // Slate Glass
      bgGlassDark: "rgba(10, 15, 30, 0.58)",
      bgGlassLight: "rgba(255, 255, 255, 0.04)",
      borderGlass: "rgba(255, 255, 255, 0.14)",
      borderAccent: "rgba(99, 102, 241, 0.45)",
      borderWarning: "rgba(244, 63, 94, 0.45)",
      textWhite: "#F8FAFC",
      textMuted: "#CBD5E1",
      textDim: "#94A3B8",
      highlightInk: "#0B0F19",
    },
    shadows: {
      glass: "0 20px 50px rgba(0, 0, 0, 0.4), 0 0 0 1px rgba(255, 255, 255, 0.1)",
      glowAccent: "0 0 35px rgba(99, 102, 241, 0.35)",
      glowSecondary: "0 0 35px rgba(16, 185, 129, 0.35)",
      glowWarning: "0 0 35px rgba(244, 63, 94, 0.4)",
    },
    fonts: {
      sans: '-apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif',
      mono: '"JetBrains Mono", ui-monospace, Menlo, monospace',
      display: '"Playfair Display", Georgia, serif',
    },
    motion: {
      damping: 16,
      mass: 0.9,
      stiffness: 95,
      speedMultiplier: 0.9, // Elegant, deliberate
    },
  },

  // Fallback General
  general: {
    id: "general",
    name: "Universal Broadcast",
    colors: {
      accent: "#E2FF00",
      accentSecondary: "#06B6D4",
      bgGlass: "rgba(10, 15, 26, 0.48)",
      bgGlassDark: "rgba(8, 12, 22, 0.58)",
      bgGlassLight: "rgba(255, 255, 255, 0.05)",
      borderGlass: "rgba(255, 255, 255, 0.16)",
      borderAccent: "rgba(226, 255, 0, 0.45)",
      borderWarning: "rgba(239, 68, 68, 0.45)",
      textWhite: "#F8FAFC",
      textMuted: "#CBD5E1",
      textDim: "#94A3B8",
      highlightInk: "#05080F",
    },
    shadows: {
      glass: "0 20px 50px rgba(0, 0, 0, 0.45), 0 0 0 1px rgba(255, 255, 255, 0.12)",
      glowAccent: "0 0 35px rgba(226, 255, 0, 0.35)",
      glowSecondary: "0 0 35px rgba(6, 182, 212, 0.35)",
      glowWarning: "0 0 35px rgba(239, 68, 68, 0.4)",
    },
    fonts: {
      sans: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
      mono: 'ui-monospace, SFMono-Regular, Menlo, monospace',
      display: '-apple-system, BlinkMacSystemFont, sans-serif',
    },
    motion: {
      damping: 14,
      mass: 0.8,
      stiffness: 105,
      speedMultiplier: 1.0,
    },
  },
};

// Helper to retrieve theme by channel id
export function getChannelTheme(channel?: string): ChannelTheme {
  if (!channel) return CHANNEL_THEMES.thinklate;
  const key = channel.toLowerCase().replace(/[^a-z]/g, "") as ChannelId;
  return CHANNEL_THEMES[key] || CHANNEL_THEMES.thinklate;
}

// Backward compatibility export
export const THEME = {
  colors: {
    bgGlass: CHANNEL_THEMES.thinklate.colors.bgGlass,
    bgGlassDark: CHANNEL_THEMES.thinklate.colors.bgGlassDark,
    bgGlassLight: CHANNEL_THEMES.thinklate.colors.bgGlassLight,
    borderGlass: CHANNEL_THEMES.thinklate.colors.borderGlass,
    borderAccent: CHANNEL_THEMES.thinklate.colors.borderAccent,
    borderCrimson: CHANNEL_THEMES.thinklate.colors.borderWarning,
    textWhite: CHANNEL_THEMES.thinklate.colors.textWhite,
    textMuted: CHANNEL_THEMES.thinklate.colors.textMuted,
    textDim: CHANNEL_THEMES.thinklate.colors.textDim,
    acidLime: CHANNEL_THEMES.thinklate.colors.accent,
    warmAmber: "#F59E0B",
    crimsonRed: "#EF4444",
    cyanElectric: "#06B6D4",
  },
  shadows: {
    glass: CHANNEL_THEMES.thinklate.shadows.glass,
    glassHover: "0 25px 60px rgba(0, 0, 0, 0.55), 0 0 0 1px rgba(226, 255, 0, 0.3)",
    glowLime: CHANNEL_THEMES.thinklate.shadows.glowAccent,
    glowAmber: "0 0 35px rgba(245, 158, 11, 0.35)",
    glowCrimson: CHANNEL_THEMES.thinklate.shadows.glowWarning,
  },
  fonts: CHANNEL_THEMES.thinklate.fonts,
};
