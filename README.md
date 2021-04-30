# img2gds
A small python 3 script to convert images to a GDSII file. The output layer and datatype is automatically set to 0 and 1000, respectively.

Based on [opencv-python](https://github.com/opencv/opencv-python), [numpy](https://numpy.org), and [gdstk](https://github.com/heitzmann/gdstk).

## Usage:
```
$ python3 img2gds.py <input> <pixel size [um]> <output>
```
## Example:
```
$ python3 img2gds.py example.png 0.001 example.gds
```
