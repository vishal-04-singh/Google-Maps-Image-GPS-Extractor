from shapely.geometry import Point
import csv
import random
import geopandas as gpd

# Load Singapore land boundary
gdf = gpd.read_file("singapore-boundary.geojson")

# Use the correct union method
land = gdf.geometry.union_all()

# Generate a large number of random points in Singapore's bounding box
coords = [(random.uniform(1.2, 1.5), random.uniform(103.6, 104.1)) for _ in range(10000)]

# Filter: keep only the ones on land
land_points = []
for lat, lon in coords:
    pt = Point(lon, lat)
    if pt.within(land):
        land_points.append((lat, lon))
    if len(land_points) >= 800:
        break

# Save to CSV
with open("singapore_land_coords.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Latitude", "Longitude"])
    writer.writerows(land_points)
