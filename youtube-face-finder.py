import sys
import os
from os import path
import face_recognition
import constants

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

    return face_recognition.load_image_file(image_path)

"""
Reads multiple images from the given directory path.
Uses read_image(...)
"""
def read_multiple_images(dir_path):
    if(path.exists(dir_path) == False):
        print("There is not such directory with that path: {}".format(dir_path))
        sys.exit()
    
    all_image_files_paths = [f for f in os.listdir(dir_path) if path.isfile(path.join(dir_path, f)) and is_authorized_image_file(f)]

    images_content_list = []
    for image_file_path in all_image_files_paths:
        new_image_content = read_image(dir_path + "/" + image_file_path)
        images_content_list.append(new_image_content)

    return images_content_list


#def find_face(known_image, unknown_image_to_eval):

def main():
    """
    unknown_image_content = read_image(constants.UNKNOWN_PEOPLE_DIR + "/picture_example1.jpg") #This will be a youtube stream
    known_image_content = read_image(constants.KNOWN_PEOPLE_DIR + "/me_1.jpg")

    face_locations = face_recognition.face_locations(unknown_image_content)
    print(face_locations)
    print("How many people are in this image: {}".format(len(face_locations)))
    """
    all_dir_images_content = read_multiple_images(constants.UNKNOWN_PEOPLE_DIR)
    for image_content in all_dir_images_content:
        face_locations = face_recognition.face_locations(image_content)
        print(face_locations)

if __name__ == "__main__":
    main()
