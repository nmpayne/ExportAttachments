
import arcpy
from arcpy import da
import os

inTable = arcpy.GetParameterAsText(0) #can be attachement table within geodatabase
fileLocation = arcpy.GetParameterAsText(1) #output folder where photos will be stored

with da.SearchCursor(inTable, ['DATA', 'ATT_NAME','REL_OBJECTID', 'ATTACHMENTID','SiteID','ident']) as cursor: # ##in order to add addtional fields not included in additional table a join must be done on feature class and fields must match
    for item in cursor:
        attachment = item[0]
        filenum = str(item[4]) + "_" + str(item[5]) + "_" + str(item[2]) ##indexes align with indexes in search cursor above
        filename = filenum 
        open(fileLocation + os.sep + filename, 'wb').write(attachment.tobytes())
        del item
        del filenum
        del filename
        del attachment
del cursor
