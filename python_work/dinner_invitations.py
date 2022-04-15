# 3.4: Guest List 
index = 0
guest_list = ['Jim', 'Sam', 'Joe']

while index < 3:
	invite = f"Hello {guest_list[index]}, come to dinner tonight."
	print(invite)
	index = index+1

# 3.5: Changing Guest List
print('\tSam cannot make it to dinner.')
guest_list[1] = 'Bob'
index = 0

while index < 3:
	invite = f"Hello {guest_list[index]}, come to dinner tonight."
	print(invite)
	index = index+1

# 3.6: More Guests
print('\tWe have found a bigger table.')

guest_list.insert(0,'Wyatt')
guest_list.insert(2,'Jake')
guest_list.append('Fred')
index = 0

while index < 6:
	invite = f"Hello {guest_list[index]}, come to dinner tonight."
	print(invite)
	index = index+1

# 3.7: Shrinking Guest List
print("\tThe table won't be ready in time, we only have space for two guests.")
index = 0

# Un-invitation:
while index < 4:
    deinvited = guest_list.pop()
    deinvite_message = f"Sorry {deinvited}, I have to take back my dinner invitation."
    print(deinvite_message)
    index = index+1

# Re-invitation:
index = 0
while index < 2:
	reinvite = f"Hello {guest_list[index]}, you are still welcome to join us."
	print(reinvite)
	index = index+1

# Clear list: (Unsure why I get "IndexError: list assignment index out of range" when guest_list[index]; for some reason guest_list[0] works.)
index = 0
print(guest_list)
print(len(guest_list))
while index < 2:
	del guest_list[0]
	index = index+1

print(guest_list)








