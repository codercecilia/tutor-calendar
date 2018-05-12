# Date, Category, Sub-Category, Team Member, Start, End

import csv
import json
import os
import shutil
import sys, string


csvfile = open('Tutor Schedule Beta - Convert to CSV.csv', 'r')

fieldnames = ("title", "start", "end")
reader = csv.DictReader( csvfile, fieldnames)
readerList = list(reader)

def write_to_many_files(readerList):
    tutors = []
    for row in range(1, len(readerList)):
        name = str.split(readerList[row]["title"])[0]
        tutorfile = open(name + ".json", 'a')
        if name in tutors:
            tutorfile.write(',')
            json.dump(readerList[row], tutorfile, indent=1)
        else:
            tutorfile.write('[')
            tutors.append(name)
            json.dump(readerList[row], tutorfile, indent=1)
    return tutors

def write_last_bracket(tutors):
    for name in tutors:
        tutorfile = open(name+".json", 'a')
        tutorfile.write(']')

def delete_files(tutors):
    for name in tutors:
        os.remove(name+".json")
        os.remove(name+".html")

def create_html_calendars(tutors):
    for name in tutors:
        tutorfile = open(name+".html", 'w')
        shutil.copyfile('template.html', name+".html")
        tutorfile = open(name+".html", 'r')
        tutordata = tutorfile.read()
        tutordata = tutordata.replace("albert", name)
        tutorfile = open(name+".html", 'w')
        tutorfile.write(tutordata)
        tutorfile.close()

def create_index_html(tutors):
    indexList = ""
    for name in tutors:
        indexList = indexList +"<p><a href = \"" + name + ".html\">" + name + " </a></p>"
    indexfile = open("index_template.html", 'r')
    indexdata = indexfile.read()
    indexdata = indexdata.replace("<p><a href=\"albert.html\">Albert</a></p>", indexList)
    indexfile = open("index.html", 'w')
    indexfile.write(indexdata)
    indexfile.close()


# Create JSON files
tutors = write_to_many_files(readerList)
write_last_bracket(tutors)

#Create HTML templates
create_html_calendars(tutors)
create_index_html(tutors)

#Delete files
#delete_files(tutors)
