import asyncio
import edge_tts

async def generate_voiceover(text, output_path, voice="en-US-GuyNeural"):
    """Convert text to voiceover using Edge TTS."""
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_path)
    print(f"Voiceover saved to {output_path}")

def run_voiceover_sync(text, output_path):
    """Wrapper to run the async voiceover function."""
    asyncio.run(generate_voiceover(text, output_path))
