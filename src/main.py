import pprint
import os
import sys
import colors

def main():
    fn = sys.argv[1]

    img = colors.get_image(fn)
    colores = colors.get_colors(img)

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(colores)

    palette = colors.get_palette(colores)

    print("\nThe palette of " + fn + " is: " + str(palette))

if __name__ == "__main__":
    main()