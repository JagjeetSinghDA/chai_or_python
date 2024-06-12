# def print_kwargs(name, power):
#     print("Name:", name, "Power:", power)

# print_kwargs(name = 'Shaktimaan', power = 'Laser')



def print_kwargs(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}", sep = ", ")

print_kwargs(name = 'Shaktimaan', power = 'Laser', enemy = 'Dr. Jackaal', mitra = 'ginny')