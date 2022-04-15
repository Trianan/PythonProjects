agent_number = input("Agent number: ")
agents = {
    '198289': ['Redrock', 34, 'M', 'In field: Moscow'],
    '227413': ['Snake Eyes', 39, 'M', 'KIA'],
    '423459': ['Jimothy', 27, 'M', 'Available'],
    '166633': ['Veranda', 29, 'F', 'Unavailable']
}
if agent_number in agents:
    profile = agents.get(agent_number)
    name, age, sex, status = profile
    print(f'''
Agent Number: {agent_number}
Name: {name}
Age: {age}
Sex: {sex}
Status: {status}
''')
else:
    print('Number not recognized.')
