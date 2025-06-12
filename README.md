# YelpMate

**YelpMate** is a mini AI agent that recommends restaurants based on the user's location, preferred cuisine, and price level. It fetches real-time data from the Yelp Fusion API and displays results in a simple, clean web interface using Streamlit.

---

## Demo Video

Link: [Insert your YouTube or Google Drive link here]

---

## Project Overview

YelpMate was built as part of a take-home challenge to demonstrate the ability to:

- Build a functional AI agent
- Interact with a public data platform (Yelp API)
- Complete a practical, user-facing task: recommending relevant restaurants based on location, cuisine, and budget

The agent takes user input (city, food type, and price level), queries Yelp’s API for top-rated restaurants, and displays results including name, rating, address, phone, image, and a short summary.

---

## Tech Stack

- **Language**: Python 3
- **Framework**: Streamlit (for frontend UI)
- **API**: Yelp Fusion API (real-time data source)
- **Packages**:
  - `requests`: for API calls
  - `python-dotenv`: for securely managing API keys

---

## Design Choices

- **Yelp API** was chosen to interact with a real, public platform offering structured restaurant data.
- **Streamlit** was used for fast, clean, and interactive UI building.
- Logic is split into two files:
  - `app.py`: Handles UI, user input, and display.
  - `yelp_api.py`: Handles API communication and data processing.
- Results are displayed as cards containing:
  - Image
  - Clickable name (links to Yelp)
  - Rating
  - Location
  - Phone number
  - Auto-generated one-line summary

---

## How to Run the Project

1. Clone the repository using:

   `git clone https://github.com/your-username/yelp-mate.git`  
   `cd yelp-mate`

2. Create a virtual environment and activate it:

   `python3 -m venv venv`  
   `source venv/bin/activate`

3. Install all required dependencies:

   `pip install -r requirements.txt`

4. Create a `.env` file in the root folder and add your Yelp API key in the following format:

   `YELP_API_KEY=your_yelp_api_key_here`

5. Run the app locally:

   `streamlit run app.py`

The app will open in your browser at `http://localhost:8501`. Enter a city, food type, and price level to get live restaurant recommendations from Yelp.

