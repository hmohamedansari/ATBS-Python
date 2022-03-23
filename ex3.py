while True:
    print ('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print ('Hello Joe what\'s the password?(It is a Fish)')
    password = input()
    if password == 'swordfish':
        break
print ('Access Granted')