import requests
import json

def send_request_emotion(video_emotion, voice_emotion):
    # face_emotion과 voice_emotion을 포함한 딕셔너리 생성
    data = {
        "video_emotion": video_emotion,
        "voice_emotion": voice_emotion
    }

    # 요청을 보낼 URL 지정
    url_emotion = "http://192.168.0.96:5001/emotion"
    
    # 필요한 경우 헤더 설정 (예: content-type)
    headers = {'Content-Type': 'application/json'}

    # POST 요청 보내기
    response = requests.post(url_emotion, json=data, headers=headers)

    # 응답 출력
    print(response)
    return response;


def send_request_text(stance, interpretation):
    # face_emotion과 voice_emotion을 포함한 딕셔너리 생성
    data = {
        "stance": stance,
        "interpretation": interpretation
    }

    # 요청을 보낼 URL 지정
    url_emotion = "http://192.168.0.96:5001/text"
    
    # 필요한 경우 헤더 설정 (예: content-type)
    headers = {'Content-Type': 'application/json'}

    # POST 요청 보내기
    response = requests.post(url_emotion, json=data, headers=headers)

    # 응답 출력
    print(response)
    return response;
