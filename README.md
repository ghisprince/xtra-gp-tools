# xtra-gp-tools
Deliver a handful of additional gp tools and demonstrates easy 
deployment with python, github and pip.


Install
-------

```
pip.exe install git@github.com:ghisprince/xtra-gp-tools.git
```

if you don't have pip go to https://pip.pypa.io/en/latest/installing.html


After running install, ArcGIS desktop apps will have system toolbox automatically added and visible in the System Toolboxes.  Also related arcpy.xtra toools.


Tools
-----

##DatasetExtentToFeatures
in_datasets : input geodata (raster, feature class)
out_featureclass : a feature class with on polygon feature representing the extent of each in_dataset

![alt text][logo]

[logo]: https://github.com/ghisprince/xtra-gp-tools/raw/master/src/esri/help/gp/DatasetExtentToFeatures.png "Inputs in various color, output as hashed polys"


Doc on deploying gp tools with python
-------------------------------------
see arcgis.com [Extending gp through Python modules](http://desktop.arcgis.com/en/desktop/latest/analyze/python/extending-geoprocessing-through-python-modules.htm)

Issues
------
1. Only works with ArcGIS 10.2+ 
