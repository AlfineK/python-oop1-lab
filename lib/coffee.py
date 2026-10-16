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

    def set_size(self):
        if self.size=="Large" or self.size=="Medium" or self.size=="Small":
            self.size=self._size
        else:
            print("size must be Small, Medium, or Large")