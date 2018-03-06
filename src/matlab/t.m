clc;clear;
DIR_PATH = 'E:/kaggle data/2018 bowl';
img_path = strcat(DIR_PATH, '/train/0a7d30b252359a10fd298b638b90cb9ada3acced4e0c0e5a3692013f432ee4e9/images/0a7d30b252359a10fd298b638b90cb9ada3acced4e0c0e5a3692013f432ee4e9.png');
img = imread(img_path);
subplot(1,2,1);
imshow(img);
title('Origin')
if ndims(img) == 3
    I = rgb2gray(img);
else
    I = img;
end
% subplot(1,2,2);
% imhist(I);
% title('Histogram');
g = imbinarize(I, graythresh(I));
gc = ~g;
D = bwdist(gc);
L = watershed(~D);
w =L ==0;
g2 = g & ~w;
subplot(1,2,2);
imshow(g2);

title('watershed');