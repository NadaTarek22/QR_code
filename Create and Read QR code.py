#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install qrcode


# In[3]:


# Importing library
import qrcode

# Data to be encoded
data = 'Nada Tarek'

# Encoding data using make() function
img = qrcode.make(data)

# Saving as an image file
img.save('MyQRCodeMyName.png')


# In[4]:


import cv2
# read the QRCODE image
img = cv2.imread("MyQRCodeMyName.png")
# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()
# detect and decode
data, bbox, straight_qrcode = detector.detectAndDecode(img)
# if there is a QR code
if bbox is not None:
    print(f"QRCode data:\n{data}")
    # display the image with lines
    # length of bounding box
    n_lines = len(bbox)
    for i in range(n_lines):
        # draw all lines
        point1 = tuple(bbox[i][0])
        point2 = tuple(bbox[(i+1) % n_lines][0])
        cv2.line(img, point1, point2, color=(255, 0, 0), thickness=2)
# display the result
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()        


# In[ ]:




