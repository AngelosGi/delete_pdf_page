import fitz

# Path of the PDF file 
input_file = r"Angelos-Giannopoulos-Resume (1).pdf"

# Path for the output PDF file 
output_file = r"Angelos-Giannopoulos-Resume.pdf"

# Opening the PDF file and creating a handle for it 
file_handle = fitz.open(input_file)

# The page no. denoted by the variable will be deleted 
page = 1

# Passing the variable as an argument 
file_handle.delete_page(page)

# Saving the file 
file_handle.save(output_file)