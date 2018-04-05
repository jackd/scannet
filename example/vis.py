from mayavi import mlab
from scannet.ply import get_ply_dataset
from scannet.mayavi_vis import vis_ply_data


with get_ply_dataset() as ds:
    for key in ds.keys():
        scene_idx, view_idx, code = key
        data = ds[key]
        vis_ply_data(data)
        vertices = data['vertex']

        try:
            label = vertices['label']
            print(sorted(list(set(label))))
        except Exception:
            pass
        print(scene_idx, view_idx, code)
        mlab.show()
