#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      npayne
#
# Created:     17/01/2019
# Copyright:   (c) npayne 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import arcpy
from arcpy import da
import os

inTable = arcpy.GetParameterAsText(0)
fileLocation = arcpy.GetParameterAsText(1)

with da.SearchCursor(inTable, ['DATA', 'ATT_NAME','REL_OBJECTID', 'ATTACHMENTID','SiteID','ident']) as cursor:
    for item in cursor:
        attachment = item[0]
        filenum = str(item[4]) + "_" + str(item[5]) + "_" + str(item[2])
        filename = filenum + str(item[1])
        open(fileLocation + os.sep + filename, 'wb').write(attachment.tobytes())
        del item
        del filenum
        del filename
        del attachment