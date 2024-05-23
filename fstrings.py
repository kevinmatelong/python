first_name = 'Corey'
last_name = 'Schafer'

# sentence = 'My name is {} {}'.format(first_name, last_name)
# print(sentence)

sentence = f'My name is {first_name} {last_name}'
sentence = f'My name is {first_name.upper()} {last_name.upper()}'

print(sentence)


person = {'name':'Jenn','Age':23}

sentence = f"My name is {person['name']} and i am {person['Age']} years old"
print(sentence)

calculation = f'4 times 11 is { 4 * 11}'
print(calculation)

for i in range(1,11):
    sentence = f'The value is {i:02}'  # i:02 number of digits
    print(sentence)

pi = 3.142234434
sentence = f'pi is equal to {pi:.4f}'
print(sentence)
