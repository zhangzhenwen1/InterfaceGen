# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2019 replay file
# Internal Version: 2018_09_25-02.41.51 157541
# Run by ps on Mon Jun 28 14:43:42 2021
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=334.433319091797, 
    height=223.503707885742)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
Mdb()
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, 
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
openMdb(pathName='C:/repo/UEL/TEST2.cae')
#: The model database "C:\repo\UEL\TEST2.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['Model-1'].parts['Part-3']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
openMdb(pathName='C:/repo/UEL/test.cae')
#: The model database "C:\repo\UEL\test.cae" has been opened.
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
p = mdb.models['Model-1'].parts['Part-3']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
a.features['Part-5-1'].suppress()
a = mdb.models['Model-1'].rootAssembly
a.features['Part-4-1'].resume()
p = mdb.models['Model-1'].parts['Part-3']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
a.features['Part-4-1'].suppress()
a = mdb.models['Model-1'].rootAssembly
a.features['Part-5-1'].resume()
p = mdb.models['Model-1'].parts['Part-3']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
p1 = mdb.models['Model-1'].parts['Part-5']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
p = mdb.models['Model-1'].parts['Part-5']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
a.features['Part-5-1'].suppress()
a = mdb.models['Model-1'].rootAssembly
a.features['Part-1-1'].resume()
elemType1 = mesh.ElemType(elemCode=C3D20R, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=C3D15, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D10, elemLibrary=STANDARD, 
    secondOrderAccuracy=OFF, distortionControl=DEFAULT)
a = mdb.models['Model-1'].rootAssembly
c1 = a.instances['Part-1-1'].cells
cells1 = c1.getSequenceFromMask(mask=('[#1 ]', ), )
pickedRegions =(cells1, )
a.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
    elemType3))
a = mdb.models['Model-1'].rootAssembly
partInstances =(a.instances['Part-1-1'], )
a.generateMesh(regions=partInstances)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    renderStyle=WIREFRAME)
session.viewports['Viewport: 1'].view.setValues(nearPlane=42.9212, 
    farPlane=64.5616, width=43.9016, height=22.4035, cameraPosition=(55.1311, 
    24.8027, 6.97364), cameraUpVector=(-0.574874, 0.787017, -0.223885), 
    cameraTarget=(6.19316, 9.75833, 3.32747))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(renderStyle=SHADED)
a = mdb.models['Model-1'].rootAssembly
partInstances =(a.instances['Part-1-1'], )
a.deleteMesh(regions=partInstances)
a = mdb.models['Model-1'].rootAssembly
partInstances =(a.instances['Part-1-1'], )
a.deleteSeeds(regions=partInstances)
a = mdb.models['Model-1'].rootAssembly
partInstances =(a.instances['Part-1-1'], )
a.seedPartInstance(regions=partInstances, size=10.0, deviationFactor=0.1, 
    minSizeFactor=0.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=40.55, 
    farPlane=63.2069, width=41.4762, height=21.1658, cameraPosition=(43.9677, 
    11.5565, 38.8743), cameraUpVector=(-0.00508804, 0.832361, -0.554211), 
    cameraTarget=(5.69182, 9.16346, 4.7601))
elemType1 = mesh.ElemType(elemCode=C3D20R, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=C3D15, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D10, elemLibrary=STANDARD, 
    secondOrderAccuracy=OFF, distortionControl=DEFAULT)
a = mdb.models['Model-1'].rootAssembly
c1 = a.instances['Part-1-1'].cells
cells1 = c1.getSequenceFromMask(mask=('[#1 ]', ), )
pickedRegions =(cells1, )
a.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
    elemType3))
a = mdb.models['Model-1'].rootAssembly
partInstances =(a.instances['Part-1-1'], )
a.generateMesh(regions=partInstances)
a = mdb.models['Model-1'].rootAssembly
partInstances =(a.instances['Part-1-1'], )
a.deleteMesh(regions=partInstances)
a = mdb.models['Model-1'].rootAssembly
c1 = a.instances['Part-1-1'].cells
pickedRegions = c1.getSequenceFromMask(mask=('[#1 ]', ), )
a.setMeshControls(regions=pickedRegions, elemShape=TET, technique=FREE)
a = mdb.models['Model-1'].rootAssembly
partInstances =(a.instances['Part-1-1'], )
a.generateMesh(regions=partInstances)
session.viewports['Viewport: 1'].view.setValues(nearPlane=42.8755, 
    farPlane=65.4773, width=43.8548, height=22.3796, cameraPosition=(9.92649, 
    43.308, 43.1523), cameraUpVector=(0.320073, 0.415914, -0.851216), 
    cameraTarget=(5.33055, 9.50043, 4.8055))
