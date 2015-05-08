# -*- coding: utf-8 -*-
""""""
__all__ = ['DatasetExtentToFeatures']
__alias__ = u'xtra'
from arcpy.geoprocessing._base import gptooldoc, gp, gp_fixargs
from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject

# Tools
@gptooldoc('DatasetExtentToFeatures_xtra', None)
def DatasetExtentToFeatures(in_datasets=None, out_featureclass=None):
    """DatasetExtentToFeatures_xtra(in_datasets;in_datasets..., out_featureclass)

     INPUTS:
      in_datasets (Geodataset / Feature Layer)

     OUTPUTS:
      out_featureclass (Feature Class)"""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DatasetExtentToFeatures_xtra(*gp_fixargs((in_datasets, out_featureclass), True)))
        return retval
    except Exception, e:
        raise e


# End of generated toolbox code
del gptooldoc, gp, gp_fixargs, convertArcObjectToPythonObject