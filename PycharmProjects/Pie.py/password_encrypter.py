
password = int(input("Password: "))

keys = [7727, 13, 5483, 643]
encrypted_password = password * keys[1]
encrypted_passwords = []

encrypted_passwords.append(encrypted_password)
print(encrypted_passwords)

restored_password = encrypted_passwords[0] / keys[1]

print(int(restored_password))



