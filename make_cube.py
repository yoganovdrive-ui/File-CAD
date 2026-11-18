from cadquery import Workplane, exporters
import os

OUT = os.path.dirname(os.path.abspath(__file__))
# Simple solid cube: 50 x 50 x 50 mm
part = Workplane("XY").box(50, 50, 50)
exporters.export(part, os.path.join(OUT, "cube_50x50x50.step"))
exporters.export(part, os.path.join(OUT, "cube_50x50x50.stl"))
print("OK: cube 50 x 50 x 50 mm")