session.viewports['Viewport: 1'].view.setValues(nearPlane=41.8233, 
    farPlane=66.998, width=42.7786, height=21.8304, cameraPosition=(-32.1055, 
    36.8864, 29.0665), cameraUpVector=(0.46736, 0.579103, -0.667993), 
    cameraTarget=(3.12057, 9.16279, 4.06489))
session.viewports['Viewport: 1'].view.setValues(nearPlane=41.3385, 
    farPlane=64.8913, width=42.2828, height=21.5774, cameraPosition=(35.8641, 
    18.8312, 46.0835), cameraUpVector=(0.126203, 0.711817, -0.690934), 
    cameraTarget=(6.97151, 8.13984, 5.02902))
a = mdb.models['Model-1'].rootAssembly
partInstances =(a.instances['Part-1-1'], )
a.deleteMesh(regions=partInstances)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-1-1'].edges
pickedEdges = e1.getSequenceFromMask(mask=('[#fff ]', ), )
a.seedEdgeByNumber(edges=pickedEdges, number=1, constraint=FINER)
a = mdb.models['Model-1'].rootAssembly
partInstances =(a.instances['Part-1-1'], )
a.generateMesh(regions=partInstances)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
mdb.jobs['Job-1'].writeInput(consistencyChecking=OFF)
#: The job input file has been written to "Job-1.inp".
mdb.jobs['Job-1'].writeInput(consistencyChecking=OFF)
#: The job input file has been written to "Job-1.inp".
mdb.jobs['Job-1'].writeInput(consistencyChecking=OFF)
#: The job input file has been written to "Job-1.inp".
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].setValues(displayedObject=None)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    elementLabels=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    nodeLabels=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=41.8549, 
    farPlane=66.1765, width=42.811, height=21.847, cameraPosition=(23.5253, 
    38.8335, 42.9414), cameraUpVector=(0.0700803, 0.490492, -0.868623), 
    cameraTarget=(6.55638, 8.81279, 4.92331))
session.viewports['Viewport: 1'].view.setValues(nearPlane=42.6177, 
    farPlane=61.1581, width=43.5913, height=22.2452, cameraPosition=(2.33917, 
    6.68036, 56.8427), cameraUpVector=(0.371239, 0.878076, -0.301936), 
    cameraTarget=(5.50218, 7.21289, 5.61502))
session.viewports['Viewport: 1'].view.setValues(nearPlane=40.212, 
    farPlane=63.3518, width=41.1306, height=20.9895, cameraPosition=(-31.9692, 
    12.9147, 40.457), cameraUpVector=(0.532824, 0.844105, -0.0598827), 
    cameraTarget=(5.13197, 7.28016, 5.43821))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    renderStyle=WIREFRAME)
session.viewports['Viewport: 1'].view.setValues(nearPlane=42.2326, 
    farPlane=64.9422, width=43.1975, height=22.0442, cameraPosition=(-1.12321, 
    48.7675, 35.3392), cameraUpVector=(0.811792, 0.127571, -0.569841), 
    cameraTarget=(5.40235, 7.59442, 5.39335))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(renderStyle=SHADED)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-1-1'].elements
elements1 = e1.getSequenceFromMask(mask=('[#1 ]', ), )
leaf = dgm.LeafFromMeshElementLabels(elementSeq=elements1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=41.5066, 
    farPlane=63.7633, width=42.4549, height=21.6652, cameraPosition=(-18.8262, 
    50.118, 21.078), cameraUpVector=(0.945727, 0.220546, -0.238661), 
    cameraTarget=(5.1726, 7.61195, 5.20827))
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=39.7884, 
    farPlane=64.5161, width=40.6974, height=20.7684, cameraPosition=(-22.5872, 
    -17.2266, 43.2795), cameraUpVector=(0.529437, 0.756726, 0.383487), 
    cameraTarget=(5.02161, 4.90842, 6.09954))
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-1-1'].elements
elements1 = e1.getSequenceFromMask(mask=('[#1 ]', ), )
leaf = dgm.LeafFromMeshElementLabels(elementSeq=elements1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38.9163, 
    farPlane=61.0254, width=39.8054, height=20.3132, cameraPosition=(-26.5406, 
    43.0472, 15.1961), cameraUpVector=(0.940427, 0.278651, 0.194808), 
    cameraTarget=(5.11166, 3.5356, 6.73918))
mdb.save()
#: The model database has been saved to "C:\repo\UEL\test.cae".
