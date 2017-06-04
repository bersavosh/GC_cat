import sys, os, inspect
from astropy.io import fits

online = True

if online == True:
    try:
        gc_cat = fits.open('https://github.com/bersavosh/GC_cat/raw/master/gc_cat.fits',cache=False)[1].data
    except:
        path = os.path.abspath(inspect.getfile(inspect.currentframe())).replace('gc_cat_cl.py','gc_cat.fits')
        gc_cat = fits.open(path)[1].data

if online == False:
    path = os.path.abspath(inspect.getfile(inspect.currentframe())).replace('gc_cat_cl.py','gc_cat.fits')
    gc_cat = fits.open(path)[1].data

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

found_flg = False
for i in range(len(gc_cat)):
    if query == gc_cat['Name'][i].lower() or query == gc_cat['Alt.Name'][i].lower():
        found_flg = True
        print '============================================================================================='
        print 'Cluster name: ', gc_cat['Name'][i]
        print 'Other commonly used cluster name: ', gc_cat['Alt.Name'][i]
        print 'Right ascension: (epoch J2000):', gc_cat['RA'][i]
        print 'declination (epoch J2000):', gc_cat['Dec'][i]
        print 'Galactic longitude and latitude (deg): ', gc_cat['L'][i],gc_cat['B'][i]
        print 'Distance from Sun (kpc): ', gc_cat['R_sun'][i]
        print 'Distance from Galactic center (kpc), assuming R_0=8.0 kpc: ', gc_cat['R_galcen'][i]
        print 'Galactic distance components X,Y,Z in kiloparsecs: ', gc_cat['X'][i],gc_cat['Y'][i],gc_cat['Z'][i]
        print 'in a Sun-centered coordinate system:'
        print 'X towards Gal. cen., Y in direction of Gal. rot., Z toward North Gal. Pole'
        print '----------------- Metallicity and Photometry ------------------------------------------------'
        print 'Metallicity [Fe/H]:', gc_cat['Fe_H'][i]
        print 'Foreground reddening E(B-V):', gc_cat['Reddening'][i]
        print 'V magnitude level of the horizontal branch (or RR Lyraes):', gc_cat['V_HB'][i]
        print 'Apparent visual distance modulus:', gc_cat['m_M_V'][i]
        print 'Integrated V magnitude of the cluster:', gc_cat['V_t'][i]
        print 'Absolute visual magnitude (cluster luminosity)(M_V,t = V_t - (m-M)V):', gc_cat['M_V,t'][i]
        print 'Integrated color indices (uncorrected for reddening):'
        print 'U-B =',gc_cat['U-B'][i],'B-V =',gc_cat['B-V'][i],'V-R =',gc_cat['V-R'][i],'V-I =',gc_cat['V-I'][i]
        print 'Projected ellipticity of isophotes, e = 1-(b/a):', gc_cat['ellip'][i]
        print '----------------- Velocities and Structural Parameters --------------------------------------'
        print 'Heliocentric radial velocity (km/s):', gc_cat['v_r'][i]
        print 'Observational (internal) uncertainty in radial velocity:', gc_cat['v_r_err'][i]
        print 'Radial velocity relative to Solar neighborhood LSR:', gc_cat['v_LSR'][i]
        print 'Central velocity dispersion sig_v (km/s):', gc_cat['sig_v'][i]
        print 'Observational (internal) uncertainty in velocity dispersion:', gc_cat['sig_v_err'][i]
        print 'King-model central concentration, c = log(r_t/r_c) :', gc_cat['c'][i]
        if gc_cat['cc'][i] == 'c': cc_stat= 'yes'
        elif gc_cat['cc'][i] == 'c:': cc_stat= 'maybe'
        else: cc_stat= 'no'
        print 'core collapsed?', cc_stat
        print 'Core radius in arcmin:', gc_cat['rc'][i]
        print 'Half-light radius in arcmin:', gc_cat['rh'][i]
        print 'Central surface brightness, V magnitudes per square arcsecond:', gc_cat['mu_V'][i]
        print 'Central luminosity density, log_10(Solar luminosities per cubic parsec):', gc_cat['rho_0'][i]
        print 'Core relaxation time t(r_c), in log_10(years):', gc_cat['lg_tc'][i]
        print 'Median relaxation time t(r_h), in log_10(years):', gc_cat['lg_th'][i]
        print '----------------- Other paramters -----------------------------------------------------------'
        print 'Predicted NH based on extinction (Bahramian+2015):', '{:.2e}'.format(eval(gc_cat['Reddening'][i])*3.1*2.81e21),'cm^-2'
        print 'Integrated stellar encounter rate (Bahramian+2013, 47tuc = 1000):', gc_cat['Gamma1'][i]
        print 'Simplified stellar encounter rate [rho^2 * r^3 /sigma] (Bahramian+2013, 47tuc = 1000):', gc_cat['Gamma2'][i]
        print 'Simplified stellar encounter rate [rho^1.5 * r^2] (Bahramian+2013, 47tuc = 1000):', gc_cat['Gamma3'][i]
        print 'Theoretical mass (Gnedin+2002):', gc_cat['model Mass'][i] ,'Msol'
        print 'Theoretical central velocity dispersion (Gnedin+2002):',gc_cat['model sig_v'][i],'km/s'
        print 'Theoretical escape velocity in the center (Gnedin+2002):',gc_cat['model v_esc'][i],'km/s'
        print 'Catalog Notes:',gc_cat['notes'][i]
        print '============================================================================================='

if found_flg == False:
    print 'Cluster not found in the catalog'
