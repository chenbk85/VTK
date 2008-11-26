/*=========================================================================

  Program:   Visualization Toolkit
  Module:    vtkInteractorStyleTreeRingSelectHover.h

  Copyright (c) Ken Martin, Will Schroeder, Bill Lorensen
  All rights reserved.
  See Copyright.txt or http://www.kitware.com/Copyright.htm for details.

     This software is distributed WITHOUT ANY WARRANTY; without even
     the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
     PURPOSE.  See the above copyright notice for more information.

=========================================================================*/
/*-------------------------------------------------------------------------
  Copyright 2008 Sandia Corporation.
  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
  the U.S. Government retains certain rights in this software.
-------------------------------------------------------------------------*/
// .NAME vtkInteractorStyleTreeRingSelectHover - An interactor style for an RSF tree view
//
// .SECTION Description
// The vtkInteractorStyleTreeRingSelectHover specifically works with pipelines
// that create an Hierarchical RSF tree.  Such pipelines will have a vtkTreeRingLayout
// filter which must be passed to this interactor style for it to function correctly.
// This interactor style allows only 2D panning and zooming, rubber band selection and
// provides a balloon containing the name of the vertex hovered over.

#ifndef __vtkInteractorStyleTreeRingSelectHover_h
#define __vtkInteractorStyleTreeRingSelectHover_h

#include "vtkInteractorStyleRubberBand2D.h"

class vtkBalloonRepresentation;
class vtkPoints;
class vtkRenderer;
class vtkTree;
class vtkTreeRingLayout;
class vtkWorldPointPicker;
class vtkPolyData;

class VTK_INFOVIS_EXPORT vtkInteractorStyleTreeRingSelectHover : public vtkInteractorStyleRubberBand2D
{
public:
  static vtkInteractorStyleTreeRingSelectHover* New();
  vtkTypeRevisionMacro(vtkInteractorStyleTreeRingSelectHover,vtkInteractorStyleRubberBand2D);
  void PrintSelf(ostream& os, vtkIndent indent);

  // Description:
  // Must be set to the vtkTreeRingLayout used to compute the bounds of each vertex
  // for the tree map.
  void SetLayout(vtkTreeRingLayout* layout);
  vtkGetObjectMacro(Layout, vtkTreeRingLayout);

  // Description:
  // The name of the field to use when displaying text in the hover balloon.
  vtkSetStringMacro(LabelField);
  vtkGetStringMacro(LabelField);

  // Description:
  // Determine whether or not to use rectangular coordinates instead of 
  // polar coordinates.
  vtkSetMacro(UseRectangularCoordinates, bool);
  vtkGetMacro(UseRectangularCoordinates, bool);
  
  // Description:
  // Overridden from vtkInteractorStyleImage to provide the desired
  // interaction behavior.
  void OnMouseMove();

  virtual void SetInteractor(vtkRenderWindowInteractor *rwi);

  // Description:
  // Set the color used to highlight the hovered vertex.
  void SetHighLightColor(double r, double g, double b);

  // Description:
  // The width of the line around the hovered vertex.
  void SetHighLightWidth(double lw);
  double GetHighLightWidth();

protected:
  vtkInteractorStyleTreeRingSelectHover();
  ~vtkInteractorStyleTreeRingSelectHover();

private:
  vtkInteractorStyleTreeRingSelectHover(const vtkInteractorStyleTreeRingSelectHover&); // Not implemented
  void operator=(const vtkInteractorStyleTreeRingSelectHover&); // Not implemented

  // These methods are used internally
  vtkIdType GetTreeRingIdAtPos(int x, int y);
  void GetBoundingSectorForTreeRingItem(vtkIdType id, float *sinfo);
  
  vtkWorldPointPicker* Picker;
  vtkBalloonRepresentation* Balloon;
  vtkPolyData *HighlightData;
  vtkActor *HighlightActor;
  vtkTreeRingLayout* Layout;
  char *LabelField;
  bool UseRectangularCoordinates;
};

#endif
