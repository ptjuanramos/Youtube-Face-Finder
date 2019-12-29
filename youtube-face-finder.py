import sys
from os import path
import face_recognition

def read_image(image_path):
    if path.exists(image_path) == False:
        print("There is not such file with that path: {}".format(image_path))
        sys.exit()

    filename, file_extension = path.splitext(image_path)
    if file_extension != "jpg": #For now is only jpg
        print("{} needs to be a jpg".format(filename))
        sys.exit()

    image = face_recognition.load_image_file(image_path)

    return image

def main():
    if len(sys.argv) != 2:
        print("Please provide the image path as argument")
        sys.exit()

    image_content = read_image(sys.argv[1])

if __name__ == "__main__":
    main()
