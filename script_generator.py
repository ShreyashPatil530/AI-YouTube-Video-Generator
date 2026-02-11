import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class ScriptGenerator:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def generate_script(self, topic):
        """Generate a 120-150 word YouTube narration script."""
        prompt = f"""
        Write a 120-150 word YouTube narration script about: {topic}.
        Tone: educational, simple, conversational.
        Rules:
        - Output ONLY plain narration text.
        - NO titles, NO emojis, NO directions, NO speaker names.
        - Focus on being engaging.
        """
        
        chat_completion = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a professional YouTube scriptwriter."},
                {"role": "user", "content": prompt}
            ],
            model="llama-3.3-70b-versatile",
        )
        return chat_completion.choices[0].message.content.strip()

    def generate_keywords(self, script):
        """Extract high-quality visual keywords from the script."""
        prompt = f"""
        Based on this script, identify 10 distinct scenes or visual concepts.
        For each scene, provide a simple 'stock photo' search term (e.g., 'spaceship landing on mars red dust').
        Script: {script}
        Output ONLY the keywords comma-separated. Do not use numbering or titles.
        """
        
        chat_completion = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a visual content curator."},
                {"role": "user", "content": prompt}
            ],
            model="llama-3.3-70b-versatile",
        )
        return [k.strip() for k in chat_completion.choices[0].message.content.split(",")]
