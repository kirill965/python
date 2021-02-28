#!/usr/bin/env python3

#Exercise 1. В эту неделю вы спали 6.2, 7.8, 5, 6, 5, 6.5, 7.1, 8.5 часа. Вычислите среднюю продолжительность сна в часах.
sleep_time = (6.2 + 7.8 + 5 + 6 + 5 + 6.5 + 7.1 + 8.5)/8
print(f'You slept this week {sleep_time} hours.')

#Exercise 2. Making it another way.
time_which_you_slept = [6.2, 7.8, 5, 6, 5, 6.5, 7.1, 8.5]
sum_ = 0
for i in time_which_you_slept:
    sum_ += i
print(f'You slept this week {sum_/len(time_which_you_slept)} hours.')

#Exercise 3. Делится ли число  297 без остатка на 3?
print(f'Result of the division of 297 and 3 is {297//3} + {297%3}.')

#Exercise 4. 2 power 10. Print result.
print(f'Result of 2 power 10 is {2 ** 10}.')

#Exercise 5. Определение високосного года.
def check_year(year:int):
    if year%4 == 0 and year%100 == 0 and year%400 == 0:
        print(f'{year} is visokosn')
    elif year%4 == 0 and year %100 == 0 and not year%400 == 0:
        print(f'{year} is not visokosn')
    elif year%4 == 0 and not year %100 == 0 and not year%400 == 0:
        print(f'{year} is not visokosn')
    else:
        print(f'{year} is not visokosn')


years = [1800, 1900, 1903, 2000, 2002]
for year in years:
    check_year(year)

