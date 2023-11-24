from enum import Enum

days= Enum('days', ['MON','TUE','WED','THU','FRI','SAT','SUN'])
print("Monday:" , days.MON.value)
print("Tuesday:" , days.TUE.value)
print("Wednesday:" , days.WED.value)
print("Thursday:" , days.THU.value)
print("Friday:" , days.FRI.value)
print("Saturday:" , days.SAT.value)
print("Sunday:" , days.SUN.value)
