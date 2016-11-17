import os
#"en_"

def un_encrypt(x):
        
	for z in range(len(x)):
		f = open(x[z][3:], 'w')
		with open(x[z], 'r') as file:
		    for i, line in enumerate(file):
		        try:
		            filename = line.rstrip('\n')
		            encrypt_string = ""
		            for char in range(len(filename)):
		            	encrypt_string = encrypt_string + char_encryt(filename[char])
		            f.write(encrypt_string  +"\n")
		        except Exception as e:
		        	print "error"
		        	print str(e)
		f.close()
    
    
    

def encrpyted_file_search(x):
    en_file_list = []
    for z in range(len(x)):
        file_name = x[z]
        if file_name[0] == "e" and file_name[1] == "n" and file_name[2] == "_":
            en_file_list.append(x[z])
    return en_file_list
	
def create_file_list():
	file_list = []
	# maps the entire computer
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
	
			
def char_encryt(char):
    y = ord(char)
    y = y - 3
    if y < 0:
        y = y + 256
    return chr(y)


if __name__ == "__main__":
	x = create_file_list()
	x = encrpyted_file_search(x)
	un_encrypt(x)
	