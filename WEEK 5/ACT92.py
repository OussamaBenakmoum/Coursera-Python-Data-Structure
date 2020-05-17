#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender s mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
llc = list()
count = dict()
for line in handle:
    if line.startswith('From'):
        if line.startswith('From:') : continue
        lst = line.split()
        llc.append(lst[1])
for name in llc:
    count[name]=count.get(name,0)+1

largest = -1;
for clefs,value in count.items():
    if value > largest : 
        keysup = clefs
        largest = value

print(keysup,largest)
    
