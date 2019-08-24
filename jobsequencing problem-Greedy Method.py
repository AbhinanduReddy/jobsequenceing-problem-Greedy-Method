def jobprofitseq(res,l,j):
    print(res)
    print(j)
             
    res=dict(sorted(res.items(),reverse=True))
    print(res)
    job=[0]*len(res)
    p=0
    for i,j in zip(res.keys(),res.values()):
        while j>0 and j<=l:
            if job[j]==0:
                p=p+i
                job[j]=i
                break
            j=j-1
            
    return (job,p)      
        
            
    
    
    
p=[20,15,10,5,1]
d=[2,2,1,3,3]
j=['a','b','c','d','e']
l=3
res=dict(zip(p,d))
job,p=jobprofitseq(res,l,j)
print(job,p)
