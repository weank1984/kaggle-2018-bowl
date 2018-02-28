import cv2
import math
import numpy as np


def run_length_encode(mask):
    """
    Descripition: Convert mask image into run-length enconde. 

    Args
    -----    
    mask: A simple of gray image. The simple consists of digital signals(1 and 0).

    Returns
    --------    
    rle: A list of positions which encoded by run-length.
    """
    signals = np.where(mask == 255)[0] # get positions of mask pixels.
    # brance 0: no mask in image.
    if signals is None:
        print("Check input image, there isn't mask.")
        return None
    # print(signals)
    head = signals[0]                  # first pixel of run-length encode.
    signal = head                      # recode previous position.
    rle = [[head+1,1]]                 # branch 1: only one pixel
    for dot in signals: 
        if dot - signal > 1:           # check if position is adjacent(nearby)
            rle[-1][1] = signal - head + 1  #branch 2: no adjacent, new encode and update length of previous encode
            rle.append([dot+1, 1])      
            head = dot                 # update head and signal
        signal = dot
    # branch 4: no end signal
    else:
        rle[-1][1] = signals[-1] - head + 1   
    return rle


def run_length_decode(shape, rle):
    """
    Descripition: Convert run-length encode into mask image.

    Args 
    ----
    shape: size of origin image.
    rle: Run-length encode.

    Returns
    ------- 
    mask: Mask image.
    """
    # width, heigth = shape[0], shape[1]
    image = np.zeros(shape)
    image = image.flatten()
    for [pos, range] in rle:
        image[pos-1:pos+range-1] = 255
    image = np.reshape(image, shape).T
    return image


def test_mask():
    """
    Test mask moudle.
    -----------------
    """
    # import moudles
    import matplotlib.pyplot as plt
    from utils.common import ROOT_DIR  
    # define file path
    test_file = ROOT_DIR + "/data/train/0a7d30b252359a10fd298b638b90cb9ada3acced4e0c0e5a3692013f432ee4e9/masks/39acbc082528c996d9fc3a3181938580f6c48461ee9eea91ff273e9d2c4499d0.png"    
    # test run_length_encode and run_length_decode
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