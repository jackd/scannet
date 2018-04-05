from __future__ import division
import random
import numpy as np
from util3d.mayavi_vis import vis_colored_point_cloud


def vis_ply_data(ply_data, n_samples=1024):
    vertices = ply_data['vertex']
    x, y, z, r, g, b = (
        vertices[k] for k in ('x', 'y', 'z', 'red', 'green', 'blue'))

    if n_samples is None:
        n_samples = len(x)
    else:
        indices = range(len(x))
        indices = random.sample(indices, n_samples)
        x, y, z, r, g, b = (v[indices] for v in (x, y, z, r, g, b))

    colors = np.empty((n_samples, 4), dtype=np.uint8)
    colors[:, 0] = r
    colors[:, 1] = g
    colors[:, 2] = b
    colors[:, 3] = 255
    points = np.stack((x, y, z), axis=1)
    vis_colored_point_cloud(points, colors, scale_factor=0.05)
