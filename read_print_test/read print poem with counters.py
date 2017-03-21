#   This reads and prints the whole document.
#           It does not prt a blank line after each line of the file

name_of_mydocument = 'tuesdayafternoon.txt'
file_input = open(name_of_mydocument, 'r')     #open file for reading

line = file_input.readline()
print(line, end='')

line = file_input.readline()
print(line, end='')

line = file_input.readline()
print(line, end='')

line = file_input.readline()

line_counter = 0
stanza_counter = 1
total_lines_in_file = 3

while line != '':                      # while not end of file

    if line == '\n':
      total_lines_in_file +=1
      stanza_counter += 1
      print ()
    else:
      line_counter += 1
      if line_counter <= 9:
        print(line_counter,')', '   ', line, end = '')   # don't print another new line
      else:
        if  line_counter >= 10:
          print(line_counter,')', '  ', line, end = '')
      total_lines_in_file +=1  
   
    line = file_input.readline()
    
   
# print ("--End of Poem---")

print ()
print ()
print ("Total number of stanzas in this poem are",  stanza_counter, ".")
print ("Total number of lines in this poem are", total_lines_in_file, ".")
print("Tuesday Afternoon is in the Days of Future Passed album")
print("The Moody Blues released this album in 1967")
print("Ray Thomas, Mike Pinder, Denny Laine, Clint Warwick, Rodney Clark, and Patrick Moraz were all members of the band")
file_input.close()
