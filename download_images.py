import os
import requests
from pathlib import Path

# Create Images/favorites directory if it doesn't exist
Path("Images/favorites").mkdir(parents=True, exist_ok=True)

# List of image URLs and their corresponding filenames
images = [
    # Hero Section
    ("https://images.unsplash.com/photo-1513258496099-48168024aec0", "hero.jpg"),
    # Features Grid
    ("https://images.unsplash.com/photo-1503676382389-4809596d5290", "feature-teacher.jpg"),
    ("https://images.unsplash.com/photo-1517486808906-6ca8b3f04846", "feature-books.jpg"),
    ("https://images.unsplash.com/photo-1464983953574-0892a716854b", "feature-guidance.jpg"),
    ("https://images.unsplash.com/photo-1516979187457-637abb4f9353", "feature-material.jpg"),
    ("https://images.unsplash.com/photo-1465101046530-73398c7f28ca", "feature-assessment.jpg"),
    ("https://images.unsplash.com/photo-1503676382389-4809596d5290", "feature-support.jpg"),
    # Cards Grid
    ("https://images.unsplash.com/photo-1517841905240-472988babdf9", "card-mission.jpg"),
    ("https://images.unsplash.com/photo-1465101046530-73398c7f28ca", "card-vision.jpg"),
    ("https://images.unsplash.com/photo-1513258496099-48168024aec0", "card-courses.jpg"),
    ("https://images.unsplash.com/photo-1519125323398-675f0ddb6308", "card-success.jpg"),
    ("https://images.unsplash.com/photo-1503676382389-4809596d5290", "card-facilities.jpg"),
    ("https://images.unsplash.com/photo-1516979187457-637abb4f9353", "card-contact.jpg"),
    # Split Section
    ("https://images.unsplash.com/photo-1464983953574-0892a716854b", "split.jpg"),
]

def download_image(url, filename):
    try:
        # Add parameters to get a medium-sized image
        full_url = f"{url}?auto=format&fit=crop&w=800&q=80"
        response = requests.get(full_url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
        if response.status_code == 200:
            filepath = os.path.join("Images/favorites", filename)
            with open(filepath, 'wb') as f:
                f.write(response.content)
            print(f"Successfully downloaded {filename}")
        else:
            print(f"Failed to download {filename}: HTTP {response.status_code}")
            
    except Exception as e:
        print(f"Error downloading {filename}: {str(e)}")

# Download all images
for url, filename in images:
    download_image(url, filename)

print("Download complete!") 