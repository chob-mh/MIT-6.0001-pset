# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 08:05:23 2020

@author: Brian
"""


round(.1,1)
round(.1,1)+round(.1,1)+round(.1,1)==round(0.3,1)

my_list=[5,2,7,-4,0]
for i in range(len(my_list)):
    my_list[i]+=1
print(my_list)

###############################################################################
# Part A: House Hunting
###############################################################################

# total_cost=float(input('cost of dream home: '))
# annual_salary=float(input('Enter your annual salary: '))
# percent_saved= float(input('Enter the percent to save as a decimal: '))
# portion_down_payment = round(total_cost*0.25,2)
# current_savings = 0
# numberofmonths=0
# r=0.04
# monthlysavings=0
# monthlysalary=0

# while current_savings < portion_down_payment:
#     monthlysalary=(annual_salary/12)
#     investment=(current_savings*r/12)
#     monthlysavings=(monthlysalary*percent_saved+investment)
#     current_savings+=monthlysavings
#     numberofmonths+=1
# print('it will take you',numberofmonths, 'months to save for a down payment')

###############################################################################
# Part B: Savings with a raise
###############################################################################


# total_cost=float(input('cost of dream home: '))
# annual_salary=float(input('Enter your annual salary: '))
# percent_saved= float(input('Enter the percent to save as a decimal: '))
# semi_annual_raise=float(input('Enter the semi-annual raise: '))
# portion_down_payment = round(total_cost*0.25,2)
# current_savings = 0
# numberofmonths=0
# tillraise=0
# r=0.04
# monthlysavings=0
# monthlysalary=0

# while current_savings < portion_down_payment:
#     monthlysalary=(annual_salary/12)
#     investment=(current_savings*r/12)
#     monthlysavings=(monthlysalary*percent_saved+investment)
#     current_savings+=monthlysavings
#     numberofmonths+=1
#     tillraise+=1
#     if tillraise > 0 and tillraise%6==0:
#         annual_salary=(semi_annual_raise*annual_salary+annual_salary)
        
# print('it will take you',numberofmonths, 'months to save for a down payment')

###############################################################################
#Part C Finding the right amount
###############################################################################

#Parameters
## 1.semiannual raise=0.7
## 2.r=0.04
## 3.down payment = 0.25
## 4. cost of house = 1000000


annual_salary=float(input('Enter your annual salary: '))
current_savings=0
costofhouse=1000000
portion_down= 0.25
total_cost=(costofhouse*portion_down)
semi_annual_raise=0.07
r=0.04
months=0
high=10000
low=0
percent_rate = (high+low)//2
steps=0

while abs(current_savings-total_cost) >= 100:
    current_savings=0
    present_salary=annual_salary
    rate=percent_rate/10000
    #iterate values over 36 months to find final savings
    for month in range (36):
        if month % 6 ==0 and month > 0:
            present_salary+= present_salary*semi_annual_raise
        monthlysalary=present_salary/12
        current_savings+=monthlysalary*rate+current_savings*r/12
## here is where the bisection search begins
    if current_savings < total_cost:
        low=percent_rate
    else:
        high=percent_rate
    percent_rate=(high+low)//2
#where I went wrong the first time. 
#######1)Steps count after all the search is completed not after each check
#######2)Did not set any tolerance threshold to break loop (steps 13)
#######3) why 13?  
###########The max amount of guesses needed is log base 2 of 10000 which is slightly
###########above 13. Once it gets to the 14th guess it breaks out of the while loop.
    steps+=1
    if steps >13:
        break

if steps > 13:
    print('not possible')
else:
    print('Best savings rate', rate)
    print('steps in bisection search', steps)









    

    
    
    
    



    
    
    

