# Decorator = A function that extends the behavior of another function
#             without modifying the base function
#             Pass the base function as an argument to the decorator

#             @add_sprinkles
#             get_ice_cream("vanilla")

def add_spinkles(func):
    def wrapper(*args, **kwargs):
        print("* You add sprinkles *")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        # here we return this little chunk of code + our function that we took as input
        print("** You add fudge **")
        func(*args, **kwargs)
    return wrapper

# this is the decorator syntax : @decorator
# the base function is passed as an argument of the decorator
@add_spinkles
@add_fudge
def get_ice_cream(flavor, flavor2):
    print(f"Here is your {flavor} {flavor2} ice cream")

get_ice_cream("vanilla", "chocolate")