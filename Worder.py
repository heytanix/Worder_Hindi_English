from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
from docx import Document
import re

def get_video_id(url):
    # Extract video ID from YouTube URL
    video_id = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11}).*', url)
    return video_id.group(1) if video_id else None

def save_english_subtitles():
    # Get YouTube URL from user
    url = input("Please enter the YouTube video URL: ")
    
    # Extract video ID
    video_id = get_video_id(url)
    if not video_id:
        print("Invalid YouTube URL")
        return
    
    try:
        # Get available transcript languages
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        
        # Try to get Hindi transcript first
        try:
            transcript = transcript_list.find_transcript(['hi'])
        except:
            print("No Hindi transcript available")
            return
            
        # Translate to English if available
        try:
            transcript = transcript.translate('en')
        except:
            print("Could not translate to English")
            return
            
        # Create a new Word document
        doc = Document()
        
        # Get filename from user
        filename = input("Please enter the filename (with .docx extension): ")
        
        # Add each subtitle to the document
        for entry in transcript.fetch():
            doc.add_paragraph(entry['text'])
        
        # Save the document
        doc.save(filename)
        print(f"Subtitles saved successfully to {filename}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    save_english_subtitles()