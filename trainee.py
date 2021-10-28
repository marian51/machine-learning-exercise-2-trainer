import argparse
import fileinput
import sys

#parsowanie argumentow
parser = argparse.ArgumentParser(description="Do")
parser.add_argument('-d', '--description')
args = parser.parse_args()

array = [] # tablica na dane z pliku description

# przerobienie danych z pliku na tablice dwuwymiarowa
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
   
result = 0 # koncowy wynik danego rownania
equation = 0 # wartosc podstawiana pod dany x

dimension = int(array[0][1]) # stopien wielomianu

# glowna czesc programu 
for k in range(len(file_in)-1): # petla iterujaca po wierszach in.txt
    equation = file_in[k] # stopien danego wielomianu
    result = 0 # wyzerowanie koncowego wyniku przed przejsciem do nastepnej iteracji
    for i in range(1, len(array)): # petla iterujaca po skladnikach sumy (koncowego wyniku); od 1, bo 1 wiersz description to inne dane niz reszta
        line = array[i] # dany wiersz pliku description
        factor = float(line[-1]) # wspolczynnik (ostatni element wiersza)
        inner_result = factor  # wynik danego skladnika sumy
        for j in range(dimension): # petla iterujaca po danym elemencie sumy; przemnaza wspolczynnik przez dane wartosci danych x
	        inner_result *=  float(equation[int(line[j])])
		
        result += inner_result # sumowanie skladnikow wielomianu
	
    print(result) # zwrocenie koncowego elementu

