for file in *.{webp}; do convert "$file" -colorspace Gray -level 0x90% "${file%.*}_bw.png"; done

# jpg,jpeg,png,bmp,tiff,gif,
