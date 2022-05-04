filename1 = "topic5_1.txt"
filename2 = "topic5_1_out.txt"

infile = open(filename1, "r")
outfile = open(filename2, "w")
line = infile.readline()
while line != "":
    sum = 0
    num_strings = line.rstrip().split(",")
    for num_str in num_strings:
        sum+=float(num_str)
    outfile.write(f"{sum:.2f}\n")
    line = infile.readline()
infile.close()
outfile.close()