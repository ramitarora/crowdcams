from livestreamer import Livestreamer
import cv2
import subprocess as sp
FFMPEG_BIN = 'C:/ffmpeg/bin/ffmpeg.exe'
import numpy

livestreamer = Livestreamer()
plugin = livestreamer.resolve_url("http://www.ustream.tv/channel/jamthehype")
streams = plugin.get_streams()
print streams
stream = streams.get("best")
cv2.namedWindow("GoPro",cv2.CV_WINDOW_AUTOSIZE)
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
    image =  numpy.fromstring(raw_image, dtype='uint8').reshape((240,426,3))
    cv2.imshow("GoPro",image)
    if cv2.waitKey(5) == 27:
        break
cv2.destroyAllWindows()