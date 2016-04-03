import json
import os, sys
import pandas as pd #http://pandas.pydata.org/

inputDir='ab-duplicates1000-2016-03-02/' # This is the input directory. This .py file should be in the same directory with this folder.
fileCount = 0 #Initial file count
fname_MBID = "" #Initial MusicBrainz ID name
fname_List = [] # List of file names
path_Array = [] # List of full paths of the duplicates of a given song
ultimate_Key = [[0],[0],[0],[0],[0],[0]] # MBID, #1 Most Used Key, Rate of 1st, #2 Most Used Key, Rate of 2nd,Total # Duplicates

def json_Read(path_Array):
	song_Key = "" 
	key_Array = [[],[]]
	for n in path_Array:
		fDict = json.load(open((str(n))))
		song_Key = str(fDict['tonal']['key_key']) + str(fDict['tonal']['key_scale'])

		try:
			index = key_Array[0].index(song_Key)
			key_Array[1][index] = key_Array[1][index]+1

		except:
			key_Array[0].append(song_Key)
			index = key_Array[0].index(song_Key)
			key_Array[1].append(1)

	
	total_Songs = sum(key_Array[1]) # Total number of songs
	most_Key_Index = key_Array[1].index(max(key_Array[1])) # Index of the most frequent key
	rate = float(key_Array[1][most_Key_Index])/total_Songs*100 # Rate of the first most frequent key



	ultimate_Key[0].append(fname_MBID)
	ultimate_Key[1].append(key_Array[0][most_Key_Index])
	ultimate_Key[2].append(rate)


	key_Array[0].remove(key_Array[0][most_Key_Index]) # Remove the Max Key Name
	key_Array[1].remove(key_Array[1][most_Key_Index]) # Remove the Max Key Count

	try:
		most_Key_Index = key_Array[1].index(max(key_Array[1])) # Index of second most frequent key
		rate = float(key_Array[1][most_Key_Index])/total_Songs*100 # Rate of the second most frequent key

		ultimate_Key[3].append(key_Array[0][most_Key_Index])
		ultimate_Key[4].append(rate)

	except:
		ultimate_Key[3].append("Nan")
		ultimate_Key[4].append("Nan")


	ultimate_Key[5].append(total_Songs)		

	print (fname_MBID) + ' Processed!'
	

def file_trav(inputDir):
	for path,dname,fnames in os.walk(inputDir):
		for fname in fnames:
			if '.json' in fname.lower():
				global fileCount, path_Array
				fileCount += 1
				global fname_MBID
				fname_MBID = fname[0:36] #first 36 characters of fname, without duplicate number
				fname_List.append(fname_MBID)
				 
				if (len(path_Array) >= 3 and (fname_List [-1] == fname_List[-2])): # "Same file as previous"	
					path_Array.append(str(path) + "/" + str(fname))

				elif (len(path_Array) >= 3 and (fname_List [-1] != fname_List [-2])): # "New file"
				#--- call new function for JSON file opening here ---
					json_Read(path_Array)
					path_Array = []
					path_Array.append(str(path) + "/" + str(fname))
					
				elif (len(path_Array) <= 2):
					path_Array.append(str(path) + "/" + str(fname))

file_trav(inputDir)
df = pd.DataFrame()

# Assign the values to relevant cells to write the csv file.
df['MBID'] = ultimate_Key[0]
df['#1 Most Used Key'] = ultimate_Key[1]
df['Rate of 1st'] = ultimate_Key[2]
df['#2 Most Used Key'] = ultimate_Key[3]
df['Rate of 2nd'] = ultimate_Key[4]
df['Total # Duplicates'] = ultimate_Key[5]

df = df.ix[1:] # Delete the First Row as they were 0's

df.to_csv('Key.csv') # Write the file to 'Key.csv' file, to the same directory as this python code is.

print str(fileCount) + " -->  File Count" # Show total file count in the terminal, after writing the .csv file.
