def getStart():
    start = int(input("Starting value:  "))
    return start
  
def getEnd():
    end = int(input("Ending value:  "))
    return end

def mulTable(start, end):
    # Print top left cell
    print "{0:<4}".format("X"),

    # Print header row
    for h in range(start, end+1):
        if h != end:
            print "{0:<4}".format(h),
        else:
            print "{0:<4}".format(h)

    for i in range(start, end+1):
        # Print starting value first
        print "{0:<4}".format(i),

        for j in range(start, end+1):
            result = i*j
            # End of a row
            if j == end:
                print "{0:<4}".format(result)
            # Non-ending row value
            else:
                print "{0:<4}".format(result),
      
def main():
  start = getStart()
  end = getEnd()
  mulTable(start, end)
  
main()
input()

