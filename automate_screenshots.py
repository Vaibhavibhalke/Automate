import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# Function to get URLs from sitemap.xml
def get_urls_from_sitemap(sitemap_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(sitemap_url, headers=headers)
    if response.status_code == 200:
        print("Sitemap fetched successfully")
        print(response.text[:500])  # Print the first 500 characters of the response to see the XML structure
        soup = BeautifulSoup(response.content, 'lxml')  # Use lxml parser
        urls = [loc.text for loc in soup.find_all('loc')]
        print(f"Found URLs: {urls}")  # Debugging statement
        return urls[:5]  # Return only the first 5 URLs
    else:
        print(f"Failed to fetch sitemap. Status code: {response.status_code}")
        return []

# Function to set browser window size (resolution)
def set_browser_resolution(browser, width, height):
    browser.set_window_size(width, height)

# Function to take and save screenshot
def save_screenshot(browser, url, browser_name, width, height):
    print(f"Processing {url} for {browser_name} at {width}x{height}")  # Debugging statement
    folder_name = f"C:\\Users\\HP\\Desktop\\test\\{browser_name}_{width}x{height}"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    browser.get(url)
    filename = url.split('//')[-1].replace('/', '_') + '.png'
    screenshot_path = os.path.join(folder_name, filename)
    browser.save_screenshot(screenshot_path)
    print(f"Screenshot saved at {screenshot_path}")  # Debugging statement

# Main function to automate screenshots for all browsers and resolutions
def automate_screenshots(sitemap_url, resolutions):
    # Step 1: Get URLs from the sitemap
    print(f"Fetching URLs from {sitemap_url}")
    urls = get_urls_from_sitemap(sitemap_url)
    if not urls:
        print("No URLs found. Exiting...")
        return
    print(f"Found {len(urls)} URLs")

    # Step 2: Set up the browsers (Chrome and Firefox in this case)
    browsers = {
        "Chrome": webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())),
        "Firefox": webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    }

    # Step 3: Iterate through all browsers and resolutions
    for browser_name, browser in browsers.items():
        for width, height in resolutions:
            set_browser_resolution(browser, width, height)
            for url in urls:
                print(f"Taking screenshot for {url} in {browser_name} at {width}x{height}")
                save_screenshot(browser, url, browser_name, width, height)

    # Step 4: Close all browsers after screenshots
    for browser in browsers.values():
        browser.quit()

# List of resolutions to test (add more if needed)
resolutions = [
    (1920, 1080),  # Desktop - Full HD
    (1366, 768),   # Laptop - HD
    (1280, 800),   # Tablet - WXGA
    (375, 812)     # Mobile - iPhone X
]

# URL of the sitemap.xml
sitemap_url = "https://www.getcalley.com/page-sitemap.xml"

# Run the automation
if __name__ == "__main__":
    automate_screenshots(sitemap_url, resolutions)
