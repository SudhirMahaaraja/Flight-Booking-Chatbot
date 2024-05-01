# Flight Booking Chatbot

## Description
This repository contains code for a Flight Booking Chatbot, which assists users in booking flights seamlessly. The chatbot is powered by Rasa for natural language understanding and dialogue management. The frontend interface is designed using HTML, CSS, and JavaScript to provide an intuitive user experience, while the backend server is built with Flask to handle communication between the user and the chatbot. Additionally, spaCy is used for entity extraction and TF-IDF for intent classification, ensuring accurate and efficient responses tailored to users' travel requirements.

## Installation
1. Clone the repository.
2. Install dependencies:pip install flask rasa scikit-learn spacy
3. Download spaCy model:python -m spacy download en_core_web_sm



## Contents
1. **HTML Files:**
- `index.html`: Frontend interface for the Flight Booking Chatbot.

4. **Python Files:**
- `app.py`: Backend Flask application managing HTTP requests and responses.


## Usage
1. Data Preparation:
- Ensure training and test data are in CSV format with appropriate columns.
- Place the data files in the root directory of the project.

2. Running the Code:python app.py


## Enhancements
- Integration of multi-city flight booking and fare comparison features.
- Implementation of sentiment analysis for gauging user satisfaction.
- Expansion of chatbot capabilities to support hotel bookings and travel itineraries.
- Incorporation of predictive analytics for suggesting optimal travel options based on user preferences.

## Contributors
S Sudhir Mahaaraja

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Acknowledgements
Special thanks to the Rasa team and the open-source community for their invaluable contributions to natural language processing and chatbot development.


