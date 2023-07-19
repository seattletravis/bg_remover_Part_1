from rembg import remove
from PIL import Image
import os
from datetime import datetime

named_directory_in = r'C:\Users\tmanl\Desktop\Project Bin\with_bg' #Replace this with your images file where the images with bg are kept
named_directory_out = r'C:\Users\tmanl\Desktop\Project Bin\without_bg' #Replace this with where the images are going

pic_list = []
pic_list = os.listdir(named_directory_in)
save_number = 0
new_dir_name = datetime.now().strftime('%Y-%m-%d')
path = fr'{named_directory_out}\{new_dir_name}'

if not os.path.exists(path):
    os.makedirs(path)

#Loop the images with bg
for pic in pic_list:
    save_number += 1
    input_path = fr'{named_directory_in}\{pic}'
    
    output_path = fr'{named_directory_out}\{new_dir_name}\no_bg{save_number}.png'

    if os.path.exists(output_path):
        continue
    
    input = Image.open(input_path)

    output = remove(input)

    output.save(output_path)