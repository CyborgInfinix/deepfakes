import subprocess
import ffmpeg
import os
import glob
import cv2
import numpy as np
import os
import shutil
import os, binascii
from backports.pbkdf2 import pbkdf2_hmac
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
from PIL import Image 

# Playing video from file:
cap = cv2.VideoCapture('idea.mp4')
#to extract audio
print('extracting audio..........')
command = "ffmpeg -i D:/deep/idea.mp4 -ab 160k -ac 2 -ar 44100 -vn audio.wav"

subprocess.call(command, shell=True)
#to check the path specified
try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')
#setting current frame value
currentFrame = 0
#condition for the number of frames
while(currentFrame<500):
    
    # Capture frame-by-frame
    ret, frame = cap.read()
       

    # Saves image of the current frame in jpg file
    name = './data/' + str(currentFrame) + '.png'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)


    # To stop duplicate images
    print('stoping duplicate images.........')
    currentFrame += 1
    print('stopped!')
# When everything done, release the capture
print('initiating cap release')
cap.release()
print('cap released')
cv2.destroyAllWindows()
#to get the password
pass1=input('enter your password')


#to encrypt using rsa algorithm

key = RSA.generate(2048)
private_key = key.export_key('PEM')
public_key = key.publickey().exportKey('PEM')
message = pass1
message = str.encode(message)

rsa_public_key = RSA.importKey(public_key)
rsa_public_key = PKCS1_OAEP.new(rsa_public_key)
encrypted_text = rsa_public_key.encrypt(message)
    #encrypted_text = b64encode(encrypted_text)

print('your rsa encrypted_text is : {}'.format(encrypted_text))


rsa_private_key = RSA.importKey(private_key)
rsa_private_key = PKCS1_OAEP.new(rsa_private_key)
decrypted_text = rsa_private_key.decrypt(encrypted_text)

print('your rsa decrypted_text is : {}'.format(decrypted_text))


#to hash using pbkdf2
salt = binascii.unhexlify('aaef2d3f4d77ac66e9c5a6c3d8f921d1')
passwd = pass1.encode("utf8")
key = pbkdf2_hmac("sha256", passwd, salt, 50000, 32)
pbkkey=binascii.hexlify(key)
print("Derived key:",pbkkey)

#creating the signature using rsa and pbkdf2
key=encrypted_text+pbkkey
print(key)

#to combine images into a video
image_folder = 'd:/deep/data'
video_name = 'video.avi'

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
#sorts images based on order
images.sort(key=lambda x: int(''.join(filter(str.isdigit, x))))
print(images)

frame = cv2.imread(os.path.join(image_folder, images[0]))
print(images[77])
height, width, layers = frame.shape
#to do image steganograpy on the image frames
print('encrypting...........')







fourcc = cv2.VideoWriter_fourcc(*'XVID')
#15.0 is the fps rate (frame per second value)
video = cv2.VideoWriter(video_name, fourcc,15.0, (width,height))



for image in images:
  
    video.write(cv2.imread(os.path.join(image_folder, image)))


cv2.destroyAllWindows()
video.release()
#to merge audio and video
cmd = 'ffmpeg -y -i audio.wav -r 30 -i video.avi  -filter:a aresample=async=1 -c:a flac -c:v copy av.mkv'
subprocess.call(cmd, shell=True)                                     # "Muxing Done
print('Muxing Done')

#completion of process
print('is the process complete')
#to free the memory
status=input('yes/no')
if(status=="yes"):

 shutil.rmtree('d:\\deep\\data')
