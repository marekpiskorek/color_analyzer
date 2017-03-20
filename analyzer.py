#!/usr/bin/env python
import argparse
from colorthief import ColorThief
import imghdr
from os import listdir, path, getcwd
from os.path import isfile, join


parser = argparse.ArgumentParser(
    description='''Get most dominant colors from picture files in directory.
    If no directory is provided, current directory is used.'''
)
parser.add_argument(
    'directory', nargs='?', default=getcwd(), help='File directory',
)

BLACK = (False, False, False)
RED = (True, False, False)
YELLOW = (True, True, False)
GREEN = (False, True, False)
CYAN = (False, True, True)
BLUE = (False, False, True)
MAGENTA = (True, False, True)
WHITE = (True, True, True)

WEB_COLOURS = {
    BLACK: 'black',
    RED: 'red',
    YELLOW: 'yellow',
    GREEN: 'green',
    CYAN: 'cyan',
    BLUE: 'blue',
    MAGENTA: 'magenta',
    WHITE: 'white',
}


def get_colors_from_file(filename, color_number=3):
    # Keep in mind that ColorThief palette contains unique colors in terms of
    # RGB palette. We need to get 3 colors from our simplified base of 8
    # colors. I assume that among top 10 colors there will be at least 3 unique
    # colors of our simplified palette.
    # quality = 5 is an attempt to improve the runtime of color analyzer.
    # - in our base of 8 colors there is no need for higher quality.
    palette = ColorThief(filename).get_palette(color_count=10, quality=5)
    unique_colors = []
    for color in palette:
        simplified_color = get_matching_color_for_rgb(color)
        if simplified_color not in unique_colors:
            unique_colors.append(simplified_color)
        if len(unique_colors) >= color_number:
            break
    return unique_colors


def get_matching_color_for_rgb(color):
    # Here we simply need to map value for each tuple element (each of R, G. B)
    # onto bool value in order to determine whether it is more of 0 or 255.
    simplified_color = tuple([elem > 127 for elem in color])
    return WEB_COLOURS.get(simplified_color, 'Unknown')


def __main__():
    args = parser.parse_args()
    filepath = args.directory
    try:
        filenames = [
            path.join(filepath, f)
            for f in listdir(filepath) if isfile(join(filepath, f))
        ]
    except OSError:
        print '>>> {} is not a directory!'.format(filepath)
        return
    filenames = filter(lambda x: imghdr.what(x) is not None, filenames)
    if not filenames:
        print '>>> There are no image files!'
    for filename in filenames:
        print '>>> {}:'.format(filename)
        colors = get_colors_from_file(filename)
        for color in colors:
            print '> {}'.format(color)


if __name__ == '__main__':
    __main__()
