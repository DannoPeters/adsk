

import adsk.core, adsk.fusion, traceback

def run(context):
    ui = None
    try: 
        app = adsk.core.Application.get()
        ui = app.userInterface

        # Create a new document and get the Design.
        doc = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
        design = app.activeProduct

        # Get the root component of the active design.
        rootComp = design.rootComponent

        # Create a new sketch on the XY construction plane.
        sk = root.sketches.add(root.xYConstructionPlane)

        # Get the SketchTexts collection object.
        texts = sk.sketchTexts

        # Add multi-line text.
        input = texts.createInput2('This is a long line that is broken automatically.\n\nAnd this is a defined line break.', 0.5)
        input.setAsMultiLine(adsk.core.Point3D.create(0, 0, 0),
                             adsk.core.Point3D.create(10, 5, 0),
                             adsk.core.HorizontalAlignments.LeftHorizontalAlignment,
                             adsk.core.VerticalAlignments.TopVerticalAlignment, 0)
        texts.add(input)

        # Draw an arc to use to create text along a curve.
        arc = sk.sketchCurves.sketchArcs.addByThreePoints(adsk.core.Point3D.create(-10, 0, 0),
                                                          adsk.core.Point3D.create(-5, 3, 0),
                                                          adsk.core.Point3D.create(0, 0, 0))

        # Create text along the arc.
        input = texts.createInput2('Text Along a Curve', 0.75)
        input.setAsAlongPath(arc, False, adsk.core.HorizontalAlignments.CenterHorizontalAlignment, 0)
        input.isHorizontalFlip = True
        input.isVerticalFlip = True
        input.fontName = 'Comic Sans MS'
        texts.add(input)        
        
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

