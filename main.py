#! -*- encoding: utf-8 -*-

import os
import sys
import shutil
from PIL import Image

PATH = '/Users/vitor/ext4/{0}'
IMAGE_PATH = '/Users/vitor/Pictures/backup/'
DOC_PATH = '/Users/vitor/Documents/backup/'
COMPRESSED_PATH = '/Users/vitor/Documents/backup/'
SONG_PATH = '/Users/vitor/Music/backup/'
VIDEO_PATH = '/Users/vitor/Movies/backup/'
COMP = '/{0}'
# only images bigger than 400px are included
LIMIAR = 400


def collect_dirs(directory):
  dirs = os.listdir(directory.format(""))
  dirs.remove('.DS_Store')
  return dirs 

def collect_files(directory):
  files = list()
  for file in os.listdir(directory):
    if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".gif"):
      files.append(file)
  return files

def collect_info_image(image_path):
  try:
    img = Image.open(image_path)
    return img.size
  except Exception, e:
    return (-1, e)

def move_general_files(directory):
  files = list()
  for file in os.listdir(directory):
    if file.endswith(".docx") or file.endswith(".doc") or file.endswith(".ppt") or file.endswith(".pptx") or file.endswith(".pdf"):
      files.append(file)
  for file in files:
    file_path = directory + COMP.format(file)
    shutil.move(file_path, DOC_PATH)
    print "[DOC] " + file_path

def move_song_files(directory):
  files = list()
  for file in os.listdir(directory):
    if file.endswith(".mp3") or file.endswith(".ogg") or file.endswith(".wma"):
      files.append(file)
  for file in files:
    file_path = directory + COMP.format(file)
    shutil.move(file_path, SONG_PATH)
    print "[SONG] " + file_path

def move_image_files(directory):
  files = collect_files(directory)
  for file in files:
    image_path = directory + COMP.format(file) 
    info = collect_info_image(image_path)
    if info[0] == -1:
      print "couldn't read image info, reason:" + info[1]
      continue
    else:
      if info[0] > LIMIAR:
        shutil.move(image_path, IMAGE_PATH)
        print "[IMG] " + image_path

def move_compressed_files(directory):
  files = list()
  for file in os.listdir(directory):
    if file.endswith(".zip") or file.endswith(".rar"):
      files.append(file)
    for file in files:
      file_path = directory + COMP.format(file)
      try:
        shutil.move(file_path, COMPRESSED_PATH)
      except Exception, e:
        print e
        continue
      print "[ZIP] " + file_path

def move_video_files(directory):
  files = list()
  for file in os.listdir(directory):
    if file.endswith(".mpg") or file.endswith(".mp4"):
      files.append(file)
    for file in files:
      file_path = directory + COMP.format(file)
      try:
        shutil.move(file_path, VIDEO_PATH + 'video-' + file)
      except Exception, e:
        print e
        continue
      print "[MOV] " + file_path

def main(argv):
  directories = collect_dirs(PATH)
  # directories = list()
  # directories.append(argv[1])
  for directory in directories:
    # moving general files (docx, doc, ppt, pptx, pdf)
    move_general_files(PATH.format(directory))
    # moving song files (mp3, ogg, wma)
    move_song_files(PATH.format(directory))
    # moving image files (png, jpg, gif)
    move_image_files(PATH.format(directory))
    # moving zip files (zip, rar)
    move_compressed_files(PATH.format(directory))
    # moving video files (mpg, mp4)
    move_video_files(PATH.format(directory))

if __name__ == '__main__':
  main(sys.argv)