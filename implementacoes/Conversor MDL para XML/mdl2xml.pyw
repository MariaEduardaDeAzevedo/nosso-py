# Powered by @EuclidesRamos

import matlab.engine # It is important to have the matlab engine installed on your pc
import sys

# Call matlab engine on background and convert to XML
def mdl2xml(fileName):
    myengine = matlab.engine.start_matlab() # Start engine background=true

    myengine.load_system(fileName) # Put MDL/SLX on memory

    partialFilename = fileName.split(".") # Create xml filename
    xmlCompleteFilename = partialFilename[0] + '.xml'

    myengine.save_system(fileName, xmlCompleteFilename, 'ExportToXML', True)

    myengine.quit() # Stop engine

fileName = sys.argv[1]
mdl2xml(fileName) # Call function
