

def checksum(fix_message):
    cks = 0
    for idx in range(0, len(fix_message)):
        cks += ord(fix_message[idx])

    return cks % 256


def checksum_diff(int_value):
    zero = ord('0')
    diff = 0
    for idx in range(0, len(int_value)):
        diff += ord(int_value[idx]) - zero

    return diff



strZero = "PRICE=0000"
cksZero = checksum(strZero)

strA = "PRICE=2186"
strB = "PRICE=2252"
print checksum(strA)
print checksum(strB)

print cksZero + checksum_diff("2252")


# pre-build fix messages: (example) for each instrument used by the model,
# a submit, a mod, and a cancel (plus perhaps others for ack, etc.)

# calculate the checksum for these pre-built messages using some placeholder
# for numbers like price and qty (such as "0000000" or "000")

# build a lookup cache (array) that is populated with various numbers
# (say [0] - [999] for the "000" placeholder) and store the checksum delta
# for that number at each array location
# (example) [0]=0, [1]=1, [2]=2, ... [22]=2+2=4, [23]=2+3=5, ...

# since the checksum is mod 256, we may be able to compute a shortcut rather
# than create a huge array....but maybe not (if the speed is much better on a
# straight array lookup compared to even modest arithmetic)

