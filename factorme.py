import os,sys

def factor(num):
    temp = []
    pairs = []
    for i in range(1,num+1):
        if (num/i).is_integer():
            if i not in temp and int(num/i) not in temp:
                temp.append(i)
                temp.append(i/num)
                pairs.append((i,int(num/i)))
    for pair in pairs:
        print(pair)

def fac_sum(num,summ):
    temp = []
    pairs = []
    for i in range(1,num+1):
        if (num/i).is_integer():
            if i not in temp and int(num/i) not in temp:
                temp.append(i)
                temp.append(i/num)
                pairs.append((i,int(num/i)))
    print('\n')
    for pair in pairs:
        a = pair[0]
        b = pair[1]
        if int(a+b) == summ:
            print(pair)
            print("({}) + ({}) = {}\n".format(a,b,(a+b)))
        elif int(a+-b) == summ:
            print(pair)
            print("({}) + ({}) = {}\n".format(a,-b,(a+-b)))
        elif int(-a+b) == summ:
            print(pair)
            print("({}) + ({}) = {}\n".format(-a,b,(-a+b)))
        elif int(-a+-b) == summ:
            print(pair)
            print("({}) + ({}) = {}\n".format(-a,-b,(-a+-b)))
    #else:
    #    sys.exit("No factors of {} sum to {}.".format(num,summ))
        #print("{:<5}{:<5}{:<5}{:<5}{:<5}".format('('+a+')' ,'+','('+b+')','=',(a+b)))
        #print("{:<5}{:<5}{:<5}{:<5}{:<5}".format('('+a+')' ,'+','('+-b+')','=',(a+-b)))
        #print("{:<5}{:<5}{:<5}{:<5}{:<5}".format('('+-a+')','+','('+b+')','=',(-a+b)))
        #print("{:<5}{:<5}{:<5}{:<5}{:<5}".format('('+-a+')','+','('+-b+')','=',(-a+-b)))
        
        #print("({}) + ({}) = {}".format(a,b,(a+b)))
        #print("({}) + ({}) = {}".format(a,-b,(a+-b)))
        #print("({}) + ({}) = {}".format(-a,b,(-a+b)))
        #print("({}) + ({}) = {}".format(-a,-b,(-a+-b)))

if __name__ == '__main__':
    if len(sys.argv) == 3:
        if sys.argv[1] == '-f':
            num = int(sys.argv[2])
            factor(num)
    elif len(sys.argv) == 5:
        try:
            factor = int(sys.argv[sys.argv.index('-f')+1])
        except:
            sys.exit("-f not in arguments")
        try:
            summ = int(sys.argv[sys.argv.index('-t')+1])
        except:
            sys.exit("-t not in arguments")
        fac_sum(factor,summ)