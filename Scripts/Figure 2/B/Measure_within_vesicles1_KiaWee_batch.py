from ij import IJ
from ij import *
from ij import ImagePlus
from ij import ImageStack
from ij.measure import *
from ij.plugin import *
from ij.process import *
from ij.plugin import ChannelSplitter
from ij.measure import Measurements
from ij.plugin import ImageCalculator
from ij.plugin.frame import RoiManager
from ij.plugin import Duplicator
from ij.process import ImageProcessor
from ij.process import ImageStatistics
from ij.gui import Roi
from ij.gui import PointRoi
import math 
from java.awt import * 
from java.awt import Font
import itertools 
from ij.plugin.filter import MaximumFinder
from ij.measure import ResultsTable
import time
import glob
import os
# Indicate channel which should be used for Thresholding

# Save the results automatically as  CSV file ?
#automatic_save_results = False

channel2_name = "EEA1"

channel1_name = "Jip4"

Threshold_Channel = 2

Measure_Channel = 1
    


#path for CSV fave
filepath = "D:/181118_af"

datapath = filepath
dir_name = os.path.basename(datapath)
print(dir_name)
print(datapath)
#splits = dir_name.split('_')
#print(splits[0])
#print(splits[1])
savepath = datapath + "/Measurements/"
files = glob.glob(datapath+"/*.tif")


def DoG(imp0, kernel1, kernel2):
    """Thresholds image and returns thresholded image,
    merge code still quite clumsy but functional"""
    imp1 = imp0.duplicate()
    imp2 = imp0.duplicate()
    IJ.run(imp1, "Gaussian Blur...", "sigma=" + str(kernel1) + " stack")
    IJ.run(imp2, "Gaussian Blur...", "sigma="+ str(kernel2) + " stack")
    ic = ImageCalculator()
    imp3 = ic.run("Subtract create stack", imp1, imp2)
    return imp3



def ExtractChannel(imp, channel):
    imp_height = imp.getHeight()
    imp_width = imp.getWidth()
    channelnumber = imp.getNChannels()
    slicenumber = imp.getNSlices()
    timepoints = imp.getNFrames()
    ExtractedChannel = Duplicator().run(imp, channel, channel, 1, slicenumber, 1, timepoints)
    ExtractedChannel.setTitle("Gallery_Channel_" + str(channel))
    return ExtractedChannel


def Generate_segmented_image(imp, channel):
    imp_Threshold_1 = ExtractChannel(imp1, channel)
    imp_Threshold_1.setTitle(("Threshold" + "Channel" + str(channel)))
    imp_Threshold_1.show()
    IJ.run(imp_Threshold_1, "Median...", "radius=1");
    IJ.run(imp_Threshold_1, "Subtract Background...", "rolling=50");
    IJ.setAutoThreshold(imp_Threshold_1, "Triangle dark");
    #Prefs.blackBackground = True;
    IJ.run(imp_Threshold_1, "Convert to Mask", "");
    return imp_Threshold_1


for current_file in files:

    # Clear all items from ROI manager
    rm = RoiManager.getInstance()
    rm.runCommand("reset")
    

    
    
    imp1 = IJ.openImage(current_file)
    dataname = imp1.getShortTitle()
    print(dataname)
    imp1.show

    
    
    
    
    
    # def maxZprojection(stackimp):
    #     """ from EMBL python / Fiji cookbook"""
    #     allTimeFrames = Boolean.TRUE
    #     zp = ZProjector(stackimp)
    #     zp.setMethod(ZProjector.MAX_METHOD)
    #     zp.doHyperStackProjection()
    #     zpimp = zp.getProjection()
    #     return zpimp
    
    

    
    
    imp2 = Generate_segmented_image(imp1, 2)
    # # # # Generate ROIs by "Analyse Particles"
    IJ.run(imp2, "Analyze Particles...", "size=5-Infinity pixel add exclude stack");
    IJ.run("Clear Results", "");
    ort = ResultsTable() 
    ort.setPrecision(1) 
    imp_measure = ExtractChannel(imp1, Measure_Channel)
    imp_measure.show()
    for i, roi in enumerate(RoiManager.getInstance().getRoisAsArray()):
        roi2 = rm.getRoiIndex(roi)
        rm.select(imp_measure, roi2)
        stats = imp_measure.getStatistics(Measurements.MEAN | Measurements.AREA | Measurements.FERET | Measurements.CENTROID)
    
        ort.incrementCounter()
        #ort.addValue("ROI", str(i))
        ort.addValue("Mean intensity", str(stats.mean))
        ort.addValue("Area", str(stats.area))
        ort.addValue("Compartment", (channel2_name))
    
    #ort.show("Results")
	
    imp_measure.close()
    
    

   	
    
    filename = dataname+"_001.csv"
    savename = "D:/"+filename
    ort.saveAs(savename)
    imp1.close()
    






# # #    IJ.run(imp_measure, "Make Band...", "band=0.63")    # values are in um, assumes pixelsize of 0.21

# #   # imp_measure.setRoi(roi)
# #   # ROIFrame = roi.getPosition()
# #   # imp_measure.setPosition(ROIFrame)
# #  #    imp_measure.setT(roi.getTPosition())
# #  #    imp_measure.setZ(roi.getZPosition())
# #  #    imp_measure.setC(1)
# #     IJ.run(imp_measure, "Measure", "")

# dataname = imp1.getShortTitle()
# ort = ResultsTable.getResultsTable()
# if automatic_save_results:
#     # Gather filenames of the savedirectory
#     filename_ort = "Measurements_"+dataname+"_001.csv"
#     files_ort = glob.glob(savepath+"/"+"Measurements_"+dataname+"*.csv")

#     files_ort.sort() # sort by numbering, needed to get the last filenname number
#     #print files
#     # if len(files_ort) == 0: # check if a file exists, if not, simply use the existing filename
#     #     cur_num_ort = 0  # do we need this?
#     # else:
#         # Check if filenames already exists, if so, get the last available number and increment by 1
#     if len(files_ort) != 0:
#         cur_num_ort = int(os.path.basename(files_ort[-1])[-7:-4]) # get the curtrent file number
#         filename_ort = os.path.basename(files_ort[-1][:-7]) # get the current file name
#         cur_num_ort += 1   # increment file number by 1
#         cur_num_ort = str(cur_num_ort).zfill(3)  # pad it to 3 digits
#         #print cur_num
#         filename_ort = filename_ort+cur_num_ort+str(os.path.basename(files_ort[-1][-4:])) # generate final filename
#     savename_ort = savepath+filename_ort # Generate complete savepath
#     print savename_ort
#     ort.saveAs(savename_ort) # save


