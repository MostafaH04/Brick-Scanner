import cv2
import numpy as np
import os

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        img = cv2.resize(img, (1280,720))

        if img is not None:
            images.append(img)
    return images

images = load_images_from_folder("Simulation/Images/")
for i in range(len(images)-1):
  img = cv2.cvtColor(images[i],cv2.COLOR_BGR2GRAY)
  img2 = cv2.cvtColor(images[i+1], cv2.COLOR_BGR2GRAY)

# Initiate SIFT detector
  sift = cv2.SIFT_create()
# find the keypoints and descriptors with SIFT
  kp1, des1 = sift.detectAndCompute(img,None)
  kp2, des2 = sift.detectAndCompute(img2,None)

  FLANN_INDEX_KDTREE = 1
  index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
  search_params = dict(checks=50)   # or pass empty dictionary
  flann = cv2.FlannBasedMatcher(index_params,search_params)
  matches = flann.knnMatch(des1,des2,k=2)

  # Need to draw only good matches, so create a mask
  matchesMask = [[0,0] for i in range(len(matches))]
# ratio test as per Lowe's paper
  for i,(m,n) in enumerate(matches):
    if m.distance < 0.7*n.distance:
        matchesMask[i]=[1,0]
  draw_params = dict(matchColor = (0,255,0),
                   singlePointColor = (255,0,0),
                   matchesMask = matchesMask,
                   flags = cv2.DrawMatchesFlags_DEFAULT)
  img3 = cv2.drawMatchesKnn(img,kp1,img2,kp2,matches,None,**draw_params)
  img3 = cv2.resize(img3, (1280,640))

  # ret, thresh = cv2.threshold(img, 117, 255, 0)
  # contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

  # cv2.drawContours(img, contours, -1, (0,255,0), 3)
#   gray = img
#   gray = 255-gray

#   # do adaptive threshold on gray image
#   thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
#   thresh = 255-thresh

#   # apply morphology
#   kernel = np.ones((3,3), np.uint8)
#   morph = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
#   morph = cv2.morphologyEx(morph, cv2.MORPH_CLOSE, kernel)


#   # separate horizontal and vertical lines to filter out spots outside the rectangle
#   kernel = np.ones((7,3), np.uint8)
#   vert = cv2.morphologyEx(morph, cv2.MORPH_OPEN, kernel)
#   kernel = np.ones((3,7), np.uint8)
#   horiz = cv2.morphologyEx(morph, cv2.MORPH_OPEN, kernel)

#   # combine
#   rect = cv2.add(horiz,vert)

#   # thin
#   kernel = np.ones((3,3), np.uint8)
#   rect = cv2.morphologyEx(rect, cv2.MORPH_ERODE, kernel)

#   # get largest contour
#   contours = cv2.findContours(rect, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#   contours = contours[0] if len(contours) == 2 else contours[1]
#   for c in contours:
#       area_thresh = 0
#       area = cv2.contourArea(c)
#       if area > area_thresh:
#           area = area_thresh
#           big_contour = c

#   # get rotated rectangle from contour
#   rot_rect = cv2.minAreaRect(big_contour)
#   box = cv2.boxPoints(rot_rect)
#   box = np.int0(box)
#   print(box)

#   # draw rotated rectangle on copy of img
#   rot_bbox = img.copy()
#   cv2.drawContours(rot_bbox,[box],0,(0,0,255),2)

  cv2.imshow("tes",img3)
  cv2.waitKey(0)