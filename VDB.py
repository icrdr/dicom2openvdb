import openvdb as vdb

cube = vdb.FloatGrid()
cube.fill(min=(100, 100, 100), max=(199, 199, 199), value=1.0)
cube.name = 'cube'

sphere = vdb.createLevelSetSphere(radius=50, center=(1.5, 2, 3))

sphere['radius'] = 50.0

sphere.transform = vdb.createLinearTransform(voxelSize=0.5)

sphere.name = 'sphere'

vdb.write('mygrids.vdb', grids=[cube, sphere])