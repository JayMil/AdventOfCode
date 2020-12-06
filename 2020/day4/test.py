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
def processPassportData(lines):
    record = ""
    ppCount = 0
    validPassports = 0
    for i, line in enumerate(lines):
        if len(line) == 0 or i == len(lines)-1:
            if i == len(lines)-1:
                record += line + " "

            ppCount += 1
            pp = Passport(record)
            if pp.isValid():
                validPassports += 1
            record = ""
        else:
            record += line + " "

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

    def isValidOld(self):
        return  (self.fields["byr"] is not None and self.fields["iyr"] is not None 
            and self.fields["eyr"] is not None and self.fields["hgt"] is not None
            and self.fields["hcl"] is not None and self.fields["ecl"] is not None 
            and self.fields["pid"] is not None)


    def isValid(self):
        if (not (self.fields["byr"] is not None and self.fields["iyr"] is not None 
            and self.fields["eyr"] is not None and self.fields["hgt"] is not None
            and self.fields["hcl"] is not None and self.fields["ecl"] is not None 
            and self.fields["pid"] is not None)):
            return False

        # 1920 - 2002
        p = re.compile("1\d[2-9]\d|200[0-2]$")
        m = p.match(self.fields["byr"])
        if (not m):
            return False

        # 2010 - 2020
        p = re.compile("20(1\d|20)$")
        m = p.match(self.fields["iyr"])
        if (not m):
            return False

        # 2020 - 2030
        p = re.compile("20(2\d|30)$")
        m = p.match(self.fields["eyr"])
        if (not m):
            return False
        
        # 150cm - 193cm  or  59in - 76in
        p = re.compile("1([5-8]\d|9[0-3])cm|(59|6\d|7[0-6])in")
        m = p.match(self.fields["hgt"])
        if (not m):
            return False


        # #000000 - #ffffff
        p = re.compile("#[0-f]{6}$")
        m = p.match(self.fields["hcl"])
        if (not m):
            return False

        p = re.compile("(amb|blu|brn|gry|grn|hzl|oth)$")
        m = p.match(self.fields["ecl"])
        if (not m):
            return False

        p = re.compile("(\d{9})$")
        m = p.match(self.fields["pid"])
        if (not m):
            return False
        
        return True

    def __str__(self):
        return f"Passport({self.fields})"

if __name__ == "__main__":
    main()
