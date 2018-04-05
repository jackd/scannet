import os


def get_data_dir():
    key = 'SCANNET_PATH'
    if key in os.environ:
        dataset_dir = os.environ[key]
        if not os.path.isdir(dataset_dir):
            raise Exception('%s directory does not exist' % key)
        return dataset_dir
    else:
        raise Exception('%s environment variable not set.' % key)


def get_subfolder(scene_idx, view_idx):
    return 'scene%04d_%02d' % (scene_idx, view_idx)


def get_subpath(scene_idx, view_idx, code):
    subfolder = get_subfolder(scene_idx, view_idx)
    return os.path.join(subfolder, '%s_%s' % (subfolder, code))


def parse_filename(filename):
    if filename[:5] != 'scene':
        raise ValueError(
            'Invalid filename: must start with "scene", but got %s' % filename)
    scene_idx = int(filename[5:9])
    view_idx = int(filename[10:12])
    code = filename[13:]
    return scene_idx, view_idx, code


def parse_subpath(subpath):
    return parse_filename(subpath.split('/')[-1])
