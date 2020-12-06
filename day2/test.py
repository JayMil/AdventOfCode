import os

def main():
    script_dir = os.path.dirname(__file__)
    data_file = os.path.join(script_dir, "data.txt")

    f = None
    try:
        f = open(data_file, "r")
        lines = f.readlines()
        countValidPasswords(lines)
    except Exception as e:
        print(e)
    finally:
        f.close()


def countValidPasswords(lines):
    valid = 0
    actuallyValid = 0
    for line in lines:
        parts = line.split()

        policy = parts[0]
        lowhigh = policy.split("-")
        low = int(lowhigh[0])
        high = int(lowhigh[1])

        letter = parts[1][0]

        password = parts[2]

        if isValidPassword(low, high, letter, password):
            valid += 1

        if isActuallyValidPassword(low, high, letter, password):
            actuallyValid += 1

    print(f"Found {valid} passwords")
    print(f"Found {actuallyValid} actual passwords")

    return valid


def isActuallyValidPassword(first, second, letter, password):
    return (password[first-1] == letter) ^ (password[second-1] == letter)


def isValidPassword(low, high, letter, password):
    count = 0
    for l in password:
        if l == letter:
            count += 1

    return count >= low and count <= high



if __name__ == "__main__":
    main()
