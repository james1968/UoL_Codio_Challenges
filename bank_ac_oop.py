from typing import *

class Person:
    _first_name: str
    _last_name: str
    _address: str

    def __init__(self, fn: str, ln: str):
        "creates a new person with first name fn last name ln and empty address"
        self._first_name = fn
        self._last_name = ln

    def set_address(self, adr: str) -> None:
        "sets the address to adr"
        self._address = adr

    def get_address(self) -> str:
        "returns the address"
        return self._address


class BankAccount:
    _sort: int
    _account_num: int

    def __init__(self, sort_code: int, account_number: int) -> None:
        '''creates a bank account with given sort code and account number'''
        self._sort = sort_code
        self._account_num = account_number

    def set_sort_code(self, sort_code: int) -> None:
        '''updates sort code'''
        self._sort = sort_code

    def get_sort_code(self) -> int:
        '''returns sort code'''
        return self._sort

    def set_account_number(self, account_number: int) -> None:
        '''updates account number'''
        self._account_num = account_number

    def get_account_number(self) -> int:
        '''returns account number'''
        return self._account_num

    def get_account_data(self) -> str:
        '''returns string "SC AN" where SC is sort code, AN is account number'''
        return f"{self._sort} {self._account_num}"


class IndividualBankAccount(BankAccount):
    _owner: Person

    def __init__(self, sort_code: int, account_number: int, owner: Person):
        '''creates a new bank account with given sort code, account number, and owner'''
        super().__init__(sort_code, account_number)
        self._owner = owner

    def get_account_data(self) -> str:
        '''returns string "FN LN SC AN" where FN and LN are owner's first and last names,
        SC is sort code, AN is account number'''
        return f"{self._owner._first_name} {self._owner._last_name} {self._sort} {self._account_num}"


class SharedBankAccount(BankAccount):
    _owners: List[Person]

    def __init__(self, sort_code: int, account_number: int, owners: List[Person]):
        '''creates a new bank account with given sort code, account number, and owners'''
        super().__init__(sort_code, account_number)
        self._owners = owners

    def get_account_data(self):
        '''returns string "FN1 LN1, FN2 LN2, ..., FNM LNM, SC AN" where FNi LNi is the i-th       owner first and last names, SC is sort code, AN is account number'''
        owners_str = ''
        for i in self._owners:
            owners_str += i._first_name + ' ' + i._last_name + ', '
        return f"{owners_str}{self._sort} {self._account_num}"