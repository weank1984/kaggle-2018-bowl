import cv2
import numpy as np
import matplotlib.pyplot as plt

from encode.mask import *
from utils.common import *

test_file = ROOT_DIR + "/data/train/0a7d30b252359a10fd298b638b90cb9ada3acced4e0c0e5a3692013f432ee4e9/masks/39acbc082528c996d9fc3a3181938580f6c48461ee9eea91ff273e9d2c4499d0.png"


if __name__ == '__main__':
    mask_file = np.array(cv2.imread(test_file, cv2.IMREAD_GRAYSCALE))
    shape = mask_file.shape
    mask = mask_file.T.flatten()
    rle = run_length_encode(mask)
    print(rle)
    img = run_length_decode(shape, rle)
    plt.imshow(img)
    n_rle = run_length_encode(img.T.flatten())
    print(n_rle)
    plt.show()