#Write a program that reads the microarray data in “data.csv” and computes
#the mean and standard deviation of the expression values of a specific gene
#overall, and within each sample category.
#   Get the name of the microarray datafile from the command-line.
#   Get the name of the gene from the command-line.

# will need sqr root for hw
# everything in dictionary will be string, must change it to something else
# dont use statistics module
# implement std dev and mean directly

import csv
import sys
import math
datacsv = sys.argv[1]
gene = sys.argv[2]

f = open('data.csv')
# read csv
rows = csv.DictReader(f) #no headers

#expression values overall and expression values within sample category 1 or 2
expression_values = []
sample_category = {1:[], 2:[]}

for row in rows:                                     #iterate through rows
    if gene in row:                                  #checks if gene is key in row
        value = float(row[gene])                     #gets gene, converts it to do math with later
        expression_values.append(value)              #add to expression_values of gene list
        category = int(row['TUMOUR'])                #gets values from TUMOUR column, converts from str to int

        if category in sample_category:              #checks if category is either 1 or 2 in sample_category
            sample_category[category].append(value)  #adds value to respective list in sample_category
f.close()

#calc mean
def means(data):
    return sum(data)/len(data)      #return mean

#calc std devs 
def std_dev(data):
    mean = means(data)                                        #calc mean
    variance = sum((x - mean) ** 2 for x in data) / len(data) #calc variance
    return math.sqrt(variance)                                #return std dev

#overall mean and std dev
overall_mean = means(expression_values)
overall_stddev = std_dev(expression_values)
print('Overall Gene Mean:',overall_mean)
print('Overall Gene Std Dev:',overall_stddev)

#mean and std dev within each sample category
for category, values in sample_category.items():
    category_mean = means(values)
    category_stddev = std_dev(values)   
    print('Sample Category',category,'Mean:',category_mean)
    print('Sample Category',category,'Std Dev:',category_stddev)
