# img2gds
A small python script to convert images to a GDSII file.

Based on opencv-python (https://github.com/opencv/opencv-python), numpy (https://numpy.org), and gdstk (https://github.com/heitzmann/gdstk)

Usage: python3 img2gds.py \<input\> \<pixel size [um]\> \<output\>
  
  e.g.: python3 img2gds.py example.png 0.001 example.gds
