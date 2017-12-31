import os
import csv

output_file = os.path.join("finaloutput", "ElectionResults.txt")

input_files_dict = {}
candidates_list = []
vote_totals = []
candidate_summary = []
TotalVotes = 0
ask = "Y"
filenum = 0

print ("=======================================================================================================================================")
while ask == "Y" or ask == "y":
    filename = input("Enter the name of the file (with extension) containing the voting results; located in the 'finaloutput' folder:  ")
    input_files_dict ["emp"+str(filenum)+"_csv"] = filename
    filenum = filenum + 1
    ask = input("Your file ("+filename+") has been added.  Do you have another file? Y/N:  ")
print ("Your "+str(filenum)+" results file(s) are being aggregated - the results summary will print below.")
print ("The results summary has also been exported to ElectionResults.txt in the 'finaloutput' folder.")
print ("=======================================================================================================================================")

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
            TotalVotes = TotalVotes + 1
            if str(row[2]) in candidates_list:
                vote_totals[candidates_list.index(str(row[2]))] = int((vote_totals[candidates_list.index(str(row[2]))])+1)
            else:
                candidates_list.append(str(row[2]))
                vote_totals.append(int(1))
                candidate_summary.append("SUMMARY")

    counter = counter + 1
winner = str(candidates_list[0])
winnercount = int(vote_totals[0])

print ("============================")
print ("  ELECTION RESULTS SUMMARY")
print ("----------------------------")
print ("    Total Votes: " + str(TotalVotes))
print ("----------------------------")

with open(output_file, 'a') as resultssummary:
    resultssummary.write("============================\n")
    resultssummary.write("  ELECTION RESULTS SUMMARY\n")
    resultssummary.write("----------------------------\n")
    resultssummary.write("    Total Votes: " + str(TotalVotes)+"\n")
    resultssummary.write("----------------------------\n")

i = 0
while i < len(candidate_summary):
    candidate_summary[i] = str(str(candidates_list[i]) + ": " + str(round(float((vote_totals[i]/TotalVotes)*100),1)) + "% (" + str(vote_totals[i]) + ")")
    print("   "+candidate_summary[i])
    with open(output_file, 'a') as resultssummary:
        resultssummary.write("   "+candidate_summary[i]+"\n")
    if vote_totals[i] > winnercount:
        winner = candidates_list[i]
        winnercount = vote_totals[i]
    i += 1

print ("----------------------------")
print ("       Winner: " + str(winner))
print ("============================")

with open(output_file, 'a') as resultssummary:
    resultssummary.write("----------------------------\n")
    resultssummary.write("       Winner: " + str(winner)+"\n")
    resultssummary.write("============================")
    