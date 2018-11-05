madlib = "Got me looking so adjective right now, your love got me verb so crazy right now."

def user_input(prompt):
    user_input = input(prompt)
    return user_input


word_type_list = ['noun', 'verb', 'adjective', 'color', 'animal']

for wordtype in word_type_list:
    if madlib.find(wordtype) != -1:
        madlib = (madlib.replace(wordtype, input("Enter a {}: ".format(wordtype)), 1))

print(madlib);
