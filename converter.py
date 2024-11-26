def convert_from_10(num, basis, round_to = 100):
    convert_num = ''
    num_s = str(num)
    all_basis = '0123456789abcdefghijklmnopqrstuvwxyz'

    if num_s.find('.') == -1:
        while num != 0:
            remaind = all_basis[num % basis]
            convert_num += remaind
            num //= basis
        return convert_num[::-1]

    else:
        int_part = int(num_s[:num_s.find('.')])
        float_part = num_s[num_s.find('.') - 1:]
        float_part = float(float_part.replace(float_part[0], '0', 1))
        convert_float_part = ''

        while int_part != 0:
            remaind = all_basis[int_part % basis]
            convert_num += remaind
            int_part //= basis

        while float_part > 0 and round_to > 0:
            new_float = float_part * basis
            if basis <= 10: 
                convert_float_part += all_basis[int(str(new_float)[0])]
                float_part = new_float - int(str(new_float)[0])
            else:
                if new_float >= 10: 
                    convert_float_part += all_basis[int(str(new_float)[0:2])]
                    float_part = new_float - int(str(new_float)[0:2])
                else:
                    convert_float_part += all_basis[int(str(new_float)[0])]
                    float_part = new_float - int(str(new_float)[0])
            round_to -= 1

        return convert_num[::-1] + '.' + convert_float_part

def convert_to_10(num, basis):
    all_basis = '0123456789abcdefghijklmnopqrstuvwxyz'
    convert_num = 0
    if num.find('.') == -1:
        for i in range(len(num)):
            convert_num += int(all_basis.find(num[i])) * pow(basis, len(num) - 1 - i)
        return convert_num
    else:
        int_part = num[:num.find('.')]
        float_part = num[num.find('.') + 1:]
        convert_float_part = 0

        for i in range(len(int_part)):
            convert_num += int(all_basis.find(num[i])) * pow(basis, len(int_part) - 1 - i)

        for i in range(len(float_part)):
            convert_float_part += int(all_basis.find(float_part[i])) * pow(basis, -1 - i)
        return str(convert_num) + '.' + str(convert_float_part)[2:]

def convert(num, basis_from, basis_to, round_to = 100):
    if basis_from == 10: return convert_from_10(num, basis_to, round_to)
    if basis_to == 10: return convert_to_10(str(num).lower(), basis_from)
    else: return convert_from_10(convert_to_10(str(num).lower(), basis_from), basis_to, round_to)

