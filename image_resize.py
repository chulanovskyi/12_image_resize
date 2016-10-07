from  PIL import Image
import argparse
from os.path import basename


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('original_path')
    parser.add_argument('--width', type=int)
    parser.add_argument('--height', type=int)
    parser.add_argument('-s', '--scale', type=float)
    parser.add_argument('resized_path')
    return parser


def resize_image(**params):
    image = Image.open(params['original_path'])
    if params['scale']:
        width, height = image.size
        new_size = (int(params['scale']*width), int(params['scale']*height))
        resized_image = image.resize(new_size)
    return resized_image


def save_image(image, resized_path):
    pass


if __name__ == '__main__':
    parser = create_parser()
    params = parser.parse_args()
    if params.scale and params.width or params.scale and params.height:
        print('Error!')
        print('If --scale is defined, then --height or --width not allowed')
        exit(11)
    new_image = resize_image(**vars(params))
    if params.resized_path:
        save_image(new_image, params.resized_path)
    else:
        file_name = basename(params.original_path)
        
