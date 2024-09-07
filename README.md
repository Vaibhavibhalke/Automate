# UI Testing

This project automates the process of taking screenshots of web pages at different resolutions using multiple browsers. It fetches URLs from a sitemap file and captures screenshots of these URLs across specified screen resolutions.

## Contents

- Project Description
- Features
- Requirements
- How to Run
- License

## Project Description

This script performs the following tasks:
1. Fetches URLs from a `sitemap.xml` file.
2. Sets up multiple browsers (Chrome and Firefox).
3. Captures screenshots of the URLs at various screen resolutions.
4. Saves the screenshots in a structured directory format.

## Features

- Fetches URLs from a provided `sitemap.xml`.
- Supports multiple browsers: Chrome and Firefox.
- Captures screenshots at specified resolutions.
- Saves screenshots in a directory structure based on browser and resolution.

## Requirements

The script requires the following Python libraries:

- `requests` - To fetch the sitemap XML.
- `beautifulsoup4` - To parse the sitemap XML.
- `lxml` - XML parser used by BeautifulSoup.
- `selenium` - For browser automation.
- `webdriver-manager` - To automatically manage browser drivers.

You can install these dependencies using pip:

```bash
pip install requests beautifulsoup4 lxml selenium webdriver-manager
