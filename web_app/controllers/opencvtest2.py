from time import clock
import numpy as np
import cv2
import cv2.cv as cv
from livestreamer import Livestreamer
import subprocess as sp

help_message = '''
USAGE: facedetect.py [--cascade <cascade_fn>] [--nested-cascade <cascade_fn>] [<video_source>]
'''

def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30), flags = cv.CV_HAAR_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        #if (150 < y1 < 370 and 100 < x1 < 350) or (100 < x2 < 350 and 150 < y2 < 370):
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

if __name__ == '__main__':
    import sys, getopt
    print help_message
    
    args, video_src = getopt.getopt(sys.argv[1:], '', ['cascade=', 'nested-cascade='])
    try: video_src = video_src[0]
    except: video_src = 0
    args = dict(args)
    cascade_fn = args.get('--cascade', "haarcascade_frontalface_alt.xml")
    nested_fn  = args.get('--nested-cascade', "haarcascade_eye.xml")

    cascade = cv2.CascadeClassifier(cascade_fn)
    nested = cv2.CascadeClassifier(nested_fn)

    FFMPEG_BIN = 'C:/ffmpeg/bin/ffmpeg.exe'

    livestreamer = Livestreamer()
    plugin = livestreamer.resolve_url("http://www.ustream.tv/channel/personal-cam1")
    streams = plugin.get_streams()
    stream = streams.get("best")
    VIDEO_URL = stream.url
    print VIDEO_URL
    pipe = sp.Popen([FFMPEG_BIN, "-i", VIDEO_URL,
           "-loglevel", "quiet", # no text output
           "-an",   # disable audio
           "-f", "image2pipe",
           "-pix_fmt", "bgr24",
           "-vcodec", "rawvideo", "-"],
           stdin = sp.PIPE, stdout = sp.PIPE)

    while True:
        raw_image = pipe.stdout.read(426*240*3) # read 432*240*3 bytes (= 1 frame)
        img = np.fromstring(raw_image, dtype='uint8').reshape((240,426,3))

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        rects = detect(gray, cascade)
        vis = img.copy()

        draw_rects(vis, rects, (0, 255, 0))
        for x1, y1, x2, y2 in rects:
            roi = gray[y1:y2, x1:x2]
            vis_roi = vis[y1:y2, x1:x2]
            subrects = detect(roi.copy(), nested)
            draw_rects(vis_roi, subrects, (255, 0, 0))

        cv2.imshow('facedetect', vis)
        if cv2.waitKey(5) == 27:
            break
    cv2.destroyAllWindows()
