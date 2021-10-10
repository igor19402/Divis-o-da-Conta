# write your code here
import random
print("Enter the number of friends joining (including you):")
valid_options = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
number_of_friends = input()
if number_of_friends not in valid_options :
    print("No one is joining for the party")
else:
    number_of_friends = int(number_of_friends)
    list_of_friends = []
    print()
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(number_of_friends):
        name_friend = input()
        list_of_friends.append(name_friend)
    print("Enter the total bill value:")
    total_bill_value = int(input())
    value_pay_each = round(total_bill_value / number_of_friends, 2)
    dict_friends = dict.fromkeys(list_of_friends, value_pay_each)
    print()
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    answer = input()
    if answer == "Yes":
        lucky_one = random.choice(list_of_friends)
        print(f"{lucky_one} is the lucky one!")
        value_pay_each = round(total_bill_value / (number_of_friends - 1), 2)
        dict_friends = dict.fromkeys(list_of_friends, value_pay_each)
        dict_friends[lucky_one] = 0
        print(dict_friends)
    else:
        print("No one is going to be lucky")
        print(dict_friends)
