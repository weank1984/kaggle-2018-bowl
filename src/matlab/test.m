clear;clc;
DIR_PATH = 'E:/kaggle data/2018 bowl';
img_path = strcat(DIR_PATH, '\train\2a1a294e21d76efd0399e4eb321b45f44f7510911acd92c988480195c5b4c812\images\2a1a294e21d76efd0399e4eb321b45f44f7510911acd92c988480195c5b4c812.png');
image = imread(img_path);


images = cell_segmentation(rgb2gray(image));

