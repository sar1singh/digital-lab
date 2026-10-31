import asyncio
import edge_tts

async def main():
    voices = await edge_tts.list_voices()
    for v in voices:
        if v['Locale'].startswith('en-') and v['Gender'] == 'Male':
            print(f"{v['ShortName']:30} | {v['Locale']:8} | {v.get('FriendlyName', '')}")

if __name__ == '__main__':
    asyncio.run(main())

