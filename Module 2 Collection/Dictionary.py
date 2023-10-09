p={'id':101,'name':'Parth','address':'Halvad'}
print(p)

# print(len(p))
# print(p['name'] )  # Wthouth methods koi specipif value print krva

# print(p.get('address')) # With methods koi specipif value print krva

# print(p.keys()) # only keys=id,name,address print krva

# print(p.values())   # only values=101,Parth,Halvad print krva

# print(p.pop('id'))  #delete krva
# del p['name']   #delete krva

# p['id']=201 # value update krva

# s=p.copy()
# print(s)    # value copy krva

# print(p)

# if 'name' in p:   # only for keys 
#     print('Yes')
# else :
#     print('No')

# if 'Parth' in p.values(): # only for values 
#     print('Yes')
# else :
#     print('no')

# for i in p:     # only for keys 
#     print(i)
    
# for i in p.values():    # only for Values 
#     print(i)

# for i in p.items():     # keys and values banne print krva
#     print(i)

for i,j in p.items():   # keys and values banne print krva
    # print(i,j)
    print(f'{i} - {j}')
