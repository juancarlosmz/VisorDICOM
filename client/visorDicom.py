from .visorDicom import pydicom as dicom
from .visorDicom import numpy as np
import matplotlib.pyplot as plt
import os
#Creacion del proyecto DICOM 05-2-2023 por JCMZ
path="./img"
ct_images=os.listdir(path)

slices = [dicom.read_file(path+'/'+s,force=True) for s in ct_images]
print(slices[0])
PatientName = "Paciente: "+str(slices[0].PatientName)
PatientBdate = " Naciemiento: "+str(slices[0].PatientBirthDate)
PatientSex = " Sexo: "+str(slices[0].PatientSex)
PatientAge = " Edad: "+str(slices[0].PatientAge)
slices = sorted(slices,key=lambda x:x.ImagePositionPatient[2])

pixel_spacing = slices[0].PixelSpacing
slices_thickess = slices[0].SliceThickness

axial_aspect_ratio = pixel_spacing[1]/pixel_spacing[0]
sagital_aspect_ratio = pixel_spacing[1]/slices_thickess
coronal_aspect_ratio = slices_thickess/pixel_spacing[0]

#print("Pixel spacing is:",pixel_spacing)
#print("Slices Thickness is:",slices_thickess)

#print("Axial Aspect Ratio:",axial_aspect_ratio)
#print("Sagital Aspect Ratio:",sagital_aspect_ratio)
#print("Coronal Aspect Ratio:",coronal_aspect_ratio)

img_shape = list(slices[0].pixel_array.shape)
img_shape.append(len(slices))
volume3d=np.zeros(img_shape)

for i,s in enumerate(slices):
    array2D=s.pixel_array
    volume3d[:,:,i]= array2D
plt.suptitle(PatientName+PatientBdate+PatientSex+PatientAge)
axial=plt.subplot(2,2,1)
plt.title("Axial")
plt.imshow(volume3d[:,:,img_shape[2]//2])
axial.set_aspect(axial_aspect_ratio)

sagital=plt.subplot(2,2,2)
plt.title("Sagital")
plt.imshow(volume3d[:,img_shape[1]//2,:])
sagital.set_aspect(sagital_aspect_ratio)

coronal = plt.subplot(2,2,3)
plt.title("Coronal")
plt.imshow(volume3d[img_shape[0]//2,:,:].T)
coronal.set_aspect(coronal_aspect_ratio)


plt.show()




print(array2D.shape)
print(volume3d.shape)    
