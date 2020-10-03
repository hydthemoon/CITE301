import cv2
import os
import shutil

## FILE 생성
shutil.rmtree('C:/cited3_img', ignore_errors = True)
os.mkdir('C:/cited3_img')

vidcap = cv2.VideoCapture('C:/cite301/cited3_vid/vid_lecture1.mp4')
cnt = 0

while(vidcap.isOpened()):
    ret, img = vidcap.read()
    if int(vidcap.get(1)) % 500 == 0 :
        cnt += 1
        cv2.imwrite('C:/cited3_img/frame{0}.jpg'.format(cnt), img)
        print('Count : {0} saved'.format(cnt))
    else :
        pass

vidcap.release()