import cv2
import face_recognition
from engine import get_faces

visages_connus, nom_des_visages = get_faces()

# Initializer la camera( le 0 indique la camera par defaut)
video_capture = cv2.VideoCapture(0) 
frame_count = 0
intervale_detection = 5

while True:
    # le methode read() retourne deux valeur, le ret indique si la capture a ete bien fait et frame contien le frame obtenu
    ret, frame = video_capture.read()

    # trouver des visages sur le frame de la camera
    face_locations = face_recognition.face_locations(frame)
    if len(face_locations) > 0:
        # Codifier le visage trouvé sur la webcam
        face_encoding = face_recognition.face_encodings(frame, face_locations)[0]

        # comparer les faces trouves sur le webcam avec les faces sauvegardé dasn notre 'BD'
        matches = face_recognition.compare_faces(visages_connus, face_encoding)

        name = "unknow"

        # Verifier s'il y a des carrespondances avec les visages connus
        for i in range(len(matches)):
            if matches[i]:
                name = nom_des_visages[i]
                break

        # Faire un rectangle dans la fenetre avec le nom du visage ou 'unknow'
        for (top, right, bottom, left) in face_locations:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2) #faire un rectangle en tour du visage
            cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1) #saisir le texte dans le rectangle

    # Montrer le frame dans le webcam
    cv2.imshow('Capture', frame)

    # condiction de sortir: tapper 'q' pour sortir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberer la camera et fermer la fenetre
video_capture.release()
cv2.destroyAllWindows()
