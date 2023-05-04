# UET Truyen
A Python UI application, utilizing the Flet framework, for reading and managing comics.

## About the app
- An application for reading and managing comics stored in an online repository
- Makes use of Google Firebase and ImageKit.IO for storing comic datas
- Allows uploading (WIP) and reading comic chapters
- Features a user account system for saving history and following comics data (WIP)

## Instructions for running the app
- Clone the repository
- Install the required Python libraries for the app with the following command (Python 3.10 or newer):
> pip install -r requirements.txt
- Run the app with the following command
> python main.py
By default, the app will open in the system's default web browser

## Notes
- This application was written purely for the purpose of practicing and applying Python, its frameworks and database APIs. It is not meant for use anywhere else or any other purpose.
- The comic data are stored on a cloud server. The application may break at some point in the future due to the lack of fault tolerance in the code for when the database structure changes, or when the server goes down.
- Comic data were taken randomly offline as placeholder.
