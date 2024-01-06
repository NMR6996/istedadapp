def qapali_duz(f_q, d_q, number):
    duz = 0
    for i in range(number):
        if f_q[i] == d_q[i] or d_q[i] == '*':
            duz += 1
    return duz


def xarici_dil(x_dil):
    fenn = ''
    if x_dil == "I":
        fenn = 'İngilis dili'
    elif x_dil == "F":
        fenn = 'Fransız dili'
    elif x_dil == "A":
        fenn = 'Alman dili'
    elif x_dil == "R":
        fenn = 'Rus dili'
    else:
        pass
    return fenn


def convert_to_list(string):
    my_list = string.split(',')
    my_list = [element.strip() for element in my_list]
    return my_list


def aciq_duz(f_a, d_a, ):
    duz = 0
    for i in range(len(d_a)):
        if f_a[i] == d_a[i] or d_a[i] == '*':
            duz += 1
    return duz


def part_of_question(f_q, coordinate1):
    question_list = [f_q[:coordinate1], f_q[coordinate1:]]
    question_list[0] = question_list[0].replace(" ", "&nbsp;")
    question_list[1] = question_list[1].replace(" ", "&nbsp;")
    return question_list
