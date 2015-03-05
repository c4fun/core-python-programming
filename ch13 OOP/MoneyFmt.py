class MoneyFmt(object):
    #instance attribute contains a DATA value, and a MONETARY_AMOUNT

    def __init__(self, data=0.0):
        """Input the float number so as to create a monetary_amount"""
        self.data = data
        self.monetary_amount = dollarize(self.data)

    #object都没有这个类，所以这个__nonzero__的定义无效
    def __nonzero__(self):
        """return True if the data value is non-zero"""
        return abs(self.data) < 0.5

    def __repr__(self):
        'return the amount as a float'
        return repr(self.data)

    def __str__(self,beautify = False):
        """return the monetary_amount, beautify it by replacing '-' with <>"""
        if self.data < 0:
            return str('<'+self.monetary_amount[1:]+'>')
        else:
            return str(self.monetary_amount)

    def update(self, new_data):
        'replace the data value with a new one'
        try:
            float_of_new_data = float(new_data)
            self.data = float_of_new_data
            self.monetary_amount = dollarize(self.data)
        except ValueError:
            print('The new data is wrong type. Input a float type.')




def add_commas(fl):
    """This amounts to reversing everything left of the decimal,
    grouping by 3s, joining with commas, reversing and reassembling
    """
    left,right = ('%0.2f'%fl).split('.')
    rleft = [left[::-1][i:i+3] for i in range(0,len(left),3)]
    return (','.join(rleft)[::-1] + '.' + right)

def dollarize(f):
    'Make a float(f) into a financially readable amount'
    CURRENCY = '$'
    if f < 0:
        negative_flag = True
        f = abs(f)
    else:
        negative_flag = False
    financial_expression = CURRENCY + add_commas(f)
    # if negative, add the minus
    if negative_flag:
        financial_expression = '-' + financial_expression
    return financial_expression


if __name__ == '__main__':
    while True:
        num = input("Please input a number to dollarize.\n")
        if num == '':
            break
        print(dollarize(float(num)))
        #print(add_commas(float(num)))
