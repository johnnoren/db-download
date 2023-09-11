import csv
import requests
import os

# Directory to save downloaded videos
DOWNLOAD_DIR = 'downloaded_videos'
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

# Read URLs from the CSV file and download videos one by one
with open('videos.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    
    for row in reader:
        caption, url = row
        # Create a valid filename from the caption
        filename = os.path.join(DOWNLOAD_DIR, caption.replace(" ", "_") + ".mp4")
        
        print(f"Downloading {caption}...")
        
        # Send a GET request to fetch the video content
        response = requests.get(url, stream=True)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Write video content to file
            with open(filename, 'wb') as video_file:
                for chunk in response.iter_content(chunk_size=1024):
                    video_file.write(chunk)
            print(f"Downloaded {caption} to {filename}")
        else:
            print(f"Failed to download {caption}. Status code: {response.status_code}")

print("All videos downloaded!")
