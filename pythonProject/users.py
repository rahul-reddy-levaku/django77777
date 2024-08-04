user_dict={'naresh':23,'ramesh':'r321','kishore':'k321'}

def login(user,password):
    if user in user_dict and user_dict[user]==password:
        print(f'{user} welcome')
    else:
        print('not welcome')