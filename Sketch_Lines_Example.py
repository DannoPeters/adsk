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
        sketches = rootComp.sketches;
        xyPlane = rootComp.xYConstructionPlane
        sketch = sketches.add(xyPlane)

        # Draw three lines.
        lines = sketch.sketchCurves.sketchLines;
        line1 = lines.addByTwoPoints(adsk.core.Point3D.create(0, 0, 0), adsk.core.Point3D.create(3, 1, 0))
        line2 = lines.addByTwoPoints(adsk.core.Point3D.create(4, 3, 0), adsk.core.Point3D.create(2, 4, 0))
        line3 = lines.addByTwoPoints(adsk.core.Point3D.create(-1, 0, 0), adsk.core.Point3D.create(0, 4, 0))

        # Draw circle tangent to the lines.
        circles = sketch.sketchCurves.sketchCircles
        circle1 = circles.addByThreeTangents(line1, line2, line3, adsk.core.Point3D.create(0,0,0))

        # Apply tangent contstraints to maintain the relationship.
        constraints = sketch.geometricConstraints
        constraints.addTangent(circle1, line1)
        constraints.addTangent(circle1, line2)
        constraints.addTangent(circle1, line3)
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
