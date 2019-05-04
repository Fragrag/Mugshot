############
# ANALYZER #
############

"""
This script will analyze the dataset collected by Collector 
and it will go through all the images.

If it finds and is able to encode a face, it will add it to a JSON file.

A single JSON object will contain the following information:
    Unique ID
    Face encoding
    Charges


"""

import face_recognition
import json
import glob
import os
import numpy as np

def get_face_encoding(img_loc):
    """
    Gets the face encoding of an image. 

    :param img_loc: image location

    :return: face location as numpy array and face encoding as list, If an inappropriate amount of faces is found, then it will return None
    """
    image = face_recognition.load_image_file(img_loc)

    face_loc = face_recognition.face_locations(image)

    face_enc = face_recognition.face_encodings(image, face_loc)
    return face_loc, face_enc

def analyze_folder(folder_location):
    data = {}
    data['mugshots'] = []
    nr = 0

    for file in glob.glob(os.path.join(folder_location, '**/*.png'), recursive=True):
        file_face_loc, file_face_enc = get_face_encoding(file)

        if len(file_face_loc) == 1:
            print(nr)
            # file_face_enclist = file_face_enc.tolist()
            data['mugshots'].append({
                'id': nr,
                'location': file_face_loc,
                'encoding': file_face_enc[0].tolist()
            })
            nr += 1
            # print(file_face_enc)


    with open('./mugshot/dataset/dataset.json', 'w') as outfile:
        json.dump(data, outfile)

# analyze_folder("D:\\Photography\\CurrentProjects\\Mugshot\\mugshot\\dataset\\images\\sd18\\single\\f1_p0")
analyze_folder("D:\\Photography\\CurrentProjects\\Mugshot\\mugshot\\dataset\\images\\sd18")
# analyze_folder("D:\\Photography\\CurrentProjects\\Mugshot\\mugshot\\dataset\\images\\sd18\\single\\f0_p1")
# analyze_folder("D:\Photography\CurrentProjects\Mugshot\mugshot\dataset\images\personal")

print("Analysis complete!")

# test_face_loc, test_face_enc = get_face_encoding("D:\Photography\CurrentProjects\Mugshot\mugshot\images\haryo2.jpg")

# print(test_face_loc)
# print(test_face_enc)

# data = {}
# data['mugshots'] = []
# data['mugshots'].append({
#     'id': '1',
#     'location': test_face_loc,
#     'encoding': str(test_face_enc)
# })

# with open('data.json', 'w') as outfile:
#     json.dump(data, outfile)
