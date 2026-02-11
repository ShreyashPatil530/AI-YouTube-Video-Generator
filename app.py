import streamlit as st
import os
import time
from generator_utils import setup_directories, clear_temp, get_temp_path, get_output_path
from script_generator import ScriptGenerator
from voice_generator import run_voiceover_sync
from image_generator import ImageGenerator
from video_editor import create_video

# Page config
st.set_page_config(page_title="AI YT Video Gen", page_icon="🎥", layout="centered")

# Custom CSS for premium look
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
    }
    .stTextInput>div>div>input {
        background-color: #262730;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.title("🎥 AI YouTube Video Generator")
    st.write("Enter a topic and generate a YouTube-ready video in seconds.")

    topic = st.text_input("Video Topic", placeholder="Enter any topic (e.g., The Future of SpaceX)")
    
    if st.button("Generate Video"):
        if not topic:
            st.error("Please enter a topic!")
            return

        # Initialize directories
        setup_directories()
        
        # Pipeline execution
        try:
            progress_bar = st.progress(0)
            status_text = st.empty()

            # 1. Script Generation
            status_text.text("✍️ Generating script...")
            script_gen = ScriptGenerator()
            script = script_gen.generate_script(topic)
            st.info(f"Generated Script: \n\n{script}")
            progress_bar.progress(25)

            # 2. Voiceover Generation
            status_text.text("🎙️ Converting script to voiceover...")
            voice_path = get_temp_path("voice.mp3")
            run_voiceover_sync(script, voice_path)
            progress_bar.progress(50)

            # 3. Image Sourcing
            status_text.text("🖼️ Sourcing images...")
            keywords = script_gen.generate_keywords(script)
            img_gen = ImageGenerator()
            image_paths = img_gen.search_and_download(keywords, 'temp')
            progress_bar.progress(75)

            # 4. Video Creation
            status_text.text("🎬 Assembling video...")
            output_video = get_output_path("final_video.mp4")
            create_video(image_paths, voice_path, output_video)
            progress_bar.progress(100)

            status_text.text("✅ Video generated successfully!")
            
            # Display video
            video_file = open(output_video, 'rb')
            video_bytes = video_file.read()
            st.video(video_bytes)
            
            # Download button
            st.download_button(
                label="Download Video",
                data=video_bytes,
                file_name="final_video.mp4",
                mime="video/mp4"
            )

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
        finally:
            # Note: We might want to keep temp files for debugging, 
            # or clear them in a real app.
            # clear_temp()
            pass

if __name__ == "__main__":
    main()
