import pyopencl as cl
from pyopencl import array
import numpy

if __name__ == "__main__":
    ## Step #1.  Obtain an OpenCL platform.
    platform = cl.get_platforms()[0]


    #platform_extensions = platforms[0].extensions

    ## Step #2.  Obtain a device id for at least one device (accelerator).
    device = platform.get_devices()[0]

    
