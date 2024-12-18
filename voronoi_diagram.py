"""
This Python script generates and visualizes a Voronoi diagram based on randomly generated 2D points.

It achieves the following:
1. Generates random 2D points to serve as input for the Voronoi diagram.
2. Computes a Voronoi tessellation using the scipy.spatial Voronoi function.
3. Adjusts the Voronoi regions to handle infinite regions (making them finite).
4. Visualizes the Voronoi diagram with colorized regions and borders around the regions.

"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi

# From: https://stackoverflow.com/questions/20515554/colorize-voronoi-diagram/20678647#20678647
# Updated to Python 3 standard
def voronoi_finite_polygons_2d(vor, radius=None):
    if vor.points.shape[1] != 2:
        raise ValueError("Requires 2D input")

    new_regions = []
    new_vertices = vor.vertices.tolist()

    center = vor.points.mean(axis=0)
    if radius is None:
        radius = np.ptp(vor.points, axis=0).max()  # Fix: Use np.ptp()

    # Construct a map containing all ridges for a given point
    all_ridges = {}
    for (p1, p2), (v1, v2) in zip(vor.ridge_points, vor.ridge_vertices):
        all_ridges.setdefault(p1, []).append((p2, v1, v2))
        all_ridges.setdefault(p2, []).append((p1, v1, v2))

    # Reconstruct infinite regions
    for p1, region in enumerate(vor.point_region):
        vertices = vor.regions[region]

        if all(v >= 0 for v in vertices):
            # finite region
            new_regions.append(vertices)
            continue

        # reconstruct a non-finite region
        ridges = all_ridges[p1]
        new_region = [v for v in vertices if v >= 0]

        for p2, v1, v2 in ridges:
            if v2 < 0:
                v1, v2 = v2, v1
            if v1 >= 0:
                # finite ridge: already in the region
                continue

            # Compute the missing endpoint of an infinite ridge

            t = vor.points[p2] - vor.points[p1] # tangent
            t /= np.linalg.norm(t)
            n = np.array([-t[1], t[0]])  # normal

            midpoint = vor.points[[p1, p2]].mean(axis=0)
            direction = np.sign(np.dot(midpoint - center, n)) * n
            far_point = vor.vertices[v2] + direction * radius

            new_region.append(len(new_vertices))
            new_vertices.append(far_point.tolist())

        # sort region counterclockwise
        vs = np.asarray([new_vertices[v] for v in new_region])
        c = vs.mean(axis=0)
        angles = np.arctan2(vs[:,1] - c[1], vs[:,0] - c[0])
        new_region = np.array(new_region)[np.argsort(angles)]

        # finish
        new_regions.append(new_region.tolist())

    return new_regions, np.asarray(new_vertices)

# Make up data points
np.random.seed(1234)
points = np.random.rand(15, 2)

# Compute Voronoi tessellation
vor = Voronoi(points)

# Get finite regions and vertices
regions, vertices = voronoi_finite_polygons_2d(vor)

# Print some details to the console
print("Voronoi Regions:")
for i, region in enumerate(regions):
    print(f"Region {i}: {region}")
print("\nVoronoi Vertices:")
print(vertices)

# Plot
for region in regions:
    # Colorize the region
    polygon = vertices[region]
    plt.fill(*zip(*polygon), alpha=0.4)
    
    # Add a border around the region (draw lines between the vertices)
    polygon = np.array(polygon)
    plt.plot(np.append(polygon[:, 0], polygon[0, 0]), np.append(polygon[:, 1], polygon[0, 1]), 'k-', lw=2)

# Plot the points
plt.plot(points[:, 0], points[:, 1], 'ko')

# Set plot limits
plt.xlim(vor.min_bound[0] - 0.1, vor.max_bound[0] + 0.1)
plt.ylim(vor.min_bound[1] - 0.1, vor.max_bound[1] + 0.1)

# Show the plot
plt.show()
