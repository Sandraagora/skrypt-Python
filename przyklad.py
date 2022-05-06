# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__
#sys.path.insert(0, 'C:/Users/Szczepan/source/repos/LM')
import xalglib

def Macro1(alpha1, alpha2, alpha3, alpha4):
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    Mdb()
    mdb.models['Model-1'].setValues(absoluteZero=-273.15, 
        stefanBoltzmann=5.67037E-11)
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=166.985, 
        farPlane=210.139, width=144.914, height=84.278, cameraPosition=(
        -3.78358, 1.18373, 188.562), cameraTarget=(-3.78358, 1.18373, 0))
    s.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=2000.0)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=STANDALONE)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1459.45, 
        farPlane=2311.79, width=2862.22, height=1664.59, cameraPosition=(
        -166.813, 37.2298, 1885.62), cameraTarget=(-166.813, 37.2298, 0))
    s1.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(400.0, 0.0))
    s1.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(700.0, 0.0))
    s1.RadialDimension(curve=g[3], textPoint=(-1430.02868652344, 308.427612304688), 
        radius=995.0)
    s1.RadialDimension(curve=g[2], textPoint=(-651.845092773438, 134.754150390625), 
        radius=425.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1372.52, 
        farPlane=2398.72, width=3446.04, height=2004.12, cameraPosition=(
        -97.2335, 68.5668, 1885.62), cameraTarget=(-97.2335, 68.5668, 0))
    p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Part-1']
    p.BaseSolidExtrude(sketch=s1, depth=1200.0)
    s1.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Part-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    p = mdb.models['Model-1'].parts['Part-1']
    p.DatumCsysByThreePoints(name='Datum csys-1', coordSysType=CYLINDRICAL, 
        origin=(0.0, 0.0, 0.0), line1=(1.0, 0.0, 0.0), line2=(0.0, 1.0, 0.0))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4835.17, 
        farPlane=7920.95, width=4187, height=2325.61, cameraPosition=(-1999.76, 
        23.2037, -5456.84), cameraUpVector=(-0.443554, 0.736008, 0.511421), 
        cameraTarget=(53.0419, -51.2847, 598.24))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4559.42, 
        farPlane=8302.89, width=3948.22, height=2192.98, cameraPosition=(
        432.924, -4991.31, -3432.57), cameraUpVector=(-0.956061, 0.276394, 
        0.0977382), cameraTarget=(46.9532, -38.7339, 593.173))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4657.71, 
        farPlane=8261.18, width=4033.33, height=2240.25, cameraPosition=(
        5405.63, -110.959, -2934.53), cameraUpVector=(-0.60901, -0.736352, 
        -0.294776), cameraTarget=(75.6603, -10.5599, 596.048))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4480.94, 
        farPlane=8372.31, width=3880.25, height=2155.23, cameraPosition=(
        -1256.89, 4541.62, -3769.88), cameraUpVector=(0.838855, -0.48208, 
        -0.252826), cameraTarget=(8.19054, 36.5556, 587.589))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4371.06, 
        farPlane=8524.2, width=3785.1, height=2102.38, cameraPosition=(5072.84, 
        3885.96, 1458.84), cameraUpVector=(0.218105, -0.685877, -0.694265), 
        cameraTarget=(40.2985, 33.2298, 614.112))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4920.39, 
        farPlane=7988.42, width=4260.79, height=2366.6, cameraPosition=(
        741.909, 1567.73, 6817.01), cameraUpVector=(0.898059, -0.109777, 
        -0.425957), cameraTarget=(4.29205, 13.9565, 658.659))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4728.93, 
        farPlane=8183.37, width=4095, height=2274.51, cameraPosition=(-3052.95, 
        -353.18, 6277.74), cameraUpVector=(0.921887, 0.361741, 0.138808), 
        cameraTarget=(-31.2075, -4.01291, 653.614))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4828.05, 
        farPlane=8080.84, width=4180.83, height=2322.19, cameraPosition=(
        2617.87, 167.065, 6497.35), cameraUpVector=(0.358914, 0.757163, 
        -0.545789), cameraTarget=(23.3551, 0.992615, 655.727))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4706.55, 
        farPlane=8202.47, width=4075.62, height=2263.75, cameraPosition=(
        1316.99, 2139.24, 6545.57), cameraUpVector=(0.407836, 0.615932, 
        -0.674016), cameraTarget=(11.1791, 19.452, 656.178))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4976.91, 
        farPlane=7933.26, width=4309.74, height=2393.79, cameraPosition=(
        -944.371, 625.377, 6954.93), cameraUpVector=(0.483636, 0.80398, 
        -0.345995), cameraTarget=(-10.0113, 5.26617, 660.014))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4889.74, 
        farPlane=8019.69, width=4234.26, height=2351.86, cameraPosition=(
        1109.19, 809.855, 6906.92), cameraUpVector=(0.185299, 0.855391, 
        -0.483705), cameraTarget=(9.41426, 7.0112, 659.56))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4776.02, 
        farPlane=8133.26, width=4135.78, height=2297.16, cameraPosition=(
        838.797, 2040.38, 6665.94), cameraUpVector=(-0.0281152, 0.787421, 
        -0.615774), cameraTarget=(6.87195, 18.5809, 657.294))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5148.73, 
        farPlane=7761.15, width=4458.53, height=2476.43, cameraPosition=(
        107.491, 225.353, 7050.11), cameraUpVector=(0.193661, 0.909154, 
        -0.368692), cameraTarget=(0.00471497, 1.5372, 660.901))
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    p = mdb.models['Model-1'].parts['Part-1']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    region = regionToolset.Region(cells=cells)
    orientation = mdb.models['Model-1'].parts['Part-1'].datums[2]
    mdb.models['Model-1'].parts['Part-1'].MaterialOrientation(region=region, 
        orientationType=SYSTEM, axis=AXIS_1, localCsys=orientation, 
        fieldName='', additionalRotationType=ROTATION_NONE, angle=0.0, 
        additionalRotationField='', stackDirection=STACK_3)
    mdb.models['Model-1'].Material(name='Material-1')
    mdb.models['Model-1'].materials['Material-1'].Conductivity(type=ORTHOTROPIC, 
        temperatureDependency=ON, table=((17.976, 59.92, 59.92, 0.0), (
        17.6056125, 58.685375, 58.685375, 50.0), (17.1639, 57.213, 57.213, 
        100.0), (16.6605375, 55.535125, 55.535125, 150.0), (16.1052, 53.684, 
        53.684, 200.0), (15.5075625, 51.691875, 51.691875, 250.0), (14.8773, 
        49.591, 49.591, 300.0), (14.2240875, 47.413625, 47.413625, 350.0), (
        13.5576, 45.192, 45.192, 400.0), (12.8875125, 42.958375, 42.958375, 
        450.0), (12.2235, 40.745, 40.745, 500.0), (11.5752375, 38.584125, 
        38.584125, 550.0), (10.9524, 36.508, 36.508, 600.0), (10.3646625, 
        34.548875, 34.548875, 650.0), (9.8217, 32.739, 32.739, 700.0)))
    mdb.models['Model-1'].materials['Material-1'].Density(table=((7.8e-09, ), ))
    mdb.models['Model-1'].materials['Material-1'].SpecificHeat(
        temperatureDependency=ON, table=((457300000.0, 0.0), (471944601.3, 
        50.0), (487449123.8, 100.0), (503864061.5, 150.0), (521242873.4, 
        200.0), (539642157.5, 250.0), (559121835.3, 300.0), (579745346.7, 
        350.0), (601579857.0, 400.0), (624696475.1, 450.0), (649170485.5, 
        500.0), (675081593.5, 550.0), (702514184.4, 600.0), (731557598.8, 
        650.0), (762306423.0, 700.0)))
    mdb.models['Model-1'].materials.changeKey(fromName='Material-1', toName='S235')
    mdb.models['Model-1'].HomogeneousSolidSection(name='Section-S235', 
        material='S235', thickness=None)
    p = mdb.models['Model-1'].parts['Part-1']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    region = p.Set(cells=cells, name='Set-2')
    p = mdb.models['Model-1'].parts['Part-1']
    p.SectionAssignment(region=region, sectionName='Section-S235', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
        engineeringFeatures=OFF)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=ON)
    p1 = mdb.models['Model-1'].parts['Part-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    mdb.models['Model-1'].parts.changeKey(fromName='Part-1', toName='coil')
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    a = mdb.models['Model-1'].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    p = mdb.models['Model-1'].parts['coil']
    a.Instance(name='coil-1', part=p, dependent=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=ON)
    mdb.models['Model-1'].HeatTransferStep(name='Step-1', previous='Initial', 
        timePeriod=216000.0, maxNumInc=100000, initialInc=200.0, minInc=5.0, 
        maxInc=1000.0, deltmx=100.0)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4255.03, 
        farPlane=8533.01, width=3684.63, height=2046.57, cameraPosition=(
        3744.63, 3640.31, 4289.83), cameraUpVector=(-0.571989, 0.577326, 
        -0.582687), cameraTarget=(53.0432, -51.2839, 598.241))
    a = mdb.models['Model-1'].rootAssembly
    c1 = a.instances['coil-1'].cells
    cells1 = c1.getSequenceFromMask(mask=('[#1 ]', ), )
    f1 = a.instances['coil-1'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#f ]', ), )
    e1 = a.instances['coil-1'].edges
    edges1 = e1.getSequenceFromMask(mask=('[#f ]', ), )
    v1 = a.instances['coil-1'].vertices
    verts1 = v1.getSequenceFromMask(mask=('[#f ]', ), )
    region = a.Set(vertices=verts1, edges=edges1, faces=faces1, cells=cells1, 
        name='Set-1')
    mdb.models['Model-1'].Temperature(name='Predefined Field-1', 
        createStepName='Initial', region=region, distributionType=UNIFORM, 
        crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, magnitudes=(650.0, 
        ))
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
        predefinedFields=OFF, interactions=ON, constraints=ON, 
        engineeringFeatures=ON)
    mdb.models['Model-1'].FilmConditionProp(name='IntProp-1', 
        temperatureDependency=ON, dependencies=0, property=((alpha1/1000.0, 20.0), (
        alpha2/1000.0, 190.0), (alpha3/1000.0, 340.0), (alpha4/1000.0, 650.0 ) ))
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['coil-1'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#f ]', ), )
    region=a.Surface(side1Faces=side1Faces1, name='Surf-1')
    mdb.models['Model-1'].FilmCondition(name='Int-1', createStepName='Step-1', 
        surface=region, definition=PROPERTY_REF, 
        interactionProperty='IntProp-1', sinkTemperature=20.0, 
        sinkAmplitude='', sinkDistributionType=UNIFORM, sinkFieldName='')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4462.33, 
        farPlane=8368.7, width=3864.14, height=2146.28, cameraPosition=(
        4285.54, 1797.98, -3823.27), cameraUpVector=(-0.670384, 0.727769, 
        0.144696), cameraTarget=(53.0435, -51.2838, 598.241))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4526.55, 
        farPlane=8335.13, width=3919.75, height=2177.17, cameraPosition=(
        3526.91, 1744.5, 5687.05), cameraUpVector=(-0.226805, 0.803222, 
        -0.550812), cameraTarget=(50.5016, -51.463, 630.106))
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['coil-1'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#d ]', ), )
    region=a.Surface(side1Faces=side1Faces1, name='Surf-2')
    mdb.models['Model-1'].RadiationToAmbient(name='Int-2', createStepName='Step-1', 
        surface=region, radiationType=AMBIENT, distributionType=UNIFORM, 
        field='', emissivity=0.93, ambientTemperature=20.0, 
        ambientTemperatureAmp='')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4498.28, 
        farPlane=8379.27, width=3895.27, height=2163.57, cameraPosition=(
        4464.06, 1370.9, 5033.43), cameraUpVector=(-0.280951, 0.8353, 
        -0.472589), cameraTarget=(55.8662, -53.6017, 626.364))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4518.05, 
        farPlane=8359.23, width=3912.39, height=2173.08, cameraPosition=(
        4307.79, 1311.14, 5202.68), cameraUpVector=(-0.256477, 0.840032, 
        -0.478086), cameraTarget=(54.7802, -54.017, 627.54))
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['coil-1'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#2 ]', ), )
    surf1 = a.Surface(side1Faces=side1Faces1, name='Surf-3')
    surfaces =(surf1, )
    mdb.models['Model-1'].CavityRadiationProp(name='IntProp-2', property=((0.93, ), 
        ))
    props =("IntProp-2", )
    mdb.models['Model-1'].CavityRadiation(name='Int-3', createStepName='Step-1', 
        surfaces=surfaces, surfaceEmissivities=props, ambientTemp=20.0)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
        constraints=OFF, connectors=OFF, engineeringFeatures=OFF, 
        adaptiveMeshConstraints=ON)
    del mdb.models['Model-1'].fieldOutputRequests['F-Output-1']
    mdb.models['Model-1'].FieldOutputRequest(name='F-Output-1', 
        createStepName='Step-1', variables=('NT', ), numIntervals=6)
    session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    p1 = mdb.models['Model-1'].parts['coil']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4353.75, 
        farPlane=8556.44, width=3770.12, height=2101.89, cameraPosition=(
        1876.53, -5135.21, -2831.7), cameraUpVector=(0.782151, 0.369967, 
        0.501363), cameraTarget=(16.6974, -49.0451, 567.656))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4457.21, 
        farPlane=8451.23, width=3859.71, height=2151.84, cameraPosition=(
        3645.29, 2625.58, -4034.12), cameraUpVector=(0.589147, -0.428506, 
        0.685047), cameraTarget=(33.4288, 24.3669, 556.282))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4508.18, 
        farPlane=8400.53, width=3903.85, height=2176.45, cameraPosition=(
        2283.95, 3318.21, -4442.99), cameraUpVector=(0.763511, -0.335092, 
        0.552055), cameraTarget=(20.7337, 30.826, 552.469))
    p = mdb.models['Model-1'].parts['coil']
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    v1, e, d1 = p.vertices, p.edges, p.datums
    p.PartitionCellByPlaneThreePoints(point2=v1[1], point3=v1[0], 
        cells=pickedCells, point1=p.InterestingPoint(edge=e[1], rule=CENTER))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4584.19, 
        farPlane=8324.31, width=3969.69, height=2213.15, cameraPosition=(
        3978.7, 1145.81, -4351.21), cameraUpVector=(0.536466, -0.217365, 
        0.815449), cameraTarget=(36.5726, 10.523, 553.327))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4700.38, 
        farPlane=8208.37, width=4070.31, height=2269.25, cameraPosition=(
        3234.22, 707.86, -4940.55), cameraUpVector=(0.647726, -0.0486769, 
        0.760317), cameraTarget=(29.6274, 6.43736, 547.829))
    p = mdb.models['Model-1'].parts['coil']
    e = p.edges
    pickedEdges1 = e.getSequenceFromMask(mask=('[#1 ]', ), )
    p.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, ratio=1.0, 
        number=5, constraint=FINER)
    p = mdb.models['Model-1'].parts['coil']
    p.seedPart(size=160.0, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['coil']
    p.generateMesh()
    elemType1 = mesh.ElemType(elemCode=DC3D8, elemLibrary=STANDARD)
    elemType2 = mesh.ElemType(elemCode=DC3D6, elemLibrary=STANDARD)
    elemType3 = mesh.ElemType(elemCode=DC3D4, elemLibrary=STANDARD)
    p = mdb.models['Model-1'].parts['coil']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#3 ]', ), )
    pickedRegions =(cells, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
        elemType3))
    a = mdb.models['Model-1'].rootAssembly
    a.regenerate()
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=OFF)
    mdb.Job(name='Job_coil_s', model='Model-1', description='', type=ANALYSIS, 
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
        scratch='', resultsFormat=ODB)
    mdb.jobs['Job_coil_s'].writeInput(consistencyChecking=OFF)
    mdb.jobs['Job_coil_s'].submit()
    mdb.jobs['Job_coil_s'].waitForCompletion()

