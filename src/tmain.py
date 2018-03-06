import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat

from encode import mask, image
from utils import evalute

from utils.common import *


if __name__ == '__main__':
    # test_mask()
    # image.test_image(label = True)
    img = loadmat(ROOT_DIR + '/data/cell_seg.mat')
    # print(img)
    img = np.array(img['BW'])
    print(img.shape)
    img = np.int_(img)

    id = '0a7d30b252359a10fd298b638b90cb9ada3acced4e0c0e5a3692013f432ee4e9'
    file = ROOT_DIR + "/data/train/{}/images/{}.png".format(id,id)
    true_masks = ROOT_DIR + "/data/train/{}/masks/*.png".format(id)

    evalute.evalute_score(true_masks, img)