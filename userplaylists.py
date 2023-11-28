from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

import output

def scrape_spotify_playlists(user_url):
    # Set up the Selenium WebDriver (you need to have the appropriate driver for your browser installed)
    driver = webdriver.Chrome()  # You can use another driver based on your browser (e.g., Firefox)

    # Load the page
    driver.get(user_url)

    # Use WebDriverWait to wait for the playlists to load
    wait = WebDriverWait(driver, 15)  # Adjust the timeout based on your needs

    # Wait for the playlists to be present in the page
    playlists_present = EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href^="/playlist/"]'))
    wait.until(playlists_present)

    # Get the page source after it has been fully loaded
    page_source = driver.page_source

    # Close the browser
    driver.quit()

    # Parse the HTML content of the page
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find all playlist links on the user's profile
    playlist_links = soup.select('a[href^="/playlist/"]')

    # Create a dictionary to store playlist names and links
    playlist_dict = {}

    # Iterate through playlist links and populate the dictionary
    for playlist_link in playlist_links:
        # Extract playlist name and link
        playlist_name = playlist_link.select_one('div[data-encore-id="type"]').text.strip()
        playlist_url = 'https://open.spotify.com' + playlist_link['href']

        # Store in the dictionary
        playlist_dict[playlist_name] = playlist_url

    return playlist_dict
