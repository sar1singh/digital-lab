import re

with open(r'digital-lab/03-content-lab/thinklate/videos/04_the-subscription-trap/script_final.md', 'r', encoding='utf-8') as f:
    raw_lines = f.readlines()

clean_lines = []
skip = True

for line in raw_lines:
    line_s = line.strip()
    if "In July twenty twenty-two" in line_s:
        skip = False
    if skip:
        continue
    
    # Skip non-spoken metadata
    if line_s.startswith("#") or line_s.startswith("[") or line_s.startswith("*") or line_s.startswith("---") or not line_s:
        continue
    
    # // is a half-beat catch breath -> natural comma
    # /// is a full stop and pitch drop -> period
    t = line_s
    t = t.replace("///", ".")
    t = t.replace("//", ",")
    
    # Clean up double punctuation
    t = re.sub(r'([,\.\?!])\s*([,\.\?!])', r'\1', t)
    t = re.sub(r',\s*,', ',', t)
    t = re.sub(r'\.\s*\.', '.', t)
    t = re.sub(r',\s*\.', '.', t)
    t = re.sub(r'\.\s*,', ',', t)
    t = re.sub(r'\s+', ' ', t).strip()
    
    # Polish spacing around punctuation
    t = t.replace(" ,", ",").replace(" .", ".")
    if not t.endswith((".", "!", "?")):
        t += "."
        
    if t:
        clean_lines.append(t)

full_text = "\n\n".join(clean_lines)

# Split into two parts at John Deere pivot
mid_target = "Now watch the trick."
parts = full_text.split(mid_target)

part1 = parts[0].strip() + "\n\n" + mid_target
part2 = parts[1].strip()

with open(r'digital-lab/03-content-lab/thinklate/videos/04_the-subscription-trap/assets/audio/elevenlabs_paste_part1.txt', 'w', encoding='utf-8') as f:
    f.write(part1)

with open(r'digital-lab/03-content-lab/thinklate/videos/04_the-subscription-trap/assets/audio/elevenlabs_paste_part2.txt', 'w', encoding='utf-8') as f:
    f.write(part2)

print("Part 1 characters:", len(part1), "words:", len(part1.split()))
print("Part 2 characters:", len(part2), "words:", len(part2.split()))
print("\n--- SAMPLE PART 1 HEAD ---")
for p in part1.split("\n\n")[:6]:
    print(p)
