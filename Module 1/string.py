sp=("Hello i am PARTH chavda!!!") 
print(len(sp))  #space sahit character ni calculation krva
print(sp.strip())   #paragraph ni starting space/tab apel hoy to tene dur krva
print(sp.lower())   # all character ne Small character ma convert krva 
print(sp.casefold())    # this word like (.lower) string
print(sp.upper())   # all character ne capital character ma convert krva
print(sp.replace('PARTH','Parth'))  #Je-te character ke word ne Je-te Character ke word ma convertv krva mate
print(sp.split())   #all word me ( , ) api alg krva
print(sp.capitalize())  #Paragraph na first character ne capital kri baki na character me small krva
print(sp.count('a'))    # je-te character ne count krva
print(sp.title())   #Paragraph na all word na first character ne Capital krva
print(sp.find("am"))  #Loction find krva 
print(sp.index("am"))  #Loction find krva 
#-------Blooling String--------
print("\n")
print(sp.startswith("Hello"))   #paragraph (Hello) thi start thati hoy to true otherwise false
print(sp.endswith('!'))     #paragraph ( ! ) thi end thati hoy to true otherwise false
print(sp.isalpha())     #all character Alphabet hoy to true otherwise false
print(sp.isdigit())     #all character Numberic hoy tu True otherwise false
print(sp.isalnum())     #Alphabet and number banne type krva 
print(sp.islower())   #all character small hoy to True otherwise false
print(sp.isupper())   #all character capital hoy to True otherwise false
