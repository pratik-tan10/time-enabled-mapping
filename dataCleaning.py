import pandas as pd
import geopandas as gpd
df = pd.read_csv("population_usafacts.csv")
gdf = gpd.read_file("states.shp")

print(gdf.columns)
print(df.columns)
# Reduce the size of geometry
gdf["geometry"] = gdf["geometry"].simplify(0.01)
# Join data with Polygons
merged = gdf.merge(df, left_on = "NAME", right_on = "State", how = "inner")
merged.to_file("simplified.shp")
# Export to geojson
merged.to_file("simplified.geojson")
