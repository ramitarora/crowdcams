import cv2
import numpy
import sms
import thread
import gc

def image_not_equal(img1, img2):
    return not (numpy.allclose(img1, img2, 24.50, 30.0))

def diffImg(t0, t1, t2):
    d1 = cv2.absdiff(t2, t1)
    d2 = cv2.absdiff(t1, t0)
    return cv2.bitwise_and(d1, d2)


cam = cv2.VideoCapture(0)

winName = "Movement Indicator"
cv2.namedWindow(winName, cv2.CV_WINDOW_AUTOSIZE)

# Read three images first:
t_minus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
store_t =t
counter = 0
while True:
    cv2.imshow(winName, diffImg(t_minus, t, t_plus))
    # Read next image
    t_minus = t
    t = t_plus
    t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
    counter+=1
    if (counter %10==0):
        store_t = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
    if (counter %19==0):
        counter = 0
        motion_detected = image_not_equal(store_t, t_plus)
        print motion_detected
        gc.collect()
        #gc.collect()
    #if motion_detected:
    #     try:
    #         thread.start_new_thread(sms.send_sms())
    #     except:
    #         print "Error: unable to start thread"
    key = cv2.waitKey(10)
    if key == 27:#escape key
        cv2.destroyWindow(winName)
        break

