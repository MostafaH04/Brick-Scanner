import cv2
import numpy as np
import os

clickNum = -1

def getLengths(img):
  global clickNum
  coords = []
  lengths = []
  def getClick(event, x, y, flags, param):
    global clickNum
    if event == cv2.EVENT_LBUTTONDBLCLK:
      clickNum += 1
      coords.append([x,y])
      if clickNum < 2:
        color = (255,0,0)
      else:
        color = (0,255,0)
      
      cv2.circle(img, (x,y), 4, color, -1)

  def getLen(coords):
    squareSum = 0
    print(coords)
    for i in range(2):
      squareSum += (coords[0][i]-coords[1][i])**2
    return squareSum ** (1/2)
     
  cv2.namedWindow("Select Corners Frame")
  cv2.setMouseCallback("Select Corners Frame", getClick)
  while (1):
    cv2.imshow("Select Corners Frame", img)
    k = cv2.waitKey(1)
    if k == ord('q') and clickNum != 3:
      break
    elif k is ord('q'):
      return lengths
    
    if clickNum == 3:
      print(coords)
      cv2.line(img, tuple(coords[0]), tuple(coords[1]), (255,0,0),1)
      cv2.line(img, tuple(coords[2]), tuple(coords[3]), (0,255,0),1)
      lengths = [getLen(coords[:2]),getLen(coords[2:])]
      print("Done")
      print(f"Side 1 Coords: {coords[:2]}, with Length: {lengths[0]}")
      print(f"Side 2 Coords: {coords[2:]}, with Length: {lengths[1]}")
      

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        img = cv2.resize(img, (1280,720))

        if img is not None:
            images.append(img)
    return images

images = load_images_from_folder("Simulation/Images/")
for i in range(len(images)):
  clickNum = -1
  getLengths(images[i])
  