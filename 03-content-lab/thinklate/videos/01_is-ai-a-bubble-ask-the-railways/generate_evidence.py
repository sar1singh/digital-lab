import pypdfium2 as pdfium
from PIL import Image, ImageDraw, ImageFont

pdf = pdfium.PdfDocument('assets/mania18_paper.pdf')
page_img = pdf[1].render(scale=3).to_pil()

# Canvas 1920x1080 #1B2A4A
canvas = Image.new('RGB', (1920, 1080), '#1B2A4A')

w, h = page_img.size
# Crop around the chart and the quote paragraph below it: y from 500 to 1850
crop_box = (200, 520, w - 200, 1850)
snippet = page_img.crop(crop_box)

snippet_rgba = snippet.convert('RGBA')
overlay = Image.new('RGBA', snippet_rgba.size, (255, 255, 255, 0))
draw = ImageDraw.Draw(overlay)

# The quote is near the bottom of this snippet:
# snippet offset is 520, so y in snippet = 1616 - 520 = 1096
# Line 1: "...The two railway manias of the 1840s and 1860s involved"
draw.rectangle([(120, 1055), (snippet.width - 120, 1098)], fill=(255, 230, 0, 100))
# Line 2: "capital investments of 15 to 20% of GDP, comparable to £300 to 400 billion for UK..."
draw.rectangle([(120, 1099), (snippet.width - 120, 1142)], fill=(255, 230, 0, 100))
# Line 3: "$3 to 4 trillion for USA today. (These were not stock market valuations, but actual funds..."
draw.rectangle([(120, 1143), (snippet.width - 120, 1186)], fill=(255, 230, 0, 100))
# Line 4: "provided by investors.)"
draw.rectangle([(120, 1187), (480, 1230)], fill=(255, 230, 0, 100))

snippet_highlighted = Image.alpha_composite(snippet_rgba, overlay).convert('RGB')

# Scale to fit nicely
target_h = 750
target_w = int(snippet.width * (target_h / snippet.height))
snippet_resized = snippet_highlighted.resize((target_w, target_h), Image.Resampling.LANCZOS)

pos_x = (1920 - target_w) // 2
pos_y = 60
canvas.paste(snippet_resized, (pos_x, pos_y))

draw_canvas = ImageDraw.Draw(canvas)
# Border around paper
draw_canvas.rectangle([(pos_x-2, pos_y-2), (pos_x + target_w + 2, pos_y + target_h + 2)], outline='#98A2B3', width=2)

# Citation banner lower-third
draw_canvas.rectangle([(140, 880), (1780, 1010)], fill='#24365C', outline='#D99A2B', width=2)

try:
    font_title = ImageFont.truetype('C:/Windows/Fonts/georgia.ttf', 32)
    font_sub = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 23)
except Exception:
    font_title = font_sub = ImageFont.load_default()

draw_canvas.text((180, 902), 'RESEARCH EVIDENCE: Prof. Andrew Odlyzko, University of Minnesota', fill='#F4F1EA', font=font_title)
draw_canvas.text((180, 950), '\"The railway mania of the 1860s and financial innovation\" (2024) — Page 2, Chart & GDP Data', fill='#98A2B3', font=font_sub)

canvas.save('assets/evidence_gdp_odlyzko.png')
print('Successfully generated evidence_gdp_odlyzko.png with exact quote highlighted')
