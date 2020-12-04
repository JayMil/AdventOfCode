import os
import traceback

def main():
    try:
        data = getData()
        processPassportData(data)
    except Exception as e:
        traceback.print_exc()

# Read data from file and return array of lines without newline characters
def getData():
    script_dir = os.path.dirname(__file__)
    data_file = os.path.join(script_dir, "data.txt")
    with open(data_file, "r") as reader:
        lines = f.readlines()
        return list(map(trimNewline, lines))

# Trim newline character off line
def trimNewline(line):
    return line.rstrip('\n')

#
def processPassportData(lines):
    record = ""
    ppCount = 0
    validPassports = 0
    for line in lines:
        if len(line) > 0:
            record += line + " "
        else:
            ppCount += 1
            pp = Passport(record)
            #print(pp)
            if pp.isValid():
                validPassports += 1
            else:
                print(f"'{pp.record}'")
                print(f"'{pp}'is {pp.isValid()}")
            record = ""

    print(f"Got {ppCount} Passports")
    print(f"Got {validPassports} valid passports")



class Passport:
    def __init__(self, record):
        self.record = record
        self.byr = None
        self.iyr = None
        self.eyr = None
        self.hgt = None
        self.hcl = None
        self.ecl = None
        self.pid = None
        self.cid = None

        elements = record.split()
        for element in elements:
            key, value = element.split(":")
            if key == "byr":
                self.byr = value
            elif key == "iyr":
                self.iyr = value
            elif key == "eyr":
                self.eyr = value
            elif key == "hgt":
                self.hgt = value
            elif key == "hcl":
                self.hcl = value
            elif key == "ecl":
                self.ecl = value
            elif key == "pid":
                self.pid = value
            elif key == "cid":
                self.cid = value
            else:
                raise Exception(f"Key '{key}' Not Found!")

    def isValid(self):
        return (self.byr is not None and self.iyr is not None 
                and self.eyr is not None and self.hgt is not None
                and self.hcl is not None and self.ecl is not None 
                and self.pid is not None)

    def __str__(self):
        return (f"byr:'{self.byr}' "
                f"iyr:'{self.iyr}' "
                f"eyr:'{self.eyr}' "
                f"hgt:'{self.hgt}' "
                f"hcl:'{self.hcl}' "
                f"ecl:'{self.ecl}' "
                f"pid:'{self.pid}' "
                f"cid:'{self.cid}'")


if __name__ == "__main__":
    main()
