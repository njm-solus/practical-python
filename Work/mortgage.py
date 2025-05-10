# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
time = 0
extra_payment_start_month = int(input('Enter extra payment start month number: '))
extra_payment_end_month = int(input('Enter extra payment end month number: '))
extra_payment = int(input('Enter extra payment amount: '))


while principal > 0:
    time += 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

    if time >= extra_payment_start_month and time <= extra_payment_end_month:
        principal -= extra_payment
        total_paid += extra_payment


    print(f'{time}\t{total_paid}\t{principal}')


    if principal < payment:
        time += 1
        total_paid += principal
        principal -= principal
        print(f'{time}\t{total_paid}\t{principal}')

print(f'Total paid: {total_paid} over {time} months')
