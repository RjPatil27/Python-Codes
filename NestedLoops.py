#This code is for NestedLoops.
# In which students data is available in [name,marks] format, we have to find 2nd highest marks from that data.
""" INPUT : 
2
rajat
38
akshay
34
OUTPUT : 
rajat """

marksheet = []
for _ in range(0,int(raw_input())):
    marksheet.append([raw_input(), float(raw_input())])

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))
