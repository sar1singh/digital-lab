import os

path = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\05_how-airbnb-stole-100b\script.md"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

target = "They got twenty thousand dollars in seed funding, // but getting into Y Combinator didn't magically save them. //"

replacement = """They got twenty thousand dollars in seed funding, // but getting into Y Combinator didn't magically save them. //
Right here in March 2009, they made the smartest strategic pivot of their lives. //
The original name—Airbed and Breakfast—was actively suffocating the business. //
Travelers assumed they would be sleeping on squeaky rubber pool mattresses in a stranger's living room, //
and hosts with beautiful spare bedrooms or empty apartments refused to list on a site that literally had the word "Airbed" in the title! //
So in the middle of Y Combinator, they officially bought the domain and shortened the name down to just three letters: //
Airbnb dot com. //
Dropping the words "Airbed" and "Breakfast" was the psychological masterstroke // that transformed them from an eccentric floor-rental gimmick into a real marketplace for actual homes. //
Yet even with the new name, growth refused to budge. //"""

if target in text:
    new_text = text.replace(target, replacement)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("SUCCESS: Inserted March 2009 rebrand bridge into script.md!")
else:
    print("ERROR: Target string not found in script.md")
