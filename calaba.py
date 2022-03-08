from __future__ import annotations
from typing import List
from dataclasses import dataclass


@dataclass
class Person:
    number: int
    contacts: List[int]

    def knows(self, pers: Person):
        return pers.number in self.contacts


def celeba(persons: List[Person]) -> int:
    l = 0
    r = len(persons) - 1
    while l!=r:
        if persons[l].knows(persons[r]):
            l+=1
        else:
            r-=1
    for p in persons:
        if p != persons[l] and (not p.knows(persons[l]) or persons[l].knows(p)):
            return(None)
    return(persons[l], persons[l].number)


steve1 = Person(1, [2,3,4])
steve2 = Person(2, [3])
steve3 = Person(3, [])
steve4 = Person(4, [3])
room4 = [steve1, steve2, steve3, steve4]

ce = celeba(room4)
print(ce)