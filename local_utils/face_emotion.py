# video
import cv2
from keras.models import save_model
import face_recognition
import tensorflow as tf # 딥러닝 라이브러리
import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, Flatten, BatchNormalization

def create_cnn_model():
    num_classes = 7
    num_detectors = 32
    width, height = 48, 48
    
    network = Sequential()

    network.add(Conv2D(filters=num_detectors, kernel_size=3, activation='relu', padding='same', input_shape=(width, height, 3)))
    network.add(BatchNormalization())
    network.add(Conv2D(filters=num_detectors, kernel_size=3, activation='relu', padding='same'))
    network.add(BatchNormalization())
    network.add(MaxPooling2D(pool_size=(2, 2)))
    network.add(Dropout(0.2))

    network.add(Conv2D(2*num_detectors, 3, activation='relu', padding='same'))
    network.add(BatchNormalization())
    network.add(Conv2D(2*num_detectors, 3, activation='relu', padding='same'))
    network.add(BatchNormalization())
    network.add(MaxPooling2D(pool_size=(2, 2)))
    network.add(Dropout(0.2))

    network.add(Conv2D(2*2*num_detectors, 3, activation='relu', padding='same'))
    network.add(BatchNormalization())
    network.add(Conv2D(2*2*num_detectors, 3, activation='relu', padding='same'))
    network.add(BatchNormalization())
    network.add(MaxPooling2D(pool_size=(2, 2)))
    network.add(Dropout(0.2))

    network.add(Conv2D(2*2*2*num_detectors, 3, activation='relu', padding='same'))
    network.add(BatchNormalization())
    network.add(Conv2D(2*2*2*num_detectors, 3, activation='relu', padding='same'))
    network.add(BatchNormalization())
    network.add(MaxPooling2D(pool_size=(2, 2)))
    network.add(Dropout(0.2))

    network.add(Flatten())

    network.add(Dense(2*2*num_detectors, activation='relu'))
    network.add(BatchNormalization())
    network.add(Dropout(0.2))

    network.add(Dense(2*num_detectors, activation='relu'))
    network.add(BatchNormalization())
    network.add(Dropout(0.2))

    network.add(Dense(num_classes, activation='softmax'))

    with open('trained_network.json', 'w') as trained_network_json:
        trained_network_json.write(network.to_json())
    
    with open('trained_network.json', 'r') as trained_network_json:
        trained_model_json = trained_network_json.read()
    
    network = tf.keras.models.model_from_json(trained_model_json)
    network.load_weights('weights_emotions.hdf5')
    network.compile(loss='categorical_crossentropy', optimizer='Adam', metrics=['accuracy'])
    
    return network


def face_encodings():
    image_to_be_matched = face_recognition.load_image_file('powell.png')
    name = "Chair Powell"
    
    # encoded the loaded image into a feature vector
    image_to_be_matched_encoded = face_recognition.face_encodings(image_to_be_matched)[0]
    return image_to_be_matched_encoded

def Create_Video():
    cap = cv2.VideoCapture('powell video.mp4')
    
    video_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # Video capture's frame width
    video_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # Video capture's frame height
    video_size = (round(video_width), round(video_height)) # Video size
    video_fps = cap.get(cv2.CAP_PROP_FPS)  # FPS(Frames Per Second)
    frame_cnt = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # Number of frames
    
    print('Number of frames:', frame_cnt, '/ FPS:', round(video_fps), '/ Frame size:', video_size)
    
    # In Linux, the extension of video output must be set to avi
    video_output_path = 'emotion_classification_result2.avi'
    
    codec = cv2.VideoWriter_fourcc(*'XVID')  # Set the codec
    
    video_writer = cv2.VideoWriter(video_output_path, codec, video_fps, video_size)
    return cap, video_writer, video_fps, frame_cnt


def face_emotion_recognition(cap, network, image_to_be_matched_encoded, video_writer, frame_cnt, video_fps):
    data_list = []
    green_color = (0, 255, 0)
    red_color = (0, 0, 255)
    emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

    count = 1
    skip_frames = 500  # Number of frames to skip

    while cv2.waitKey(1) < 0:
        connected, frame = cap.read()  # Read one frame from a VideoCapture object
        # frame에서 얼굴 검출
        if not connected:  # 영상 다 돌았을 때, break
            break

        # Skip frames if count is not a multiple of skip_frames
        if count % skip_frames != 0:
            count += 1
            continue

        face_detections = face_recognition.face_locations(frame, number_of_times_to_upsample=0, model="cnn")  # CNN 기반 얼굴 검출기
        # 검출된 얼굴 개수가 0보다 크면 수행
        if len(face_detections) > 0:
            for face_detection in face_detections:
                # Print the location of each face in this image
                top, right, bottom, left = face_detection
                # 얼굴 위치
                face_image = np.ascontiguousarray(frame[top:bottom, left:right])

                # 얼굴 이미지 encoding
                try:
                    face_encoded = face_recognition.face_encodings(face_image)[0]
                    result = face_recognition.compare_faces([image_to_be_matched_encoded], face_encoded, 0.5)
                    # 연준의장이면 수행
                    if result[0] == True:
                        cv2.rectangle(frame, (left, top), (right, bottom), green_color, 2)
                        roi = face_image
                        # 감정분석
                        roi = cv2.resize(roi, (48, 48))  # Extract region of interest from image
                        roi = roi / 255  # Normalize
                        roi = np.expand_dims(roi, axis=0)
                        preds = network.predict(roi)
                        print("Predictions:", preds)
                        # 라벨링 및 영상 frame부분에 감정값 렌더링
                        if preds is not None:
                            frame_time = count / video_fps
                            emotion_probabilities = preds[0]  # 모든 감정 클래스의 확률 배열
                            pred_emotion_index = np.argmax(emotion_probabilities)  # 가장 높은 확률을 가진 감정 클래스의 인덱스
                            predicted_emotion = emotions[pred_emotion_index]  # 가장 높은 확률을 가진 감정 클래스
                            data_list.append(
                                {"time": frame_time, "emotion": predicted_emotion, **{emotions[i]: prob for i, prob in
                                                                                    enumerate(emotion_probabilities)}}
                            )
                            print("Data List After Appending:", data_list)
                            cv2.putText(frame, emotions[pred_emotion_index], (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX,
                                        0.5, red_color, 1)
                    # 연준의장이 아니면 넘김
                    else:
                        continue
                except Exception as e:
                    print(f"Error: {e}")
                    continue

        video_writer.write(frame)

        # Calculate and display the progress
        progress = (count / frame_cnt) * 100
        print(f"Progress: {progress:.2f}%")
        count += 1

        # if count >= 1000:
        #     break

    # Create the DataFrame outside the loop
    df = pd.DataFrame(data_list)
    # Calculate the average based on selected emotions
    df["Average"] = df[emotions].mean(axis=1)

    main_emotion = df.loc[df["Average"].idxmax(), "emotion"]
    return main_emotion