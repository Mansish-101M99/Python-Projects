import barcode  # pip install python_barcode
from barcode.writer import ImageWriter

# Creating a barcode in python
t1 = "Python barcode1"
t2 = str(t1)
code = barcode.get_barcode_class("code128")
image = code(t1, writer = ImageWriter())
save_img = image.save('final barcode')