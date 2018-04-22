import tomopy
from PIL import Image
import numpy as np


def load_image( infilename ) :
    pil_imgray = Image.open( infilename ).convert('LA')
    img = np.array(list(pil_imgray.getdata(band=0)), float)
    img.shape = (pil_imgray.size[1], pil_imgray.size[0])
    return img

obj = tomopy.misc.phantom.baboon(size=256, dtype=u'float32')
ang = tomopy.angles(25)

prj = tomopy.project(obj, ang)
rec = tomopy.recon(prj, ang, algorithm='gridrec', num_gridx=1024, num_gridy=1024)