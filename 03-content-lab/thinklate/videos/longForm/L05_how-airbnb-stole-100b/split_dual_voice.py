import os
import sys

spoken_file = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\05_how-airbnb-stole-100b\audio_takes\spoken_text_clean.txt"
with open(spoken_file, "r", encoding="utf-8") as f:
    text = f.read()

# Let's see where the split point is for Act 1:
# The end of Act 1 is right before:
# "How do you keep a website alive when you can't even afford groceries? Then came August 2008..." or "twenty thousand dollars in high interest debt"
# Specifically in the script:
# "So your business doesn't destroy itself once it wins." or after Nate Blecharczyk builds the site:
# "Once the website was live in early 2008, they thought the hardest part was over... Every single investor said no."

target_phrase = "Every single investor said no."
idx = text.find(target_phrase)
if idx != -1:
    split_end = idx + len(target_phrase)
    # Find next period
    next_period = text.find(".", split_end)
    if next_period != -1:
        split_end = next_period + 1
    act1_text = text[:split_end].strip()
    act2_text = text[split_end:].strip()
    print(f"Act 1 (Hook & Setup): {len(act1_text):,} chars ({len(act1_text.split())} words)")
    print(f"Act 2-8 (Deep Dive):   {len(act2_text):,} chars ({len(act2_text.split())} words)")
    
    with open(r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\05_how-airbnb-stole-100b\audio_takes\act1_george_text.txt", "w", encoding="utf-8") as f1:
        f1.write(act1_text)
    with open(r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\05_how-airbnb-stole-100b\audio_takes\act2_andrew_text.txt", "w", encoding="utf-8") as f2:
        f2.write(act2_text)
    print("Files written: act1_george_text.txt and act2_andrew_text.txt")
else:
    print("Target phrase not found, showing text sample:")
    print(text[:500])

