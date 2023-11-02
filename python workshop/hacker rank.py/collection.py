from collections import Counter
# collections counter
# l=[1,1,2,3,3,5,6,1,2,3,4,5,6,7,8,9]
# print(Counter(l))
# print(Counter(l).items())# it return (number , how many times the number present in the list)
# print(Counter(l).keys())
# print(Counter(l).values())

# l=[1,2,3,4,5,6]
# print(l.index(6))
def merge_the_tools(string, k):
    for i in range(0,len(string),3):
        s=string[i:k+i]
        f=" ".join(s)
        m=f.split()
        # print(m)
        for j in range(0,len(m)):
            if(m.count(m[j])>1):
                m.pop(j)
                print("".join(m))
                break
        # 

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    # AABCAAADA