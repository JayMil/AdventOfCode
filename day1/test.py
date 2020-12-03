import os

def main():
    script_dir = os.path.dirname(__file__)
    data_file = os.path.join(script_dir, "data.txt")

    f = None
    try:
        f = open(data_file, "r")
        lines = f.readlines()
        ilines = map(int, lines)
        slines = sorted(ilines)

        getTwo(slines)
        getThree(slines)
    except Exception as e:
        print(e)
    finally:
        f.close()


def getTwo(lines):
    print("== Get Two == ")
    ans = 2020
    result = 0
    l = 0
    h = len(lines) - 1

    while(result != ans and h > l):
        result = lines[l] + lines[h]
        
        if result > ans:
            h -= 1
        elif result < ans:
            l += 1
    
    if result == ans:
        print(f"{lines[l]} + {lines[h]} = {result}")
        print(f"{lines[l]} * {lines[h]} = {lines[l]*lines[h]}")
    else:
        print(f"Did not find a sum equal to {ans}")

def getThree(lines):
    print("\n== Get Three == ")
    ans = 2020
    result = 0
    l = 0
    m = 1
    h = len(lines) - 1

    while(result != ans and h > l and h > m and m > l):
        low = lines[l]
        med = lines[m]
        high = lines[h]

        result = low + med + high
        
        if result > ans:
            if h - 1 == m:
                m -= 1
            else:
                h -= 1
        elif result < ans:
            if l + 1 == m:
                m += 1
            else:
                l += 1
    
    if result == ans:
        print(f"{low} + {med} + {high} = {result}")
        print(f"{low} * {med} + {high} = {low * med * high}")
    else:
        print(f"Did not find a sum equal to {ans}")

if __name__ == "__main__":
    main()
