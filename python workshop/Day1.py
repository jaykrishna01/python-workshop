
from itertools import product
from itertools import combinations
from itertools import permutations
from itertools import combinations_with_replacement
# # print("Hello parmeet kaddu")
# t=(1,2,3,4,5,6,"GLA UNIVERSITY")
# print(t)
# print(type(t))
# j=list(t)
# j.append("raju")
# n=tuple(j)
# print(n)
# l=["liz",1.73,"mom",4.44,]
# a=[1,2]
# b=[3,4]
# c=list(product(a,b))
# print(c)
# a=list(map(int,input().split))
# b=set(map(int,input().split()))\

# hackerrank itertool product code 
# code start ------------
# from itertools import product
# a=list(map(int,input().split()))
# b=list(map(int,input().split()))
# c=list(product(a,b))
# for i in c:
#     print(i,end=" ")
    # code start -----------
# *****************
# use of itertool combinations
# print(list(combinations("hac",2)))
# output
# [('h', 'a'), ('h', 'c'), ('a', 'c')]
# *************************
#********** use of itertools permutations***
# print(list(permutations("raj",2)))
# [('r', 'a'), ('r', 'j'), ('a', 'r'), ('a', 'j'), ('j', 'r'), ('j', 'a')]
# ******************************
# use of combinations with replacement 
# print(list(combinations_with_replacement("raj",3)))
# print(list(combinations((1,2,3,4),2)))

 # Enter your code here. Read input from STDIN. Print output to STDOUT
# from itertools import combinations
# n=int(input())
# j=[]
# a=0
# for i in range(1,n+1):
#     j.append(i)
# l=list(map(str,input().split()))
# k=int(input())
# m=list(combinations(j,k))
# # print(m)
# for z in range(len(m)):
#     for g in range(k):
#         if(m[z][g]==1 or m[z][g]==2):
#             a=a+1
# print(a)            
# v=a/len(m)  
# print(v)        
# # print(f"{v:.4f}")  
# l=[(1,2),(3,2)]
# print(sum(l[0]))
# if):
#     print("yes")
# else:
#     print("sory")    


    # Enter your code here. Read input from STDIN. Print output to STDOUT
# from itertools import combinations
# n=int(input())
# j=[]
# a=0
# for i in range(1,n+1):
#     j.append(i)
# l=list(map(str,input().split()))
# k=int(input())
# m=list(combinations(j,k))
# # print(m)
# for z in range(len(m)):
#     for g in range(k):
#         if(m[z][g]<=2 or m[z][g]==2):
#             a=a+1
#         if(m[z][g]==1 and m[z][g+1]==2):
#             a=a-1    
# # print(a)            
# v=a/len(m)  
# print(v)        
# # print(f"{v:.4f}")  

# # formatted = "{:.3f}".format(9.999) 


# h=int(input())
# f=int(input())
# c=int(input())
# if(h>f and h>c):
#     print(f"{h} is greater than {f} and {c}")
# elif(f>h and f>c):
#     print(f"{f} is greater than {h} and {c}")
# elif(c>f and c>h):
#     print(f"{c} is greater than {f} and {h}")    

a=(1,2)
print(sum(a))

