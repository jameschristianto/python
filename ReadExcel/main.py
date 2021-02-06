import sys
import xlrd

# write location file / filename
loc = "data.xlsx"
# open file
wb = xlrd.open_workbook(loc)
# select sheet excel
sheet = wb.sheet_by_index(0)

# print total rows
print("Total row : " + str(sheet.nrows))
# print total columns
print("Total column : " + str(sheet.ncols) + "\n")

# declare looping variable
# skip first row
i = 1
# max range
j = 2
# skip first column
k = 1

# declare variable for place data
data = []

# looping rows and cols for print data
for w in range(sheet.nrows - 1):
    for x in range(i, j):
        for y in range(k, sheet.ncols):
            # print(sheet.cell_value(x, y))
            if 2 <= y <= 5:
                if sheet.cell_value(x, y) == "Besar":
                    data.append(1)
                elif sheet.cell_value(x, y) == "Sedang":
                    data.append(2)
                elif sheet.cell_value(x, y) == "Kecil":
                    data.append(3)
            else:
                if sheet.cell_value(x, y) == "Besar":
                    data.append(3)
                elif sheet.cell_value(x, y) == "Sedang":
                    data.append(2)
                elif sheet.cell_value(x, y) == "Kecil":
                    data.append(1)
        # print("\n")
    i = i + 1
    j = j + 1

# print total data
print("Total data : " + str(len(data)))
print("")

# declare score variable
max_score = 0
min_score = sys.maxsize

# print data number
# for z in range(len(data)):
#     print(data[z])

for a in range(0, len(data), 7):
    score = (20/100*data[a]) + (15/100*data[a + 1]) + (10/100*data[a + 2]) + (10/100*data[a + 3]) \
            + (20/100*data[a + 4]) + (15/100*data[a + 5]) + (10/100*data[a + 6])

    # round 2 digit after comma
    score = round(score, 2)

    # print score
    # print(score)

    # get max score
    if score > max_score:
        max_score = score

    # get min score
    if score < min_score:
        min_score = score

# print max score & min score
print("Max score : " + str(max_score))
print("Min score : " + str(min_score))
