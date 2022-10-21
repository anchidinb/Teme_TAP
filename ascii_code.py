def ascii_code(character):
    return ord(character)

user_input = input('Introduceti caracterul: ')
x = ascii_code(user_input)
print('codul ascii pentru {} este: {}'.format(user_input, x))