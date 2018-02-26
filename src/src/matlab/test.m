clear;clc;
DIR_PATH = 'E:/kaggle data/2018 bowl';
img_path = strcat(DIR_PATH, '/train/0a7d30b252359a10fd298b638b90cb9ada3acced4e0c0e5a3692013f432ee4e9/masks');

images = masks_overlay(img_path);
imshow(images{1});
