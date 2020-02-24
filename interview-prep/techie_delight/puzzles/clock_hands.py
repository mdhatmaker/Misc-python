import sys

# https://www.techiedelight.com/angle-between-hour-minute-hand/


def find_angle_between_hands(hh, mm):
    mangle = mm * 360 / 60
    hangle = hh * 360 / 12 + mm / 60 * 360 / 12
    #print(mangle, hangle)
    return int(abs(mangle - hangle) % 180)


if __name__ == "__main__":

    print(find_angle_between_hands(5, 30))      # 15 degrees
    print(find_angle_between_hands(9, 00))      # 90 degrees
    print(find_angle_between_hands(12, 00))     # 0 degrees