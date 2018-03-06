from skimage.io import imread
from skimage.io import imread_collection
import numpy as np


def masks_merge(masks_files, label = False):
    """
    Descripition: Merge all mask images into one.
    
    Args
    ----
    mask_files: Path to masks files.
    
    Returns
    -------
    image: A matrix of image.
    """
    masks = imread_collection(masks_files)
    print(masks[0].shape)
    if masks:
        height, weight = masks[0].shape
    else:
        print("Masks io error!")
        exit(False)
    image = np.zeros((height,weight), np.uint16)
    sign = 0 if label else 255
    for mask in masks:
        sign = sign+1 if label else sign
        image[mask > 0] = sign
    return image


def test_image(label):
    """
    Test image moudle.
    ------------------
    """
    # import moudles
    import matplotlib.pyplot as plt
    from utils.common import ROOT_DIR    
    # define path file.
    id = '0a7d30b252359a10fd298b638b90cb9ada3acced4e0c0e5a3692013f432ee4e9'
    origin_file = ROOT_DIR + "/data/train/{}/images/{}.png".format(id, id)
    masks_files = ROOT_DIR + "/data/train/{}/masks/*.png".format(id)
    # test masks_merge moudle.
    origin_image = imread(origin_file)
    plt.subplot(1,2,1)
    plt.imshow(origin_image)
    plt.title("origin")
    img = masks_merge(masks_files, label)
    plt.subplot(1,2,2)    
    plt.imshow(img)
    plt.title("masks merge")
    plt.show()