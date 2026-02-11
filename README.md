# 🎥 AI YouTube Video Generator

An automated, end-to-end pipeline that takes a single text topic and generates a high-quality, YouTube-ready MP4 video. Built with Python and modern AI tools.

## 🚀 Features
- **One-Click Generation**: Just enter a topic and get a finished video.
- **AI Script Writing**: Uses **Groq (Llama 3)** for engaging, conversational scripts.
- **Natural Voiceovers**: High-quality TTS using **Edge TTS**.
- **Automated Sourcing**: Fetches HD stock images from **Pexels API**.
- **Pro Video Editing**: Automated assembly with **MoviePy**, featuring:
  - HD 1280x720 resolution.
  - Smooth Crossfade transitions.
  - Intelligent cropping to fit 16:9 aspect ratio.

## 🛠️ Tech Stack
- **UI**: Streamlit
- **LLM**: Groq API (Llama-3.3-70b-versatile)
- **TTS**: Edge-TTS (No API key needed)
- **Stock Media**: Pexels API
- **Video Processing**: MoviePy



## ⚙️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ShreyashPatil530/AI-YouTube-Video-Generator.git
   cd AI-YouTube-Video-Generator
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup Environment Variables**:
   Create a `.env` file in the root directory and add your keys:
   ```env
   GROQ_API_KEY=your_groq_key_here
   PEXELS_API_KEY=your_pexels_key_here
   ```

## 🏃 Run the App
```bash
streamlit run app.py
```

## 📂 Project Structure
- `app.py`: Main Streamlit UI and pipeline orchestration.
- `script_generator.py`: Script and keyword generation logic.
- `voice_generator.py`: Text-to-speech conversion.
- `image_generator.py`: Pexels image search and download.
- `video_editor.py`: MoviePy assembly and effects.
- `generator_utils.py`: File and directory management.

## 📄 License
MIT License.

---
Made with ❤️ for AI Content Creators.
