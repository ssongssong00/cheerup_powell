import extract
import face_emotion
import voice_emotion
import text_classification
import request_json

if __name__ == "__main__":
    try:
        # start_recording()
        # stop_recording()
        mov_file_path = 'powell video.mov'  # File Name 불러오는 방법 수정해야 함
        extract.MOV_to_MP4(mov_file_path)

        # face
        network = face_emotion.create_cnn_model()
        image_to_be_matched_encoded = face_emotion.face_encodings()
        cap, video_writer, video_fps, frame_cnt = face_emotion.Create_Video()
        face_emotion_result = face_emotion.face_emotion_recognition(cap, network, image_to_be_matched_encoded, video_writer, frame_cnt, video_fps)

        # voice
        output_file_path = "output.wav"
        extract.convert_mov_to_wav(mov_file_path)
        voice_emotion_result = voice_emotion.voice_emotion_recognition()

        text = extract.transcribe_audio(output_file_path)
        stance, interpretation = text_classification.analyze_fed_statement(text)
        response = request_json.send_request_emotion(face_emotion_result, voice_emotion_result[0])
        response_text = request_json.send_request_text(stance, interpretation)

    except Exception as e:
        print(f"An error occurred: {e}")
        raise  # Re-raise the exception to see the full traceback
