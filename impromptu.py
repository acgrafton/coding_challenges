def digitSumsDifference(n):
    num_digits = len(str(n))

    even_sum = 0
    odd_sum = 0
    
    while num_digits > 0:
        
        digit = n % (10 ** num_digits) // (10** (num_digits -1))
        
        if digit % 2 == 0:
            even_sum += digit
        
        else:
            odd_sum += digit
        num_digits -= 1
        
    return even_sum - odd_sum

def alarmClock(setTime, timeToSet):

    setTimeHr, setTimeMin = map(int, setTime.split(':'))
    timeToSetHr, timeToSetMin = map(int, timeToSet.split(':'))

    higherHr = max(setTimeHr, timeToSetHr)
    lowerHr = min(setTimeHr, timeToSetHr)
    higherMin = max(setTimeMin, timeToSetMin)
    lowerMin = min(setTimeMin, timeToSetMin)

    chgHr = (24 - higherHr) + lowerHr if lowerHr < 12 < higherHr else higherHr - lowerHr
    chgMin = (60 - higherMin) + lowerMin if lowerMin < 30 < higherMin else higherMin - lowerMin

    return chgHr + chgMin


print(alarmClock('07:30', '08:00'))
print(alarmClock('23:45', '08:15'))
print(alarmClock('21:15', '09:25'))
print(alarmClock('00:00', '00:00'))
print(alarmClock('08:00', '21:00'))
