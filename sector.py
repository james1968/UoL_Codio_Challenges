from __future__ import annotations  # keep this in because of recursive annotations


class Sector:
    fr: int
    to: int
    rad: int

    def __init__(self):
        '''Creates a circular sector with from and to angles 0 and radius 0.'''
        self.fr = 0
        self.to = 0
        self.rad = 0

    def rotate(self, angle: int) -> None:
        '''Rotates sector by the angle. For simplicity, assume that the rotation will result in a sector with fr <= to'''
        self.fr += angle
        self.to += angle

    def intersect(self, other: Sector) -> Sector:
        '''Returns a new sector that is the result of the intersection of this sector with the other one. For simplicity, assume that the two sectors have non-empty intersection (overlap).'''
        sector3 = Sector()
        list1 = {self.fr, self.to, self.rad}
        list2 = {other.fr, other.to, other.rad}

        ans = list1.intersection(list2)
        print(list(ans))

    def is_empty(self) -> bool:
        '''Returns True if the sector has empty area, otherwise returns False.'''
        if self.fr == self.to:
            return False

    def __eq__(self, other: Sector) -> bool:
        '''Returns True this sector is the same as the other, otherwise False.'''
        if self.fr == other.fr and self.to == other.to:
            return True
        else:
            return False

    def __str__(self) -> str:
        '''Returns string "F T R" where F is from angle, T is to, and R is radius.'''
        return f"{self.fr} {self.to} {self.rad}"

s1 = Sector()
s1.fr = 0
s1.to = 20
s1.rad = 40
assert str(s1)=="0 20 40"   #test_1
s1.rotate(50)
assert str(s1)=="50 70 40"   #test_2
s2 = Sector()
s2.fr = 50
s2.to = 70
s2.rad = 40
assert s1==s2   #test_3
s2.fr = 60
s2.to = 100
s2.rad = 30
s3 = s1.intersect(s2)
