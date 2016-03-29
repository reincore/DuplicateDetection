import json
import os, sys

inputDir='ab-duplicates100-2016-03-02/'
fileCount = 0
fname_MBID = ""
fname_List = [] # List of fnames of songs and duplicates
path_Array = [] # List of full paths of the duplicates of a given song

#fDict = json.load(open(str('ab-duplicates1000-2016-03-02/00/00c47ea6-3a10-4a32-b1f1-990ac756c6a0-0.json')))
#dataDetails={}
#dataDetails[cname][sname] ={'number':'0','feature':fDict}
#[u'lowlevel', u'tonal', u'rhythm', u'metadata']
# fDict['lowlevel'].keys()
# fDict['tonal']['key_key']
# fDict['tonal']['key_scale']

def file_trav(inputDir):
	#print inputDir
	for path,dname,fnames in os.walk(inputDir):
		for fname in fnames:
			global fileCount, path_Array
			fileCount += 1
			#print fname
			global fname_MBID
			fname_MBID = fname[0:36] #first 36 characters of fname, without duplicate number
			#print (fname_MBID)  + (" --> MBID")
			fname_List.append(fname_MBID)

			if '.json' in fname.lower():
				last_Dash_Index = fname.rfind('-', 0, 10) #Find the index of last dash
				last_Dot_Index = fname.rfind('.', 0, 10) #Find the index of last dot
				root_Name = fname[37:(len(fname)-last_Dot_Index)]
				root_Name = root_Name[:-5]
				#print(root_Name) + " ---> Root Name" #The root part of the file name without duplicate number and .json part.

				if (len(fname_List) >> 2) and (fname_List [-1] == fname_List [-2]):
					#call new function to deal with JSON files
					print "Same file as previous"	
					path_Array.append(str(path) + "/" + str(fname))

				elif (len(fname_List) >> 2 and fname_List [-1] != fname_List [-2]):
					print "New file"

				#call function
				#clear array
				#append current path
				elif (len(fname_List) << 3):
					path_Array.append(str(path) + "/" + str(fname))
					print path_Array

file_trav(inputDir)
print str(fileCount) + " -->  File Count"
