import keras
import sys, os

from encode.image import *
from model.unet import *
from utils.common import *

from tqdm import tqdm
from skimage.io import imread, imshow, imread_collection, concatenate_images
from skimage.transform import resize
from keras.callbacks import EarlyStopping, ModelCheckpoint
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
#
TRAIN_PATH = "../data/train/"
# TEST_PATH =  "../data/test/"

train_ids = next(os.walk(TRAIN_PATH))[1]
# test_ids = next(os.walk(TEST_PATH))[1]


# getting and resizing input images.
X_train = np.zeros((len(train_ids), IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_CHANNELS), dtype=np.int8)
Y_train = np.zeros((len(train_ids), IMAGE_HEIGHT, IMAGE_WIDTH, 1), dtype=np.bool)

# X_test = np.zeros((len(test_ids), IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_CHANNELS), dtype=np.int8)

print("Getting and resizing input images.")
sys.stdout.flush()
for n, id_ in tqdm(enumerate(train_ids), total=len(train_ids)):
    img_path = TRAIN_PATH + id_
    img = imread(img_path + "/images/" + id_ + ".png")[:,:,:IMAGE_CHANNELS]
    img = resize(img, (IMAGE_HEIGHT, IMAGE_WIDTH), mode='constant', preserve_range=True)
    X_train[n] = img

    # mask = np.zeros((IMAGE_HEIGHT, IMAGE_WIDTH, 1), dtype=np.bool)
    # for mask_file in next(os.walk(img_path + '/masks/'))[2]:
    #     mask_ = imread(img_path + '/masks/' + mask_file)
    #     mask_ = np.expand_dims(resize(mask_, (IMAGE_HEIGHT, IMAGE_WIDTH), mode='constant', 
    #                                   preserve_range=True), axis=-1)
    #     mask = np.maximum(mask, mask_)
    # Y_train[n] = mask

    mask = masks_merge(img_path + "/masks/*.png", flag_resize = True, new_shape = (IMAGE_HEIGHT, IMAGE_WIDTH, 1))
    Y_train[n] = mask
print("Finished!")

if __name__ == '__main__':
    model = unet(128, 128, 3)
    earlystopper = EarlyStopping(patience=7, verbose=1)
    checkpointer = ModelCheckpoint('model-dsbowl2018-1.h5', verbose=1, save_best_only=True)
    results = model.fit(X_train, Y_train, validation_split=0.1, batch_size=16, epochs=50,
                        callbacks=[earlystopper, checkpointer])