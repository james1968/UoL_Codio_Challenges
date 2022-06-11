from __future__ import annotations
class Person:
    first: str
    last: str
    friends: list[Person]

    def __init__(self, first: str, last: str):
        '''create a new Person with specified first and last names'''
        self.first = first
        self.last = last
        self.friends = []

    def get_name(self) -> str:
        '''returns a string having first name and last name of this person separated by space'''
        return f"{self.first} {self.last}"

    def get_friends(self, name: str) -> list[Person]:
        friends = []
        for f in self.friends:
            if f.last == name:
                friends.append(f)
        return friends

    def add_friend(self, f: Person) -> None:
        '''adds f as a friend of this person'''
        self.friends.append(f)

    def common_friends(self, p: Person) -> list[Person]:
        '''returns a list of common friends of this person and p'''
        common_friends = []
        for i in self.friends:
            for j in p.friends:
                if i.first == j.first and i.last == j.last:
                    common_friends.append(j)
        return common_friends

    def friends_of_friends(self) -> list[Person]:
        '''returns a list of friends of friends of this person, i.e.,
       of persons o for which there exists p such that o is a friend of p and p is a friend of this person'''
        friends_of_friends = []
        for i in self.friends:
            for j in f.friends:
                friends_of_friends.append(j)
        return friends_of_friends
