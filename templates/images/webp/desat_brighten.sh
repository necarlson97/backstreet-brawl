for file in *.webp; do convert "$file" -colorspace Gray -level 0x90% "${file%.*}_bw.png"; done
# ignoring jpg,jpeg,png,bmp,tiff,gif,

# Use rename to remove everything before the first ' - ' in the filenames
rename 's/^.*? - //' *.png
