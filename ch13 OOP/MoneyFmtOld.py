#function dollarize() No. this is so wrong! There must be easier way to do that
def old_dollarize(f):
    CURRENCY = '$'
    'Make a float(f) into a financially readable amount'
    #1234567.8901
    #Turn the negative number to positive
    if f < 0:
        negative_flag = True
        f = abs(f)
    else:
        negative_flag = False
    s = str(f) #s = '1234567.8901'
    s_len = len(s)
    dot_position = s.find('.')
    financial_expression = ''

    if dot_position != -1:
        # Deal with the fraction after dot
        for i in range(dot_position+1, s_len):
            financial_expression+=s[i]
        if financial_expression != '':
            financial_expression = '.'+financial_expression
        else:
            financial_expression = '.00'

        # Deal with the integer before dot
        for i in range(dot_position, 0, -3):
            financial_expression = ','+ s[i-3:i] + financial_expression \
                if (i-3>0) else s[0:i] + financial_expression
        financial_expression = CURRENCY + financial_expression
        if negative_flag:
            financial_expression = '-' + financial_expression

    else: #It is an integer
        # Deal with the "fraction"
        financial_expression = '.00'

        # Deal with the integer before dot
        dot_position = s_len
        for i in range(dot_position, 0, -3):
            financial_expression = s[i-3:i] + financial_expression if (i-3>=0) \
                else s[0:i] + financial_expression
        financial_expression = CURRENCY + financial_expression
        if negative_flag:
            financial_expression = '-' + financial_expression

    return financial_expression
