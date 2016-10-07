from  PIL import Image
import argparse
from os.path import basename, splitext


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('original_path')
    parser.add_argument('--width', type=int)
    parser.add_argument('--height', type=int)
    parser.add_argument('--scale', type=float)
    parser.add_argument('--output')
    return parser


def resize_image(image, **params):
    width, height = image.size
    image_ratio = round((image.width / image.height), 1)
    if params['scale']:
        new_size = (int(params['scale']*width), int(params['scale']*height))
    if params['width'] and params['height']:
        new_size = (params['width'], params['height'])
    elif params['width']:
        new_size = (params['width'], int(params['width']/image_ratio))
    elif params['height']:
        new_size = (int(params['height']*image_ratio), params['height'])
    resized_image = image.resize(new_size)
    return resized_image


def save_image(image, name, ext, out_path=None):
    width, height = image.size
    new_file_name = '{name}__{w}x{h}{ext}'.format(
        name=name,
        w=width,
        h=height,
        ext=ext)
    if out_path:
        new_file_name = out_path + new_file_name
    if '.jpg' in ext:
        ext = 'JPEG'
    if '.png' in ext:
        ext = 'PNG'
    image.save(new_file_name, ext)


if __name__ == '__main__':
    parser = create_parser()
    params = parser.parse_args()
    if params.scale and params.width or params.scale and params.height:
        print('Error!')
        print('If [--scale] is defined, then [--height] or [--width] not allowed')
        exit(11)
    image = Image.open(params.original_path)    
    image_name, image_ext = splitext(basename(params.original_path))
    new_image = resize_image(image, **vars(params))
    image_ratio = round((image.width / image.height), 1)
    new_image_ratio = round((new_image.width / new_image.height), 1)
    if image_ratio != new_image_ratio:
        print('Warning! New image size ratio is different than original')
    save_image(new_image, image_name, image_ext, params.output)
