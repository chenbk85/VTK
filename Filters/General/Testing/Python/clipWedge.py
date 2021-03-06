#!/usr/bin/env python
import vtk
from vtk.test import Testing
from vtk.util.misc import vtkGetDataRoot
VTK_DATA_ROOT = vtkGetDataRoot()

#define a Single Cube
Scalars = vtk.vtkFloatArray()
Scalars.InsertNextValue(1.0)
Scalars.InsertNextValue(0.0)
Scalars.InsertNextValue(0.0)
Scalars.InsertNextValue(0.0)
Scalars.InsertNextValue(0.0)
Scalars.InsertNextValue(0.0)
Points = vtk.vtkPoints()
Points.InsertNextPoint(0,0,0)
Points.InsertNextPoint(1,0,0)
Points.InsertNextPoint(0,0,1)
Points.InsertNextPoint(0,1,0)
Points.InsertNextPoint(1,1,0)
Points.InsertNextPoint(0,1,1)
Ids = vtk.vtkIdList()
Ids.InsertNextId(0)
Ids.InsertNextId(1)
Ids.InsertNextId(2)
Ids.InsertNextId(3)
Ids.InsertNextId(4)
Ids.InsertNextId(5)
Grid = vtk.vtkUnstructuredGrid()
Grid.Allocate(10,10)
Grid.InsertNextCell(13,Ids)
Grid.SetPoints(Points)
Grid.GetPointData().SetScalars(Scalars)
#Clip the wedge
clipper = vtk.vtkClipDataSet()
clipper.SetInputData(Grid)
clipper.SetValue(0.5)
# build tubes for the triangle edges
#
wedgeEdges = vtk.vtkExtractEdges()
wedgeEdges.SetInputConnection(clipper.GetOutputPort())
wedgeEdgeTubes = vtk.vtkTubeFilter()
wedgeEdgeTubes.SetInputConnection(wedgeEdges.GetOutputPort())
wedgeEdgeTubes.SetRadius(.005)
wedgeEdgeTubes.SetNumberOfSides(6)
wedgeEdgeMapper = vtk.vtkPolyDataMapper()
wedgeEdgeMapper.SetInputConnection(wedgeEdgeTubes.GetOutputPort())
wedgeEdgeMapper.ScalarVisibilityOff()
wedgeEdgeActor = vtk.vtkActor()
wedgeEdgeActor.SetMapper(wedgeEdgeMapper)
wedgeEdgeActor.GetProperty().SetDiffuseColor(lamp_black)
wedgeEdgeActor.GetProperty().SetSpecular(.4)
wedgeEdgeActor.GetProperty().SetSpecularPower(10)
#shrink the triangles so we can see each one
aShrinker = vtk.vtkShrinkFilter()
aShrinker.SetShrinkFactor(1)
aShrinker.SetInputConnection(clipper.GetOutputPort())
aMapper = vtk.vtkDataSetMapper()
aMapper.ScalarVisibilityOff()
aMapper.SetInputConnection(aShrinker.GetOutputPort())
Wedges = vtk.vtkActor()
Wedges.SetMapper(aMapper)
Wedges.GetProperty().SetDiffuseColor(banana)
#build a model of the cube
Edges = vtk.vtkExtractEdges()
Edges.SetInputData(Grid)
Tubes = vtk.vtkTubeFilter()
Tubes.SetInputConnection(Edges.GetOutputPort())
Tubes.SetRadius(.01)
Tubes.SetNumberOfSides(6)
TubeMapper = vtk.vtkPolyDataMapper()
TubeMapper.SetInputConnection(Tubes.GetOutputPort())
TubeMapper.ScalarVisibilityOff()
CubeEdges = vtk.vtkActor()
CubeEdges.SetMapper(TubeMapper)
CubeEdges.GetProperty().SetDiffuseColor(khaki)
CubeEdges.GetProperty().SetSpecular(.4)
CubeEdges.GetProperty().SetSpecularPower(10)
# build the vertices of the cube
#
Sphere = vtk.vtkSphereSource()
Sphere.SetRadius(0.04)
Sphere.SetPhiResolution(20)
Sphere.SetThetaResolution(20)
ThresholdIn = vtk.vtkThresholdPoints()
ThresholdIn.SetInputData(Grid)
ThresholdIn.ThresholdByUpper(.5)
Vertices = vtk.vtkGlyph3D()
Vertices.SetInputConnection(ThresholdIn.GetOutputPort())
Vertices.SetSourceConnection(Sphere.GetOutputPort())
SphereMapper = vtk.vtkPolyDataMapper()
SphereMapper.SetInputConnection(Vertices.GetOutputPort())
SphereMapper.ScalarVisibilityOff()
CubeVertices = vtk.vtkActor()
CubeVertices.SetMapper(SphereMapper)
CubeVertices.GetProperty().SetDiffuseColor(tomato)
CubeVertices.GetProperty().SetDiffuseColor(tomato)
#define the text for the labels
caseLabel = vtk.vtkVectorText()
caseLabel.SetText("Case 1")
aLabelTransform = vtk.vtkTransform()
aLabelTransform.Identity()
aLabelTransform.Translate(-.2,0,1.25)
aLabelTransform.Scale(.05,.05,.05)
labelTransform = vtk.vtkTransformPolyDataFilter()
labelTransform.SetTransform(aLabelTransform)
labelTransform.SetInputConnection(caseLabel.GetOutputPort())
labelMapper = vtk.vtkPolyDataMapper()
labelMapper.SetInputConnection(labelTransform.GetOutputPort())
labelActor = vtk.vtkActor()
labelActor.SetMapper(labelMapper)
#define the base
baseModel = vtk.vtkCubeSource()
baseModel.SetXLength(1.5)
baseModel.SetYLength(.01)
baseModel.SetZLength(1.5)
baseMapper = vtk.vtkPolyDataMapper()
baseMapper.SetInputConnection(baseModel.GetOutputPort())
base = vtk.vtkActor()
base.SetMapper(baseMapper)
# Create the RenderWindow, Renderer and both Actors
#
ren1 = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren1)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
# position the base
base.SetPosition(.5,-.09,.5)
ren1.AddActor(wedgeEdgeActor)
ren1.AddActor(base)
ren1.AddActor(labelActor)
ren1.AddActor(CubeEdges)
ren1.AddActor(CubeVertices)
ren1.AddActor(Wedges)
ren1.SetBackground(slate_grey)
renWin.SetSize(400,400)
ren1.ResetCamera()
ren1.GetActiveCamera().Dolly(1.2)
ren1.GetActiveCamera().Azimuth(30)
ren1.GetActiveCamera().Elevation(20)
ren1.ResetCameraClippingRange()
renWin.Render()
iren.Initialize()
mask = "1 2 4 8 16 32"
def cases (id,__vtk__temp0=0,__vtk__temp1=0):
    global mask
    i = 0
    while i < 6:
        m = lindex(mask,i)
        if (expr.expr(globals(), locals(),["m","&","id"]) == 0):
            Scalars.SetValue(i,0)
            pass
        else:
            Scalars.SetValue(i,1)
            pass
        caseLabel.SetText("Case " + str(id) + "")
        i = i + 1

    Grid.Modified()
    renWin.Render()

cases(7)
# --- end of script --
