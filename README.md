# xtra-gp-tools
Deliver a handful of additional gp tools and demonstrates easy 
deployment with python, github and pip.


After running install, ArcGIS desktop apps will have system toolbox automatically added and visible in the System Toolboxes.  Also related arcpy.xtra toools.

Download
--------

Use the *Download ZIP* button to your computer then
extract the contents of the ZIP.

Or use git

```
git clone git@github.com:ghisprince/xtra-gp-tools.git
```

Install
-------

Open a cmd terminal, browse into the downloaded folder and type
```
python.exe setup.py install
```


GP Tools included
-----------------

####DatasetExtentToFeatures
* in_datasets : input geodata (raster, feature class)
* out_featureclass : a feature class with on polygon feature representing the extent of each in_dataset


![DatasetExtentToFeatures Image](https://github.com/ghisprince/xtra-gp-tools/raw/master/src/esri/help/gp/DatasetExtentToFeatures.png "Inputs of various types, output rendered as hashed polygons")


Doc on extending gp tools with python
-------------------------------------
See arcgis.com [Extending gp through Python modules](http://desktop.arcgis.com/en/desktop/latest/analyze/python/extending-geoprocessing-through-python-modules.htm)

Issues
------
1. Works with ArcGIS 10.2+, does not work with ArcGIS Pro 1.0
