import cv2
import subprocess as sp
import numpy

VIDEO_URL = 'http://iphone-streaming.ustream.tv/watch/playlist.m3u8?cid=16258431&stream=live_3&appType=103&appVersion=3&conn=wifi&group=iphone'

cv2.namedWindow("GoPro",cv2.CV_WINDOW_AUTOSIZE)

pipe = sp.Popen([ 'ffmpeg.exe', "-i", VIDEO_URL,
           "-loglevel", "quiet", # no text output
           "-an",   # disable audio
           "-f", "image2pipe",
           "-pix_fmt", "bgr24",
           "-vcodec", "rawvideo", "-"],
           stdin = sp.PIPE, stdout = sp.PIPE)
while True:
    raw_image = pipe.stdout.read(432*240*3) # read 432*240*3 bytes (= 1 frame)
    image = numpy.fromstring(raw_image, dtype='uint8').reshape((240,432,3))
    cv2.imshow("GoPro",image)
    if cv2.waitKey(5) == 27:
        break
cv2.destroyAllWindows()