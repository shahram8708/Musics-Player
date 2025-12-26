# Music Player

A simple web-based music player built with Flask that lets users search for Hindi tracks using the Jamendo public music API and play them directly in the browser. The application provides a clean interface to search songs, view results, and stream audio.

## Overview

The application exposes a small Flask backend that communicates with the Jamendo API to fetch music tracks based on a search query. The frontend is built using HTML, CSS, and vanilla JavaScript, providing an interactive and responsive UI for music discovery and playback.

## Features

* Search music tracks by keyword
* Fetches results from Jamendo’s public music API
* Automatically filters tracks tagged as Hindi
* Displays song titles and artists
* Built-in HTML audio player for streaming
* Simple and clean UI

## Tech Stack

* **Backend:** Flask
* **HTTP Requests:** requests
* **Frontend:** HTML, CSS, JavaScript
* **Deployment Ready:** gunicorn support included
* **External Service:** Jamendo API

## Project Structure

```
Musics-Player-main/
│
├── app.py                # Flask application and API integration
├── requirements.txt      # Python dependencies
│
├── templates/
│   └── index.html        # Main UI page
│
└── static/
    └── style.css         # Application styling
```

## Installation

1. Clone or extract the project to your machine.

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python app.py
   ```

4. Open a browser and go to:

   ```
   http://127.0.0.1:5000/
   ```

## Usage

* Enter a search term in the search bar.
* The application will request matching Hindi-tagged tracks from Jamendo.
* Search results will display song title, artist name, and an audio player.
* Click play to listen.

## API Integration

The application uses:

```
https://api.jamendo.com/v3.0/tracks
```

Parameters used:

* `client_id`
* `format=json`
* `limit=10`
* `namesearch=<query>`
* `tags=hindi`
* `order=popularity_total`

The backend returns processed track results as JSON to the frontend.

## Notes

* The Jamendo API key is included directly in the application.
* This project is intended for learning and demonstration purposes.
* Internet connection is required for fetching and streaming music.
