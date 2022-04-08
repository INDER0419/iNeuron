# =============================================================================
# 1. Write a program which will find all such numbers which are divisible by 7 but are not a
# multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed 
# in a comma-separated sequence on a single line
# 
# =============================================================================

output_list = []
for i in range(2000,3201):
    if (i%7 ==0) and (i%5==0):
        output_list.append(str(i))
print(",".join(output_list))

# =============================================================================
# 
# 2.Write a Python program to accept the user's first and last name and then getting them
# printed in the the reverse order with a space between first name and last name.
# =============================================================================

first_name = input("Enter your firstname : " )
last_name = input("Enter your lastname : " )
print("my name is "+last_name+" "+first_name)


# =============================================================================
# 3.Write a Python program to find the volume of a sphere with diameter 12 cm
# Formula: V=4/3 * π * r 3
# =============================================================================
pi=3.1415
Vol = (4.0/3)*pi* (12**3)

