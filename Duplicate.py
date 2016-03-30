import json
import os, sys

inputDir='ab-duplicates100-2016-03-02/'
fileCount = 0
fname_MBID = ""
fname_List = [] # List of file names
path_Array = [] # List of full paths of the duplicates of a given song

#dataDetails={}
#dataDetails[cname][sname] ={'number':'0','feature':fDict}
#[u'lowlevel', u'tonal', u'rhythm', u'metadata']
# fDict['lowlevel'].keys()
# fDict['tonal']['key_key']
# fDict['tonal']['key_scale']

def json_Read(path_Array):
	song_Key = "" 
	for n in path_Array:
		fDict = json.load(open((str(n))))
		song_Key = str(fDict['tonal']['key_key']) + str(fDict['tonal']['key_scale'])
		#print song_Key
	return

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

				print (len(path_Array))
				if (len(path_Array) >= 3 and (fname_List [-1] == fname_List[-2])):
					#call new function to deal with JSON files
					json_Read(path_Array)
					#print "Same file as previous"	
					path_Array.append(str(path) + "/" + str(fname))

				elif (len(path_Array) >= 3 and (fname_List [-1] != fname_List [-2])):
					print "New file"

				#--- call new function for JSON file opening here ---

					path_Array = []
					path_Array.append(str(path) + "/" + str(fname))
					#print path_Array # one element
				elif (len(path_Array) <= 2):
					path_Array.append(str(path) + "/" + str(fname))
					#print path_Array #two and three elements

file_trav(inputDir)
print str(fileCount) + " -->  File Count"
