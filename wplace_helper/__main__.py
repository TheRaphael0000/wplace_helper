import argparse
from .split_by_color import img_to_unique_colors_imgs


def main():
    parser = argparse.ArgumentParser(
        prog='WPlace Helper',
        description='Split image by color',
        epilog='github.com/TheRaphael0000/wplace_helper'
    )
    parser.add_argument("filename")

    args = parser.parse_args()
    img_to_unique_colors_imgs(args.filename)


if __name__ == "__main__":
    main()