event_list = []

class Event:
   def __init__(self):
       self.__keys = []
       self.description = ''
       event_list.append(self)

   @property
   def keys(self):
       return self.__keys

   @keys.setter
   def keys(self, mas):
       for k in mas:
           self.__keys.append(k.lower())

   def process(self, data):
       pass