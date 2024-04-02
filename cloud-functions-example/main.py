import pygame
import requests

# Initialize PyGame
pygame.init()

# Constants
size = [600, 600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Cloud Functions Color Changer")

# Default background color
bg_color = pygame.Color('black')

# Get the current color
def fetch_color():
    global bg_color
    CLOUD_FUNCTION_URL = 'https://us-central1-cloud-functions-419021.cloudfunctions.net/function-2'
    try:
        response = requests.post(CLOUD_FUNCTION_URL, json={})
        if response.status_code == 200:
            print(response.text)
            data = response.json()
            color = data.get('color', 'black')
            bg_color = pygame.Color(color)
    except Exception as e:
        print(f"Error fetching color: {e}")


# Main loop
done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Fetch the current color from the Cloud Function
    fetch_color()

    # Fill the background with the fetched color
    screen.fill(bg_color)
    
    pygame.display.flip()
    
    # Limit to 3 frames per second
    clock.tick(3)

pygame.quit()

