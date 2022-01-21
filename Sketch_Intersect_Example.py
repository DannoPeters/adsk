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
        
        # Create a sketch
        sketches = rootComp.sketches
        sketch1 = sketches.add(rootComp.yZConstructionPlane)
        
        # Create an object collection for the points.
        points = adsk.core.ObjectCollection.create()

        # Define the points the spline with fit through.
        points.add(adsk.core.Point3D.create(-5, 0, 0))
        points.add(adsk.core.Point3D.create(5, 1, 0))
        points.add(adsk.core.Point3D.create(6, 4, 3))
        points.add(adsk.core.Point3D.create(7, 6, 6))
        points.add(adsk.core.Point3D.create(2, 3, 0))
        points.add(adsk.core.Point3D.create(0, 1, 0))

        # Create the spline.
        spline = sketch1.sketchCurves.sketchFittedSplines.add(points)
    
        # Get sketch lines
        sketchLines = sketch1.sketchCurves.sketchLines
        
        # Create sketch rectangle
        startPoint = adsk.core.Point3D.create(0, 0, 0)
        endPoint = adsk.core.Point3D.create(5.0, 5.0, 0)
        sketchLines.addTwoPointRectangle(startPoint, endPoint)
        
        # Get two sketch lines
        sketchLineOne = sketchLines.item(0)
        sketchLineTwo = sketchLines.item(1)
        
        # Get the profile
        prof = sketch1.profiles.item(0)
        
        # Create an extrusion input
        extrudes = rootComp.features.extrudeFeatures
        extInput = extrudes.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        
        # Define that the extent is a distance extent of 5 cm
        distance = adsk.core.ValueInput.createByReal(5.0)
        # Set the distance extent
        extInput.setDistanceExtent(False, distance)
        # Set the extrude type to be solid
        extInput.isSolid = True
        
        # Create the extrusion
        ext = extrudes.add(extInput)
   
        # Get the body with the extrude
        body = ext.bodies.item(0)
        
        # Get a vertex of the body
        vertex = body.vertices.item(5)
        
        # Get a face of the vertex
        face = vertex.faces.item(0)
        
        # Create perpendicular construction axis
        axes = rootComp.constructionAxes
        axisInput = axes.createInput()
        axisInput.setByPerpendicularAtPoint(face, vertex)
        axis = axes.add(axisInput)
        
         # Create construction point
        points = rootComp.constructionPoints
        pointInput = points.createInput()
        pointInput.setByTwoEdges(sketchLineOne, sketchLineTwo)
        point = points.add(pointInput)
        
        # Create construction plane
        planes = rootComp.constructionPlanes
        planeInput = planes.createInput()
        offsetValue = adsk.core.ValueInput.createByReal(3.0)
        planeInput.setByOffset(prof, offsetValue)
        plane = planes.add(planeInput)
        
        # Create another sketch
        sketch2 = sketches.add(rootComp.xZConstructionPlane)
        
        entities = []
        entities.append(body) # body
        entities.append(face) # face
        entities.append(sketchLineOne) # edge 
        entities.append(vertex) # vertex
        entities.append(spline) # sketch curve
        entities.append(axis) # construction axis
        entities.append(point) # construction point
        entities.append(plane) # construction plane
        sketchEntities = sketch2.intersectWithSketchPlane(entities)
        
    except:
        if ui:
            
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
