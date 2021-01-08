"""
Rhino batch render of all layers:
Have atleast one view

"""
import rhinoscriptsyntax as rs
import scriptcontext as sc
import sys
import Rhino

def Export():
    count = 0
    folder = ChooseFolderPath()
    layer_names = rs.LayerNames()
    newDefaultLayer = 'NewDefault'
    rs.AddLayer(newDefaultLayer)
    rs.CurrentLayer(newDefaultLayer)

    for l in layer_names:
        if l != newDefaultLayer:
            for t in layer_names:
                if rs.IsLayer(l):
                        if l != newDefaultLayer:
                            rs.LayerVisible(t, False)
                else:
                    print "The layer does not exist."
            rs.LayerVisible(l, True)
            if rs.CurrentLayer() == l:
                break
            """answer = rs.MessageBox("Continue?", 1 | 32)
            if answer is 2: break
            rs.Sleep(1000)"""
            Render(folder, count)
            count += 1
            rs.LayerVisible(l, False)
    for l in layer_names:
        if l != newDefaultLayer:
            rs.LayerVisible(l, False)
            rs.CurrentLayer(l)
    rs.DeleteLayer(newDefaultLayer)

def ChooseFolderPath():
    """
    pick a folder to save the renderings to
    return the folder
    """
    folder = rs.BrowseForFolder(rs.DocumentPath, "Browse for folder", "Batch Render")
    return folder

def Render(folder, count):
    """
    Defines the Rendering action
    Saves the render to the browsed folder
    Adds the name of the view and the name
    of the layer state to the naming of the
    view
    """
    FileName = '"'+folder+'/img_'+str(count)+'"'
    FileName = str(FileName)
    rs.Command ("!_-Render")
    rs.Command ("_-SaveRenderWindowAs "+FileName)
    rs.Sleep(2000)
    rs.Command ("_-CloseRenderWindow")
    rs.Sleep(1000)
    return 1

def ChangeView(View):
    arrLayers = Rhino.LayerNames
    rs.Command ("_-NamedView _Restore " + View + " _Enter", 0)

if __name__ == "__main__":
    Export()
