from setuptools import setup
import setuptools.command.build_py
import os
import glob
import shutil


setup(name             = "xtragptools",
      version          = 0.1,
      description      = "",
      long_description = "",
      author           = "Esri",
      url              = "https://github.com/ghisprince/xtra-gp-tools",
      license          = "Apache Software License",
      zip_safe         = False,
      package_dir      = {"": "src"},
      packages         = ["",],
      package_data     = {"": ["esri/toolboxes/*.*",
                               "esri/help/gp/toolboxes/*.xml",
                               "esri/help/gp/messages/*.xml",
                               "esri/help/gp/*.xml",
                               "esri/arcpy/*.*",
                              ] },
      classifiers      = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: Apache Software License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      )
