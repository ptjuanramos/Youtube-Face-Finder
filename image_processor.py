#!/usr/bin/env python
import os
from os import path
import face_recognition
import image_processor_models

authorized_extensions = [".jpg"] #TODO use this in the validation

"""
Check if image is .jpg extension(for now)
"""
def is_authorized_image_file(image_path):
    filename, file_extension = path.splitext(image_path)
    return file_extension == ".jpg" #For now is only jpg

"""
Reads image from the given path
"""
def read_image(image_path):
    if path.exists(image_path) == False:
        print("There is not such file with that path: {}".format(image_path))
        sys.exit()

    if is_authorized_image_file(image_path) == False: #For now is only jpg
        print("{} needs to be a jpg".format(image_path))
        sys.exit()

    image_content = face_recognition.load_image_file(image_path)
    return image_processor_models.ImageWrapper(image_path, image_content)

"""
TODO - to be removed since that we are going to create a youtube stream over the video
Reads multiple images from the given directory path.
Uses read_image(...)
"""
def read_multiple_images(dir_path):
    if(path.exists(dir_path) == False):
        print("There is not such directory with that path: {}".format(dir_path))
        sys.exit()
    
    all_image_files_paths = [f for f in os.listdir(dir_path) if path.isfile(path.join(dir_path, f)) and is_authorized_image_file(f)]
    if len(all_image_files_paths) == 0:
        print("There is no files in this directory: {}".format(dir_path))
        sys.exit()

    images_wrappers_list = []
    for image_file_path in all_image_files_paths:
        new_image_wrapper = read_image(dir_path + "/" + image_file_path)
        images_wrappers_list.append(new_image_wrapper)

    return images_wrappers_list

"""
TODO doc
"""
def process_face(known_face_encodings, unknown_face_encoding):
    faces_comparation = face_recognition.compare_faces(known_face_encodings, unknown_face_encoding)
    if faces_comparation[0] == True:
        return unknown_face_encoding
    return None

"""
TODO doc
"""
def match_encodings(known_face_encodings, unknown_faces_encodings):
    for unknown_face in unknown_faces_encodings:
        found_face = process_face(known_face_encodings, unknown_face)
        if found_face is not None:
            return found_face
    return None

"""
TODO doc
"""
def get_process_results(known_image_dir_path, unknown_image_dir_path):
    known_face_image = read_multiple_images(known_image_dir_path)[0] #TODO - change this to make multiple knwon images
    known_face_image_encoding = face_recognition.face_encodings(known_face_image.image_content)
    unknown_face_images = read_multiple_images(unknown_image_dir_path)
    list_possible_face_coords = []

    for image_wrapper in unknown_face_images:
        unknown_faces_encodings = face_recognition.face_encodings(image_wrapper.image_content)
        matched_face_encoding = match_encodings(known_face_image_encoding, unknown_faces_encodings)
        process_result = image_processor_models.ProcessingFaceResult(image_wrapper, unknown_faces_encodings, matched_face_encoding)
        list_possible_face_coords.append(process_result)

    return list_possible_face_coords