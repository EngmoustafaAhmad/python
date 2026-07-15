class Solution(object):
    def romanToInt(num):
        total = 0
        i in range(num.lenght)
            if(num[i]=="M"):
                total += 1000
            if(num[i]== "D"):
                total += 500
            if(num[i]== "C"):
                total += 100
            if(num[i]== "L"):
                total += 50
            if(num[i]== "X"):
                total +=10
            if(num[i]== "V"):
                total +=5
            if(num[i]== "I"):
                total +=1
        print(total)