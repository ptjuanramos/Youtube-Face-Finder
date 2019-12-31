from pytube import YouTube
import cv2
import image_processor

yt = YouTube("https://www.youtube.com/watch?v=UiM5CgT1g7Q")
print("Title of video: " + yt.title)

def progress_callback(stream, chunk, file_handle, bytes_remaining):
    temp_file_name = "video_chunks/frames/temp_{}.mp4".format(bytes_remaining)
    temp_file = open(temp_file_name, "wb")
    temp_file.write(chunk)

yt.register_on_progress_callback(progress_callback) #Reading meanwhile downloading
yt.streams.first().download(output_path = "video_chunks")

"""
vidcap = cv2.VideoCapture('video_chunks/' + yt.title + ".mp4")
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("video_chunks/frame-second-%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1
"""