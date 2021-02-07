import pprint
import os
import sys
import colors

def main():
    fn = sys.argv[1]

    img = colors.get_image(fn)
    colores = colors.get_colors(img)

    palette = colors.get_palette(colores)

    if sys.argv[2] == "1":
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(colores)
        print("\nThe palette of " + fn + " is: " + str(palette))
    elif sys.argv[2] == "0":
        print("\nThe palette of " + fn + " is: " + str(palette))

if __name__ == "__main__":
    main()