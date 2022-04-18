import openvdb as vdb
import vtk
from vtk.util import numpy_support
import numpy as np
from scipy import ndimage

PathDicom = "./dicom/sample1/"
dicomReader = vtk.vtkDICOMImageReader()
dicomReader.SetDirectoryName(PathDicom)
dicomReader.Update()

# # Load dimensions using `GetDataExtent`
# _extent = dicomReader.GetDataExtent()
# ConstPixelDims = [_extent[1]-_extent[0]+1, _extent[3]-_extent[2]+1, _extent[5]-_extent[4]+1]

# # Load spacing values
# ConstPixelSpacing = dicomReader.GetPixelSpacing()

# print(ConstPixelSpacing)

# # Get the 'vtkImageData' object from the reader
# imageData = dicomReader.GetOutput()
# # Get the 'vtkPointData' object from the 'vtkImageData' object
# pointData = imageData.GetPointData()
# # Ensure that only one array exists within the 'vtkPointData' object
# assert (pointData.GetNumberOfArrays()==1)
# # Get the `vtkArray` (or whatever derived type) which is needed for the `numpy_support.vtk_to_numpy` function
# arrayData = pointData.GetArray(0)

# # Convert the `vtkArray` to a NumPy array
# dicomArray = numpy_support.vtk_to_numpy(arrayData)
# # Reshape the NumPy array to 3D using 'ConstPixelDims' as a 'shape'
# dicomArray = dicomArray.reshape(ConstPixelDims, order='F')


# 取得 DICOM 影像
imageData = dicomReader.GetOutput()

# 顯示影像資訊
print("Scalar Type:", imageData.GetScalarTypeAsString())
print("Origin:", imageData.GetOrigin())
print("Extend:", imageData.GetExtent())
print("Spacing:", imageData.GetSpacing())

dicomArray = numpy_support.vtk_to_numpy(imageData.GetPointData().GetScalars())
dicomArray = dicomArray.reshape(imageData.GetDimensions())
dicomArray = ndimage.zoom(dicomArray,imageData.GetSpacing())
dicomArray = dicomArray.transpose(2, 0, 1)
print(dicomArray.shape)
dicomArray = dicomArray.astype(float)
# Copy values from a three-dimensional array of doubles
# into a grid of floats.
grid = vdb.FloatGrid()
grid.copyFromArray(dicomArray)
grid.name = 'density'
vdb.write('test.vdb', grids=[grid])
