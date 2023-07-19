from rembg import remove
from PIL import Image
import os
from datetime import datetime

named_directory_in = r'C:\Users\tmanl\Desktop\Project Bin\with_bg' #Replace path string with directory where you have your images
named_directory_out = r'C:\Users\tmanl\Desktop\Project Bin\without_bg' #Replace path string with where the images are going

pic_list = []
pic_list = os.listdir(named_directory_in)
save_number = 0
new_dir_name = datetime.now().strftime('%Y-%m-%d')
path = fr'{named_directory_out}\{new_dir_name}'

#Check for folder, create folder if not there
if not os.path.exists(path):
    os.makedirs(path)

#Loop over all Images
for pic in pic_list:
    save_number += 1
    input_path = fr'{named_directory_in}\{pic}'
    
    # Store path of the output image in the variable output_path
    output_path = fr'{named_directory_out}\{new_dir_name}\no_bg{save_number}.png'

    # Check if image exists
    if os.path.exists(output_path):
        continue
    
    # Processing the image
    input = Image.open(input_path)

    # Removing the background from the given Image
    output = remove(input)

    #Saving the image in the given path
    output.save(output_path)