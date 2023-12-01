from flask import Flask, render_template, jsonify, abort, request
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.secret_key = 'pswd'

# flask 소켓 통신
socket_io = SocketIO(app) # socket io 설정
connected_users = 0  # 접속 중인 사용자 수를 저장할 변수

# emotion, text 값 저장
stored_emotions = {}  # Dictionary to store received emotions
stored_text = {}  # Dictionary to store received text

# url 접근 제한
protected_paths = ['/emotion','/text']  # IP 제한을 적용할 경로들
allowed_ips = ['192.168.0.17']  # 허용된 IP 주소 목록

#------------------- url 접근 제한 -----------------------#
@app.before_request
def limit_remote_addr():
    client_ip = request.remote_addr
    if request.path == protected_paths and client_ip not in allowed_ips:
        print(client_ip)
        abort(403)  # /emotion URL에 대한 IP가 허용 목록에 없으면 403 Forbidden 에러 반환


#------------------- 메인 url -----------------------#
@app.route("/")
#------------------- 채팅방 기능 -----------------------#
def chatting():
    logo_path = 'images/logo.png'  # 이미지 파일의 상대 경로
    return render_template("main.html",logo_path=logo_path)

@socket_io.on("message")
def socket_request(data):
    to_client = dict()
    to_client['nickname'] = data['nickname']
    to_client['message'] = data['message']
    to_client['type'] = 'normal'
    
    send(to_client, broadcast=True)


# 현재 접속자 수
@socket_io.on('connect')
def handle_connect():
    global connected_users
    connected_users += 1
    socket_io.emit('user_count', connected_users//2)

@socket_io.on('disconnect')
def handle_disconnect():
    global connected_users
    connected_users -= 1
    socket_io.emit('user_count', connected_users//2)


#------------------- 영상, 음성 로컬에서 받고 클라이언트에게 보내는 기능 -----------------------#
@app.route('/emotion', methods=['POST', 'GET'])
def process_emotion():
    if request.method == 'POST':
        data = request.json
        # Store received emotions from POST request
        stored_emotions['voice_emotion'] = data.get('voice_emotion')
        stored_emotions['face_emotion'] = data.get('face_emotion')
        return jsonify({"message": "Emotions received successfully"})

    if request.method == 'GET':
        # Return stored emotions to the client on GET request
        return jsonify(stored_emotions)
    
#------------------- 텍스트 로컬에서 받고 클라이언트에게 보내는 기능 -----------------------#
@app.route('/text', methods=['POST', 'GET'])
def process_text():
    if request.method == 'POST':
        data = request.json
        # stored_text에 'speech'
        stored_text['speech'] = data.get('speech')
        stored_text['translation'] = data.get('translation')
        stored_text['interpretation'] = data.get('interpretation')
        stored_text['stance_score'] = data.get('stance_score')
        return jsonify({"message": "text received successfully"})

    if request.method == 'GET':
        return jsonify(stored_text)
    
# 메인 함수 실행
if __name__ == '__main__':
    socket_io.run(app, host='0.0.0.0',port=5001, debug=True)

