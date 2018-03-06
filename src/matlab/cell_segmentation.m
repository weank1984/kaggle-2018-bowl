function seg_img = cell_segmentation(image)
% https://blogs.mathworks.com/steve/2006/06/02/cell-segmentation/
I_eq = adapthisteq(image);
subplot(2,3,1);
imshow(I_eq);
title('origin');

bw = im2bw(I_eq, graythresh(I_eq));
subplot(2,3,2);
imshow(bw);
title('2');

bw2 = imfill(bw,'holes');
bw3 = imopen(bw2, ones(5,5));
bw4 = bwareaopen(bw3, 40);
bw4_perim = bwperim(bw4);
overlay1 = imoverlay(I_eq, bw4_perim, [.3 1 .3]);
subplot(2,3,3);
imshow(overlay1);
title('3');

mask_em = imextendedmax(I_eq, 30);
subplot(2,3,4);
imshow(mask_em);

mask_em = imclose(mask_em, ones(5,5));
mask_em = imfill(mask_em, 'holes');
mask_em = bwareaopen(mask_em, 40);
overlay2 = imoverlay(I_eq, bw4_perim | mask_em, [.3 1 .3]);
subplot(2,3,5);
imshow(overlay2);

I_eq_c = imcomplement(I_eq);
I_mod = imimposemin(I_eq_c, ~bw4 | mask_em);
L = watershed(I_mod);
subplot(2,3,6);
imshow(label2rgb(L));
seg_img = L;
end

