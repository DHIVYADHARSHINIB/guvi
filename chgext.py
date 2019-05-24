rupee=int(input("enter the number:"))
count=0
count1=0

for i in range(0,rupee,5):
       if(i<(rupee-1)):
         count=count+1
         
       else:
          for j in range(i,rupee+1,1):
             if(j==rupee):
               count1=count1+1
              
           
            
print(count)
print(count1)
