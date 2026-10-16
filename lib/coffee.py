#!/usr/bin/env python3

class Coffee:
    def __init__(self,size,price):
        self.size=size
        self.price=price

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price +=1

    def get_size(self):
        return self._size

    def set_size(self,Small, Medium, Large):
        if Small or Medium or Large:
            self.size=self._size
        else:
            print("size must be Small, Medium, or Large")