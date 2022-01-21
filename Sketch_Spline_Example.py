import adsk.core, adsk.fusion, traceback

def run(context):
    ui = None
    try: 
        app = adsk.core.Application.get()
        ui = app.userInterface

        doc = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
        design = app.activeProduct

        # Get the root component of the active design.
        rootComp = design.rootComponent

        # Create a new sketch on the xy plane.
        sketch = rootComp.sketches.add(rootComp.xYConstructionPlane)

        # Create an object collection for the points.
        points = adsk.core.ObjectCollection.create()

        # Define the points the spline with fit through.
        points.add(adsk.core.Point3D.create(0, 0, 0))
        points.add(adsk.core.Point3D.create(5, 1, 0))
        points.add(adsk.core.Point3D.create(6, 4, 3))
        points.add(adsk.core.Point3D.create(7, 6, 6))
        points.add(adsk.core.Point3D.create(2, 3, 0))
        points.add(adsk.core.Point3D.create(0, 1, 0))

        # Create the spline.
        spline = sketch.sketchCurves.sketchFittedSplines.add(points)

        # Get spline fit points
        fitPoints = spline.fitPoints
        
        # Get the second fit point
        fitPoint = fitPoints.item(1)
        
        # If there is no the relative tangent handle, activate the tangent handle
        line = spline.getTangentHandle(fitPoint)
        if line is None:
             line = spline.activateTangentHandle(fitPoint)
                
        # Get the tangent handle           
        gottenLine = spline.getTangentHandle(fitPoint)
        
        # Delete the tangent handle
        gottenLine.deleteMe()

        # Activate the curvature handle
        # If the curvature handle activated. the relative tangentHandle is activated automatically
        activatedArc= spline.activateCurvatureHandle(fitPoint)
        
        # Get curvature handle and tangent handle
        gottenArc= spline.getCurvatureHandle(fitPoint)
        gottenLine = spline.getTangentHandle(fitPoint)
        
        # Delete curvature handle
        gottenArc.deleteMe();

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
