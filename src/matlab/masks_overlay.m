function masks_in_one = masks_overlay(masks_path)

flist = dir(sprintf('%s/*.png', masks_path));
masks_in_one = [];

for imidx = 1:min(length(flist), 200)
    fprintf('[%d]', imidx);
    fname = sprintf('%s/%s', masks_path, flist(imidx).name);
    im = imread(fname);
    masks_in_one{length(masks_in_one)+1} = im;
end

end