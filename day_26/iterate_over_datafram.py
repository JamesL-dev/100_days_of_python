student_dict = {
    "student": ["Angela", "James", "Lily"],
    "Score": [56, 76, 98]
}

#for (key, value) in student_dict.items():
#    print(key)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
#print(student_data_frame)

# loop through data frame
#for (key, value) in student_data_frame.items():
#    print(value)

# loop through rows of a dataframe

for (index, row) in student_data_frame.iterrows():
    print(row.Score)
