import os

folder = r'poke-dataset\\'
shiny_folder = r'poke-dataset\shiny\\'
count = 0
#print("ayo?")
for image_name in os.listdir(folder):
    old_source = folder + image_name
    image_name_formatted = os.path.splitext(image_name)[0] #Remove file type from string
    # IF ENDS IN _SHINY, move to shiny folder
    if(len(image_name_formatted) > 4 and image_name_formatted[-5:] == 'SHINY'):
        new_source = shiny_folder + image_name
        os.rename(old_source, new_source)
        print("Moved: ", image_name_formatted)
