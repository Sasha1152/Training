days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
time_all = ('8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00')
time_mo = {'9:00':'Sasha', '11:00':'Oleg'}
time_tu = dict(zip(time_all, ['Alex', 'Jack', 'Bob', 'Rouzee', 'Stephany', 'Katrin', 'Bill', 'Sophi']))
register = dict(zip(days, [time_mo, time_tu, {}, {}, {}]))

# reg_file = open('register.txt', 'r')
# register = reg_file.readlines()  -- незнаю, як занести дані із файла назад у словник
# reg_file.close()

while True:
    while True:
        while True:
            day = raw_input('Enter day (from Monday to Friday): ')
            if day in days:
                break
            else:
                print('You entered wrong title of day. Try again.')
        if len(register[day]) == 8:
            print('engaged')
        else:
            break
    
    while True:
        while True:
            time = raw_input('Entrer time (from 8:00 to 16:00): ')
            if time in time_all:
                break
            else:
                print('You entered wrong title of time. Try again.')
        if time in register[day].keys():
            print('engaged')
        else:
            break
    
    name = raw_input('Enter your name: ')
    register[day][time] = name
    print(register)

    reg_file = open('register.txt', 'w')
    for key in register:
        reg_file.write(str(key) + ': ' + str(register[key]) + '\n')
    reg_file.close()

    print('Congratulation, ' + name + '!!!!')
    print('You are registered on ' + day + ' at ' + time)
    print('Do you wish to continue?')
    answer = raw_input('Press any key if YES, enter "exit", or NO:')
    if answer == 'exit':
        break
    else:
        continue
