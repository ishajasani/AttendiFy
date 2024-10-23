import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' : "https://faceattendancerealtime-6eb03-default-rtdb.firebaseio.com/",
    'storageBucket' : "faceattendancerealtime-6eb03.appspot.com"
})

#Importing student images
folderPath = 'Images'
pathList = os.listdir(folderPath)
pathList = [f for f in pathList if not f.startswith('.')]
imgList = []
studentIds = []
#print(pathList)

for path in pathList:
    img = cv2.imread(os.path.join(folderPath, path))
    img = cv2.resize(img, (216, 216))
    imgList.append(img)
    #print(os.path.splitext(path)[0])
    studentId = os.path.splitext(path)[0]
    studentIds.append(studentId)

    # Save the resized image as PNG
    pngFileName = f'{folderPath}/{studentId}.png'
    cv2.imwrite(pngFileName, img)  # Save the image as PNG

    # Upload the PNG file to Firebase storage
    bucket = storage.bucket()
    blob = bucket.blob(pngFileName)
    blob.upload_from_filename(pngFileName)

#print(studentIds)

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

print("Encoding started")
encodeListKnown = findEncodings((imgList))
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Complete")

file = open("EncodeFile.p" , 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved")
