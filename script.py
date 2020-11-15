def conversion():
    user_input = input('Please input the desired conversion (X cm/m in cm/m): ')
    try:
        user_input = user_input.split()
        from_unit = user_input[1]
        to_unit = user_input[3]
        value = int(user_input[0])

        if (from_unit == 'cm' and to_unit == 'm'):
            return print(str(value/100) + 'm')
        elif (from_unit == 'm' and to_unit == 'cm'):
            return print(str(value * 100) + 'cm')

    except:
        print('Please request a valid conversion')
        conversion()

conversion()
