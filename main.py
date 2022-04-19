import cv2 as cv
import numpy as np

img = cv.imread('numbers.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# plt.imshow(img, cmap='gray')
# plt.show()

img = img[200:800, 100:600]

ret, threshold = cv.threshold(img, 143, 255, cv.THRESH_BINARY_INV)

kernel = np.ones((3, 3), np.uint8)
open = cv.morphologyEx(threshold, cv.MORPH_OPEN, kernel)
dil = cv.dilate(open, kernel, iterations=1)

contours, h = cv.findContours(dil, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

img_copy = img.copy()
cv.drawContours(img_copy, contours, -1, (255, 0, 0), 2)

cv.imshow('img', img_copy)
cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1)

def sort_contours(cnts, method="left-to-right"):
    # initialize the reverse flag and sort index
    reverse = False
    i = 0

    # handle if we need to sort in reverse
    if method == "right-to-left" or method == "bottom-to-top":
        reverse = True

    # handle if we are sorting against the y-coordinate rather than
    # the x-coordinate of the bounding box
    if method == "top-to-bottom" or method == "bottom-to-top":
        i = 1

    # construct the list of bounding boxes and sort them from top to
    # bottom
    bound_boxes = [cv.boundingRect(c) for c in cnts]
    (cnts, bound_boxes) = zip(*sorted(zip(cnts, bound_boxes),
                                      key=lambda b: b[1][i], reverse=reverse))
    # return the list of sorted contours and bounding boxes
    return cnts, bound_boxes


# # calling the function
# cnts, bboxs = sort_contours(contours)
# print(len(cnts))
#
# xxx = []
# yyy = []
# www = []
# hhh = []
# for i in cnts:
#     (xs, ys, ws, hs) = cv.boundingRect(i)
#     if (ws >= 0) and (hs >= 100):
#         xxx.append(xs)
#         yyy.append(ys)
#         www.append(ws)
#         hhh.append(hs)
#         i += 1
#
# for x, y, w, h in zip(xxx, yyy, www, hhh):
#     image = img.copy()
#     cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 5)
#     cv.imshow('highlights', image)
#     cv.waitKey(0)
#     cv.destroyAllWindows()

# cv.imshow('img', img)
# cv.waitKey(0)
# cv.destroyAllWindows()
# cv.waitKey(1)
