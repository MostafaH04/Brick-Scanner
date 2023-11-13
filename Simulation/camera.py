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
      

#def load_images_from_folder(folder):
 #   images = []
  #  for filename in os.listdir(folder):
   #     img = cv2.imread(os.path.join(folder,filename))
    #    img = cv2.resize(img, (1280,720))

     #   if img is not None:
      #      images.append(img)
   # return images

cap = cv2.VideoCapture(0);
#images = load_images_from_folder("Simulation/Images/")
mtx = np.load("mat.npy")
dist = np.load("dist.npy")

while True:
  _,image = cap.read() 
  h,  w = image.shape[:2]
  newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))
  # undistort
  dst = cv2.undistort(image, mtx, dist, None, newcameramtx)
  # crop the image
  x, y, w, h = roi
  image = dst[y:y+h, x:x+w]
  clickNum = -1
  imgray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  ret, thresh = cv2.threshold(imgray, 50, 255, 0)
  contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  cntsSorted = sorted(contours, key=lambda x: cv2.contourArea(x))
  for cnt in cntsSorted[::-1]:
    # Get rect
    rect = cv2.minAreaRect(cnt)
    (x, y), (w, h), angle = rect
    # Display rectangle
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    (x, y), (w, h), angle = rect
    cv2.circle(image, (int(x), int(y)), 5, (0, 0, 255), -1)
    cv2.polylines(image, [box], True, (255, 0, 0), 2)
    cv2.putText(image, "Width {} px".format(round(w, 1)), (int(x - 100), int(y - 20)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
    cv2.putText(image, "Height {} px".format(round(h, 1)), (int(x - 100), int(y + 15)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
    break
  getLengths(image)
  
