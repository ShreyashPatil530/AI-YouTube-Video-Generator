import os
import requests
from dotenv import load_dotenv

load_dotenv()

class ImageGenerator:
    def __init__(self):
        self.api_key = os.getenv("PEXELS_API_KEY")
        self.headers = {"Authorization": self.api_key}

    def search_and_download(self, keywords, temp_dir):
        """Search Pexels and download 10-12 images for better variety."""
        downloaded_paths = []
        
        # Flatten keywords if they are a list of lists or similar
        search_terms = []
        for k in keywords:
            if "," in k:
                search_terms.extend([term.strip() for term in k.split(",")])
            else:
                search_terms.append(k.strip())

        for i, keyword in enumerate(search_terms):
            if i >= 12: break # limit to 12 images
            
            url = f"https://api.pexels.com/v1/search?query={keyword}&per_page=1"
            response = requests.get(url, headers=self.headers)
            
            if response.status_code == 200:
                data = response.json()
                if data.get('photos'):
                    # Use 'large2x' for better quality without being too massive
                    photo_url = data['photos'][0]['src']['large2x']
                    img_data = requests.get(photo_url).content
                    img_path = os.path.join(temp_dir, f"image_{i}.jpg")
                    
                    with open(img_path, 'wb') as f:
                        f.write(img_data)
                    downloaded_paths.append(img_path)
                    print(f"Downloaded high-quality image for: {keyword}")
            else:
                print(f"Failed to fetch image for {keyword}: {response.status_code}")
                
        return downloaded_paths
