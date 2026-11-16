path = r'c:\Users\sar1s\Documents\MyWork\Git\lifeos-hq\00-control\DAILY_JOURNAL.md'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

target = '- Archived master dossier in `thinklate/VIRAL_SHORTS_FORENSIC_DOSSIER_2025_2026.md` and centralized `shared/playbooks/VIRAL_SHORTS_PLAYBOOK.md`.'
bullet = '\n  - **The Infographics Show 2D Vector Thumbnail Standard Locked (Rule 15 in AGENTS.md):** Formally codified the Infographics Show / Kurzgesagt 2D vector cartoon thumbnail standard across `AGENTS.md`, `thinklate-packaging.md`, and `packaging-director`. Permanently banned split-screens. Locked in center-focal character framing with tangible narrative props and top-banner headline typography. Approved Option 1 ("THE $300 CHORE" - `thumbnail_infographic_chore_trap_1280x720.jpg`) as the primary master thumbnail for Episode 05.'

if target in text:
    new_text = text.replace(target, target + bullet, 1)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_text)
    print('[OK] Updated DAILY_JOURNAL.md')
else:
    print('[FAIL] Target not found')
