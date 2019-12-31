"""

"""
class ProcessingFaceResult:
    def __init__(self, image_wrapper, face_encodings, face_match):
        self.image_wrapper = image_wrapper
        self.found_match = face_match is not None
        self.face_encodings = face_encodings
        self.identified_faces = len(self.face_encodings)
        self.face_match = face_match

"""
"""
class ImageWrapper:
    def __init__(self, image_path, image_content):
        self.image_path = image_path
        self.image_content = image_content