def	dataT ():
	odbName='C:/temp/Job_coil_s.odb' #results path
	odb = session.openOdb(name=odbName)
	session.viewports['Viewport: 1'].setValues(displayedObject=odb) 

	vps = session.viewports[session.currentViewportName]
	#odbName = vps.displayedObject.name
	currentstepnumber = vps.odbDisplay.fieldFrame[0]
	currentstepname = session.odbs[odbName].steps.keys()[currentstepnumber]
	currentframe = vps.odbDisplay.fieldFrame[1]
	currentsteptime = session.odbs[odbName].steps[currentstepname].frames[currentframe].frameValue

	assembly = odb.rootAssembly
	instanceList = assembly.instances.keys()
	instanceName=instanceList[0]
	
	node=688		#node number
	node=node-1
	thePointList= []
	TemperatureList=[]
	
	#Coordinates from node
	coordsX=assembly.instances[instanceName].nodes[node].coordinates[0]
	coordsY=assembly.instances[instanceName].nodes[node].coordinates[1] 
	coordsZ=assembly.instances[instanceName].nodes[node].coordinates[2]
	coords = (coordsX, coordsY, coordsZ)
	thePointList.extend([coords])
	
	#for Name in odb.rootAssembly.instances.keys():
	  #print Name

	for licznik in range (1, currentframe+1):
		TemperaturaXYData=session.XYDataFromPath(name='Temperatura',path=session.Path(name='track', type=POINT_LIST, expression=thePointList), 
			includeIntersections=False, shape=UNDEFORMED, labelType=TRUE_DISTANCE, step=0, frame=licznik,  variable=(('NT11', NODAL),))
		
		Temperature = TemperaturaXYData.data[0]
		TemperatureList.extend([Temperature[1]])
		
	odb.close
	return TemperatureList
    

