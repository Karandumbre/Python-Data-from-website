#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 11:33:14 2018

@author: karan.ganesh.dumbre
"""

# import 
import requests    
from bs4 import BeautifulSoup 

# HTML String
html_string = """
<!doctype html>
<html lang="en">
<head>
  <title>Doing Data Science With Python</title>
</head>
<body>
  <h1 style="color:#F15B2A;">Doing Data Science With Python</h1>
  <p id="author">Author : Abhishek Kumar</p>
  <p id="description">This course will help you to perform various data science activities using python.</p>
  
  <h3 style="color:#404040">Modules</h3>
  <table id="module" style="width:100%">
      <tr>
        <th>Title</th>
        <th>Duration (In Minutes)</th> 
      </tr>
      <tr>
        <td>Getting Started</td>
        <td>20</td> 
      </tr>
      <tr>
        <td>Setting up the Environment</td>
        <td>40</td> 
      </tr>
      <tr>
        <td>Extracting Data</td>
        <td>35</td> 
      </tr>
      <tr>
        <td>Exploring and Processing Data - Part 1</td>
        <td>45</td> 
      </tr>
      <tr>
        <td>Exploring and Processing Data - Part 2</td>
        <td>45</td> 
      </tr>
      <tr>
        <td>Building Predictive Model</td>
        <td>30</td> 
      </tr>
  </table>
</body>
</html>
"""

# display HTML string in the juptyer notebook
from IPython.core.display import display, HTML
display(HTML(html_string))

# use beautiful soup 
ps = BeautifulSoup(html_string)

# print b
print(ps)


# use name parameter to select by tag name
body = ps.find(name="body")

# use text attribute to get the content of the tag
print(body.find(name="h1").text)

# get first element
print(body.find(name="p"))

# get all elements
print(body.findAll(name="p"))

# loop through each element
for p in body.findAll(name="p"):
    print(p.text)
    
# add attributes in the selection process
print(body.find(name='p', attrs={"id":"author"}))

print(body.find(name='p', attrs={"id":"description"}))

# body
body = ps.find(name="body")
# module table
module_table = body.find(name='table', attrs={"id": "module"})
# iterate through each row in the table (skipping the first row)
for row in module_table.findAll(name='tr')[1:]:
    # module title
    title = row.findAll(name='td')[0].text
    # module duration
    duration = int(row.findAll(name='td')[1].text)
    print(title,duration)