# -*- coding: utf-8 -*-
"""
Tobenna Nwufo
2054054
CISC 2348

"""

def exact_change(user_total):
    if user_total <= 0:  
        print('no change')
        
    num_dollars = user_total // 100 
    user_total -= (num_dollars * 100)
    if num_dollars == 1:  
        print(num_dollars , 'dollar')
    elif num_dollars > 1:
        print(num_dollars , 'dollars')
        
    num_quarters = user_total // 25
    user_total -= (num_quarters * 25) 
    if num_quarters == 1:
        print(num_quarters , 'quarter')
    elif num_quarters > 1:
        print(num_quarters , 'quarters')
        
    num_dimes = user_total // 10
    user_total = user_total - (num_dimes * 10)
    if num_dimes == 1:
        print(num_dimes , 'dime')
    elif num_dimes > 1:
        print(num_dimes , 'dimes')
        
    num_nickels = user_total // 5
    user_total = user_total - (num_nickels * 5)
    if num_nickels == 1:
        print(num_nickels , 'nickel')
    elif num_nickels > 1:
        print(num_nickels , 'nickels')
    
    num_pennies = user_total // 1
    if num_pennies == 1:
        print(num_pennies , 'penny')
    elif num_pennies > 1:
        print(num_pennies , 'pennies')
    
    return (num_dollars , num_quarters , num_dimes , num_nickels , num_pennies)
            
if __name__ == '__main__':   
    dollars, quarters, dimes, nickels, pennies = exact_change(int(input()))