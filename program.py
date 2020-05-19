# solution to the final project of python data representation course
# with a score of approx. 70-75/100


def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    list1 = list(line1)
    list2 = list(line2)
    length_of_line1 = len(line1)  # length of line1
    length_of_line2 = len(line2)  # length of line2

    if length_of_line1 < length_of_line2:
        if list1[:] == list2[0:length_of_line1]:  # if list1 is smaller and similar to beginning of list2
            if list2[length_of_line1] == " ":
                return length_of_line1 + 1
            else:
                return length_of_line1
        else:
            for i in range(length_of_line1):
                if list1[i] != list2[i]:
                    if list2[i] == " ":
                        return i + 1
                    else:
                        return i

    if length_of_line2 < length_of_line1:
        if list2[:] == list1[0:length_of_line2]:    # if list2 is smaller and similar to beginning of list1
            if list1[length_of_line2] == " ":
                return length_of_line2 + 1
            else:
                return length_of_line2
        else:
            for i in range(length_of_line2):
                if list2[i] != list1[i]:
                    if list1[i] == " ":
                        return i + 1
                    else:
                        return i

    if length_of_line1 == length_of_line2:     # if list1 is equal to list2
        for i in range(length_of_line1):
            if list1[i] != list2[i]:
                return i
        return -1


def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    length_of_line1 = len(line1)
    length_of_line2 = len(line2)

    if idx != singleline_diff(line1, line2):          # invalid index returns an empty string
        return ""
    else:
        pattern = "\n" + "=" * idx + "^\n"           # used to print in given format
        if length_of_line1 > length_of_line2:
            return line1 + pattern + line2 + "\n"
        if length_of_line2 > length_of_line1:
            return line1 + pattern + line2 + "\n"
        if length_of_line1 == length_of_line2:
            return line1 + pattern + line2 + "\n"


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.
      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    diff = False
    line_number = 0

    if len(lines1) <= len(lines2):
        min_line = lines1
        max_len = lines2
    else:
        min_line = lines2
        max_len = lines1

    if not lines1 == lines2:
        line_number = singleline_diff(lines1, lines2)
        diff = True

    if len(max_len) > len(min_line):
        return line_number, 0

    if not lines1 == lines2:
        idx = singleline_diff(lines1[line_number], lines2[line_number])
    else:
        return -1, -1

    if diff:
        return line_number, idx


def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    file = open(filename, "rt")
    lines = [line[:-1] if '\n' in line else line[:] for line in file.readlines()]   # reading lines from file
    file.close()
    return lines


def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    list1 = get_file_lines(filename1)
    list2 = get_file_lines(filename2)
    j = 0
    index = 0
    if len(list1) > len(list2):                                     # if list1 is smaller than list2
        for i in range(len(list2)):
            idx = singleline_diff(list2[i], list1[i])               # finding index from previous function
            if idx != -1:
                j = i
                index = idx
                break

    elif len(list1) < len(list2):                                  # if list2 is smaller than list1
        for i in range(len(list1)):
            idx = singleline_diff(list1[i], list2[i])              # finding index from previous function
            if idx != -1:
                j = i
                index = idx
                break

    elif len(list1) == len(list2):                                 # if both lists are equal
        for i in range(len(list1)):
            idx = singleline_diff(list1[i], list2[i])             # finding index from previous function
            if idx != -1:
                j = i
                index = idx
                break

    if filename1 == filename2:
        return 'No differences\n'
    else:
        a = "Line " + str(j) + ":\n"
        return a + singleline_diff_format(list1[j], list2[j], index)
        
 # submitted by Dhananjay pratap Lodhi
