import time
import pyautogui
import cv2
from moviepy.editor import VideoFileClip
import requests
import os 

def start_recording():
    pyautogui.hotkey('command', 'shift', '5')
    time.sleep(2)  
    pyautogui.press('enter')
    
def stop_recording():
    time.sleep(10)
    pyautogui.hotkey('command', 'ctrl', 'esc')
    time.sleep(2)
    
def get_most_recent_file(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    most_recent_file = max(files, key=lambda f: os.path.getmtime(os.path.join(directory, f)))
    
    return most_recent_file


def MOV_to_MP4(mov_file_path):
    mp4_file_path = 'powell video.mp4' # mp4파일 path

    cap = cv2.VideoCapture(mov_file_path)
    
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You may need to adjust the codec based on your system
    out = cv2.VideoWriter(mp4_file_path, fourcc, fps, (width, height))
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        out.write(frame)
    
    cap.release()
    out.release()
    
def convert_mov_to_wav(mov_file_path):
    output_file_path = "output.wav"  # Replace with the desired output WAV file path

    video_clip = VideoFileClip(mov_file_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_file_path)
    
def transcribe_audio(file_path):
    url = "https://transcribe.whisperapi.com"
    headers = {
        'Authorization': 'Bearer ZAZ7CT9CBPV9RSNWBPF25GSL9ZER6L8V'
    }
    
    # Open the audio file in binary mode
    file = {'file': open(file_path, 'rb')}
    
    data = {
        "fileType": "wav",  # default is wav
        "diarization": "false",
        "numSpeakers": "1",
        "initialPrompt": "",
        "language": "en",
        "task": "transcribe",
        "callbackURL": ""
    }
    
    response = requests.post(url, headers=headers, files=file, data=data)
    json_response = response.json()
    
    # Extracted text from the response
    extracted_text = json_response.get('text', '')
    
    return extracted_text