# OPTION 1: Linked chain

#Copied discusion
class ListNode:
    def __init__(self,key,val):
        self.pair = (key,val)
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = 1000;
        self.h = [None]*self.m #defined a list with 1000 None value. [None, None, None, ... , None]

    def put(self, key: 'int', value: 'int') -> 'None':
        """
        value will always be non-negative.
        """
        index = key%self.m
        if self.h[index] == None: #Not sure why self.h[index] can work as h did not pre-defined. Answer: it defined in __init__part
            self.h[index] = ListNode(key,value)
        else:
            cur = self.h[index]
            while True:
                if cur.pair[0] == key:
                    cur.pair = (key, value) #update
                    return
                if cur.next == None: break
                cur = cur.next
            cur.next = ListNode(key,value) # Linked chain?

    def get(self, key: 'int') -> 'int':
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self.m
        cur = self.h[index]
        while cur:
            if cur.pair[0] == key:
                return cur.pair[1]
            else:
                cur = cur.next
        return -1 #if cur is none then skip from line 39, and return -1.
        

    def remove(self, key: 'int') -> 'None':
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % self.m
        cur = prev = self.h[index]
        if not cur: return 
        if cur.pair[0]==key:
            self.h[index]=cur.next
        else:
            cur = cur.next
            while cur:
                if cur.pair[0] == key:
                    prev.next = cur.next
                    break
                else:
                    cur,prev = cur.next, prev.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


# OPTION 2:  multi-dimension lists. 1000*1001 two-d list.
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = 1000
        self.itemsPerBuckect = 1001 # Need to define itemsPerBucket because question note 1: all keys and values will be in the range of [0,1000000]
        self.hashmap =[[] for _ in range(self.buckets)] #In this step, hashmap is defined as [[],[],[],... ,[]] (1000 empty lists)
        
    def hash(self,key):
        return key %self.buckets
    
    def pos(self,key):
        return key//self.buckets # when key is within 1000, pos(key) will always be 0. That's why following codes use this 
    
    def put(self, key: 'int', value: 'int') -> 'None':
        """
        value will always be non-negative.
        """
        hashkey = self.hash(key)
        if not self.hashmap[hashkey]:
            self.hashmap[hashkey] = [None]*self.itemsPerBuckect #In this step, hashmap[hashkey] is a list of 1001 [None, None .... None]
        self.hashmap[hashkey][self.pos(key)] = value #did not quite get this statement

    def get(self, key: 'int') -> 'int':
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hashkey = self.hash(key)
        if (not self.hashmap[hashkey]) or self.hashmap[hashkey][self.pos(key)]== None:
            return -1
        else:
            return self.hashmap[hashkey][self.pos(key)]
        

    def remove(self, key: 'int') -> 'None':
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hashkey = self.hash(key)
        if self.hashmap[hashkey]:
            self.hashmap[hashkey][self.pos(key)] = None
