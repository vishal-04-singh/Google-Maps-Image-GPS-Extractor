# Google Maps Image GPS Extractor

This script automates the process of extracting GPS coordinates from Google Maps image URLs. It uses Selenium WebDriver with Chrome to navigate through a series of images in a Google Maps contribution, extracting the image ID and GPS coordinates for each image.

## Features

- Extracts image IDs and GPS coordinates from Google Maps contribution pages
- Uses Selenium WebDriver for accurate navigation and data extraction
- Saves extracted data to a CSV file
- Handles errors gracefully to ensure continuous operation

## Prerequisites

Before running this script, ensure you have the following installed:

- Python 3.x
- Selenium WebDriver
- ChromeDriver (compatible with your Chrome browser version)

## Installation

1. Clone this repository or download the script.
2. Install the required Python packages:

   ```
   pip install selenium
   ```

3. Download the appropriate version of ChromeDriver and place it in the specified location (update the `chrome_driver` path in the script if necessary).

## Usage

1. Update the `in_URL` variable with the Google Maps contribution URL you want to scrape.
2. Run the script:

   ```
   python script_name.py
   ```

3. The script will start navigating through the images and save the data to `example.csv` in the same directory.

## Output

The script generates a CSV file named `example.csv` with the following structure:

- Column 1: Image ID
- Column 2: GPS coordinates (latitude,longitude)

## Important Notes

- Ensure you have the right to access and use the data you're scraping.
- Be mindful of Google's terms of service and robots.txt file.
- The script includes a sleep time of 0.3 seconds between actions to avoid overwhelming the server.

## Troubleshooting

- If you encounter `ElementClickInterceptedException`, try increasing the sleep time.
- Make sure your ChromeDriver version matches your Chrome browser version.

## License

[Specify your license here]

## Contributing

[Instructions for contributing to the project, if applicable]

## Disclaimer

This script is for educational purposes only. Use responsibly and in accordance with Google's terms of service.
