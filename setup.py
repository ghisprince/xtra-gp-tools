from setuptools import setup
import setuptools.command.build_py
import os
import glob
import shutil

class BuildToolboxSupportFiles(setuptools.command.build_py.build_py):
    def run(self):
        import arcpy
        setuptools.command.build_py.build_py.run(self)

        esri_pth = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                                      "build",
                                                      "lib",                                
                                                      "esri")
        tbx_pth = os.path.join(esri_pth, "toolboxes")

        # find all tbx & pyt, create arcpy & help files for them
        for f in (glob.glob(os.path.join(tbx_pth, "*.pyt")) +
                  glob.glob(os.path.join(tbx_pth, "*.tbx"))):
            arcpy.gp.CreateToolboxSupportFiles(f)

        for root, dirs, files in os.walk(tbx_pth + "\\esri", topdown=False):
            for f in files:
                import pdb;pdb.set_trace()
                
                os.renames(os.path.join(root, f),
                      os.path.join(root.replace(tbx_pth + "\\esri", esri_pth), f))

        

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
                               "esri/help/gp/messages/*.xml",                               
                                       ] },
      cmdclass         = {'build_py': BuildToolboxSupportFiles},
      classifiers      = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: Apache Software License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      )
