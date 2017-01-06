#Author: Islam Youssief Mohamed
#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def calculateEquation():
    print('Result of the equation (2**2+3*5)/(2*2+3*5) = ',((2**2+3*5)/(2*2+3*5)))
    print('--------------------------------------')    

def multiplicationTable():
     for i in range(1,11):
         for j in range(1,11):
             print(i,' x ',j,' = ',i*j)
         print('--------------------------------------')  

def isKey(num=5):
    if num!=5: print(num,'Sorry This Is Not The Key');return
    print(num,'Here You Go Bravo This is the Key')

def sumNums(x=2,y=5,z=8):
    print('Result of Nums',x,',',y,',',z,'=',x+y+z)
    

def main():
    calculateEquation()
    multiplicationTable()
    isKey(6)
    isKey(5)
    sumNums(2)
    sumNums(3,7)
    sumNums(3,4,5)
    
#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
if __name__=='__main__':
    main()
