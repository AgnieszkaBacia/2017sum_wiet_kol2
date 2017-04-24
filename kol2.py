# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.
#
#Additional:
#1. 1 Class + Print show me what you got
#2. All data should be in dict
#3. Use optparse or argparse
#4. python module.py -h /arg1/file
#5. store data as json dump + pass path to json file in argument

#sample command to run this file: python kol2.py -f students_data.json

import json
from optparse import OptionParser
import numpy as np


class Diary(object):
    def __init__(self, path_to_dump):
        self.diary_file = path_to_dump
        self.list_of_students = []
        self.attendance_of_student = {}
        self.students_scores = {}
        self.subjects = []
        self.data_to_load = {}
        self.load_data(self.diary_file)

    def load_data(self, data):
        with open(data) as data:
            self.data_to_load = json.load(data)
        self.subjects = self.data_to_load["subject"]
        for student in self.data_to_load["student"]:
            self.attendance_of_student[student["name"]] = student["attendance"]
            self.list_of_students.append(student["name"])
            for subject in self.subjects:
                self.students_scores[student["name"], subject] = student[subject]

    def get_total_average_score(self):
        grades = []
        [[grades.extend(self.students_scores[student_name, subject]) for subject in self.subjects] for student_name in self.list_of_students]
        return np.mean(grades)

    def get_total_average_attendance(self):
        return np.mean(self.attendance_of_student.values())

    def get_student_total_average_score(self, student_name):
        scores = []
        [scores.extend(self.students_scores[student_name, subject]) for subject in self.subjects]
        return np.mean(scores)

    def get_student_subject_average_score(self, student_name, subject):
        return np.mean(self.students_scores[student_name, subject])
 


#print what you got section

    def print_students(self):
        print "Students list {}.".format(self.list_of_students)

    def print_student_attendance(self, student):
        print "{}s attendance is {}.".format(student, self.attendance_of_student[student])

    def print_total_average_score(self):
        print "Total average score is {}.".format(self.get_total_average_score())

    def print_total_average_attendance(self):
        print "Total average attendance is {}.".format(self.get_total_average_attendance())

    def print_student_average_score(self, student):
        print "{} has total average score of {}.".format(student, self.get_student_total_average_score(student))

    def print_student_subject_average_score(self, student, subject):
        print "{} has average score {} from {}.".format(student,self.get_student_subject_average_score(student, subject), subject)


if __name__ == "__main__":
#source taken from https://docs.python.org/2/library/optparse.html
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename",
                      help="write report to FILE", metavar="FILE")
    (options, args) = parser.parse_args()

    diary1A = Diary(options.filename)

    diary1A.print_students()
    diary1A.print_student_attendance("Iron Man")
    diary1A.print_total_average_score()
    diary1A.print_total_average_attendance()
    diary1A.print_student_average_score("Captain America")
    diary1A.print_student_subject_average_score("Incredible Hulk", "Math")
