import cv2
import numpy as np
import dlib
import random


# def video_stream():
#     cap = cv2.VideoCapture(0)  # Use 0 for the default web camera
#     while True:
#         success, frame = cap.read() # Read a frame from the web camera
#         if not success:
#             break
#         else:
#             ret, buffer = cv2.imencode('.jpg', frame) # Encode the frame as JPEG
#             frame = buffer.tobytes() # Convert the frame to bytes
#             yield (b'--frame\r\n' # Yield a multipart response
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


def video_stream():
    # Create a video capture object
    cap = cv2.VideoCapture(0)

    # Create a face detector object
    detector = dlib.get_frontal_face_detector()

    # Create a face landmark predictor object
    predictor = dlib.shape_predictor("ml_models/shape_predictor_68_face_landmarks.dat")

    # Define the admin desired direction for the face
    # Possible values are 'left', 'right', 'up', 'down', or 'center'

    number = random.randint(1000, 9999)

    # directions = ['left', 'right', 'up', 'down', 'center']
    directions = ['left', 'right']

    # Define a function to calculate the angle between two points
    def angle_between(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return np.degrees(np.arctan2(y2 - y1, x2 - x1))

    # Define a function to check if the face is in the desired direction
    def check_direction(face, direction):
        # Get the landmarks of the face
        landmarks = predictor(gray, face)

        # Get the coordinates of the nose tip and the chin
        nose = (landmarks.part(30).x, landmarks.part(30).y)
        chin = (landmarks.part(8).x, landmarks.part(8).y)

        # Calculate the angle of the face
        face_angle = angle_between(nose, chin)

        # Define the thresholds for the directions

        left_threshold = 105
        right_threshold = 75
        up_threshold = -110
        down_threshold = -15

        # Check if the face is in the desired direction
        if direction == 'left':
            return face_angle > left_threshold
        elif direction == 'right':
            return face_angle < right_threshold
        elif direction == 'up':
            return nose[1] - chin[1] > up_threshold
        elif direction == 'down':
            return nose[1] - chin[1] < down_threshold
        elif direction == 'center':
            return abs(face_angle) < 10 and abs(nose[1] - chin[1]) < 10
        else:
            return False

    # Define a function to plot the landmarks and the node angles on the face
    def plot_landmarks_and_angles(face):
        # Get the landmarks of the face
        landmarks = predictor(gray, face)

        # Loop over the landmarks and draw circles on them
        for i in range(0, 68):
            x = landmarks.part(i).x
            y = landmarks.part(i).y
            cv2.circle(frame, (x, y), 2, (0, 0, 255), -1)

        # Get the coordinates of the nose tip, the chin, and the left and right eye corners
        nose = (landmarks.part(30).x, landmarks.part(30).y)
        chin = (landmarks.part(8).x, landmarks.part(8).y)
        left_eye = (landmarks.part(36).x, landmarks.part(36).y)
        right_eye = (landmarks.part(45).x, landmarks.part(45).y)

        # Calculate the angles of the nose-chin and the eye-eye lines
        face_angle = angle_between(nose, chin)
        eye_angle = angle_between(left_eye, right_eye)

        # Draw the lines on the face
        cv2.line(frame, nose, chin, (0, 255, 0), 2)
        cv2.line(frame, left_eye, right_eye, (0, 255, 0), 2)

        # Display the angles on the frame
        cv2.putText(frame, "Face : {:.2f}".format(face_angle), (nose[0] + 10, nose[1] - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 0), 2)
        cv2.putText(frame, "Eye : {:.2f}".format(eye_angle), (right_eye[0] + 10, right_eye[1] + 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    counter = 0
    direction = directions[int(str(number)[counter]) % 2]
    while True and counter < 4:
        # Read a frame from the video stream
        ret, frame = cap.read()

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect the faces in the frame
        faces = detector(gray)

        # Loop over the detected faces
        for face in faces:
            # Draw a rectangle around the face
            cv2.rectangle(frame, (face.left(), face.top()), (face.right(), face.bottom()), (0, 255, 0), 2)

            # Plot the landmarks and the node angles on the face
            plot_landmarks_and_angles(face)

            # Check if the face is in the desired direction

            if check_direction(face, direction):
                # Display a message that the face is in the correct direction
                cv2.putText(frame, "Face is in the correct direction", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (0, 255, 0),
                            2)
                counter += 1
                try:
                    direction = directions[int(str(number)[counter]) % 2]
                except:
                    cap.release()
                    print("All done")
                    return {"Success": "All ok"}
                continue
            else:
                # Display a message that the face is not in the correct direction
                cv2.putText(frame, "Please turn your face to the " + direction, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (0, 0, 255), 2)
        if not ret:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)  # Encode the frame as JPEG
            frame = buffer.tobytes()  # Convert the frame to bytes
            yield (b'--frame\r\n'  # Yield a multipart response
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
