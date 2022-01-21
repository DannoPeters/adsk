import adsk.core, adsk.fusion, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        
        # Create a document.
        doc = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
 
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)

        # Get the root component of the active design
        rootComp = design.rootComponent

        allOccs = rootComp.occurrences
        transform = adsk.core.Matrix3D.create()
        
        # Create three components under root component
        occ1 = allOccs.addNewComponent(transform)
        subComp1 = occ1.component
        occ2 = allOccs.addNewComponent(transform)
        subComp2 = occ2.component
        occ3 = allOccs.addNewComponent(transform)
        subComp3 = occ3.component
      
        # Create a sketch in sub component 1
        sketches1 = subComp1.sketches
        sketch1 = sketches1.add(rootComp.yZConstructionPlane)
        
        # Get sketch lines
        sketchLines = sketch1.sketchCurves.sketchLines
        
        # Create sketch rectangle
        startPoint = adsk.core.Point3D.create(-8.0, 0, 0)
        endPoint = adsk.core.Point3D.create(8.0, 8.0, 0)
        sketchLines.addTwoPointRectangle(startPoint, endPoint)
        
        # Get the profile of the first sketch
        prof1 = sketch1.profiles.item(0)
        
        # Create an extrusion input
        extrudes1 = subComp1.features.extrudeFeatures
        extInput1 = extrudes1.createInput(prof1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        
        # Define that the extent is a distance extent of 2 cm
        distance1 = adsk.core.ValueInput.createByReal(2.0)
        # Set the distance extent
        extInput1.setDistanceExtent(False, distance1)
        # Set the extrude type to be solid
        extInput1.isSolid = True
        
        # Create the extrusion
        ext1 = extrudes1.add(extInput1)
        
        # Create construction plane
        planes = rootComp.constructionPlanes
        planeInput = planes.createInput()
        offsetValue = adsk.core.ValueInput.createByReal(8.0)
        planeInput.setByOffset(rootComp.yZConstructionPlane, offsetValue)
        plane = planes.add(planeInput)

         # Create a sketch in sub component 2
        sketches2 = subComp2.sketches
        sketch2 = sketches2.add(plane)
        
        # Create the spline.
        points = adsk.core.ObjectCollection.create()
        points.add(adsk.core.Point3D.create(0, 8, 0))
        points.add(adsk.core.Point3D.create(5, 6, 0))
        points.add(adsk.core.Point3D.create(-5, 5, 0))
        
        sketch2Curves = sketch2.sketchCurves
        spline = sketch2Curves.sketchFittedSplines.add(points)
        
        # Create sketch rectangle
        sketch2Lines = sketch2Curves.sketchLines
        startPoint2 = adsk.core.Point3D.create(-4, 2, 0)
        endPoint2 = adsk.core.Point3D.create(3, 4, 0)
        sketch2Lines.addTwoPointRectangle(startPoint2, endPoint2)
        
        # Get the profile of the second sketch
        prof2 = sketch2.profiles.item(0)
        
        # Create an extrusion input       
        extrudes2 = subComp2.features.extrudeFeatures
        extInput2 = extrudes2.createInput(prof2, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        
        # Define that the extent is a distance extent of 2 cm
        extent_distance_2 = adsk.fusion.DistanceExtentDefinition.create(adsk.core.ValueInput.createByString("2cm"))
        # Define that the taple angle is 10 degree
        deg10 = adsk.core.ValueInput.createByString("10 deg")

        extInput2.setOneSideExtent(extent_distance_2, adsk.fusion.ExtentDirections.PositiveExtentDirection, deg10)
        
        # Set the extrude type to be solid
        extInput2.isSolid = True

        # Create the extrusion
        ext2 = extrudes2.add(extInput2)
        
        # Get the body with the first extrude
        body = ext1.bodies.item(0)
        
        # Get faces
        faceList = []
        for face in body.faces:
            faceList.append(face)

        # Get curves
        curveList = []
        for curve in sketch2Curves:
            curveList.append(curve)
        
        # Get points
        for point in sketch2.sketchPoints:
            curveList.append(point)
        
        # Get the body with the second extrude
        body2 = ext2.bodies.item(0)
        
        # Get eges
        for edge in body2.edges:
            curveList.append(edge)
        
        # Get construction axis
        curveList.append(rootComp.yConstructionAxis)
        
        # Get construction point
        curveList.append(rootComp.originConstructionPoint)
        
        sketches3 = subComp3.sketches
        # Create a sketch in sub component 3
        skAlongVecProject = sketches3.add(rootComp.yZConstructionPlane)
        # sketch project to surface (along vector)
        projectedEntities = skAlongVecProject.projectToSurface(faceList, curveList, adsk.fusion.SurfaceProjectTypes.AlongVectorSurfaceProjectType, rootComp.xConstructionAxis)

        projectedEntities = []
        # Create a sketch in sub component 3
        skClosestPtProject = sketches3.add(rootComp.yZConstructionPlane)
        # sketch project to surface (closest point)
        projectedEntities = skClosestPtProject.projectToSurface(faceList, curveList, adsk.fusion.SurfaceProjectTypes.ClosestPointSurfaceProjectType)
        
    except:
        if ui:
            
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
