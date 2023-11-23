from flask import Flask, jsonify, request
from flask_cors import CORS  # CORS import 추가

app = Flask(__name__)
CORS(app)  # CORS 활성화

# 감정과 텍스트 값을 저장하는 딕셔너리
stored_emotions = {}
stored_text = {}

# ------------------- 메인 url -----------------------#
@app.route("/")

# ------------------- 영상, 음성 로컬에서 받고 클라이언트에게 보내는 기능 -----------------------#
@app.route('/emotion', methods=['POST', 'GET'])
def process_emotion():
    if request.method == 'POST':
        data = request.json
        print("데이터 타입", type(data))
        print("실제 값", data)
        
        stored_emotions['voice_emotion'] = data.get('voice_emotion')
        stored_emotions['video_emotion'] = data.get('video_emotion')
        return jsonify({"message": "감정이 성공적으로 저장되었습니다."})

    if request.method == 'GET':
        # GET 요청에 대한 저장된 감정을 클라이언트에게 반환
        return jsonify(stored_emotions)

# ------------------- 텍스트 로컬에서 받고 클라이언트에게 보내는 기능 -----------------------#
@app.route('/text', methods=['POST', 'GET'])
def process_text():
    if request.method == 'POST':
        # Parse the JSON data
        data = request.json
        print("Received text data:", data)

        # Save the text received from the POST request
        stored_text['stance'] = data.get('stance')
        stored_text['interpretation'] = data.get('interpretation')
        return jsonify({"message": "Text was saved successfully."})

    if request.method == 'GET':
        # Return the stored text for the GET request to the client
        return jsonify(stored_text)

# 메인 함수 실행
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)