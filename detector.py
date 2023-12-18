import numpy as np
import cv2
from joblib import Parallel, delayed
import joblib
import time
start = time.time()
cap = cv2.VideoCapture('C:\\Users\Vriska S\Desktop\ImAAT\\1_b.mp4')
dictio={}
cornerlist=[]
f = 0
while(cap.isOpened()):
    print(f)
    f = f+1
    ret, frame = cap.read()
    img = frame
    try:
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    except:
        break
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray,2,3,0.04)
    dst = cv2.dilate(dst,None)
    ret, dst = cv2.threshold(dst,0.5*dst.max(),255,0)
    dst = np.uint8(dst)
    ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
    corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)
    corners =  np.around(corners)
    cornerlist.append((str(corners)))
    dictio[str(corners)] = 2
    #print(dictio)
end = time.time()
print("Time taken : ")
print(end-start)
base = joblib.load('C:\\Users\Vriska S\Desktop\ImAAT\\final.pkl')
for ele in cornerlist:
    if ele in base:
        print("Source is "+ str(base[ele]))
        break
