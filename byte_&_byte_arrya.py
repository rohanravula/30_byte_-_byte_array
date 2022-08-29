# a=b"hello rohan"
# print(a,type(a)) #b'hello rohan' 'bytes'
# b=b'ABCD'
# print(list(b)) #[65,66,67,68]
# c=b'abcde'
# print(list(c)) #[97,98,99,100,101]
# d=b'rohan'
# print(tuple(d)) #(114,111,104,97,110)
# e=b'kumar'
# print(set(e)) #{97,107,109,114,117}

"now we want the ASCI values in vertically in bytes"

# y=b"python"
# for r in y:
#     print(r) #now the python asci values will be comming in vertically

"even numbers brackets etc aslo have the ASCI vlauaes"
# a=b"[1,2,3]"
# print(list(a)) #[91,49,44,50,44,51,93]


m=bytearray(b"python")
print(m,type(m))
print(m[0])
m[0]=81
print(m) #(Qython) bytearray