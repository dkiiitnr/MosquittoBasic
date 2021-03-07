# import serial
import sys
# from serial import Serial
# ser  = serial.Serial("com11",9600)
# data = ser.readline(1000)
# print(data)
# a1,a2,a3,a4,a5=input("Enter you name: ").splitlines()

# a1,a2,a3,a4,a5 = input("Enter name:  ").splitlines()
# a1,a2,a3,a4,a5 = sys.stdin.readlines()
# print(a1,a2,a3,a4,a5)

# print("Enter the array:\n")   
# a1,a2,a3 = input().splitlines()

# a1,a2,a3= sys.stdin.readlines()
# print(a1,a2,a3)

# print("Enter the array:\n")   
# userInput = input().splitlines()
# userInput = sys.stdin.readlines()
# print(userInput)





# def multi_input():
#     try:
#         while True:
#             data=input("Enter name:   ")
#             if not data:
#                  break
#             yield data
#     except KeyboardInterrupt:
#         return
# userInput = list(multi_input())
# print(userInput)
for i in range(0,4):
    userInput = input("Enter the array:\n")
    userInput = sys.stdin.readlines()
    userInput.splitlines()
print(userInput)