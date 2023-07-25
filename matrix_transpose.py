""" x = [[12,7],
    [4 ,5],
    [3, 8]   
]

result = [[0,0,0],
          [0,0,0]]


# iterate through rows

for i in range(len(x)):
    # iterate through columns
    for j in range(len(x[0])):
        result[j][i] = x[i][j]

for r in result:
    print(r) """
    
    
''' Program a transpose a matrix using list comprehension'''

x = [[12,7],
     [4,5],
     [3, 8]]

result = [[x[j][i] for j in range(len(x))] for i in range(len(x[0]))]

for r in result:
    print(r)
