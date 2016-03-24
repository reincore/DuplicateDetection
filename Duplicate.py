import json
import os, sys

inputDir='ab-duplicates100-2016-03-02/'
i = 0
fname_array = []
fname_List = []

#fDict = json.load(open(str('ab-duplicates1000-2016-03-02/00/00c47ea6-3a10-4a32-b1f1-990ac756c6a0-0.json')))

#dataDetails={}
#dataDetails[cname][sname] ={'number':'0','feature':fDict}

#[u'lowlevel', u'tonal', u'rhythm', u'metadata']

# fDict['lowlevel'].keys()

# fDict['tonal']['key_key']
#fDict['tonal']['key_scale']


# def file_trav(inputDir):

# 	print inputDir

#     for path,dname,fnames in os.walk(inputDir):

#         for fname in fnames:
#             if '.json' in fname.lower():
#                 remain, rname, cname, sname = path.split('/')[:-3], path.split('/')[-3], path.split('/')[-2], path.split('/')[-1]
#                       #MainFile,instrum,sound
#                 #ComputeAndWriteExtractor(rname,cname,sname,fname)

#                 print remain,rname,cname,sname

def file_trav(inputDir):
	#print inputDir
	for path,dname,fnames in os.walk(inputDir):

		#print fnames
		#print '\n' 
		for fname in fnames:
			global i
			i += 1
			print fname
			fname_List.append(fname)
			#print path
			#print dname
			if '.json' in fname.lower():
				last_Dash_Index = fname.rfind('-', 0, 10) #Find the index of last dash
				#print(last_Dash_Index, len(fname))
				root_Name = fname[:len(fname)-last_Dash_Index+1]
				#print(root_Name)  #The root part of the file name without duplicate number and .json part.
				if (root_Name[-1] == '-'):
					root_Name = root_Name[:len(root_Name)-1]
					print root_Name
				# add another else if to check for 3 digits of duplicate number. Right now it only checks the case for 2 digits of duplicate number.				

				else: 
					print root_Name
				print i
				
				#fname_base = fname_base.substr				
				#fname_array = []
				
				
				#remain, rname, cname, sname = path.split('/')[:-3], path.split('/')[-3], path.split('/')[-2], path.split('/')[-1]
				#print remain,rname,cname,sname

file_trav(inputDir)
