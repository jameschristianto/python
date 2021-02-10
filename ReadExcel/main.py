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

# declare variable for place data array 2D
data_array2d = [[0 for r in range(sheet.ncols - 1)] for s in range(sheet.nrows - 1)]

# # looping rows and cols for print data
# for w in range(sheet.nrows - 1):
#     for x in range(i, j):
#         # print("x = " + str(x))
#         for y in range(k, sheet.ncols):
#             # print("y = " + str(y))
#             # print(sheet.cell_value(x, y))
#             if 2 <= y <= 5:
#                 if sheet.cell_value(x, y) == "Besar":
#                     data.append(1)
#                 elif sheet.cell_value(x, y) == "Sedang":
#                     data.append(2)
#                 elif sheet.cell_value(x, y) == "Kecil":
#                     data.append(3)
#             else:
#                 if sheet.cell_value(x, y) == "Besar":
#                     data.append(3)
#                 elif sheet.cell_value(x, y) == "Sedang":
#                     data.append(2)
#                 elif sheet.cell_value(x, y) == "Kecil":
#                     data.append(1)
#         # print("\n")
#     i = i + 1
#     j = j + 1

# looping rows and cols for print data_array2d
for m in range(1, sheet.nrows):
    for n in range(1, sheet.ncols):
        if 2 <= n <= 5:
            if sheet.cell_value(m, n) == "Besar":
                data_array2d[m - 1][n - 1] = 1
                data.append(1)
            elif sheet.cell_value(m, n) == "Sedang":
                data_array2d[m - 1][n - 1] = 2
                data.append(2)
            elif sheet.cell_value(m, n) == "Kecil":
                data_array2d[m - 1][n - 1] = 3
                data.append(3)
        else:
            if sheet.cell_value(m, n) == "Besar":
                data_array2d[m - 1][n - 1] = 3
                data.append(3)
            elif sheet.cell_value(m, n) == "Sedang":
                data_array2d[m - 1][n - 1] = 2
                data.append(2)
            elif sheet.cell_value(m, n) == "Kecil":
                data_array2d[m - 1][n - 1] = 1
                data.append(1)

# print total data
print("Total data : " + str(len(data)))
print("")

# declare score variable
max_score = 0
min_score = sys.maxsize

# print data number
counter = 1
for z in range(len(data)):
    print(data[z], end=' ')
    if counter == sheet.ncols - 1:
        print(" ")
        counter = 0
    counter += 1

print(" ")

# print data_array2d number
for p in range(sheet.nrows - 1):
    for q in range(sheet.ncols - 1):
        print(data_array2d[p][q], end=' ')
    print(" ")


for a in range(0, len(data), sheet.ncols - 1):
    score = (20 / 100 * data[a]) + (15 / 100 * data[a + 1]) + (10 / 100 * data[a + 2]) + (10 / 100 * data[a + 3]) \
            + (20 / 100 * data[a + 4]) + (15 / 100 * data[a + 5]) + (10 / 100 * data[a + 6])

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
print(" ")
print("Max score : " + str(max_score))
print("Min score : " + str(min_score))
