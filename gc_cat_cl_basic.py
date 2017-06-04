import sys, os, inspect, urllib2

"""
online = True

if online == True:
    try:
		gc_cat = urllib2.urlopen('https://github.com/bersavosh/GC_cat/raw/master/gc_cat.txt').readlines()
    except:
    	print 'offfline'
        cat_file = os.path.abspath(inspect.getfile(inspect.currentframe())).replace('gc_cat_cl_basic.py','gc_cat.txt')
        with open(cat_file) as f:
            gc_cat = f.readlines()

if online == False:
	cat_file = os.path.abspath(inspect.getfile(inspect.currentframe())).replace('gc_cat_cl_basic.py','gc_cat.txt')
	with open(cat_file) as f:
		gc_cat = f.readlines()
"""

request = urllib2.Request('https://github.com/bersavosh/GC_cat/raw/master/gc_cat.txt')
request.add_header('Pragma', 'no-cache')

gc_cat = urllib2.urlopen('https://github.com/bersavosh/GC_cat/raw/master/gc_cat.txt').readlines()


if len(sys.argv) == 1:
    query = raw_input('Enter gc name: ')
if len(sys.argv) == 2:
    query = sys.argv[1]
if len(sys.argv) == 3:
    query = sys.argv[1]+sys.argv[2]
if len(sys.argv) > 3:
	print 'Error: Too many arguments'
	sys.exit(1)

query = query.replace(' ','')
query = query.lower()

for i in range(1,len(gc_cat)):
    entry = gc_cat[i].split()
    if query == gc_cat[i].lower().split()[0] or query == gc_cat[i].lower().split()[1]:
	   	print '============================================================================================='
	   	print 'Cluster name: ',entry[0]
	   	print 'Other commonly used cluster name: ', entry[1]
		print 'Right ascension: (epoch J2000):', entry[2]
		print 'declination (epoch J2000):', entry[3]
		print 'Galactic longitude and latitude (deg): ', entry[4],entry[5]
		print 'Distance from Sun (kpc): ', entry[6]
		print 'Distance from Galactic center (kpc), assuming R_0=8.0 kpc: ', entry[7]
		print 'Galactic distance components X,Y,Z in kiloparsecs: ', entry[8],entry[9],entry[10]
		print 'in a Sun-centered coordinate system:'
		print 'X towards Gal. cen., Y in direction of Gal. rot., Z toward North Gal. Pole'
		print '----------------- Metallicity and Photometry ------------------------------------------------'
		print 'Metallicity [Fe/H]:', entry[11]
		print 'Foreground reddening E(B-V):', entry[12]
		print 'V magnitude level of the horizontal branch (or RR Lyraes):', entry[13]
		print 'Apparent visual distance modulus:', entry[14]
		print 'Integrated V magnitude of the cluster:', entry[15]
		print 'Absolute visual magnitude (cluster luminosity)(M_V,t = V_t - (m-M)V):', entry[16]
		print 'Integrated color indices (uncorrected for reddening):'
		print 'U-B =',entry[17],'B-V =',entry[18],'V-R =',entry[19],'V-I =',entry[20]
		print 'Projected ellipticity of isophotes, e = 1-(b/a):', entry[21]
		print '----------------- Velocities and Structural Parameters --------------------------------------'
		print 'Heliocentric radial velocity (km/s):', entry[22]
		print 'Observational (internal) uncertainty in radial velocity:', entry[23]
		print 'Radial velocity relative to Solar neighborhood LSR:', entry[24]
		print 'Central velocity dispersion sig_v (km/s):', entry[25]
		print 'Observational (internal) uncertainty in velocity dispersion:', entry[26]
		print 'King-model central concentration, c = log(r_t/r_c) :', entry[27]
		if entry[28] == 'c': cc_stat= 'yes'
		elif entry[28] == 'c:': cc_stat= 'maybe'
		else: cc_stat= 'no'
		print 'core collapsed?', cc_stat
		print 'Core radius in arcmin:', entry[29]
		print 'Half-light radius in arcmin:', entry[30]
		print 'Central surface brightness, V magnitudes per square arcsecond:', entry[31]
		print 'Central luminosity density, log_10(Solar luminosities per cubic parsec):', entry[32]
		print 'Core relaxation time t(r_c), in log_10(years):', entry[33]
		print 'Median relaxation time t(r_h), in log_10(years):', entry[34]
		print '----------------- Other paramters -----------------------------------------------------------'
		print 'Predicted NH based on extinction (Bahramian+2015):', '{:.2e}'.format(eval(entry[12])*3.1*2.81e21),'cm^-2'
		print 'Integrated stellar encounter rate (Bahramian+2013, 47tuc = 1000):', entry[35]
		print 'Simplified stellar encounter rate [rho^2 * r^3 /sigma] (Bahramian+2013, 47tuc = 1000):', entry[36]
		print 'Simplified stellar encounter rate [rho^1.5 * r^2] (Bahramian+2013, 47tuc = 1000):', entry[37]
		print 'Theoretical mass (Gnedin+2002):', entry[38] ,'Msol'
		print 'Theoretical central velocity dispersion (Gnedin+2002):', entry[39],'km/s'
		print 'Theoretical escape velocity in the center (Gnedin+2002):', entry[40],'km/s'
		print 'Catalog Notes:', ' '.join(entry[42:])
		print '============================================================================================='
