from base import BaseClient
from methods import FriendsGet
from methods import UserGet

print("Добро пожаловать в мою программу!")
print()

a = UserGet('maximmazunin')
b = a.execute()
print(b)

c = FriendsGet(b)
a = c.execute()
print(a)

list_date = sorted(list(a.keys()), reverse=True)
for i in list_date:
    print(2016 - int(i), end=": ")
    print("*" * int(a[i]), end=" ")
    print()