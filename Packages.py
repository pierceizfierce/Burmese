#Packages (refer to ecommerce folder and files that go with this)
#Another way to organize multiple modules
#for example a store has a mens, womens, and kids section
#right click abnd create a directory, then a py file called __init__
#import ecommerce.shipping
#ecommerce.shipping.calc_shipping() #this is cumbersome but needed in some instances

# #this will import just this function. if you add comma you can add multiple functions:
# from ecommerce.shipping import calc_shipping

# #it can then be called like this
# calc_shipping()

# #this makes the shipping module an object
# from ecommerce import shipping
#
# #now you can use the dot operator
# shipping.calc_shipping()

#Jango uses packages for python

