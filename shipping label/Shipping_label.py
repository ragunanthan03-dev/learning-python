#Shipping label program
def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg,end=' ')
    print()
    if "apt" in kwargs :
        print(f"{kwargs.get('apt')}",end=',')
        print()
        print(f"{kwargs.get('street')}",end=',')
        print()
        print(f"{kwargs.get('state')}",end=',')
        print()
        print(f"{kwargs.get('country')}",end='.')
    elif "House_no" in kwargs:
        print(f"{kwargs.get('House_no')}",end=',')
        print()
        print(f"{kwargs.get('street')}",end=',')
        print()
        print(f"{kwargs.get('state')}",end=',')
        print()
        print(f"{kwargs.get('country')}",end='.')

    else:
 
        print(f"{kwargs.get('street')}",end=',')
        print()
        print(f"{kwargs.get('state')}",end=',')
        print()
        print(f"{kwargs.get('country')}",end='.')

#Sample input
shipping_label("Mr.","Ben",Tennyson,
               House_no=100,
               street="Boston street",
               state="Boston",
               country="USA"
               )
        
#Output:

"""
Mr. Ragunanthan
100,
Boston street,
Boston,
USA.
"""
