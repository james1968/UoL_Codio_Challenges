from bank_ac_oop import *

john01 = Person("John", "Doe")
john01.set_address("Birkbeck, Malet st., WC1E 7HX")
john01s_account = IndividualBankAccount(123456, 12345678, john01)
assert john01s_account.get_account_data() =="John Doe 123456 12345678"   #test_1
john01s_account.set_sort_code("111111")
assert john01s_account.get_sort_code()=="111111"   #test_2


mary01 = Person("Mary", "Ann")
mary01.set_address("UCL, Gower st., WC1E 6BT")
mary01s_account = IndividualBankAccount(654321, 87654321, mary01)
assert mary01s_account.get_account_data()=="Mary Ann 654321 87654321"   #test_3
mary01s_account.set_account_number(99999999)
assert mary01s_account.get_account_number()==99999999   #test_4


acc02 = SharedBankAccount(112233, 11223344, [john01, mary01])
assert acc02.get_account_data() =="John Doe, Mary Ann, 112233 11223344"   #test_5