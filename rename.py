import os

folder = r'poke-dataset\\'

count = 0
print("ayo?")
for image_name in os.listdir(folder):
    source = folder + image_name
    image_name_formatted = os.path.splitext(image_name)[0] #Remove file type from string
    print(image_name_formatted)
    count+= 1
    last_char = image_name_formatted[-1]
    if last_char.isnumeric(): #if shiny, rename to pokemon_SHINY
        replaceStr = '_SHINY'
        image_name_formatted =  image_name_formatted[:-1] + replaceStr
        destination = folder + image_name_formatted + ".jpg"
        # Renaming the file
        os.rename(source, destination)
        print("New file name:", image_name_formatted)

print("Total number of images:", count)