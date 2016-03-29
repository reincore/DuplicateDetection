import json
import os, sys

inputDir='ab-duplicates100-2016-03-02/'
fileCount = 0
fname_MBID = ""
fname_array = []
fname_List = []

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
			global fileCount
			fileCount += 1
			print fname

			global fname_MBID
			fname_MBID = fname[0:36] #first 36 characters of fname, without duplicate number
			print (fname_MBID)  + (" --> MBID")
			fname_List.append(fname_MBID)

			if '.json' in fname.lower():
				last_Dash_Index = fname.rfind('-', 0, 10) #Find the index of last dash
				last_Dot_Index = fname.rfind('.', 0, 10) #Find the index of last dot
				root_Name = fname[37:(len(fname)-last_Dot_Index)]
				root_Name = root_Name[:-5]
				#root_Name = fname[:len(fname)-last_Dash_Index+1]
				print(root_Name) + " ---> Root Name" #The root part of the file name without duplicate number and .json part.

				if (len(fname_List) >> 2) and (fname_List [-1] == fname_List [-2]):
					#call new function to deal with JSON files
					print "Same file as previous"				

				elif (len(fname_List) >> 2 and fname_List [-1] != fname_List [-2]):
					print "New file"
				
				# add another else if to check for 3 digits of duplicate number. Right now it only checks the case for 2 digits of duplicate number.				

file_trav(inputDir)
print str(fileCount) + " -->  File Count"
