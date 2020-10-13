
### SETTINGS    ###
vid_target = "lyrics_coldplay_2"
text_target = "tearme"
###             ###

``

import cv2

vidcap = cv2.VideoCapture('C:/cited3_db/cited3_vid/{0}.mp4'.format(vid_target))
fps = cv2.CAP_PROP_FPS
print(fps)

vidcap.release()

text = open('C:/cited3_db/cited3_tesseract/{0}.txt'.format(vid_target), 'rt', -1, 'utf-8')
i = 0
result = []

while True :
    line = text.readline()
    if line == '' :
        text.close()
        break
    if line == 'sample{0}\n'.format(i + 1) :
        i += 1
    if text_target in line :
        result.append(i)

timeline = [i for i in result]
print(timeline)