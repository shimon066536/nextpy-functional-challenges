"""
range_string_parser.py

Parses a string like '1-2,4-4,8-10' into a list of integers using generator expressions.
"""

def parse_ranges(ranges_string):
    num_range  = (i for i in ranges_string.split(','))
    ranges     = (num.split('-') for num in num_range)
    result     = (range(int(x[0]), int(x[1]) + 1) for x in ranges)
    new_result = (x for y in result for x in y)
    return new_result

def main():
    example = "1-2,4-4,8-10"
    print(f"Parsing ranges from: {example}")
    print(list(parse_ranges(example)))

if __name__ == "__main__":
    main()
