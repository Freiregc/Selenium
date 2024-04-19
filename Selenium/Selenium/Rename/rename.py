# Python 3 code to rename multiple 
# files in a directory or folder

# importing os module
import os

# Function to rename multiple files
def main():

	folder = "C:/Users/sn1076327/Desktop/Selenium/Selenium/Selenium/Rename"
	for count, filename in enumerate(os.listdir(folder)):
		a = (4963 + (count+1))
		dst = f"{str(a)}.png"
		src =f"{folder}/{filename}" # foldername/filename, if .py file is outside folder
		dst =f"{folder}/{dst}"
		
		# rename() function will
		# rename all the files
		os.rename(src, dst)

# Driver Code
if __name__ == '__main__':
	
	# Calling main() function
	main()