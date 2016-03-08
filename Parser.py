##########
# This file is a very simple .JSON parser to load datasets from a specified folder,
# reach the specified values and compare them. OS library is imported to be able to
# change directories with os.chdir(path) in the future. The dataset is provided by
# Alastair Porter and Dmitry Bogdanov as a part of the Audio Signal Processing Lab. 
# This project is a practical coursework, also related with the Acoustic Brainz.
#
# Deniz Saglam,
# Barcelona, 2016.
##########

import os
import json
from pprint import pprint

with open('.json') as data_file1: # data name comes here.
    data = json.load(data_file1)
pprint(data)

with open('.json') as data_file2: # second data name comes here.
    data2 = json.load(data_file2)
pprint(data2)

new_array1 = data["lowlevel"]["barkbands"]["mean"]
new_array2 = data2["lowlevel"]["barkbands"]["mean"]
new_array1 == new_array2 # if returns True, we have an exact duplicate
