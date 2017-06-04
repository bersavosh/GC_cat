# GC_cat

A Catalog of Galactic globular clusters' properties and dynamics. 

## The catalog:
This is a combination of multiple globular cluster catalogs. The base catalog is the [Harris catalog, 2010 edition](http://www.physics.mcmaster.ca/~harris/Databases.html) ([Harris 1996](http://adsabs.harvard.edu/abs/1996AJ....112.1487H)). There are two other catalogs currently implemented as well: cluster stellar encounter rates from [Bahramian et al. 2013](http://adsabs.harvard.edu/abs/2013ApJ...766..136B) and theoretical mass, velocity disspersion and escape velocities from [Gnedin et al. 2002](http://adsabs.harvard.edu/abs/2002ApJ...568L..23G).

Additionally, if I encounter new studies which provide updated measurements for one or more clusters, they are added (and such updates are mentioned in the "notes" column in the catalog).

Currently this catalog is available in fits, ascii and [online](https://bersavosh.github.io/research/gc_cat.html).

## Command-line module:
The CL module is a simple python script that accepts a query (cluster name) from the command-line and searches the catalog for that cluster. If the cluster is listed, it will print out all available information on the cluster.

It does not require any installation, simply download this repository as a zip folder and run the appropriate file. 

There are two versions of the script:
- `gc_cl_astpy.py`: This version uses astropy fits capability to read the database. Slightly more convenient to write and maintain.
- `gc_cl_simple.py`: Written for those who do not use non-standard python packages (astropy in this case). It solely relies on python 2.7's core packages. 

It is possible to run the script without any arguments, in which case, the user will be asked to enter a cluster name:
`$ python gc_cl_astpy.py`
or
`$ python gc_cl_simple.py`

It is also possible to pass cluster name as an argument:
`$ python gc_cl_astpy.py terzan5`
or
`$ python gc_cl_simple.py terzan5`

Spaces or small/capitalized letters in the argument do not affect the query; `teR za n 5` will be recognized as `Terzan5`.

## Updating:
The catalog is being maintained and updated intermittently. These updates are automatically applied to the catalog files (`gc_cat.fits` and `gc_cat.txt`). By default, the command-line module first tries to access the database online and check if there are any updates, if failed to find/access the online database, it will look for a local copy of the catalog file in the same folder. If you do not want the module to check online at all, and just read the local copy, you can change this in the script by setting `online = False` at the top of the script.

## Contact:
If you have questions/suggestion, feel free to contact [me](https://bersavosh.github.io/).
