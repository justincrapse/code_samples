"""
Last night you had to study, but decided to party instead. Now there is a black and white photo of you that is about
to go viral. You cannot let this ruin your reputation, so you want to apply box blur algorithm to the photo to hide
its content. The algorithm works as follows: each pixel x in the resulting image has a value equal to the average value
of the input image pixels' values from the 3 × 3 square with the center at x. All pixels at the edges are cropped. As
pixel's value is an integer, all fractions should be rounded down.
input:
image: [[36,0,18,9,9,45,27],
        [27,0,54,9,0,63,90],
        [81,63,72,45,18,27,0],
        [0,0,9,81,27,18,45],
        [45,45,27,27,90,81,72],
        [45,18,9,0,9,18,45],
        [27,81,36,63,63,72,81]]
output:
[[39,30,26,25,31],
 [34,37,35,32,32],
 [38,41,44,46,42],
 [22,24,31,39,45],
 [37,34,36,47,59]]
"""


def box_blur(image):
    new_image = []

    m_list = [i[1:-1] for i in image[1:-1]]
    for i1, v1 in enumerate(m_list):
        new_row = []
        for i2, v2 in enumerate(v1):
            pixels = [i[i2:i2 + 3] for i in image[i1:i1 + 3]]
            new_row.append(int(sum([sum(i) for i in pixels]) / 9))
        new_image.append(new_row)
    return new_image


image_in = [[36, 0, 18, 9, 9, 45, 27],
            [27, 0, 54, 9, 0, 63, 90],
            [81, 63, 72, 45, 18, 27, 0],
            [0, 0, 9, 81, 27, 18, 45],
            [45, 45, 27, 27, 90, 81, 72],
            [45, 18, 9, 0, 9, 18, 45],
            [27, 81, 36, 63, 63, 72, 81]]

print(*box_blur(image_in), sep='\n')
