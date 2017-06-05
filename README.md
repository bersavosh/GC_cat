# GC_cat

A Catalog of Galactic globular clusters' properties and dynamics. 

## The catalog:
This is a combination of multiple globular cluster catalogs. The base catalog is the [Harris catalog, 2010 edition](http://www.physics.mcmaster.ca/~harris/Databases.html) ([Harris 1996](http://adsabs.harvard.edu/abs/1996AJ....112.1487H)). There are two other catalogs currently implemented as well: cluster stellar encounter rates from [Bahramian et al. 2013](http://adsabs.harvard.edu/abs/2013ApJ...766..136B) and theoretical mass, velocity disspersion and escape velocities from [Gnedin et al. 2002](http://adsabs.harvard.edu/abs/2002ApJ...568L..23G). More catalogs and studies will be added in the future.

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

sample output:
```
=============================================================================================
Cluster name:  NGC104
Other commonly used cluster name:  47Tuc
Right ascension: (epoch J2000): 00:24:05.67
declination (epoch J2000): -72:04:52.6
Galactic longitude and latitude (deg):  305.89 -44.89
Distance from Sun (kpc):  4.5
Distance from Galactic center (kpc), assuming R_0=8.0 kpc:  7.4
Galactic distance components X,Y,Z in kiloparsecs:  1.9 -2.6 -3.1
in a Sun-centered coordinate system:
X towards Gal. cen., Y in direction of Gal. rot., Z toward North Gal. Pole
----------------- Metallicity and Photometry ------------------------------------------------
Metallicity [Fe/H]: -0.72
Foreground reddening E(B-V): 0.04
V magnitude level of the horizontal branch (or RR Lyraes): 14.06
Apparent visual distance modulus: 13.37
Integrated V magnitude of the cluster: 3.95
Absolute visual magnitude (cluster luminosity)(M_V,t = V_t - (m-M)V): -9.42
Integrated color indices (uncorrected for reddening):
U-B = 0.37 B-V = 0.88 V-R = 0.53 V-I = 1.14
Projected ellipticity of isophotes, e = 1-(b/a): 0.09
----------------- Velocities and Structural Parameters --------------------------------------
Heliocentric radial velocity (km/s): -18.0
Observational (internal) uncertainty in radial velocity: 0.1
Radial velocity relative to Solar neighborhood LSR: -26.7
Central velocity dispersion sig_v (km/s): 11.0
Observational (internal) uncertainty in velocity dispersion: 0.3
King-model central concentration, c = log(r_t/r_c) : 2.07
core collapsed? no
Core radius in arcmin: 0.36
Half-light radius in arcmin: 3.17
Central surface brightness, V magnitudes per square arcsecond: 14.38
Central luminosity density, log_10(Solar luminosities per cubic parsec): 4.88
Core relaxation time t(r_c), in log_10(years): 7.84
Median relaxation time t(r_h), in log_10(years): 9.55
----------------- Other paramters -----------------------------------------------------------
Predicted NH based on extinction (Bahramian+2015): 3.48e+20 cm^-2
Integrated stellar encounter rate (Bahramian+2013, 47tuc = 1000): 1000.0
Simplified stellar encounter rate [rho^2 * r^3 /sigma] (Bahramian+2013, 47tuc = 1000): 1000.0
Simplified stellar encounter rate [rho^1.5 * r^2] (Bahramian+2013, 47tuc = 1000): 1000.0
Theoretical mass (Gnedin+2002): 1500000.0 Msol
Theoretical central velocity dispersion (Gnedin+2002): 16.4 km/s
Theoretical escape velocity in the center (Gnedin+2002): 68.8 km/s
Catalog Notes: 
=============================================================================================
```

**Note 1**: It is possible to simply download one of the two scripts and simply run those, without the database files. The script can either search for the catalog files locally (within the same directory as the script) or online (from this repository). To set the script to look online primarily, you can set `online = True` in the script. This option will prioritize looking for catalog file online. If you do not wish the module to read anything online and want it to read the local copy, you can reset `online = False` (this is the default setting).

**Note 2**: Besides the information within the catalog, the CL module also reports expected hydrogen column density (NH) towards the cluster. These values are based on recent studies of correlation between E(B-V) and NH  ([Bahramian et al. 2015](http://adsabs.harvard.edu/abs/2015MNRAS.452.3475B), [Foight et al. 2016](http://adsabs.harvard.edu/abs/2016ApJ...826...66F)). These studies find NH ~ 2.81e21xAv, and here I assume Av ~ 3.1xE(B-V).

## Updating:
The catalog is being maintained and updated intermittently. These updates are automatically applied to the catalog files (`gc_cat.fits` and `gc_cat.txt`). You can either check the repository every once in a while to see when was the last update applied or you can set `online = True` in the CL module so it will automatically use the online copy of the catalog instead of a local copy.

Note that updates (e.g., replacing an already reported measurement by a newer measurement based on a deeper study) are always explained in the "notes" column in the catalog. If there is no note, the values are from the three catalogs mentioned above.

## Contact/disclaimer:
**Contact**: If you have questions/suggestion, feel free to contact [me](https://bersavosh.github.io/).

**Disclaimer**: This catalog does not contain any original data at the moment, and it is based on published results in various publications. If you find this catalog useful, please make sure to cite the original references, and if possible acknowlege use of this repository.
