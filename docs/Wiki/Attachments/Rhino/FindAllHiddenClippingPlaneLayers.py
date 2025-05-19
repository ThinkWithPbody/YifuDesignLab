#! python3
import rhinoscriptsyntax as rs

def find_all_hidden_clipping_plane_layers():
    cps = rs.ObjectsByType(536870912)
    
    if not cps:
        print("No hidden clipping planes found!")
        return
    
    msg = ""
    for cp in cps:
        layer = rs.ObjectLayer(cp)
        if not rs.IsLayerOn(layer) or rs.IsObjectHidden(cp):
            msg += f"Hidden clipping plane found on layer {layer}\n"
    
    if msg:
        rs.MessageBox(msg, 0, "ClippingPlane finder")
    else:
        print("No hidden clipping planes found!")

find_all_hidden_clipping_plane_layers()