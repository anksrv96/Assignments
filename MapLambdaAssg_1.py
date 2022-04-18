def lambda_demo(a,b,c,x):
    f = lambda a, b, c, x : (a*x*x) + (b*x) + c

    print(f(a, b, c, x))


lambda_demo(2,3,4,5)