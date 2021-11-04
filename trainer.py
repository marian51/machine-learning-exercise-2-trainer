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
max_iterations = int(data_in[0][11:].rstrip()) # liczba iteracji programu

# zapis do pliku data_out
with open(args['data_out'], 'w') as file:
    text = str(200) + '\n'
    file.write(text)

# wysylanie wynikow do pliku description_out.txt
print('description out')

def calculate_y(x, p): # p to tablica
    result = 0
    for j in range(1, len(p)):
        result += float(x[int(p[j][0])]) * float(p[j][1])
    return result

p_0 = [1,1] # TODO wpisane na sztywno, trzeba pozniej zrobic dynamicznie
p_t = [1,1]
m=1
b=1

m_prev = 1000
b_prev = 1000

z=0

learning_rate = 0.01
# zalozenia
for i in range(1000): # petla przechodzaca przez interacje # TODO warunek stopu
    #p_t_i = []
    #for k in range(1, len(description_in)): # petla przechodzaca po wspolczynnikach p
    #    sum = 0
    #    for j in range(N): # petla przechodzaca przez wszystkie punkty
    #        sum += (calculate_y(train_set[j],description_in) - float(train_set[j][2])) * float(train_set[j][int(description_in[k][0])])
    #    sum = sum / N
    #    description_in[k][1] = float(description_in[k][1]) - sum
    #    p_t_i.append(sum)
    #print(p_t_i)
    #p_t = [a_i - b_i for a_i, b_i in zip(p_t,p_t_i)]
    # odjecie wektorow p
    sum_1 = 0
    sum_0 = 0
    for j in range (N):
        x = float(train_set[j][1])
        y = float(train_set[j][2])
        sum_0 += (m*x + b) - y
        sum_1 += x*((m*x + b) - y)
    sum_1 = sum_1 / N
    sum_0 = sum_0 / N
    if (abs(m_prev - m) < 0.001) and (abs(b_prev - b) < 0.001):
        break
    m_prev = m
    b_prev = b
    m = m - (learning_rate * sum_1)
    b = b - (learning_rate * sum_0)

    z = z+1

print(m,b)
print(z)
