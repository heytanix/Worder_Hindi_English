# Worder: Hindi-English YouTube Subtitle Converter

A Python application that extracts Hindi subtitles from YouTube videos and allows you to save them in either Hindi or English as text documents.

## Features

- Extract Hindi subtitles from YouTube videos
- Option to keep subtitles in Hindi or translate to English
- Save subtitles as formatted Word documents (.docx)
- Available in both CLI and GUI versions:
  - CLI version with text prompts and inputs
  - GUI version with user-friendly interface and file dialog
- Simple and intuitive interface

## Requirements

- Python 3.6+
- pytube
- youtube-transcript-api 
- python-docx
- tkinter (for GUI version)

## Usage

### CLI Version (Worder.py)
1. Run `Worder.py`
2. Enter a valid YouTube video URL when prompted
3. Select language preference (1 for English, 2 for Hindi)
4. Enter filename for the output .docx file
5. The application will generate a Word document with the subtitles

### GUI Version (Worder_GUI.py)
1. Run `Worder_GUI.py`
2. Enter/paste a valid YouTube video URL in the text field
3. Select your preferred language from the dropdown (English or Hindi)
4. Click "Convert Subtitles" and choose where to save the file
5. The application will generate a Word document at your chosen location

## Note

- The YouTube video must have Hindi subtitles available for the conversion to work
- The application first checks for Hindi subtitles and then translates to English if requested
- If Hindi subtitles are not available or translation fails, appropriate error messages will be shown
