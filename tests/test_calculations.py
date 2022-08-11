import pytest
from app.calculations import add, multiply, subtract, divide, BankAccounts, InsufficentFunds

@pytest.fixture
def zero_bank_account():
    print('Cretting bank account')
    return BankAccounts()

@pytest.fixture
def bank_account():
    return BankAccounts(100)

@pytest.mark.parametrize("num1, num2, expected",[
    (3,4,7),
    (7,4,11),
    (6,9,15)
])
def test_add(num1, num2, expected):
    print('Assert add funciotn ')
    assert add(num1, num2) == expected
    
def test_multiply():
    assert multiply(3,9) == 27
  
def test_subtract():
    assert subtract(9,3) == 6

def test_divide():
    assert divide(9,3) == 3      
    
def test_bank_set_init_amount(bank_account):
    # bank_account = BankAccounts(50) 
    print('Reach here ', bank_account.balance)         
    assert bank_account.balance == 100

# combine with fixture 
@pytest.mark.parametrize("deposited, withdraw, expected",[
    (200,100,100),
    (7,4,3),
    (12,9,3)
])
def test_bank_transaction(zero_bank_account,deposited, withdraw, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.widthdraw(withdraw)
    assert zero_bank_account.balance == expected
   
 # error exception   
def test_insufficent_balance(bank_account):
    # with pytest.raises(Exception):
    with pytest.raises(InsufficentFunds):
        bank_account.widthdraw(120)    
    
def test_bank_default_amount():
    bank_account = BankAccounts()          
    assert bank_account.balance == 0   
    
def test_windtraw(bank_account):
    # bank_account = BankAccounts(100)
    bank_account.widthdraw(20)
    assert bank_account.balance == 80
    
def test_deposit(bank_account):  
    # bank_account = BankAccounts(100)
    bank_account.deposit(20)
    assert bank_account.balance == 120     
    
def test_collect_intrest(bank_account):  
    # bank_account = BankAccounts(100)
    bank_account.collect_interest()
    assert round(bank_account.balance, 6) == 110
    
####
## pytest.fixture
####    
def test_zero_bank_account_fix(zero_bank_account):
    return zero_bank_account.balance == 0