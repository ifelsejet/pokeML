import requests
from bs4 import BeautifulSoup

# Set the search term and number of images to scrape
search_term = "Nidoran"
num_images = 200

# Set the base URL for the Google search
base_url = "https://www.google.com/search?q=" + search_term + "&tbm=isch"

# Send a request to the Google search URL and get the response
response = requests.get(base_url)

# Use BeautifulSoup to parse the HTML response
soup = BeautifulSoup(response.text, "html.parser")

# Find all the image tags on the page
img_tags = soup.find_all("img")

# Iterate over the image tags
for img_tag in img_tags:
  # Get the image URL
  img_url = img_tag.get("src")

  # Download the image from the URL
  response = requests.get(img_url)

  # Save the image to a file
  with open(search_term + ".jpg", "wb") as f:
    f.write(response.content)

  # Print a progress message
  print(f"Downloaded image {img_url}")

  # Decrement the number of images remaining to download
  num_images -= 1

  # If we have downloaded all the images, stop the loop
  if num_images == 0:
    break
