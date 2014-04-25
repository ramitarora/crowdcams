from __future__ import absolute_import
import cv2
from cv2 import cv
from livestreamer import Livestreamer
import subprocess as sp
import numpy as np
from celery import shared_task


def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30),
                                     flags=cv.CV_HAAR_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:, 2:] += rects[:, :2]
    return rects


def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        #if (150 < y1 < 370 and 100 < x1 < 350) or (100 < x2 < 350 and 150 < y2 < 370):
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)


@shared_task
def face_detect(x, y, width, height, stream_url):
    x = x*426/651
    y = y*240/398
    width = width*426/651
    height = height*240/398
    cascade_fn = "haarcascade_frontalface_alt.xml"
    nested_fn = "haarcascade_eye.xml"

    cascade = cv2.CascadeClassifier(cascade_fn)
    nested = cv2.CascadeClassifier(nested_fn)

    FFMPEG_BIN = 'C:/ffmpeg/bin/ffmpeg.exe'

    livestreamer = Livestreamer()
    plugin = livestreamer.resolve_url(stream_url)
    streams = plugin.get_streams()
    stream = streams.get("best")
    VIDEO_URL = stream.url
    print VIDEO_URL
    pipe = sp.Popen([FFMPEG_BIN, "-i", VIDEO_URL,
                     "-loglevel", "quiet",  # no text output
                     "-an",  # disable audio
                     "-f", "image2pipe",
                     "-pix_fmt", "bgr24",
                     "-vcodec", "rawvideo", "-"],
                    stdin=sp.PIPE, stdout=sp.PIPE)
    interval = 0
    while True:
        raw_image = pipe.stdout.read(426 * 240 * 3)  # read 432*240*3 bytes (= 1 frame)
        img = np.fromstring(raw_image, dtype='uint8').reshape((240, 426, 3))
        img = img[y:(y + height), x:(x + width)]
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        rects = detect(gray, cascade)
        vis = img.copy()
        if rects:
            interval += 1
        draw_rects(vis, rects, (0, 255, 0))
        for x1, y1, x2, y2 in rects:
            roi = gray[y1:y2, x1:x2]
            vis_roi = vis[y1:y2, x1:x2]
            subrects = detect(roi.copy(), nested)
            draw_rects(vis_roi, subrects, (255, 0, 0))

        cv2.imwrite('./media/face', vis)
        if cv2.waitKey(5) == 27:
            break
    cv2.destroyAllWindows()