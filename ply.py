from dids.file_io.ply_dataset import PlyDataset
from path import get_data_dir, get_subpath, parse_subpath


def get_ply_dataset(view_idx=None, code=None):
    data_dir = get_data_dir()
    dataset = PlyDataset(data_dir)

    def key_fn(key):
        return get_subpath(*key)

    def inverse_fn(path):
        return parse_subpath(path.split('/')[-1])

    return dataset.map_keys(key_fn, inverse_fn)
