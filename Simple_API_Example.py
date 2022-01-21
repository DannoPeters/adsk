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
        print(sketch1.revisionId)

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
        print(sketch1.revisionId)

        # Get sketch lines
        sketchLines = sketch1.sketchCurves.sketchLines

        # Create sketch rectangle
        startPoint = adsk.core.Point3D.create(0, 0, 0)
        endPoint = adsk.core.Point3D.create(5.0, 5.0, 0)
        sketchLines.addTwoPointRectangle(startPoint, endPoint)
        print(sketch1.revisionId)

    except:
        if ui:

            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
