import argparse
from  PIL import Image
from os.path import basename, splitext


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('original_path')
    parser.add_argument('--width', type=int)
    parser.add_argument('--height', type=int)
    parser.add_argument('--scale', type=float)
    parser.add_argument('--output')
    return parser


def load_image(path):
    image = Image.open(path)
    image_name, image_ext = splitext(basename(path))
    allowed_formats = ['.jpg', '.png']
    if image_ext not in allowed_formats:
        return
    image_info = {'image': image,
                  'image_name': image_name,
                  'image_ext': image_ext}
    return image_info


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


def resize_image(image, scale=None, width=None, height=None):
    image_ratio = round((image.width / image.height), 1)
    if scale:
        new_size = (int(scale*image.width), int(scale*image.height))
    elif width and height:
        new_size = (width, height)
    elif width:
        new_size = (width, int(width/image_ratio))
    elif height:
        new_size = (int(height*image_ratio), height)
    else:
        return
    resized_image = image.resize(new_size)
    return resized_image


def check_ratio(image_1, image_2):
    image_1_ratio = round((image_1.width / image_1.height), 1)
    image_2_ratio = round((image_2.width / image_2.height), 1)
    if image_1_ratio != image_2_ratio:
        print('Warning! New image size ratio is different than original')


if __name__ == '__main__':
    parser = create_parser()
    params = parser.parse_args()
    if params.scale and params.width or params.scale and params.height:
        print('Error!')
        print('If [--scale] is defined, then [--height][--width] not allowed')
        exit(11)
    image = load_image(params.original_path)
    if not image:
        print('Error! Can\'t load image')
        exit(11)
    new_image = resize_image(
        image['image'],
        params.scale,
        params.width,
        params.height)
    if not new_image:
        print('No resize parameters were given')
        exit(11)
    check_ratio(image['image'], new_image)
    save_image(
        new_image,
        image['image_name'],
        image['image_ext'],
        params.output)
