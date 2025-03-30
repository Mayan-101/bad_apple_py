from PIL import Image
import numpy as np
import pandas as pd
import os
from time import sleep
import threading
import pygame

# Initialize pygame mixer
pygame.mixer.init()
c1, c2  = 0, 0
# Load and play the audio file
audio_file = "C:\\Users\\mayan\\bad_apple_py\\bad_apple_audio.mp3" # Replace with your audio file path
pygame.mixer.music.load(audio_file)
def play_music():
    global c1 , c2
    sleep(2)
    pygame.mixer.music.play()
    c2 += 1
        # Keep the script running while the audio plays
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(30)  # Adjusts how often it checks (10 FPS)
# Loop through only specific file types


        # Process your JPG file here
def jpg_to_ascii(image_path, width=100, output_file=None, use_pandas=True):
    """
    Convert a JPG image to ASCII art.
    
    Parameters:
    - image_path: Path to the JPG image
    - width: Width of the ASCII art in characters
    - output_file: If provided, save ASCII art to this file
    - use_pandas: If True, use pandas for data manipulation
    
    Returns:
    - ASCII art as a string
    """
    # ASCII characters from darkest to lightest
    ascii_chars = '@%#*+=-:. '
    ascii_chars = ascii_chars[::-1]
    # Open image and convert to grayscale
    img = Image.open(image_path).convert('L')
    
    # Calculate new dimensions
    orig_width, orig_height = img.size
    aspect_ratio = orig_height / orig_width
    new_height = int(width * aspect_ratio * 0.5)  # Multiply by 0.5 because chars are taller than wide
    
    # Resize image
    img = img.resize((width, new_height))
    
    # Convert image to numpy array
    pixels = np.array(img)
    
    if use_pandas:
        # Convert to pandas DataFrame for manipulation
        df = pd.DataFrame(pixels)
        
        # Normalize and map to ASCII chars
        # Map 0-255 to indices of ascii_chars
        max_val = 255
        df = df.applymap(lambda x: ascii_chars[int(x / max_val * (len(ascii_chars) - 1))])
        
        # Convert back to ASCII art
        lines = [''.join(row) for row in df.values]
        ascii_art = '\n'.join(lines)
    else:
        # Direct numpy approach (no pandas)
        # Normalize and map to ASCII chars
        indices = (pixels / 255 * (len(ascii_chars) - 1)).astype(int)
        ascii_pixels = np.array(list(ascii_chars))[indices]
        
        # Convert to string
        lines = [''.join(row) for row in ascii_pixels]
        ascii_art = '\n'.join(lines)
    
    # Save to file if requested
    if output_file:
        with open(output_file, 'w') as f:
            f.write(ascii_art)
    
    return ascii_art

# Example usage

def print_stuff():
    global c1
    folder_path = "C:\\Users\\mayan\\bad_apple_py\\frames"
    for filename in os.listdir(folder_path):
        c1 += 1
        if filename.endswith('.jpg') or filename.endswith('.jpeg'):
            image_path = os.path.join(folder_path, filename)
            ascii_result = jpg_to_ascii(image_path, width=100, output_file="ascii_art.txt")
            print(ascii_result)
            sleep(1/75)

thread1 = threading.Thread(target=play_music)
thread2 = threading.Thread(target=print_stuff)

# Start threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

print("All threads done")
print("Done!")