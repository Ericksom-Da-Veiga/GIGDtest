import face_recognition as fr
import cv2 #openCV

visages_connu = []
nom_des_visages = []

#fonction que reconnaitre les faces apartir d'une image dans notre BD
def reconaitre_face(url_photo):
    photo = fr.load_image_file(url_photo)
    photo= cv2.cvtColor(photo,cv2.COLOR_BGR2RGB)
    visage = fr.face_encodings(photo)[0]  #pour codifier les visages sur les photos

    return visage #retourner le visage touve

#fonction pour sauvegarder les faces avec se nom dans une table
def donner_nom(nom,visage):
    if(visage[0]):
        visages_connu.append(visage)
        nom_des_visages.append(nom)

#fonction pour retourner les tables des visages et ses noms
def get_faces():
    face_justion_biber = reconaitre_face('./img/jordan.jpeg')
    face_jordan = reconaitre_face('./img/bieber.jpeg')
    
    donner_nom('bieber',face_mide)
    donner_nom('jordan',face_junior)

    return visages_connu, nom_des_visages
