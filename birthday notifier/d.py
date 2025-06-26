n=int(input())
l=[]
for i in range(n):
	l.append(input())
c=0
if n==0 or n==1 or n==2:
 	print(0)
else: 
    l1=l[0]
    l2=l[1]
  
    for i in range(2,n):
        if l[i]==l1 or l[i]==l2:
            continue
        else:
            for j in range(i+1,n):
          	    if j<n-1 and l[j]==l1:
          	        l2=l[i]
                    c+=1
                    break
    		    else if j<n-1 and l[j]==l2:
          	        l1=l[i]
          	        c+=1
    	    	    break
            else:
          	    l1=l[i]
          	    c+=1

print(c)