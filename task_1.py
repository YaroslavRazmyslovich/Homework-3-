first_line = input ('please enter the first line: ')
second_line = input ('please enter the second line: ')
print ('you entered two lines:', '\033[4m', first_line, '\033[0m', 'and', '\033[4m', second_line, '\033[0m')
print ('their length respectively', len (first_line), 'and', len (second_line))
print ('first symbol of first line -', first_line[0])
print ('last symbol of second line -', second_line[-1])
print ('the first line is equal to the second line?', first_line == second_line)
print ('the second line contains the first line?', first_line in second_line)
print ('the first line contains the second line?', second_line in first_line)
