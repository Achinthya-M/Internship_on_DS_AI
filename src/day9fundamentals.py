# -*- coding: utf-8 -*-
#task 1
import pandas as pd
products = pd.Series([700, 150, 300],index=['Laptop', 'Mouse', 'Keyboard'])
print("Full Product List:")
print(products)
print("\nPrice of Laptop:")
print(products['Laptop'])
print("\nFirst Two Products:")
print(products.iloc[0:2])

#task 2
import pandas as pd
grades = pd.Series([85, None, 92, 45, None, 78, 55])
print("Original Grades:")
print(grades)
print("\nMissing Values (True means missing):")
print(grades.isnull())
filled_grades = grades.fillna(0)
print("\nGrades After Filling Missing Values:")
print(filled_grades)
filtered_grades = filled_grades[filled_grades > 60]
print("\nScores Greater Than 60:")
print(filtered_grades)

#task 3
import pandas as pd
usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])
print("Original Usernames:")
print(usernames)
cleaned_usernames = usernames.str.strip().str.lower()
print("\nCleaned Usernames:")
print(cleaned_usernames)
contains_a = cleaned_usernames.str.contains('a')
print("\nNames Containing 'a':")
print(contains_a)

import pandas as pd
s1 = pd.Series([10, 20, 30, 40])
s2 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s1)
print(s2)

marks = pd.Series([85, 90, 78], index=['Math', 'Physics', 'Chemistry'])
print(marks['Math'])
print(marks[['Math', 'Chemistry']])

scores = pd.Series([45, 67, 89, 34, 90])
passed = scores[scores > 60]
print(passed)

data = pd.Series([10, None, 30, None])
print(data.isnull())
print(data.fillna(4))

names = pd.Series(['Alice', 'bob', 'CHARLIE'])
print(names.str.lower())
print(names.str.contains('a'))
print(names.str.startswith('A'))



























