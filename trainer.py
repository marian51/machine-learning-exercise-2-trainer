import argparse
import fileinput
import sys

# wywolanie 
# python $trainer -t train_set.txt -i data_in.txt -o data_out.txt < description_in.txt > description_out.txt

parser = argparse.ArgumentParser(description="Lets go")
parser.add_argument("-t", '--train_set', type=argparse.FileType('r'), help="Filename or path to file with train data")
parser.add_argument("-i", '--data_in', type=argparse.FileType('r'), help="Filename or path to file with max number of iterations")
parser.add_argument("-o", '--data_out', help="Filename or path to file to save output data")
args = vars(parser.parse_args())

# odczytanie pliku description.txt
description_in = sys.stdin.read()

# przerobienie pliku description na tablice dwuwym
description_in = description_in.split('\n')
for i in range(len(description_in)):
    description_in[i] = description_in[i].split()
    description_in[i].insert(0,1)

# odczytanie pliku train_set
train_set = args['train_set'].readlines()

# przetworzenie danych pliku train_set do tablicy tablic kazdego wiersza
for i in range(len(train_set)):
    train_set[i] = train_set[i].rstrip()
    train_set[i] = train_set[i].split()

N = len(train_set)

# odczytanie pliku data_in
data_in = args['data_in'].readlines()

# wyciangniecie liczby iteracji z pliku
max_iterations = int(data_in[0][11:].rstrip()) # liczba iteracji programu

# zapis do pliku data_out
with open(args['data_out'], 'w') as file:
    text = str(200) + '\n'
    file.write(text)

# wysylanie wynikow do pliku description_out.txt
print('description out')
print(N)