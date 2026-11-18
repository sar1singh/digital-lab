import type { Metadata } from "next";
import { Inter, Plus_Jakarta_Sans, JetBrains_Mono } from "next/font/google";
import "./globals.css";

const inter = Inter({
  subsets: ["latin"],
  variable: "--font-inter",
  display: "swap",
});

const jakarta = Plus_Jakarta_Sans({
  subsets: ["latin"],
  variable: "--font-jakarta",
  weight: ["600", "700", "800"],
  display: "swap",
});

const mono = JetBrains_Mono({
  subsets: ["latin"],
  variable: "--font-mono",
  weight: ["400", "500", "600"],
  display: "swap",
});

export const metadata: Metadata = {
  title: "ShipLink — Zero-Login Magic Client Status & Sign-Off Portal",
  description:
    "Share live project milestones and capture client approvals with one magic URL. Zero client logins, zero password fatigue, built in 10 seconds.",
  keywords: [
    "no login client portal",
    "client status tracker",
    "magic link milestone approval",
    "agency client update tool",
    "share project progress without login",
  ],
};

const structuredData = {
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "SoftwareApplication",
      name: "ShipLink",
      applicationCategory: "BusinessApplication",
      operatingSystem: "Web",
      description:
        "Zero-login magic-link client progress tracker and milestone approval portal for freelance developers, technical consultants, and agencies.",
      offers: {
        "@type": "Offer",
        price: "0",
        priceCurrency: "USD",
      },
    },
    {
      "@type": "FAQPage",
      mainEntity: [
        {
          "@type": "Question",
          name: "Do my clients or stakeholders need an account to view progress?",
          acceptedAnswer: {
            "@type": "Answer",
            text: "No. Clients open one magic URL directly in any mobile or desktop browser without creating a password or logging in, review deliverables, and click Approve or Request Changes.",
          },
        },
        {
          "@type": "Question",
          name: "How is ShipLink different from Jira, Linear, or bloated client portals?",
          acceptedAnswer: {
            "@type": "Answer",
            text: "Jira and Linear force client seat logins and expose internal ticket noise. Heavy portals cost $49 to $150 per month and take hours to configure. ShipLink generates a clean client-ready status and approval link in 10 seconds.",
          },
        },
        {
          "@type": "Question",
          name: "How does the Pro GitHub and Linear sync tier work?",
          acceptedAnswer: {
            "@type": "Answer",
            text: "The Phase 2 AWS serverless Pro tier connects GitHub pull requests and Linear or Jira issues via EventBridge webhooks to advance client milestones automatically and send read and sign-off receipts to Slack or email.",
          },
        },
      ],
    },
  ],
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className={`${inter.variable} ${jakarta.variable} ${mono.variable}`}>
      <body className="min-h-screen flex flex-col font-sans bg-[#F8FAFC] text-[#0F172A] selection:bg-indigo-100 selection:text-indigo-900">
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(structuredData) }}
        />
        {children}
      </body>
    </html>
  );
}
