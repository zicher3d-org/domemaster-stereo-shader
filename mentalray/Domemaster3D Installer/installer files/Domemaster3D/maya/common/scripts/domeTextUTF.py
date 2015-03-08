"""
Dome Text UTF Converter V1.7
by Andrew Hazelden

The DomeTextUTF script converts text into the UTF8 encoding format

Python text encoding notes:
http://docs.python.org/2.5/lib/standard-encodings.html


Version 1.7
------------
2015-03-07 

Version 1.5
------------
July 6, 2014

Version 1
------------
Oct 8, 2013
Initial Version

Practical example:
import domeTextUTF
reload(domeTextUTF)
domeTextUTF.convertTextToUTF('C:/dometext.txt', 'C:/dometext_utf8.txt', 'big5', 'Normal Case')

local example:
convertTextToUTF('C:/dometext.txt', 'C:/dometext_utf8.txt', 'big5', 'Normal Case')

convertTextToUTF('C:/dometext.txt', 'C:/dometext_utf8.txt', 'big5', 'Binary Words')

"""

#Read the current text file and change the encoding
def convertTextToUTF(filename, savename, encoding, convertCase):
  import binascii
  #filename = "C:/dometext.txt"
  #savename = "C:/dometext_utf8.txt"
  #encoding = 'big5'
 
  #Read the Maya Generated text file
  file = open(filename, "r")
  filedata = file.read()
  file.close()
  
  #Simulated text data
  #filedata = 'hello'
  #filedata = 'aaa'

  #Convert the case of the text string
  if(convertCase == "Normal Case"):
    #Pass the text unmodified
    convertedText = filedata
  elif(convertCase == "Upper Case"):
    #Convert the text output to upper case letters
    convertedText = filedata.upper()
  elif(convertCase == "Lower Case"):
    #Convert the text output to lower case letters
    convertedText = filedata.lower()
  elif(convertCase == "Hex Words"):
    #Convert the text output to hexadecimal format letters
    #convertedText = str(filedata.encode("hex"))
    
    #Convert the text output to hexadecimal format letters
    editedData = str(filedata.encode("hex"))
    
    #Split into single byte strings
    hexList = list(split_by_n(editedData,2))
    print "List: "
    print hexList
    
    #Add spaces to each binary "word"
    convertedText = " ".join(hexList)
    print "Hex Spaced String: "
    print convertedText
  elif(convertCase == "Hex Single Column"):
    #Convert the text output to hexadecimal format letters
    editedData = str(filedata.encode("hex"))
    
    #Split into single byte strings
    hexList = list(split_by_n(editedData,2))
    print "List: "
    print hexList
    
    #Add spaces to each binary "word"
    convertedText = "\n".join(hexList)
    print "Hex Spaced String: "
    print convertedText
  elif(convertCase == "Binary Words"):
    #Convert the text from ascii to binary formatted letters
    binaryData = (bin(int(binascii.hexlify(filedata), 16)))
    print "Binary: " + binaryData

    #Trim the 0b starting characters
    editedData = binaryData.replace("0b", "")
    #print "Trimmed Binary: " + (editedData)
    
    #Skip trimming the data
    #editedData = binaryData
    
    #Split into single byte strings
    binaryList = list(split_by_n(editedData,8))
    print "List: "
    print binaryList

    #Add spaces to each binary "word"
    convertedText = " ".join(binaryList)
    print "Binary String: "
    print convertedText
  elif(convertCase == "Binary Single Column"):
    #Convert the text from ASCII to binary formatted letters
    binaryData = (bin(int(binascii.hexlify(filedata), 16)))
    print "Binary: " + binaryData

    #Trim the 0b starting characters
    editedData = binaryData.replace("0b", "")
    #print "Trimmed Binary: " + (editedData)
    
    #Skip trimming the data
    #editedData = binaryData
    
    #Split into single byte strings
    binaryList = list(split_by_n(editedData,1))
    print "List: "
    print binaryList

    #Add spaces to each binary "word"
    convertedText = "\n".join(binaryList)
    print "Binary Characters String: "
    print convertedText
  else:
    #Pass the text unmodified
    convertedText = filedata
  
  #String converted to UTF-8 Format
  u = unicode(convertedText, encoding)
  str_utf8 = u.encode("utf-8")
  
  #Save the converted text to a new UTF-8 text file
  file = open(savename, "w")
  
  #Write a Unicode Byte-Order Marker (BOM)
  #file.write( codecs.BOM_UTF8 )
  
  #Write out the converted data
  file.write(convertedText)
  file.close()
  
  print('Converting text file: \"' +  filename + '\" from ' + encoding + ' encoding, with the text case converion of: ' + convertCase)
  print('Saved as UTF encoded file: \"' + savename + '\"')

  
def split_by_n( seq, n ):
    """A generator to divide a sequence into chunks of n units."""
    while seq:
        yield seq[:n]
        seq = seq[n:]


