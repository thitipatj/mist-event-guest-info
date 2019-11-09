import csv
from random import seed
from random import randint

lucky_person=[]

with open('guest_list.csv', mode='r') as guest_file:
    reader = csv.DictReader(guest_file)
    for row in reader:
        lucky_person.append(row['Email'])
guest_file.close()

#seed(1)
value = randint(0, len(lucky_person)-1)
print (value)
dash = '-' * 60
print ("\n\n\n\n\n")
print (dash)
print('{:^60s}'.format("From Total of "+str(len(lucky_person)-1)+" Attendants"))
print('{:^60s}'.format("Lucky Email Is:"))
print (dash)
t = lucky_person[value].split("@")
print ('{:^60s}'.format(t[0]+"@xxxxxxxx"))
print (dash)
print ("\n\n\n\n\n")


