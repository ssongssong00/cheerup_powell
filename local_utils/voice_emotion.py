from speechbrain.pretrained.interfaces import foreign_class

def voice_emotion_recognition():
    classifier = foreign_class(source="speechbrain/emotion-recognition-wav2vec2-IEMOCAP", pymodule_file="custom_interface.py", classname="CustomEncoderWav2vec2Classifier")
    
    out_prob, score, index, text_lab = classifier.classify_file("output.wav") #화자분리된 오디오 파일 위치
    return text_lab
