import numpy as np

def read_swmf_tec_file(fname,nheader=23):
    """
    READ_SWMF_TEC_FILE

    A simple parser for TecPlot-formatted data files that are generated by the
    Space Weather Modeling Framework with 3d MHD format

    Jesse Woodroffe

    """

    # Start by parsing the header
    with open(fname,'r') as f:
        # Skip first line
        f.readline()

        # Second line gives the variable symbols and their units. Here we do a bunch
        # of string manipulation to put them in an easy-to-read format
        varstrs=f.readline().strip().split('=')[1].replace('`','').replace('[','').replace(']','').replace('"','').split(',')
        unit_data={}
        for s in varstrs:
            l,r=s.split()
            unit_data[l]=r
        params=f.readline()

    # Get the number of points in the data file
    npoints=int(params.split(',')[1].split()[1])

    # Now we can read the data file
    dat=np.genfromtxt(fname,skip_header=nheader,max_rows=npoints)

    # Put the data into a dictionary
    swmfdata={ 'x':dat[:, 0], 'y':dat[:, 1], 'z':dat[:, 2],
               'r':dat[:, 3],
              'ux':dat[:, 4],'uy':dat[:, 5],'uz':dat[:, 6],
              'bx':dat[:, 7],'by':dat[:, 8],'bz':dat[:, 9],
               'p':dat[:,10],
              'jx':dat[:,11],'jy':dat[:,12],'jz':dat[:,13],
              'units':unit_data}

    return swmfdata