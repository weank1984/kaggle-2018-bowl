import os
import numpy as np

import keras

Y_train = np.zeros((len(train_ids), IMAGE_HEIGHT, IMAGE_WIDTH, 1), dtype=np.bool)


if __name__ == '__main__':
    model = load_model('model-dsbowl2018-1.h5', custom_objects={'mean_iou':mean_iou})