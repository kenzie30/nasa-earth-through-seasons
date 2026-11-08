# nasa-earth-through-seasos
This program uses NASA's EPIC API to retrieve pictures of Earth from June 21 and December 21, 2025. It compares the average latitude coordinates from both dates to explore how Earth's appearance changes between seasons. 

## How it works
- get_photos(date, api_key): Retrieves Earth photo information from NASA's EPIC API and converts the response into a Python list of dictionaries. Handles unsuccessful requests, dates, and no photos. 
- get_latitude(photos): Retrieves latitude information from the photo dictionaries and calculates the average latitude. 
- compare_seasons (june_latitude, december_latitude): Compares the average latitude values from June and December and calculates the difference between them.

## How to run
1. Install the requests library: pip install requests
2. Download or clone this repository to your computer
3. Open the project folder in VS Code
4. Run the program: python main.py
5. Enter your NASA API key when prompted. 

## Built with
Python, requests library, and the NASA EPIC API
