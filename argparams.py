import argparse

__p = argparse.ArgumentParser(description="generate a recursive Battenberg image")
__p.add_argument("ncolors", help="number of unique colors used in the image. Has to be a power of 2.")
__p.add_argument("-o", "--output", help="output path, defaults to output.png", default="output.png")

__args = __p.parse_args()

number_of_colors = int(__args.ncolors)
output_path = __args.output