i=0

def function1(p, fi, param):
    global i
    Macro1(*p)
    f1=[650.0]+dataT()
    
    S = 0.0
    f0 = [650, 362.88, 201.5, 124.4, 92.3, 63, 42.17] 	
	
    assert(len(f1)==len(f0))
    
    for x in range (len(f0)):
        S = S + (f0[x]-f1[x])**2
		
        
    fi[0] = S #definicja funkcji celu

    i = i+1
    return

p = [4.0, 1.0, 0.05, 0.05]				#definicja poczatkowych wartosci wektora rozwiazan
bndl = [0.05, 0.05, 0.05, 0.05]			#ograniczenia dolne
bndu = [6, 6, 6, 6]			#ograniczenia gorne
epsx = 0.01         	#kryterium stopu
maxits = 0  			#Maksymalna liczba iteracji, jezeli maxits=0 to liczba iteracji jest nieograniczona
m = 1					#liczba funkcji celu
DiffStep =  0.0001		#numeryczny krok rozniczkowania

state = xalglib.minlmcreatev(m, p, DiffStep)
xalglib.minlmsetbc(state, bndl, bndu)
xalglib.minlmsetcond(state, epsx, maxits)
xalglib.minlmoptimize_v(state, function1)
p, rep = xalglib.minlmresults(state)

print(p)

line = str(p)
Write=open(('wyniki.txt'), 'w')
Write.writelines(line)
Write.close()

