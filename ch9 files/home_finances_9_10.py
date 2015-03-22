"""
1. accounts: It is a dictionary managing the information of 4 different
accounts, i.e. savings, checking, mm, cd. The format will be like:
accounts = {'savings':{balance:balance_amount, other_info: other_info_value}, ...}
2. Transaction: A dictionary includes the current time with the corresponding
transaction record. It looks like
transactions = {'serial_no':current_SN, 2:['20150322 10:02','deposit' function_name, account_name, amount]}
3. Operation: Deposit, withdrawals.(which will change account and record
in transactions.
   Delete Transactions: which is used to delete a transaction.)
"""

__author__ = 'Richard'
import pickle
import copy
from time import ctime

operation_sentence = "(D)eposit, (W)ithdrawal, (T)ransaction, e(X)it, (Q)uery> "

accounts = {}
transactions = {}

def init():
    """should read the pickle file to get the info"""
    global accounts
    try:
        with open('account_9_10.pickle', 'rb') as f:
            accounts = pickle.load(f)
    except FileNotFoundError:
        print("No account existed. Creating a new account...")
        init_dict = {'balance': 0, 'other_info': ''}
        # 下面这句话有误，是一个shallow copy，我需要deep copy
        accounts = {'savings': copy.deepcopy(init_dict), 'checking':copy.deepcopy(init_dict),
                    'mm':copy.deepcopy(init_dict), 'cd':copy.deepcopy(init_dict)}
    global transactions
    try:
        with open('transaction_9_10.pickle', 'rb') as tf:
            transactions = pickle.load(tf)
    except FileNotFoundError:
        print("No transaction exited.")
        transactions['serial_no'] = 0

def save():
    """save the changes into a pickle file"""
    global accounts
    with open('account_9_10.pickle', 'wb') as f:
        pickle.dump(accounts, f)

    global transactions
    with open('transaction_9_10.pickle', 'wb') as tf:
        pickle.dump(transactions,tf)

def deposit():
    global accounts
    global transactions
    try:
        account = input("Input account name: savings, checking, mm, cd> ")
        money = float(input("How much money is done?"))
        accounts[account]['balance'] += money
        # record a transaction
        import sys
        this_function_name = sys._getframe().f_code.co_name
        transactions['serial_no'] += 1
        serial_no = transactions['serial_no']
        transactions[serial_no] = [this_function_name, account, money, ctime()]
    except KeyError:
        print("Wrong account name!")
    except ValueError:
        print("Wrong money")

def withdrawal():
    global accounts
    global transactions
    try:
        account = input("Input account name: savings, checking, mm, cd> ")
        money = float(input("How much money is done?"))
        # TODO judge if the money is greater than the balance
        accounts[account]['balance'] -= money
        # record a transaction
        import sys
        this_function_name = sys._getframe().f_code.co_name
        transactions['serial_no'] += 1
        serial_no = transactions['serial_no']
        transactions[serial_no] = [this_function_name, account, money, ctime()]
    except KeyError:
        print("Wrong account name!")
    except ValueError:
        print("Wrong money")

def delete_transaction():
    global transactions
    try:
        serial_no = int(input("Input the serial_no of the transaction to delete> "))
        del(transactions[serial_no])
    except KeyError:
        print("Wrong serial no")

def main():
    print("{:*^80}".format("WELCOME TO Home Finances Manager"))
    init() # should read the pickle file to get the info
    while True:
        operation = input("Input an operation:" + operation_sentence)
        if operation.strip().upper().startswith('X'): # exit
            break;
        if operation.strip().upper().startswith('Q'): # query
            print(accounts)
        elif operation.strip().upper().startswith('D'): # deposit
            deposit()
        elif operation.strip().upper().startswith('W'): # withdrawal
            withdrawal()
        elif operation.strip().upper().startswith('T'): # delete transaction
            transactions_operation = input("Input an operation for transactions: (Q)uery, (D)elete>")
            if transactions_operation.strip().upper().startswith('Q'):
                print(transactions)  # Query transaction
            elif transactions_operation.strip().upper().startswith('D'):
                delete_transaction()  # Delete Transaction
        else:
            print("Your input is invalid. Please try again")
    save()
    print("{:*^80}:".format("Quited Home Finances Manager"))

if __name__ == '__main__':
    main()
