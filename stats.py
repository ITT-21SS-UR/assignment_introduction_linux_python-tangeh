import sys
import math

content = ""

# file or stdin?
if len(sys.argv) > 1:
    # read from file
    filename = sys.argv[1]
    content = open(filename).read()
else:
    # read from stdin
    print("Provide numbers:")
    content = sys.stdin.readline()

# calculate mean, median and standard deviation
# convert list into float numbers
content = (str(content).replace(",", ".")).split()
float_list = list()
for i in content:
    float_list.append(float(i))

length = len(float_list)

# mean
sums = 0
for i in float_list:
    sums = sums + i
mean = sums / length

# median
float_list.sort()
if length % 2 == 0:
    index = int(length / 2)
    median = (float_list[index - 1] + float_list[index]) / 2
else:
    index = int(length/2)
    median = float_list[index]

# standard deviation
numerator = 0
for i in float_list:
    sq = (i - mean) * (i - mean)
    numerator = numerator + sq
st_dev = math.sqrt(numerator / (length - 1))

# output
sys.stdout.write("Mean: " + str(mean) + ", Median: " + str(median) + ", Standard deviation: " + str(st_dev))
