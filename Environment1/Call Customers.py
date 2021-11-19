

customers_spoken_with = []
customers_messaged_with = []
customers_no_contact = []

# take input and make the lists for each contact result, if they act dumb, give them an attitude
status = 'spoke'
order_counter: int
print("Orders for which you spoke to the customer")
while status == 'spoke':
    new_order = input('Order Number: ')
    if new_order == '':
        status = 'messaged'
    else:
        try:
            new_order_number = int(new_order)
        except ValueError:
            try:
                print("Please Enter the number only")
                new_order_number = int(input('Order Number: '))
            except ValueError:
                try:
                    print("JUST THE NUMBER! NO SIGNS, NO WORDS, NO NOTHING, JUST THE NUMBER!")
                    new_order_number = int(input('Order Number: '))
                except ValueError:
                    print('You\'re retarded bro. JUST THE FUCKING NUMBER! I swear to GOd, if you enter something else that not the number, I\'m gonna break down on your ass and you\'re gonna have to call tech support and go through a whole lotta bullshit. Try me!')
                    new_order_number = int(input('Order Number: '))
        finally:
            customers_spoken_with.append(new_order_number)
            print('Order #', new_order, ' has been added to the called list')
print('\n')
print("Moving on to orders for which you messaged the customer")
while status == 'messaged':
    new_order = input('Order Number: ')
    if new_order == '':
        status = 'no contact'
    else:
        try:
            new_order_number = int(new_order)
        except ValueError:
            try:
                print("Please Enter the number only")
                new_order_number = int(input('Order Number: '))
            except ValueError:
                try:
                    print("JUST THE NUMBER! NO SIGNS, NO WORDS, NO NOTHING, JUST THE NUMBER!")
                    new_order_number = int(input('Order Number: '))
                except ValueError:
                    print('You\'re retarded bro. JUST THE FUCKING NUMBER! I swear to GOd, if you enter something else that not the number, I\'m gonna break down on your ass and you\'re gonna have to call tech support and go through a whole lotta bullshit. Try me!')
                    new_order_number = int(input('Order Number: '))
        finally:
            customers_messaged_with.append(new_order_number)
            print('Order #', new_order, ' has been added to the called list')
print('\n')
print("Moving on to orders for which you couldn't get a hold of the customer")
while status == 'no contact':
    new_order = input('Order Number: ')
    if new_order == '':
        status = 'no_contact'
    else:
        try:
            new_order_number = int(new_order)
        except ValueError:
            try:
                print("Please Enter the number only")
                new_order_number = int(input('Order Number: '))
            except ValueError:
                try:
                    print("JUST THE NUMBER! NO SIGNS, NO WORDS, NO NOTHING, JUST THE NUMBER!")
                    new_order_number = int(input('Order Number: '))
                except ValueError:
                    print('You\'re retarded bro. JUST THE FUCKING NUMBER! I swear to GOd, if you enter something else that not the number, I\'m gonna break down on your ass and you\'re gonna have to call tech support and go through a whole lotta bullshit. Try me!')
                    new_order_number = int(input('Order Number: '))
        finally:
            reason = input('What happened when you tried to contact them?: ')
            reasoned_order = (new_order_number, reason)
            customers_no_contact.append(reasoned_order)
            print('Order #', new_order_number, ' has been added to the called list with a reason you couldn\'t get a hold of them')

print("Inputting Notes Now...")

from Classlib import Lightspeed as LS
from Classlib import driver
LS.Login('marpab96@gmail.com', 'Il0veSad!e2020')

for order in customers_spoken_with:
    LS.finish_workorder(order,'Spoke','')
for order in customers_messaged_with:
    LS.finish_workorder(order,'Message', '')
for order in customers_no_contact:
    LS.finish_workorder(order[0], '', order[1])

driver.close()