import numpy

def find_coeffs(pa, pb):
    matrix = []
    for p1, p2 in zip(pa, pb):
        matrix.append([p1[0], p1[1], 1, 0, 0, 0, -p2[0]*p1[0], -p2[0]*p1[1]])
        matrix.append([0, 0, 0, p1[0], p1[1], 1, -p2[1]*p1[0], -p2[1]*p1[1]])

    A = numpy.matrix(matrix, dtype=numpy.float)
    B = numpy.array(pb).reshape(8)

    res = numpy.dot(numpy.linalg.inv(A.T * A) * A.T, B)
    return numpy.array(res).reshape(8)

from PIL import Image


def project(img, compressfactor):
    
    width, height = img.size

    x1= (compressfactor/2)*width
    x2= width-x1
    coeffs = find_coeffs(
        [(x1,0),(x2,0),(width,height),(0,height)],
        [(0,0),(width,0),(width,height),(0,height)])
    print(coeffs)

    newimg= img.transform((width, height), Image.PERSPECTIVE, coeffs, Image.BICUBIC)
    return newimg

