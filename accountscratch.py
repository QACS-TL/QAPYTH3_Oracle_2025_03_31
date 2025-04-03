import account

accounts = []
accounts.append(account.Account("Ted", "22222"))
accounts.append(account.Account("Mary", "33333"))
accounts[0].credit(50)
accounts[1].credit(70)
accounts[0].balance = 100
print(accounts[0].balance)

accounts[0].balance += 700

for acc in accounts:
    print(acc)