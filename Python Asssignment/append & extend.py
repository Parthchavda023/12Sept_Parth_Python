'''Differentiate between append () and extend () methods? '''

p=["Parth",'Sanjay','Vipul','Pankaj','Prakash']
print('orignal list:-',p)

#--------Append---------#
p.append("Mehul") # append thi list ma only one value j add kri skay
print("\nAppend:-",p)

# -------Extend---------#
s=['Mandeep','Dixit','Raj']
sp=p.extend(s)     # Extend thi list ma multiple valuee add kri skay
print('\nExtend:-',p)
