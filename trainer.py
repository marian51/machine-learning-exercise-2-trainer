import argparse
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

description_in.pop() # usuniecie tego ostatniego pustego elementu

# odczytanie pliku train_set
train_set = args['train_set'].readlines()

# przetworzenie danych pliku train_set do tablicy tablic kazdego wiersza
for i in range(len(train_set)):
    train_set[i] = train_set[i].rstrip()
    train_set[i] = train_set[i].split()
    train_set[i].insert(0,1)

N = len(train_set)
# odczytanie pliku data_in
data_in = args['data_in'].readlines()

# wyciangniecie liczby iteracji z pliku
#max_iterations = int(data_in[0][11:].rstrip()) # liczba iteracji programu
max_iterations = int(data_in[0].split("=")[1])
# nowe zmienne potrzebne do przerobienia algorytmu
n = len(description_in)-1 # wymiarowosc danego wielomianu
gradients = [0] * n # tablica na sum_1, sum_0 itp
p_factors_prev = []
for g in range(n):
    p_factors_prev.append(float(description_in[g+1][1]))

learning_rate = 0.001
epsilon = 0.001

def calculate_f(x, p):
    result = 0
    for k in range(1, len(p)-1):
        factor_p = float(p[k][1])
        factor_p_x = int(p[k][0])
        result += float(x[factor_p_x]) * factor_p
    result += float(p[-1][1])
    return result

def save_description_out(results):
    for line in results:
        print(str(line[0]) + ' ' + str(line[1]))

def save_output_txt(z):
    # zapis do pliku data_out
    with open(args['data_out'], 'w') as file:
        text = str(z) + "\n"
        file.write("iterations=" + text) 

z = 0
stop = 0
for i in range(max_iterations): # petla przechodzaca przez interacje # TODO warunek stopu
    stop = 0
    gradients = [0] * n # wyzerowanie, zeby na poczaktu kazdej iteracji bylo puste
    for p in range(n): # petla do przechodzenia po pochodnych
        p_factors_prev[n-p-1] = float(description_in[n-p][1])
        for j in range (N):
            x = train_set[j][:-1]
            y = float(train_set[j][-1])
            gradients[p] += (calculate_f(x, description_in) - y) * float(train_set[j][int(description_in[n-p][0])])
        gradients[p] = gradients[p] / N
        description_in[n-p][1] = float(description_in[n-p][1]) - (learning_rate * gradients[p])
    
    # warunek stopu
    for p in range(n):
        if(abs(float(description_in[n-p][1]) - p_factors_prev[n-p-1]) < epsilon):
            stop = stop + 1

    if (stop == n):
        break

    z += 1


save_description_out(description_in)
# zapis do pliku data_out 
save_output_txt(z)

