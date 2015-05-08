import arcpy
import json

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Xtra GP Tools"
        self.alias = "xtra"

        # List of tool classes associated with this toolbox
        self.tools = [DatasetExtentToFeatures]

class DatasetExtentToFeatures(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Dataset Extent To Features"
        self.description = ""

    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter(
            displayName="Input Datasets",
            name="in_datasets",
            datatype=["DEGeodatasetType", "GPFeatureLayer"],
            parameterType="Required",
            direction="Input",
            multiValue=True)

        param1 = arcpy.Parameter(
            displayName="Output Featureclass",
            name="out_featureclass",
            datatype="DEFeatureClass",
            parameterType="Required",
            direction="Output",)

        return [param0, param1]

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""

        # collect input parameters
        in_datasets = parameters[0].valueAsText.split(";")
        out_fc = parameters[1].valueAsText
        out_fc_sr = arcpy.Describe(in_datasets[0]).SpatialReference

        arcpy.CreateFeatureclass_management(os.path.dirname(out_fc),
                                            os.path.basename(out_fc),
                                            "POLYGON",
                                            spatial_reference=out_fc_sr)

        arcpy.AddField_management(out_fc, "dataset", "TEXT", 300)

        # add each dataset's extent & the dataset's name to the output
        with arcpy.da.InsertCursor(out_fc, ("SHAPE@", "dataset")) as cur:

            for i in in_datasets:
                d = arcpy.Describe(i)
                ex = d.Extent
                pts = arcpy.Array([arcpy.Point(ex.XMin, ex.YMin),
                                  arcpy.Point(ex.XMin, ex.YMax),
                                  arcpy.Point(ex.XMax, ex.YMax),
                                  arcpy.Point(ex.XMax, ex.YMin),
                                  arcpy.Point(ex.XMin, ex.YMin),])

                geom = arcpy.Polygon(pts,  d.SpatialReference)

                if out_fc_sr != d.SpatialReference:
                    geom = geom.projectAs(out_fc_sr)
                cur.insertRow([geom, i])
