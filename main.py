# Install necessary dependencies
!apt-get update
!apt install -y libglib2.0-0 libnss3 libgconf-2-4 libfontconfig1

# Install Python packages
!pip install selenium
!pip install webdriver-manager

# Import required modules
import time
import csv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options for headless mode in Colab
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Initialize the Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Define the search query
query = "Fitness in India"
search_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}&sp=EgIQAg%253D%253D"

# Navigate to the search URL
driver.get(search_url)

# Wait for channel renderers to load
try:
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, "ytd-channel-renderer"))
    )
except Exception as e:
    print(f"Timeout Error: Channel renderers did not load. {e}")
    driver.quit()
    exit()

# Find all channel renderer elements
channel_renderers = driver.find_elements(By.TAG_NAME, "ytd-channel-renderer")
print(f"Found {len(channel_renderers)} channel renderers")

# Initialize a list to store channel data
channels_data = []

# Extract data from each channel renderer
for renderer in channel_renderers:
    try:
        url = renderer.find_element(By.CSS_SELECTOR, "a#main-link").get_attribute("href")
        name = renderer.find_element(By.ID, "channel-title").text.strip()

        # Fix: Use correct selector for subscriber count
        try:
            subscriber_count = renderer.find_element(By.ID, "subscribers").text.strip()
        except:
            subscriber_count = "N/A"

        # Fix: Handle missing description
        try:
            description = renderer.find_element(By.ID, "description").text.strip()
        except:
            description = "No description available"

        channels_data.append({
            'Channel URL': url,
            'Name': name,
            'Description': description,
            'Subscriber Count': subscriber_count
        })

        print(f"✔ Extracted: {name} | {subscriber_count}")

    except Exception as e:
        print(f"⚠ Error extracting data from a channel: {e}")
        continue

# Save a screenshot for debugging
driver.save_screenshot("/content/youtube_screenshot.png")

# Check if data exists before writing CSV
csv_file_path = "/content/youtube_channels.csv"
if len(channels_data) > 0:
    with open(csv_file_path, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["Channel URL", "Name", "Description", "Subscriber Count"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for channel in channels_data:
            writer.writerow(channel)

    print(f"Scraped {len(channels_data)} channels and saved to {csv_file_path}")
else:
    print("No channels found. CSV not created.")

# Close the browser
driver.quit()

# Confirm completion
if os.path.exists(csv_file_path):
    print(f"File successfully created: {csv_file_path}")
    print("You can download 'youtube_channels.csv' from the Colab file browser.")
else:
    print("CSV file was not created.")
