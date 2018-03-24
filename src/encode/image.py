from skimage.io import imread
from skimage.io import imread_collection
from skimage.transform import resize
import numpy as np

"""
#图像处理模块：
    mask_merge: 将切割并标记的mask图像，合并到一张图片上。</br>

"""

def masks_merge(masks_files, label = False, flag_resize = False, new_shape = 0):
    """
    Descripition: Merge all mask images into one.

    Args
    ----
    masks_files: Path to masks files.

    label: bool.
    
    Returns
    -------
    image: A matrix of image.
    """
    masks = imread_collection(masks_files)
    # check resize option.
    if flag_resize and new_shape != 0:
        masks = list(map(lambda x:resize(x, new_shape, mode='constant', preserve_range=True), masks))
    # print(masks[0].shape)
    if masks:
        shape = masks[0].shape
    else:
        print("Masks io error!")
        exit(False)
    image = np.zeros(shape, np.int8 if label else np.bool)
    sign = 0 if label else 1
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
    id = '00071198d059ba7f5914a526d124d28e6d010c92466da21d4a04cd5413362552'
    origin_file = ROOT_DIR + "/data/train/{}/images/{}.png".format(id, id)
    masks_files = ROOT_DIR + "/data/train/{}/masks/*.png".format(id)
    # test masks_merge moudle.
    origin_image = imread(origin_file)
    plt.subplot(1,3,1)
    plt.imshow(origin_image)
    plt.title("origin")

    img = masks_merge(masks_files, label, flag_resize = True, new_shape = (128, 128))
    img = resize(img, (256, 256), mode="constant", preserve_range=True)
    plt.subplot(1,3,2)
    plt.imshow(img)
    plt.title("up sample")

    img = masks_merge(masks_files, label)
    plt.subplot(1,3,3)
    plt.imshow(img)
    plt.title("group true")
    plt.show()