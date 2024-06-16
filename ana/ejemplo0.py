# https://www.python.org
X=20
def ana(X):
    while X>0:
        print (X)
        X=X-2
    print("checabo")


print(ana.__doc__)
ana(X)