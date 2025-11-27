import sys

if len(sys.argv) == 2:
    script_name = sys.argv[0]
    temp = sys.argv[1]
else:
    temp = 25

if temp > 40:
    print("Hot")
elif temp > 20:
    print("Normal")
else:
    print("Cold")