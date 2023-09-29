from typing_extensions import SupportsIndex
from collections import UserList

class FrozenList(UserList):
    def append(self, __object) -> None:
        raise Exception("Append not allowed")

    def pop(self, __index):
        raise Exception("Pop not allowed")

    def __hash__(self):
        return 1

    def __eq__(self, other):
        return True

f_list = FrozenList([1, 2, 3])
f_list2 = FrozenList([5, 6, 7])

s = set()
s.add(f_list)
s.add(f_list2)
print(s)
