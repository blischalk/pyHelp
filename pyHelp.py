# Set a global variable that all table formatting will reference
formatter_string = "{0:<4}"

def getStart():
    start = int(input("Starting value:  "))
    return start
  
def getEnd():
    end = int(input("Ending value:  "))
    return end

def mulTable(start, end):
    # Print top left cell
    # Look into format. This allows columns to be
    # a specific width so output looks nice
    # See: https://stackoverflow.com/questions/19103052/python-string-formatting-columns-in-line
    # Notice the comma at the end of the line.
    # This will continue to print the values on the same line
    # until a print statement without a comma is encountered
    # See: https://stackoverflow.com/questions/5598181/python-multiple-prints-on-the-same-line
    print formatter_string.format("X"),

    # Print header row
    # We increase end by 1 because the range() is not
    # inclusive of the final value
    # See https://docs.python.org/2.7/library/functions.html#range
    for h in range(start, end+1):
        if h != end:
            print formatter_string.format(h),
        else:
            print formatter_string.format(h)

    for i in range(start, end+1):
        # Print starting value first to generate
        # the left hand column with the operand
        print formatter_string.format(i),

        for j in range(start, end+1):
            result = i*j
            # End of a row
            if j == end:
                print formatter_string.format(result)
            # Non-ending row value
            else:
                print formatter_string.format(result),
      
def main():
  start = getStart()
  end = getEnd()
  mulTable(start, end)
  
main()
input()

