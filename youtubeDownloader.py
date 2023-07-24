from pytube import YouTube
from moviepy.editor import *
import streamlit as st
# Function to download YouTube video as MP4
def download_video(url, output_path):
    try:
        yt = YouTube(url)
        video_stream = yt.streams.filter(file_extension='mp4').first()
        video_stream.download(output_path)
        print("Video Downloaded Successfully!")
        return video_stream.default_filename
    except Exception as e:
        print("Error:", str(e))
# Function to convert video to MP3
def convert_to_mp3(input_path, output_path):
    try:
        video_clip = VideoFileClip(input_path)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(output_path)
        audio_clip.close()
        video_clip.close()
        print("Conversion to MP3 Successful!")
    except Exception as e:
        print("Error:", str(e))
# Example usage
def main():
    st.title("Video Downloader - Converter")
    youtube_url = st.text_input("Youtube URL")
    if st.button("Download and Convert"):
        if youtube_url:
                
            # Download video
            downloaded_filename = download_video(youtube_url, './downloads/')
            if downloaded_filename:

                # Convert to MP3
                input_path = './downloads/'  # Path to the downloaded video
                output_path = './downloads/'+ downloaded_filename[:-4]  +'.mp3'  # Desired output path for the MP3 file
                convert_to_mp3(input_path + downloaded_filename, output_path)
                st.success("Downloaded and Converted")
            else:
                st.error("Failed")
        else:
            st.warning("Enter valid youtube url")


if __name__ == "__main__":
    main()
