list = [2200, 2350, 2600, 2130, 2190]
print("In Feb, how many dollars you spent extra compare to January?")
print(list[1] - list[0])
print("Find out your total expense in first quarter (first three months) of the year.")
expenses = 0
for i in range(3):
    expenses = expenses + list[i]
print(expenses)
print("Find out if you spent exactly 2000 dollars in any month")
for i in list:
    if i == 2130:
        print(True)
        break
print("June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list")
list.append(1980)
print(list)
print("You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this")
list[3] = list[3] - 200
print(list)

heros=['spider man','thor','hulk','iron man','captain america']
print("Length of the list")
print(len(heros))
print("Add 'black panther' at the end of this list")
print(heros.append("black panther"))
print(heros)
print("You realize that you need to add 'black panther' after 'hulk', so remove it from the list first and then add it after 'hulk'")
print(heros.pop())
print(heros)
print(heros.insert(3, "black panther"))
print(heros)
print("Now you don't like thor and hulk because they get angry easily :) So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool). Do that with one line of code.")
heros[1:3] = ["doctor strange"]
print(heros)
heros.sort()
print(heros)

print("Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function")
user_input = int(input())
list_odd = []
for i in range(1, user_input+1, 2):
    list_odd.append(i)
print(list_odd)