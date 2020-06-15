def count():
    global a,n,p,i
    n=ceil(log(a / (a - i * p),1+i))
    if l < 5 or p < 0 or n < 0 or yi < 0 :
       print("Incorrect parameters")
       return
#You need 8 years and 2 months to repay this credit
    y = n // 12
    m = n % 12
    if y == 0:
        print(f"You need {m} months to repay this credit!")
    elif m == 0:
        print(f"You need {y} years to repay this credit!")
    else:
        print(f"You need {y} years and {m} months to repay this credit!") 
        
    print(f"Overpayment ={ceil((a*n)) - ceil(p)}") 

def annuity():
    global a,n,p,i  
    a = p * ((i * pow((1 + i), n))/(pow((1+i), n)-1))
    if l < 5 or p < 0 or n < 0 or yi < 0 :
       print("Incorrect parameters")
       return
   # print(p,n,yi,i)
    print(f"Overpayment = {(ceil(a) * n) - p}")
    print(f"Your annuity payment = {ceil(a)}")
      
    
def princi():
    global a,n,p,i
    p = a / ((i * pow((1 + i), n)) /(pow((1 + i), n) - 1))
    if l < 5 or p < 0 or n < 0 or yi < 0 :
       print("Incorrect parameters")
       return
    
    print(f"Your credit principal = {ceil(p)}!")
    print(f"Overpayment ={ceil((a*n)) - ceil(p)}")    
    

import argparse
from sys import argv
from math import log,ceil
parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--payment", type = int)
parser.add_argument("--principal", type = int)
parser.add_argument("--periods", type = int)
parser.add_argument("--interest", type = float)
args = parser.parse_args()
l = len(argv)

p = args.principal
n = args.periods
yi = args.interest
a = args.payment

if args.type == "diff":
    
    if "--payment" in args or l < 5 or p < 0 or n < 0 or yi < 0 :
       print("Incorrect parameters")
    else:
        i = yi/(12 * 100)
        sum = 0
        for r in range(1,n+1):
          mp = ceil(p/n + i*(p - ((p * (r-1))/n)))  
          print(f"Month {r}: paid out {mp}")
          sum = sum + mp
        print(f"Overpayment = {sum - p}")
elif args.type == "annuity":
    if  "--interest" not in args:
       # print(yi)
        print("Incorrect parameters")
    else:
        i = yi/(12 * 100)
        if p == None:
            princi()
        if a == None:
            annuity()  
        if n == None:
            count()    

else:
    print("Incorrect parameters")
