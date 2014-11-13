import random

with open('/usr/share/dict/words', 'r') as words_list:
    with open('sevenLetters+.txt', 'w') as new_list:   
        for line in words_list:
            line = line[:-1]
            if "\'" not in line:
                if len(line) >= 7:
                    print(line, file=new_list)
                

with open('sevenLetters+.txt') as myfile:
    count = sum(1 for line in myfile if line.rstrip('\n'))
    print(count)

number = random.randint(0, count)
print(number)






    
    


   
        
