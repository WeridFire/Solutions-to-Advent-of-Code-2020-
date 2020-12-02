total=0

with open('input.txt', 'r') as liner:
    while True:
        cur_line = liner.readline()
        if cur_line == '':
            break
        else:
            minor = cur_line.split('-')
            greater = minor[1].split(' ')
            letter = greater[1].split(':')
            password = greater[2].split('\n')

            cont = 0

            for i in password[0]:
                if i == letter[0]:
                    cont = cont +1
            


            if int(minor[0]) <= cont and cont <= int(greater[0]):
                total = total +1

print(total)

total=0

with open('input.txt', 'r') as liner:
    while True:
        cur_line = liner.readline()
        if cur_line == '':
            break
        else:
            minor = cur_line.split('-')
            greater = minor[1].split(' ')
            letter = greater[1].split(':')
            password = greater[2].split('\n')

            key = password[0]
            pos1 = int(minor[0])-1
            pos2 = int(greater[0])-1

            if (key[pos1]!=letter[0] and key[pos2]==letter[0])or(key[pos1]==letter[0] and key[pos2]!=letter[0]):
                total = total+1
                
                        

print(total)