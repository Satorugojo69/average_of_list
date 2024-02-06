fh = open('output.txt','w')

list = [10, 8, 1, 4, 5, 9, 7, 7, 9, 1]
sum = 0

for i in list:
    sum += i

fh.write("The Average of the list element is : " + str( sum / len(list))+'\n')

fh.close