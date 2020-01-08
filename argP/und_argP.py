#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import argparse
#the package

#construct argument parser and construct arguments
ap = argparse.ArgumentParser()
#instantiate the ArgumentParser object as ap
ap.add_argument("-n","--name",required=True,help="name of the user")
#duh kinda, shorthand and longhand notation with required or not para
#help gives help if you do "python3 file.py --help"
args = vars(ap.parse_args())
#to parse the command link arguments, letting library and python know
#vars is called on ap.parse_args() to turn parsed cmd arguments into
#dictionaty with key as name of cmd line arg

print("hi there {},its nice to meet you!".format(args["name"]))
