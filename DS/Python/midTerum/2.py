# import urllib.request
# url = "https://robjhyndman.com/tsdldata/ecology1/hopedale.dat"
# with urllib.request.urlopen(url) as file:
#     for line in file:
#         line = line.strip()
#         line = line.decode("utf-8")
#         print(line)

def skip_header(input_file) -> None:
    line = input_file.readline()
    while line.startswith("#"):
        line = input_file.readline()
    return line

def process_file(input_file) -> None:
    line = skip_header(input_file) # Skip header
    return line

with open('input.txt', 'r') as students:
    line = process_file(students)


print(line)

with open('input.txt','r') as file:
    lines = file.readlines()

print(lines)

with open('input.txt','r') as file:
    line = file.readline()

print(line)

with open('output.txt','a') as file:
    file.write("programming")