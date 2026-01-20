
# // Fill along the length of the strip in various colors.
# // duration: 9 * LED_COUNT * 40ms = 8.280s
# colorWipe(col_red     , 40);
# colorWipe(col_green   , 40);
# colorWipe(col_blue    , 40);
# colorWipe(col_cyan    , 40);
# colorWipe(col_yellow  , 40);
# colorWipe(col_purple  , 40);
# colorWipe(col_white   , 40);
# colorWipe(col_white2  , 40);
# colorWipe(col_off     , 40);

LED_COUNT = 23
FRAME = 0

def colorWipe(color, ms):
    global FRAME, LED_COUNT
    for n in range(1, LED_COUNT+1):
        print(f"- time: '+{ms}ms'\n  lights:\n    l_{n}: {color}\n")
        FRAME += 1

print('#show_version=6')
print(f"- time: 0\n  lights:\n    l_1: off\n")

colorWipe('red',     40)
colorWipe('green',   40)
colorWipe('blue',    40)
colorWipe('cyan'   , 40)
colorWipe('yellow' , 40)
colorWipe('purple' , 40)
colorWipe('white'  , 40)
colorWipe('off'    , 40)