# Lesson 4: Assignments | Regex
# 1. Python Regular Expressions Mastery
# Task 1:
import re

names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", "Connor Milliken", "Jordan Alexander Williams", "Madonna", "programming is cool"]

def validate_names(names):
    pattern = re.compile(r"^([A-Z][a-z]+) ([A-z]*)?\s?([A-Z][a-z]+)")
    for name in names:
        if re.match (pattern, name):
            print(name)
        else:
            print("Invalid Name")

validate_names(names)


