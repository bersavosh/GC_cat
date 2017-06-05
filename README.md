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

It is also possible to set an alias in your shell to make interface even simpler. E.g., you can add the following line to your `.bashrc` or `.bash_profile`:

`alias gc="python /Users/arash/Research/GC_cat/gc_cat_3.0/git_repo/gc_cat_cl.py"`

and simply run in the terminal:

`$ gc 47tuc`

**Note**: It is possible to simply download one of the two scripts and simply run those, without the database files. The script can either search for the catalog files locally (within the same directory as the script) or online (from this repository). To set the script to look online primarily, you can set `online = True` in the script. This option will prioritize looking for catalog file online. If you do not wish the module to read anything online and want it to read the local copy, you can reset `online = False` (this is the default setting).

## Updating:
The catalog is being maintained and updated intermittently. These updates are automatically applied to the catalog files (`gc_cat.fits` and `gc_cat.txt`). You can either check the repository every once in a while to see when was the last update applied or you can set `online = True` in the CL module so it will automatically use the online copy of the catalog instead of a local copy.

## Contact:
If you have questions/suggestion, feel free to contact [me](https://bersavosh.github.io/).
