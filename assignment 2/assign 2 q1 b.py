a = "Python is a case sensitive language"
men= a [::-1] 
print(men)
#question c
start_word ="a"
end_word ="language"
start = a.find(start_word)
end = a.find(end_word)
b = slice(start,end)
b = a[b]
print(b)
#question d
d = a.replace("a case sensetive","object oriented")
print(d)
#question e
e = a.index("a")
print(e)
#question f
f = a.replace(" ","")
print(f)
#end
