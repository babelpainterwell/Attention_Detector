import os
import shutil
import random

DATASET_PATH = 'Columbia_Gaze_Data_Set'

def data_processing(dataset_path):
    gazing_images = []
    no_gazing_images = []

    for image_directory in os.listdir(dataset_path):
        full_dir_path = os.path.join(dataset_path, image_directory)

        # check if the path is a directory
        if os.path.isdir(full_dir_path):
            for image_file in os.listdir(full_dir_path):
                # make sure we are working with .jpg file
                if image_file.endswith('.jpg'):
                    full_img_path = os.path.join(full_dir_path, image_file)

                    if '_0V_0H' in image_file or '_0V_5H' in image_file or '_0V_-5H' in image_file:
                        gazing_images.append(full_img_path)
                    else:
                        no_gazing_images.append(full_img_path)

    # shuffle the list
    random.shuffle(gazing_images)
    random.shuffle(no_gazing_images)
    print(len(gazing_images))
    print(len(no_gazing_images))

    # split the images into training and test sets by 80%
    gazing_train = gazing_images[:int(len(gazing_images) * 0.8)]
    gazing_test = gazing_images[int(len(gazing_images) * 0.8):]

    # to avoid oversampling the majority class, we decrease by the ratio of no-gazing samples
    no_gazing_images = no_gazing_images[:int(0.16 * len(no_gazing_images))]
    no_gazing_train = no_gazing_images[:int(len(no_gazing_images) * 0.8)]
    no_gazing_test = no_gazing_images[int(len(no_gazing_images) * 0.8):]

    # make output directories
    os.makedirs('train4/gazing', exist_ok=True)
    os.makedirs('train4/no_gazing', exist_ok=True)
    os.makedirs('test4/gazing', exist_ok=True)
    os.makedirs('test4/no_gazing', exist_ok=True)

    # copy the images
    for img in gazing_train:
        shutil.copy(img, 'train4/gazing')

    for img in gazing_test:
        shutil.copy(img, 'test4/gazing')

    for img in no_gazing_train:
        shutil.copy(img, 'train4/no_gazing')

    for img in no_gazing_test:
        shutil.copy(img, 'test4/no_gazing')

# call the function
data_processing(DATASET_PATH)
