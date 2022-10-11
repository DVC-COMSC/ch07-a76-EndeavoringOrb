
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

if len(num1) == len(num2) or len(num1) < len(num2):
    merged_result = num1 + num2
else:
    merged_result = num2 + num1

print(merged_result)

# ******************************
# Make your Code
# ******************************

# print (num3) 
