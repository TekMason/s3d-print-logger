srcFile = "./Plate018.gcode"
dstFile = "G:/My Drive/3D Print Logs/s3d-print-logger/Plate018.txt"
string = ";  "
def get_lines_with(input_str, substr):
	"""
	Get all lines containing a substring.
 
	Args:
		input_str (str): String to get lines from.
		substr (str): Substring to look for in lines.
 
	Returns:
		list[str]: List of lines containing substr.
	"""
	lines = []
	for line in input_str.strip().split('\n'):
		if substr in line:
			lines.append(line)
	return lines
 
 
def txt_lines_with(fname, substr):
	"""
	Get all lines in a .txt file containing a substring.
	
	Args:
		fname (str): File name to open.
		substr (str): Substring to look for in lines.
 
	Returns:
		list[str]: List of lines containing substr.
	"""
	f_contents = open(fname, 'r').read()
	return get_lines_with(f_contents, substr)
 
 
def filter_txt_lines_to(fname_in, substr, fname_out):
	"""
	Put lines from one .txt file into another if they
	contain a substring 'substr'.
 
	Args:
		fname_in (str): Source file.
		substr (str): Substring to look for in lines.
		fname_out (str): Destination file.
	"""
	filtered_lines = txt_lines_with(fname_in, substr)
	joined_lines = '\n'.join(filtered_lines)
	open(fname_out, 'w').write(joined_lines)
  
# Add your file names and filter here
#filter_txt_lines_to("./source.txt", "this", "./dest.txt")
filter_txt_lines_to(srcFile,string,dstFile)



#G90
#M83
#; **** Replicator 1 dual start.gcode ****
#M73 P0 ; enable build progress

#M72 P1 ; play Ta-Da song
#; **** end of end.gcode ****
#; Build Summary
#;   Build time: 2 hours 16 minutes

		
# lines = []                  # Declare an empty list named "lines"
# with open ('Z:\Plate018.gcode', 'rt') as in_file:  # Open file lorem.txt for reading of text data.
	# for line in in_file:  # For each line of text in in_file, where the data is named "line",
		# lines.append(line.rstrip('\n'))   # add that line to our list of lines, stripping newlines.
	# for element in lines:            # For each element in our list,
		# print(element)              # print it. 		

		
		


#lines = [] #Declare an empty list named "lines"
#with open ('Z:\Plate018.gcode', 'rt') as in_file:  # Open file lorem.txt for reading of text data.
#	for line in in_file: # Store each line in a string variable "line"
#		lines.append(line)  #add that line to our list of lines.
#		lines.append(line.rstrip('/n'))  #add that line to our list of lines.
#		print(lines)        #print the list object.


#with open ('Z:\FlexKim.gcode', 'rt') as in_file:  # Open file lorem.txt for reading of text data.
#    contents = in_file.read()# Read the entire file into a variable named contents.
#print(contents) # Print contents.
