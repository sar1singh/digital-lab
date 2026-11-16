import os

path = r"c:\Users\sar1s\Documents\MyWork\Git\digital-lab\03-content-lab\thinklate\videos\05_how-airbnb-stole-100b\script.md"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

old_end = "[SFX: Final deep cinematic sub-bass impact — drop to complete silence]"

new_outro = """[SFX: Sub-bass swell softens into a relaxed, rhythmic synth groove]
[VISUAL: ThinkLate End Screen Card — The quirky anime owl raises an eyebrow in the corner; video thumbnail for "The Subscription Trap" slides in]

So the next time you sit there thinking // that every great business has already been built, //
look around the room. //
Every massive industry // is hiding an annoying problem // someone is desperately waiting for you to solve. //
And if you can't find one sitting at your desk, // pack a bag and travel. //
Step outside your routine, // notice what breaks, // and see what frustrates people. //
It doesn't need to start with venture capital or a revolution. //
It can start with an eighty-dollar airbed // on a living room rug... //
and turn into a hundred billion dollars. //

What's an everyday annoyance // you think someone should turn into a business right now? //
Tell me in the comments down below. //
Stay curious. //
See you in the next one. ///

[SFX: Clean mechanical camera shutter click + tape rewind stop — drop to complete silence]"""

if old_end in text:
    text = text.replace(old_end, new_outro)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("SUCCESS")
else:
    print("NOT FOUND")

