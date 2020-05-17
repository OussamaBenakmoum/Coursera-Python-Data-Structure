
#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#                   From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.


try:
    name = input("Enter file:")
except : 
    name = "mbox-short.txt"
handle = open(name)

distribution = dict()

for line in handle:
    words = line.split(' ')
    if words[0].upper() == "FROM":
        hrs = words[6].split(':')[0]
        if hrs in distribution:
            distribution[hrs] = distribution[hrs] + 1
        else:
            distribution[hrs] = 1

for key, value in sorted(distribution.items()):
    print (key,value)