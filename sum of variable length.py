def hello(*variable):
    sum=0
    for i in variable:
        sum=sum+i
    print(sum)
  
hello(10,20,30)
hello(100,200,23,41)
hello(100,34,36)