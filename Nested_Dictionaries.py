#1
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(f'{x}\n')

students[0]['last_name'] = 'Bryant'
print(f'{students}\n')

sports_directory.update({'soccer': ['Andres', 'Ronaldo','Rooney'] })
print(f'{sports_directory}\n')

z[0]['y'] = 30
print(f'{z}\n')

#2
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

a = {}
def iterateDictionary(s):
    for i in range(0, len(s)-1):
        a = ""
        for k,v in s[i].items():
            a += f'{k} - {v},'
        print(a)
iterateDictionary(students)
print()

#3
def iterateDictionary2(name,g):
    for e in range(0, len(g)):
        for w,x in g[e].items():
            if w == name:
                print(x)
iterateDictionary2('first_name',students)
print()
iterateDictionary2('last_name',students)
print()

#5
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def Print_info(dict):
    for key,val in dict.items():
        print("--------------")
        print(f'{len(val)} {key.upper()}')
        for i in range(0, len(val)):
            print(val[i])
            
Print_info(dojo)