# # a ="String" #string
# # b = True  #boolean
# # c = 1  #integer
# # d =1.4  # float
# # #complex
# # e ='a' # character
#
z = [ i for i in range(1,1000) if i%8==0 ]
print(z)
#
#
test_list = [12, 67, 98, 34]
# test_list.reverse()
# print(test_list)
asd =0
for i in test_list:
     asd+=i
print("THis is sum", asd)
# res = test_list[-1]
# # print(res)
# # sum1=0
# # sum2 = [ i for i in test_list sum+i]
# # print(sum1)
# # d =[]
# # for i in range(:
# #      d.append(i)
# #  print(d)
#
#
# # lis = ["string",1, 1.4,[1,2], 'a',('string1',1), {1:"a"}, ('string',1)]
# # print(lis[-1][0])
# # print(lis[-3][0])
# # n = (1,2,4)
# # print(type(n))
#

test = ["a", "b", "ab", "b", 2, 2, 45, 45, "ab" ]
b = set(test)
c = list(b)
print("this is ",c)
str1 =[]
intr = []
a = type("a")

b = type("ad")
print(b==a)
for i in c:
    a = type(i)
    if a ==b:
        str1.append(i)
    else:
        intr.append(i)


# print(str1)
# print(intr)



a = "sumeet"
a = list(a)
a.reverse()
dic ={}
for i in a:
    if dic.get(i):
        dic[i]=dic.get(i)+1
    else:
        dic[i]=1
print(dic)
del a
fruits =["apple","mango","kiwi","chiku", "banana"]
num = [1,2,3,4]
n = ["grapes" if i == "kiwi" else i for i in fruits if i!="banana"]
# print(n)
p = [(j,i) for i in num if i>1 and i!=3 for j in fruits]
# print(p)
q = [(j,i) for i in num if i>1 and i!=3 for j in fruits if j!="apple" and j!="manago"]
print(q)

dsgdsfhgsfd