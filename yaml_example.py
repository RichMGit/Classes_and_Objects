import yaml

file_name = 'test.yml'

with open(file_name) as infile:
    data = yaml.load(infile)

person = data['Person']
person['Name'] = input('What is your name? ')
person['Age'] = int(input('What is your age? '))
person['Nationality'] = input('What is your nationality? ')
person['Footed'] = input('What foot? ')
person['Position'] = input('What is your position? ')

with open(file_name, 'w') as outfile:
        yaml.dump(data, stream=outfile, default_flow_style=False, indent=3)
