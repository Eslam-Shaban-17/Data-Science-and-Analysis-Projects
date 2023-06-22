# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 19:08:18 2023

@author: eslam
"""


import cv2
import pafy

url = 'https://www.youtube.com/watch?v=iH1ZJVqJO3Y'
vpafy = pafy.new(url)
play = vpafy.getbest(preftype='mp4')
cap = cv2.VideoCapture(play.url)

cap.set(3,480)
cap.set(4,640)


MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)

age_list = ['(0, 2)', '(4, 6)', '(8, 12)', '(15, 20)', '(25, 32)', '(38, 43)', '(48, 53)', '(60, 100)']
gender_list = ['Male', 'Female']

def initialize_cafe_models(): 
    age_net = cv2.dnn.readNetFromCaffe('files/deploy_age.prototxt','files/age_net.caffemodel')
    gender_net = cv2.dnn.readNetFromCaffe('files/deploy_gender.prototxt','files/gender_net.caffemodel')
    return (age_net, gender_net)

def video_detector(age_net, gender_net):
    font = cv2.FONT_HERSHEY_SIMPLEX
    while True:
        ret, image = cap.read()
        face_cascade = cv2.CascadeClassifier('files/haarcascade_frontalface_alt.xml')
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.1,5)
        if(len(faces) > 0):
            print("Found {} faces".format(str(len(faces))))
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x,y), (x+w,y+h), (255,255,0),2)
            #get face
            face_img = image[y:y+h, x:h+w].copy()
            blob = cv2.dnn.blobFromImage(face_img,1,(227,227),MODEL_MEAN_VALUES,swapRB=False)
            #predict gender
            gender_net.setInput(blob)
            gender_pred = gender_net.forward()
            gender = gender_list[gender_pred[0].argmax()]
            print('Gender: '+gender)
            #predict age
            age_net.setInput(blob)
            age_pred = age_net.forward()
            age = age_list[age_pred[0].argmax()]
            print("Age: " +age)
            overlay_text = "%s %s" %(gender,age)
            cv2.putText(image,overlay_text, (x,y), font, 1,(255,255,255),2,cv2.LINE_AA)
        cv2.imshow('frame',image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # cap.release()
    # cv2.destroyAllWindows()
        
if __name__ == '__main__':
    age_net, gender_net = initialize_cafe_models()
    read_from_camera(age_net, gender_net)
