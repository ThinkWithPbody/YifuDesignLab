import rhinoscriptsyntax as rs
import Rhino.Geometry as rg

def offset_and_hatch_curves():
    # Get input curves
    curves = rs.GetObjects("Select curves to offset and hatch", 4, preselect=True)
    if not curves:
        return

    # Get the current active layer
    active_layer = rs.CurrentLayer()
    if not active_layer:
        return
    
    # Get offset distance
    distance = rs.GetReal("Offset distance", 0.05, 1e-10)
    if not distance:
        return

    # Ask if curves should be joined
    join_curves = rs.GetBoolean("Join curves?", ("Join", "No", "Yes"), False)[0]

    # Ask if sublayers should be created for centerlines and border curves
    create_centerline_layer = rs.GetBoolean("Keep centerlines?", ("Centerline", "No", "Yes"), False)[0]
    create_border_layer = rs.GetBoolean("Keep border curves?", ("Border", "No", "Yes"), False)[0]

    # Disable viewport redraw
    rs.EnableRedraw(False)

    hatches = []
    border_curves = []
    
    # Join curves based on user preference
    if join_curves:
        # Copy input curves
        copied_curves = [rs.CopyObject(curve) for curve in curves]
        curves = rs.JoinCurves(copied_curves, delete_input=True)

    # Get list of available hatch patterns
    hatch_patterns = rs.HatchPatternNames()
    
    # Get hatch pattern
    hatch_pattern = rs.GetString("Hatch pattern name", "Solid", hatch_patterns)
    if not hatch_pattern:
        return

    for curve in curves:
        # Offset curve on both sides
        offset_pos = rs.OffsetCurve(curve, [0, 0, 0], distance)
        offset_neg = rs.OffsetCurve(curve, [0, 0, 0], -distance)
        
        if offset_pos and offset_neg:
            # Create closing lines
            start_line = rs.AddLine(rs.CurveStartPoint(offset_pos), rs.CurveStartPoint(offset_neg))
            end_line = rs.AddLine(rs.CurveEndPoint(offset_pos), rs.CurveEndPoint(offset_neg))

            # Join curves to create closed shape
            border_curve = rs.JoinCurves([offset_pos, offset_neg, start_line, end_line], True)
            
            if border_curve:
                # Create hatch
                hatch = rs.AddHatch(border_curve, hatch_pattern, 1, 0)
                if hatch:
                    hatches.append(hatch)

                # Store border curve for later deletion if not keeping it
                border_curves.extend(border_curve)

                # Handle centerline curve based on user choice
                if create_centerline_layer:
                    rs.ObjectLayer(curve, None)  # Temporarily set layer to None (not assigned yet)

                if create_border_layer:
                    for bc in border_curve:
                        rs.ObjectLayer(bc, None)  # Temporarily set layer to None (not assigned yet)

                for h in hatches:
                    rs.ObjectLayer(h, None)  # Temporarily set layer to None (not assigned yet)

    # Create layers only after all operations are finalized
    centerline_layer = None
    border_layer = None
    
    if create_centerline_layer:
        centerline_layer = rs.AddLayer("Centerlines", color=rs.LayerColor(active_layer), parent=active_layer)
        
    if create_border_layer:
        border_layer = rs.AddLayer("Borders", color=rs.LayerColor(active_layer), parent=active_layer)

    # Create hatch layer and copy properties from the active layer
    hatch_layer = rs.AddLayer("Hatches", color=rs.LayerColor(active_layer), parent=active_layer)

    # Move objects to appropriate layers only if keeping them
    for curve in curves:
        if create_centerline_layer:
            rs.ObjectLayer(curve, centerline_layer)
        else:
            rs.DeleteObject(curve)  # Delete centerline curve if not keeping

    for border_curve in border_curves:
        if create_border_layer:
            rs.ObjectLayer(border_curve, border_layer)
        else:
            rs.DeleteObject(border_curve)  # Delete border curve if not keeping

    for h in hatches:
        rs.ObjectLayer(h, hatch_layer)  # Move hatches to their layer

    # Group hatches if requested (optional)
    if hatches:
        group_hatch_objects(hatches)

    # Enable viewport redraw again
    rs.EnableRedraw(True)

def group_hatch_objects(hatches):
    group_name = "Hatch Group"
    
    # Create a group for all hatches
    group_id = rs.AddGroup(group_name)
    
    for hatch in hatches:
        if rs.IsObject(hatch):
            rs.AddObjectsToGroup(hatch, group_id)

# Run the function
offset_and_hatch_curves()
