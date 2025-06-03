def parse_ranges(ranges_string):
    num_range  = (i for i in ranges_string.split(',')) # list split by ','         for example ['1-2', '4-4', '8-10']
    ranges     = (num.split('-') for num in num_range) # list in list split by '-' for example [['1', '2'], ['4', '4'], ['8', '10']]
    result     = (range(int(x[0]), int(x[1])+1) for x in ranges) # convert list to range range(1, 3) range(4, 5) range(8, 11)
    new_result = (x for y in result for x in y) # print all the ranges to list

    return new_result


print(list(parse_ranges("1-2,4-4,8-10")))
print(list(parse_ranges("0-0,4-8,20-21,43-45")))
print(list(parse_ranges("0-0,4-8,20-21,43-45,103-125")))
