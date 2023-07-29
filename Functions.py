# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# Template.py
# Version: 0.1
# Date:
# Original Author: Kyle Smiley
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
#
# This code serves as a template to begin writing new scripts

import arcpy
import os

# Set module name
#if __name__== "__main__":
    
    # Import the libraries you will need
    #import os
    #import arcpy
def currentfunction(argl):
    arcpy.AddMessage("starting currentfunction")

    argl = arcpy.GetParameterAsText(0)

    currentfunction(argl)

# parameter1 = arcpy.GetParameterAsText(0)
# parameter2 = arcpy.GetParameterAsText(1)
# parameter3 = arcpy.GetParamterAsText(2)

# Function for exporting a dataset to a csv
def createCSV(data, csvname, mode='ab'):
    with open(csvname, mode) as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(data)
    
# function for exporting a .xls
# Use with Python 2.7
def generateXLS(dataset, sheetName, fileName):
    import xlwt
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet(sheetName)
    for YCOUNTER, data in enumerate(dataset):
        for XCOUNTER, value in enumerate(data):
            sheet.write(YCOUNTER,XCOUNTER, value)
        workbook.save(fileName)
        
# function for exporting a .xlsx
# use with Python 3.x
def generateXLSX(dataset, sheetName, fileName):
    import xlsxwriter
    workbook = xlsxwriter.Workbook()
    sheet = workbook.add_sheet(sheetName)
    for YCOUNTER, data in enumerate(dataset):
        for XCOUNTER, value in enumerate(data):
            sheet.write(YCOUNTER,XCOUNTER, value)
        workbook.save(fileName)


# Function for viewing a feature class or GDB tablein ArcPro using notebooks
# Views first 5 records
def view_gdbtable(fc): # fc or gdb table (either can be viewed)
    import pandas as pd
    fields = [field.name for field in arcpy.ListFields(fc)]
    data = [row for row in arcpy.da.SearchCursor(fc,fields)]
    df = pd.DataFrame(data,columns=fields)
    return df.head()




def fileNameIncrementor(fullPath):
    '''Adds first available _int suffix to create unique folder/file name'''
    # If file/folder exists, adds integer suffix to output name
    # Requires/Returns full path - no checking or validation included
 
    base, extension = os.path.splitext(fullPath)
    i = 0
    while arcpy.Exists(fullPath):
        i += 1
        fullPath = base + "_" + str(i) + extension
    return fullPath
 
#Ex.
#uniqueFileName = fileNameIncrementor(r'C:\temp\mySpreadsheet.xlsx')
#if file already exists, uniqueFileName will be:
#'c:\temp\mySpreadsheet_1.xlsx'   # or whatever the first available int

def print_hello():
    print("hello")

def Unzip_Folders(infolder):
    # Under construction
    # import libraries
    import zipfile
    import os

    # set the extension to .zip
    extension = ".zip"

    #infolder = arcpy.GetParameterAsText(0)   # parameter to use for tool in Pro
    #infolder = "D:\Geodata\Elevation\LAS"
    os.chdir(infolder) ##change directory from working dir to dir with files if needed

    for item in os.listdir(infolder): # loop through items in dir
        if item.endswith(extension): # check for ".zip" extension
            file_name = os.path.abspath(item) # get full path of files
            zip_ref = zipfile.ZipFile(file_name) # create zipfile object
            zip_ref.extractall(infolder) # extract file to dir
            zip_ref.close() # close file
            os.remove(file_name) # delete zipped file
            
    return

