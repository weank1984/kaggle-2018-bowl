import numpy as np
import skimage.io
import matplotlib.pyplot as plt
import skimage.segmentation

# from common import *
from encode import *


def evalute_score(true_masks, pred_masks):
    """
    Descripition: .
    
    Args
    ----
        .
    
    Returns
    -------
        .
    """
    true_masks = image.masks_merge(true_masks, label = True)
    # pred_masks = image.masks_merge(pred_masks, label = True)
    #
    fig = plt.figure()
    plt.subplot(1,2,1)
    plt.imshow(true_masks)
    plt.title("Ground truth masks")
    plt.subplot(1,2,2)
    plt.imshow(pred_masks)
    plt.title("Predict masks")

    #
    true_objects = len(np.unique(true_masks))
    pred_objects = len(np.unique(pred_masks))
    print("Number of true objects: ", true_objects)
    print("Number of predicted objects: ", pred_objects)

    # Compute intersection between all objects
    intersection = np.histogram2d(true_masks.flatten(), pred_masks.flatten(), bins=(true_objects, pred_objects))[0]

    # Compute areas (needed for finding the union between all objects)
    area_true = np.histogram(true_masks, bins = true_objects)[0]
    area_pred = np.histogram(pred_masks, bins = pred_objects)[0]
    area_true = np.expand_dims(area_true, -1)
    area_pred = np.expand_dims(area_pred, 0)

    # Compute union
    union = area_true + area_pred - intersection

    # Exclude background from the analysis
    intersection = intersection[1:,1:]
    union = union[1:,1:]
    union[union == 0] = 1e-9

    # Compute the intersection over union
    iou = intersection / union

    # Precision helper function
    def precision_at(threshold, iou):
        matches = iou > threshold
        true_positives = np.sum(matches, axis=1) == 1   # Correct objects
        false_positives = np.sum(matches, axis=0) == 0  # Missed objects
        false_negatives = np.sum(matches, axis=1) == 0  # Extra objects
        tp, fp, fn = np.sum(true_positives), np.sum(false_positives), np.sum(false_negatives)
        return tp, fp, fn

    # Loop over IoU thresholds
    prec = []
    print("Thresh\tTP\tFP\tFN\tPrec.")
    for t in np.arange(0.5, 1.0, 0.05):
        tp, fp, fn = precision_at(t, iou)
        p = tp / (tp + fp + fn)
        print("{:1.3f}\t{}\t{}\t{}\t{:1.3f}".format(t, tp, fp, fn, p))
        prec.append(p)
    print("AP\t-\t-\t-\t{:1.3f}".format(np.mean(prec)))

    plt.show()

    


def loU():
    """
    Descripition: .
    
    Args
    ----
        .
    
    Returns
    -------
        .
    """
    pass