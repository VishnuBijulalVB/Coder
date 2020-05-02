def timeConversion(s):
    t = s.strip('APM').split(':')
    t[0] = int(t[0])
    t[0] = t[0] % 12
    if 'PM' in s:
        if t[0] != 12:
            t[0] = t[0] + 12
    else:
        if t[0] == 12:
            t[0] = 0
    t[0] = str(t[0]).zfill(2)
    time = ':'.join(t)
    return time


s = input("Enter time\n")
result = timeConversion(s)
print(result)
