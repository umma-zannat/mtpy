# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 15:35:39 2013

@author: Alison Kirkby

plots phase tensor ellipses as a pseudo section (distance along profile vs period)
"""

import os
import sys
import glob
import matplotlib.pyplot as plt
import mtpy.imaging.plotresponse as mtpr


def main(edi_path):
    """ plot edi files from the input directory edi_dir
    """

    # plt.style.use('dark_background')
    plt.style.use('seaborn-deep')
    plt.style.use('classic')

    elst = glob.glob(os.path.join(edi_path, "*.edi"))

    print(elst)

    for efile in elst:
        # eo = mtedi.Edi(filename=efile)
        pr = mtpr.PlotResponse(fn=efile, plot_num=2, res_limits=(
            1, 10000), phase_limits=(0, 90))

        plt.close()

    return


def plot1(edi_file):
    """
    Plot a given edi file
    Args:
        edi_file: path2edifile

    Returns:

    """
    plt.style.use('seaborn-deep')
    plt.style.use('classic')

    print("plotting edi file", edi_file)

    pr = mtpr.PlotResponse(fn=edi_file, plot_num=2, res_limits=(1, 10000), phase_limits=(0, 90))

    return pr


#########################################################
# plot one-by-one edi files in a given dirpath
# How to Run:
# export PYTHONPATH=/Softlab/Githubz/mtpy:$PYTHONPATH
# python plot_edis.py data/edi_files/

if __name__ == '__main__':
    edi_path = sys.argv[1]

    if os.path.isdir(edi_path):
        main(edi_path)
    elif os.path.isfile(edi_path):
        plot1(edi_path)
    else:
        print "Usage %s %s" % (sys.argv[0], "path2edi")