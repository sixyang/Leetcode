class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_set = [-1] * 100000

    def add(self, key: int) -> None:
        value = (key + 1) % 100000
        if not self.contains(key):
            self.hash_set[value] = key
             

    def remove(self, key: int) -> None:
        value = (key + 1) % 1000000
        self.hash_set[value] = -1

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        value = (key + 1) % 100000
        if self.hash_set[value] != -1:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
