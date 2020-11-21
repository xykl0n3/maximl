def maxsubstrlen(s):
    k=len(s)
    if k==0 or k==1:
        print(k)
    maxchar=count(s)
    minimum=k+1
    a={}
    start=0
    a[s[start]]=1
    for i in range(1,k):
        if s[i] in a:
            a[s[i]]+=1
        else:
            a[s[i]]=1
        if len(a)==maxchar:
            while start<i and a[s[start]]>1:
                a[s[start]]-=1
                start+=1
            if minimum>i+1-start:
                minimum=i+1-start
    print(minimum)
 
    
def count(s):
    p={}
    for i in s:
        if i in p:
            p[i]+=1
        else:
            p[i]=1
    return len(p)
    
s=str(input())
maxsubstrlen(s)