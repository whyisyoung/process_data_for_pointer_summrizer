import getopt
import sys
import json
import hashlib
import os

def hashhex(s):
  """Returns a heximal formated SHA1 hash of the input string."""
  h = hashlib.sha1()
  h.update(s)
  return h.hexdigest()

def processJSON(jsonFile,outputDir):
    #FILE = open(jsonFile,'r')
    
    #lines = FILE.readlines()
    
    #data = json.load(lines[0])
    
    #with open(jsonFile) as f:
    #    data = json.load(f)

#   url_dir = "url_lists"

    if not os.path.exists(outputDir): os.makedirs(outputDir)
    
    URL_FILE = open('all_urls.txt','w')
    
    lines = []
    for line in open(jsonFile,'r'):
        lines.append(json.loads(line))
    
    #at this point each line is a json dictionary for each entry in the json file
    
    #import pdb
    #pdb.set_trace()

    for line in lines:
        
        url = line['URL']
        #url = line['URL_s']
        sentences = line['Sentences']
        #sentences = line['Sentences_t']

        #print url
        
        h = hashhex(url)
        #print h
        
        fileName = outputDir + '/' + h+'.story'
        FILE = open(fileName,'w')
        FILE.write(sentences)
        FILE.close()

        URL_FILE.write(url + '\n')
        
    URL_FILE.close()

if __name__ == '__main__':
        
	print (sys.argv)
	print
	
	try:
	   #opts, args = getopt.getopt(sys.argv,"hi:o:",["ifile=","ofile="])
	   opts, args = getopt.getopt(sys.argv[1:],"f:h:o:")
	except getopt.GetoptError:
		
		print ("opts:")
		print (opts)
		
		print ('\n')
		print ("args:")
		print (args)
		
		print ("Incorrect usage of command line: ")
		print ("python html_parser.py -d <root directory name> -r <remove flag: True or False>")
		print ('python html_parser.py -f <file name> -o <output directory> -r <remove flag: True or False>')
	   
	  
	   
		sys.exit(2)
	   
	#initialize cmd line variables with default calues
	jsonFile = None
	outputDir = None

	
	for opt, arg in opts:
		print (opt,'\t',arg)
		if opt == '-h':
		   print ('python html_parser.py -d <root directory name> -r <remove flag: True or False>')
		   print ('python html_parser.py -f <file name> -o <output directory>  -r <remove flag: True or False>')
		   sys.exit()
		#set insertion flag, i.e., action to perform is inserting a pattern into a DB
		elif opt in ("-f"):
		   jsonFile = arg
		elif opt in ("-o"):
			outputDir = arg
        

           
	print('\n')
	print("JSON file:",jsonFile)
	print("Output directory:", outputDir)
	print('\n')
    
	processJSON(jsonFile,outputDir)
