# Download with wget doesn't work!
import fitsio
#from fitsio import FITS,FITSHDR
import matplotlib.pyplot as plt
filename = 'UPH20230301120000.FTS'
fits = fitsio.FITS(filename,'r',clobber=True)
#print(fits)
#data, h = fitsio.read(filename, header=True)
h=fitsio.read_header(filename)
print(h)

sun=fits[0].read()
import matplotlib.pylab as plt
plt.imshow(sun,cmap='gray')
plt.savefig('Sun-disk-March-1st-2023-at-noon.png')
plt.close()
from hashlib import sha256
with open('Sun-disk-March-1st-2023-at-noon.png','rb') as f:
    digest = sha256(f.read())

print(digest.hexdigest())  