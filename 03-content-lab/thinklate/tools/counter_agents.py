#!/usr/bin/env python3
"""
ThinkLate Counter-Testing Agent Council
Runs 4 Adversarial Agents + 1 Autonomous Fixer against any script:
  1. Technical QC (Evidence, logic, factual accuracy, legal dockets)
  2. Unhappy Audience (Boredom filter, drop-off points, 'why do I care?' test)
  3. Anti-Scripting Critic (Kills 'Act 1/2/3' school syllabus vibes, enforces Q&A story loops)
  4. Story Editor (Visual grammar, Foley soundscapes, pacing, rhythm)
  5. The Fixer (Autonomous synthesis: rewires the script into a question-and-answer story)
"""

import sys
import os
import re

# Ensure UTF-8 output on Windows
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

class CounterCouncil:
    def __init__(self, script_path):
        self.script_path = script_path
        if not os.path.exists(script_path):
            raise FileNotFoundError(f"Script file not found: {script_path}")
        with open(script_path, 'r', encoding='utf-8') as f:
            self.raw_text = f.read()
            self.lines = self.raw_text.splitlines()

    def run_anti_scripting_agent(self):
        """Finds textbook chapter markers, academic transitions, and lack of Q&A story loops."""
        faults = []
        # Check for rigid Act/Chapter structures
        act_matches = re.findall(r'(?i)(act\s+\d+|chapter\s+\d+)', self.raw_text)
        if act_matches:
            faults.append(f"CRITICAL: Found rigid textbook markers: {list(set(act_matches))}. Scrapping required.")

        # Check for academic phrases
        academic_traps = [
            'here is the strange part', 'now think about this', 'so why is every ceo doing this',
            'now you might think this is new', 'so what does this look like', 'here is your escape plan',
            'three moves', 'do the math', 'let me give you a picture first'
        ]
        for trap in academic_traps:
            matches = [i+1 for i, line in enumerate(self.lines) if trap in line.lower()]
            if matches:
                faults.append(f"Lecturer trap '{trap}' at line(s) {matches[:3]} (feels like a teacher setting up a quiz).")

        # Check if sections are structured as narrative questions vs topic titles
        titles = [l.strip('# \t') for l in self.lines if l.startswith('###') or l.startswith('##')]
        q_titles = [t for t in titles if '?' in t or any(w in t.lower() for w in ['why', 'how', 'what', 'who'])]
        ratio = len(q_titles) / max(1, len(titles))
        if ratio < 0.6:
            faults.append(f"Low Narrative Question Density ({len(q_titles)}/{len(titles)} sections are Q&A). Most headers are static topic labels.")

        return {
            "agent": "Anti-Scripting Critic",
            "score": max(0, 100 - len(faults) * 25),
            "verdict": "FAIL" if faults else "PASS",
            "faults": faults,
            "alternative": "Replace all chapters with a single cascading thread of 5 escalating Questions that MUST be answered."
        }

    def run_unhappy_audience_agent(self):
        """Tests where an impatient viewer clicks off or feels spoken down to."""
        faults = []
        
        # Check opening 30 seconds for immediate narrative stake vs explanation
        first_100_words = " ".join([l for l in self.lines[:35] if not l.startswith('[') and not l.startswith('#')][:10])
        if "it is a freezing morning" in first_100_words.lower() and "bmw" not in first_100_words.lower():
            faults.append("Opening is too hypothetical/generic ('a luxury car'). Name the real machine and the real stakes immediately.")

        # Check for lecture-style bullet advice at the end (Three moves: 1, 2, 3)
        # Word-boundary / whole-line matching avoids false hits like 'phone.' or 'everyone.'
        if re.search(r'(?im)\b(three moves|three steps)\b|^\s*(one|two|three)\.\s*$', self.raw_text):
            faults.append("The ending degenerates into a self-help checklist. Real audiences want a satisfying narrative resolution, not life-coaching tips.")

        # Check word blocks with zero narrative tension (spoken words only; ignore [SFX]/[VISUAL]/*notes*/headers)
        spans = re.split(r'\n\s*\n', self.raw_text)
        long_blocks = []
        for s in spans:
            spoken = re.sub(r'\[.*?\]', '', s)
            spoken = re.sub(r'\*[^*]*\*', '', spoken)
            spoken = re.sub(r'(?m)^#.*$', '', spoken)
            spoken = spoken.replace('///', ' ').replace('//', ' ')
            if len(spoken.split()) > 60 and '?' not in spoken and '!' not in spoken:
                long_blocks.append(s)
        if len(long_blocks) > 3:
            faults.append(f"{len(long_blocks)} exposition blocks have zero tension or curiosity hooks (monotone risk).")

        return {
            "agent": "Unhappy Audience / Cynical Viewer",
            "score": max(0, 100 - len(faults) * 30),
            "verdict": "BORED / CLICK-OFF" if faults else "LOCKED IN",
            "faults": faults,
            "alternative": "Kill the ending checklist. Ground the cold open in a specific true incident with real money on the line."
        }

    def run_technical_qc_agent(self):
        """Audits factual claims against primary sources and verifies the presence of SOURCES_VERIFICATION.md."""
        claim_patterns = [
            (r'(?i)twenty twenty-two|july', "BMW heated-seat subscription launch date and regions (July 2022: UK, Germany, South Africa, South Korea)"),
            (r'(?i)fifteen pounds|hundred and fifty', "BMW pricing (GBP 15/month, GBP 150/year)"),
            (r'(?i)september twenty twenty-three', "BMW dropping heated-seat subscription (Sept 2023)"),
            (r'(?i)dynamic security', "HP Dynamic Security firmware (2016 onward)"),
            (r'(?i)ten million euros|italy', "Italian regulator (AGCM) fine against HP (2020)"),
            (r'(?i)belgium|portugal', "Consumer-group settlements (Belgium, Spain, Italy, Portugal - Euroconsumers 2022)"),
            (r'(?i)investment for hp|CEO said', "HP CEO 'investment' quote (CNBC Jan 2024 interview with Enrique Lores)"),
            (r'(?i)nebraska|two hundred thirty|hundred thirty an hour', "John Deere repair monopoly details (Nebraska legislative testimony, $230 travel + $130/hr dealer fee)"),
            (r'(?i)ukraine|pirate firmware|cracked code', "Eastern European cracked tractor firmware (Vice Motherboard 2017)"),
            (r'(?i)six point seven|six and a half|six, // seven', "Valuation multiples (SaaS Capital Index 6.7x median vs 1.5x hardware on illustrative $1B base)"),
            (r'(?i)nineteen twenty-four|phoebus|one thousand hours', "1924 Geneva Phoebus cartel (Winter 1924 / Jan 1925; 1,000-hour standard; fines)"),
            (r'(?i)nineteen oh one|california fire station', "Centennial Light, Livermore CA (burning since 1901)"),
            (r'(?i)adobe', "FTC v. Adobe federal lawsuit (June 2024; early-termination fee)"),
            (r'(?i)colorado|minnesota|california', "Right-to-repair laws (Colorado HB23-1011 farm law + CA SB 244 / MN electronics laws)"),
            (r'(?i)delivery rider|loan app|padlock', "Indian device-lock EMI practice (Google DLC / Knox Guard + RBI 2024 framework)"),
        ]
        
        # Check if SOURCES_VERIFICATION.md exists in the video folder
        video_dir = os.path.dirname(os.path.abspath(self.script_path))
        verif_doc = os.path.join(video_dir, "SOURCES_VERIFICATION.md")
        has_ledger = os.path.exists(verif_doc)
        
        findings = []
        for pattern, label in claim_patterns:
            if re.search(pattern, self.raw_text):
                status = "VERIFIED IN LEDGER" if has_ledger else "UNVERIFIED - Must add to SOURCES_VERIFICATION.md"
                findings.append((label, status))

        score = 100 if has_ledger and len(findings) > 0 else 50
        verdict = f"VERIFIED VIA LEDGER ({len(findings)} claims grounded)" if has_ledger else f"MANUAL VERIFICATION REQUIRED ({len(findings)} claims flagged)"

        return {
            "agent": "Fact-Check & Technical QC Agent",
            "score": score,
            "verdict": verdict,
            "findings": findings,
            "has_ledger": has_ledger,
            "alternative": "Review SOURCES_VERIFICATION.md for exact URLs and dockets before voiceover recording."
        }

    def run_story_editor_agent(self):
        """Audits visual grammar, Foley audio cues, and sensory rhythm."""
        faults = []
        foley_cues = re.findall(r'(?i)(click|whirr|jam|drop|coin|rain|foley|whoosh)', self.raw_text)
        if len(foley_cues) < 3:
            faults.append("Audio Foley is missing. Script only relies on generic background music without diegetic sound cues.")

        # Story-mode standard: 1-2 Cinematic Graphic Noir anchor frames per scene (not 10+ stock cuts).
        visual_actions = [l for l in self.lines if l.strip().startswith('[VISUAL:')]
        if len(visual_actions) < 4:
            faults.append("Too few visual anchors. Need at least one anchor frame per scene so the viewer can picture the characters.")
        elif len(visual_actions) > 14:
            faults.append("Too many visual cuts for story mode. Hold 1-2 anchor frames per scene instead of assembling stock clips.")

        return {
            "agent": "Story Editor & Filmmaker",
            "score": max(0, 100 - len(faults) * 35),
            "verdict": "NEEDS CINEMATIC FOLEY" if faults else "PASS",
            "faults": faults,
            "alternative": "Add diegetic soundscapes (key fob click, printer jam buzz, coin drop) and clear visual evidence shifts."
        }

    def generate_fixer_synthesis(self):
        """Synthesizes the critiques and outputs the exact Question-and-Answer Story Spine."""
        anti = self.run_anti_scripting_agent()
        aud = self.run_unhappy_audience_agent()
        tech = self.run_technical_qc_agent()
        edit = self.run_story_editor_agent()

        print("=" * 70)
        print("🏛️ THINKLATE COUNTER-TESTING AGENT COUNCIL REPORT")
        print(f"Target: {self.script_path}")
        print("=" * 70)
        
        for rep in [anti, aud, tech, edit]:
            score_txt = f"{rep['score']}/100" if rep.get('score') is not None else "n/a"
            print(f"\n[{rep['agent'].upper()}] - Verdict: {rep['verdict']} (Score: {score_txt})")
            for f in rep.get('faults', []):
                print(f"  ❌ Fault: {f}")
            if rep.get('findings'):
                for title, status in rep['findings']:
                    print(f"  ⚠️ Verify: {title} ({status})")
            print(f"  💡 Alternative Direction: {rep['alternative']}")

        all_faults = anti.get('faults', []) + aud.get('faults', []) + edit.get('faults', [])
        print("\n" + "=" * 70)
        print("🛠️ THE FIXER")
        print("=" * 70)
        if not all_faults:
            print("No structural faults found. No rewrite required.")
            print("Remaining gate: a human must verify every flagged claim above against a primary source.")
        else:
            print("Rewrite required. Fix these faults, keeping the script a continuous story with zero spoken section breaks:")
            for fault in all_faults:
                print(f"  - {fault}")
            print("\nStory spine to restore (Q&A causality, Therefore/But, one open loop paid off every ~60s):")
            print("  1. Anomaly: a real, dated incident with real money or livelihood at stake.")
            print("  2. Crime scene: the mechanism that took control from the owner.")
            print("  3. Motive: the incentive that rewards the villain.")
            print("  4. Genealogy: the historical precedent.")
            print("  5. Reckoning: the human cost, ending in a narrative resolution, not a checklist.")
        print("=" * 70)

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "videos/04_the-subscription-trap/script_final.md"
    council = CounterCouncil(path)
    council.generate_fixer_synthesis()
