#!/usr/bin/env python
import constants
import image_processor

"""
It's only a separator
"""
def print_separator():
    print("-------------")

"""
Main function
"""
def main():
    #TODO make this being handle by sys.args

    process_result_list = image_processor.get_process_results(constants.KNOWN_PEOPLE_DIR, constants.UNKNOWN_PEOPLE_DIR)
    print_separator()
    for e in process_result_list:
        print("For image path: {}".format(e.image_wrapper.image_path))
        print("Number of faces: {}".format(e.identified_faces))
        print("Had a match: {}".format(e.found_match))
        print_separator()

if __name__ == "__main__":
    main()
