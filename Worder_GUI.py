from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
from docx import Document
import re
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

def get_video_id(url):
    # Extract video ID from YouTube URL
    video_id = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11}).*', url)
    return video_id.group(1) if video_id else None

def save_english_subtitles(url_entry, status_label, language_var):
    # Get URL from entry widget
    url = url_entry.get()
    selected_language = language_var.get()
    
    # Extract video ID
    video_id = get_video_id(url)
    if not video_id:
        messagebox.showerror("Error", "Invalid YouTube URL")
        return
    
    try:
        # Get available transcript languages
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        
        # Try to get Hindi transcript first
        try:
            transcript = transcript_list.find_transcript(['hi'])
        except:
            messagebox.showerror("Error", "No Hindi transcript available")
            return
            
        # Translate to selected language if available
        try:
            if selected_language == 'English':
                transcript = transcript.translate('en')
        except:
            messagebox.showerror("Error", f"Could not translate to {selected_language}")
            return
            
        # Create a new Word document
        doc = Document()
        
        # Get filename from user using file dialog
        filename = filedialog.asksaveasfilename(
            defaultextension=".docx",
            filetypes=[("Word Document", "*.docx")],
            title="Save Subtitles As"
        )
        
        if not filename:  # If user cancels file dialog
            return
            
        # Add each subtitle to the document
        for entry in transcript.fetch():
            doc.add_paragraph(entry['text'])
        
        # Save the document
        doc.save(filename)
        status_label.config(text=f"Subtitles saved successfully to {filename}")
        messagebox.showinfo("Success", f"Subtitles saved successfully to {filename}")
        
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def create_gui():
    # Create main window
    root = tk.Tk()
    root.title("Hindi to English Subtitle Converter")
    root.geometry("600x200")
    
    # Create and pack main frame
    main_frame = ttk.Frame(root, padding="20")
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # URL Entry
    url_label = ttk.Label(main_frame, text="YouTube Video URL:")
    url_label.pack(pady=(0, 5))
    
    url_entry = ttk.Entry(main_frame, width=50)
    url_entry.pack(pady=(0, 10))
    
    # Language Selection
    language_frame = ttk.Frame(main_frame)
    language_frame.pack(pady=(0, 10))
    
    language_label = ttk.Label(language_frame, text="Select Language:")
    language_label.pack(side=tk.LEFT, padx=(0, 10))
    
    language_var = tk.StringVar(value="English")
    language_combo = ttk.Combobox(language_frame, 
                                textvariable=language_var, 
                                values=["English", "Hindi"],
                                state="readonly",
                                width=20)
    language_combo.pack(side=tk.LEFT)
    
    # Convert Button
    convert_button = ttk.Button(
        main_frame,
        text="Convert Subtitles",
        command=lambda: save_english_subtitles(url_entry, status_label, language_var)
    )
    convert_button.pack(pady=(0, 20))
    
    # Status Label
    status_label = ttk.Label(main_frame, text="")
    status_label.pack()
    
    return root

if __name__ == "__main__":
    root = create_gui()
    root.mainloop()
