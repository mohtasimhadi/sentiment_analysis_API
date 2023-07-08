# Sentiment Analysis API

This project implements a backend service that provides a RESTful API endpoint for sentiment analysis. The API accepts text input and returns the sentiment analysis result using a pre-trained machine learning model.

## Requirements

* Python 3.11
* Flask
* transformers

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/mohtasimhadi/sentiment-analysis-api
   cd sentiment-analysis-api

   ```
2. Create and activate a virtual environment (optional but recommended):

   ```
   python3.11 -m venv env
   source env/bin/activate

   ```
3. Install the dependencies:

   ```
   pip install -r requirements.txt
   ```
## Usage

1. Start the Flask Server
   ```
   python app.py
   ```
2. The API endpoint will be accessible at http://localhost:5000/analyze.
3. Send a POST request to http://localhost:5000/analyze with the following JSON payload:
   ```
   {
     "text": "Text to be analyzed"
   }
   ```
4. The API will return a JSON response with the sentiment analysis result:
   ```
   {
     "sentiment": "positive/negative/neutral"
   }
   ```
## Error Handling
1. If the request payload is missing or has an invalid format, the API will return a JSON response with an appropriate error message and a status code of 400.
2. If there is an internal server error during the sentiment analysis process, the API will return a JSON response with an error message and a status code of 500.

## Additional Information
The sentiment analysis is performed using a pre-trained machine learning model provided by Hugging Face Transformers library. The model used in this project is StatsGary/setfit-ft-sentinent-eval.
Feel free to explore and modify the code as needed to meet your specific requirements or preferences.
