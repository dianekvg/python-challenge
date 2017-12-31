import os
import csv

output_file = os.path.join("finaloutput", "EmployeeData.csv")

EMPLID = ["Emp ID"]
FNAME = ["First Name"]
LNAME = ["Last Name"]
DOB = ["DOB"]
SSN = ["SSN"]
STATE = ["State"]

state_abbrev_dict = {'Alabama': 'AL','Alaska': 'AK','Arizona': 'AZ','Arkansas': 'AR','California': 'CA','Colorado': 'CO',
    'Connecticut': 'CT','Delaware': 'DE','Florida': 'FL','Georgia': 'GA','Hawaii': 'HI','Idaho': 'ID','Illinois': 'IL',
    'Indiana': 'IN','Iowa': 'IA','Kansas': 'KS','Kentucky': 'KY','Louisiana': 'LA','Maine': 'ME','Maryland': 'MD',
    'Massachusetts': 'MA','Michigan': 'MI','Minnesota': 'MN','Mississippi': 'MS','Missouri': 'MO','Montana': 'MT',
    'Nebraska': 'NE','Nevada': 'NV','New Hampshire': 'NH','New Jersey': 'NJ','New Mexico': 'NM','New York': 'NY',
    'North Carolina': 'NC','North Dakota': 'ND','Ohio': 'OH','Oklahoma': 'OK','Oregon': 'OR','Pennsylvania': 'PA',
    'Rhode Island': 'RI','South Carolina': 'SC','South Dakota': 'SD','Tennessee': 'TN','Texas': 'TX','Utah': 'UT',
    'Vermont': 'VT','Virginia': 'VA','Washington': 'WA','West Virginia': 'WV','Wisconsin': 'WI','Wyoming': 'WY',}

input_files_dict = {}
ask = "Y"
filenum = 0

print ("===========================================================================================================================")
while ask == "Y" or ask == "y":
    filename = input("What is the name (with extension) of the file in the 'rawdata' folder that you would like to format?  ")
    input_files_dict ["emp"+str(filenum)+"_csv"] = filename
    filenum = filenum + 1
    ask = input("Your file ("+filename+") has been added.  Do you have another file that needs to be formatted? Y/N:  ")
print ("Your "+str(filenum)+" file(s) have been formatted and exported to EmployeeData.csv in the 'finaloutput' folder.")
print ("===========================================================================================================================")

counter = 0
filelist = [list(input_files_dict)]

while counter < filenum:
    filename = (list(input_files_dict)[counter])
    for key, value in input_files_dict.items():
        if key == filename:
            fileref = value
    filename = os.path.join("rawdata",fileref)
   
    with open(filename, newline="") as csvfile:

        csv_reader = csv.reader(csvfile,delimiter=",")
        header = next(csv_reader)
    
        for row in csv_reader:
            EMPLID.append(row[0])
            FNAME.append((row[1][0:(row[1].index(" "))]).strip())
            LNAME.append((row[1][(row[1].index(" ")):]).strip())
            DOB.append((row[2][5:7]) +"/"+(row[2][8:10])+"/"+(row[2][0:4]))
            SSN.append(("###-##-")+(row[3][7:])) 
            STATE.append(list(state_abbrev_dict.values())[list(state_abbrev_dict.keys()).index(row[4])])

    counter = counter + 1

cleaned_csv = zip(EMPLID,FNAME,LNAME,DOB,SSN,STATE)
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerows(cleaned_csv)
    