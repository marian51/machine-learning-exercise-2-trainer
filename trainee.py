import argparse
import fileinput
import sys

parser = argparse.ArgumentParser(description="Do")
parser.add_argument('-d', '--description')
args = parser.parse_args()

#print("dziala")
#print(args.description)

array = []

for line in fileinput.input(files =args.description):
    line = line.rstrip()
    line = line.split()
    array.append(line)


#odczytanie pliku in.txt
file_in = sys.stdin.read()
#przerobienie na tablice dwuwymiarowa
file_in = file_in.split('\n')

for i in range(len(file_in)):
    file_in[i] = file_in[i].split()
    file_in[i].insert(0,1)
   
#print(file_in) # tablica tablic
#print(array)
result = 0
equation = 0

dimension = int(array[0][1])
#print(dimension)
#print("n petla")

for k in range(len(file_in)-1):
    equation = file_in[k]
    result = 0
    for i in range(1, len(array)):
        line = array[i]
        factor = float(line[-1])
        inner_result = factor
        #print("\n",factor)
        for j in range(dimension):
	        inner_result *=  float(equation[int(line[j])])
		
        #print(inner_result)
        result += inner_result
	
    print(result)

