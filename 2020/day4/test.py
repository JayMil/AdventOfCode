import os
import re
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
        lines = reader.readlines()
        return list(map(trimNewline, lines))

# Trim newline character off line
def trimNewline(line):
    return line.rstrip('\n')

# Count valid passports in input data array
# Getting 203, but correct answer was 204?
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
        self.fields = {
                "byr": None, "iyr": None, "eyr": None,
                "hgt": None, "hcl": None, "ecl": None,
                "pid": None, "cid": None
        }

        elements = record.split()
        for element in elements:
            key, value = element.split(":")
            self.fields[key] = value

    def isValid(self):
        if (not (self.fields["byr"] is not None and self.fields["iyr"] is not None 
            and self.fields["eyr"] is not None and self.fields["hgt"] is not None
            and self.fields["hcl"] is not None and self.fields["ecl"] is not None 
            and self.fields["pid"] is not None)):
            return False

        # 1920 - 2002
        p = re.compile("1\d[2-9]\d|200[0-2]")
        m = p.match(self.fields["byr"])
        if (not m):
            return False

        # 2010 - 2020
        p = re.compile("20[1-2]\d|200[0-2]")
        m = p.match(self.fields["iyr"])
        if (not m):
            return False

        eyr = int(self.fields["eyr"])
        if (not (eyr >= 2020 and eyr <= 2030)):
            return False
        





    def __str__(self):
        return f"Passport({self.fields})"

if __name__ == "__main__":
    main()
