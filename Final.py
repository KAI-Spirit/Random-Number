import random

def gen_digit():
    digit = random.randint(0,9)
    #print(digit)
    return digit

#gen_digit()

def gen_numlist():
    gen_num=[]
    for i in range(4):
        digit = gen_digit()
        gen_num.append(digit)
    return gen_num

#print(gen_numlist())

def TF(seq1):
    check = False
    while check ==False:
        if (len(seq1) == 4 and seq1.isdigit()):
            check = True
            return True
        else:
            check = False
            
            return False
'''     
seq = input("Enter a four digit number ")        
while TF(seq) == False:
    seq = input("Enter a four digit number ")        
print(TF(seq))
'''
def recieve(string):
    check = False
    t = 0
    numlist=[]    
    while check ==False:
        0
        if TF(string)== True:
        #(len(string) == 4 and string.isdigit()):
            #print("good")
            check = True
        else:
            string = input("Please enter a four digit number ")           
    #Won't let you progress unless you enter a four digit number
    for pos in range(len(string)):
        numlist.append(int(string[pos]))   
    #print(string)
    return numlist
'''
chars = input("Enter 4 numbers ")
print(recieve(chars))
'''
def guess(x,y):
    list1=[]
    list2=[]
    Flist =[]
    
    for pos in range(len(x)) :
        list1.append(int(x[pos]))
    for pos in range(len(y)) :
        list2.append(int(y[pos]))
    #print(list1)
   # print(list2)
    for c in range(4):
        if list1[c]==list2[c]:
            Flist.append("Y")
        else:
            Flist.append("N")
    #print(Flist)
    return Flist
'''
seq1 = input("Enter 4 numbers ")
seq2 = input("Enter another 4 number ")
print(guess(seq1,seq2))
'''
def check_char(t,k):
    
    char_list =[]
    Y_list = ["Y","Y","Y","Y"]
    comp_list=[]
    right = False
    
    for pos in range(len(t)) :
        char_list.append(t[pos])
    #print(char_list)

    for pos in t :
        char_list.remove(pos)
        char_list.append(pos.upper())
    #print(char_list)
        
    for pos in range(len(t)):
        if char_list[pos] ==Y_list[pos]:
            comp_list.append("Y")
        else:
            comp_list.append("N")
    #print(comp_list)

    for pos in range(len(t)):
        if comp_list[pos] == Y_list[pos]:
            right = True
        else:
            right = False
    print(right)
    
    return comp_list
'''    
print(check_char("yhyt"))
'''
v = 0
while ((v != 1) or (v!= 2)):
    v = int(input("Which version would you like to play "))

    if v == 1 :
    #THIS IS VERSION 1 OF THE PROGRAM
        count = 0
        gen_num =[]
        attempt =[]
        is_right = False

        gen_num = gen_numlist()
        #print(gen_num)

        while ((is_right == False) and (count < 10)):
            count = count + 1
            user = input("Guess the 4 digit number ")
            print(count)
            
            for c in range(4):
                for pos in attempt:
                    attempt.remove(pos)
            #print(attempt)
                    
            print("Your guess was",recieve(user))
            print(guess(user,gen_num))
            
            for pos in range(4):
                attempt.append(int(user[pos]))
            #print(attempt)
            
            if attempt[pos] == gen_num[pos]:
                is_right = True
            else:
                is_right = False
            if is_right == False:
                print("Sorry your guess was wrong")
                        
        if is_right == True:
            print("You won")
        else:
            print("You ran out of attempts, GAME OVER") 


    

    elif v == 2:
        #THIS IS VERSION 2 OF THE PROGRAM
        use_list =[]
        gen_list = []
        compare_list=[]
        correct = False
        counter = 0
            
        gen_list = gen_numlist()
        #print(gen_list)

        while ((correct == False) and (counter < 10)):
            counter = counter + 1
            print(counter)
            num=input("Enter 4 numbers ")
            
            for pos in range(4):
                for pos in compare_list:
                    compare_list.remove(pos)
            #print(compare_list)
            for pos in range(4):
                for pos in use_list:
                    use_list.remove(pos)
            #print(use_list)

            print("Your guess was",recieve(num))
            
            for pos in range(4):
                use_list.append(int(num[pos]))
            #print(use_list)
            
            for pos in range(4):
                if use_list[pos] == gen_list[pos]:
                
                    compare_list.append("Y")
                elif use_list[pos] < gen_list[pos]:
                    
                    compare_list.append("L")
                elif use_list[pos] > gen_list[pos]:
                    
                    compare_list.append("H")
            print(compare_list)
            if use_list[pos] == gen_list[pos]:
                correct = True
            else:
                correct = False

        if correct == True:
            print("You won")
        else:
            print("You ran out of attempts, GAME OVER")





