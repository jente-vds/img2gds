import cv2
import numpy as np
import gdstk
import sys

def main(filename, pixel_size, output):
    """Convert an image to a GDS file"""

    img = cv2.imread(filename, flags=cv2.IMREAD_GRAYSCALE)

    _, binaryImage = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
    binaryImage = cv2.flip(binaryImage, 0) # Flip image vertically since upper left corner is coordinate basis
    contours, hierarchy = cv2.findContours(binaryImage, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_TC89_KCOS) # Extract coordinates of contours
    hierarchy = np.squeeze(hierarchy)
    for i in range(len(contours)):
        contours[i] = np.squeeze(contours[i]).astype(float)*float(pixel_size) # Squeeze and correct dimensions

    lib = gdstk.Library()
    cell = gdstk.Cell("main")
    ld = {"layer":0, "datatype":1000}

    for i in np.where(hierarchy[:,3]==-1)[0]:
        if hierarchy[i,2]==-1 and len(contours[i])>2:
            cell.add(gdstk.Polygon(contours[i], **ld)) # Add a polygon without internals
        elif len(contours[i])>2 and hierarchy[i,2]!=-1:
            poly_p = gdstk.Polygon(contours[i], **ld)
            j = hierarchy[i,2]
            while True:
                if len(contours[j])>2:
                    poly_p = gdstk.boolean(poly_p, gdstk.Polygon(contours[j], **ld), "not", **ld)
                j = hierarchy[j,0]
                if j == -1:
                    break
            try:
                cell.add(*poly_p)
            except:
                cell.add(poly_p)

    lib.add(cell)
    lib.write_gds(output)

if __name__ == "__main__":
    args = sys.argv
    if len(args) == 4:
        filename = args[1]
        pixel_size = args[2]
        output = args[3]
        main(str(filename), pixel_size, str(output))
    else:
        print("usage: python img2gds.py <filename> <pixelSize[um]> <outputName>")
        quit()
