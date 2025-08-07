#Loops in Python 
# for a in range(2,50):
#     print("Girand Operation")


# a = 0
# while a < 10:
#     print("While Loop Operation")
#     a += 1
    
# for a in range(1, 10):
#     if a % 2 == 0:
#         print(a)

# a = 1
# while a <= 10:
#     if a % 2 == 0:
#         print(a)
#     a += 1

# for a in range(1, 10):
#     if a==5:
#         continue
#     print(a)

password = input("Enter your password: ")

while password != "secret123":
    print("Incorrect password, try again.")
    password = input("Enter your password: ")

print("Access granted")