# Resonate Recordings Assignment

Rush HTTP API endpoint that determines if the submission falls inside the rush fee window of three business days or less.

## Install

``python -m virtualenv venv``
``source venv/Scripts/activate``
``pip install -r requirements.txt``

## Run


``python app.py``
Code will run on PORT:5000


## API Endpoint Usage
``curl -s http://localhost:5000/rush-fees?due=YYYY-MM-DD`` 
- Will validate the input to check if it is in YYYY-MM-DD format or else return `{"error": "Invalid date - Please add date in YYYY-MM-DD"}`

- Will check if the entered due-date is a future-date or else returns {"error": "Please select future due date"}`

- If things are valid it will return `{"isRushed":false/true}`

## Points to note
- All the date calculations are done in UTC format
- 5:00 PM EDT is 9:00 PM in UTC, hence 9:00 PM UTC is used for calculating the Rush Period


## How will I improve

- In routes/rush_fees.py has RUSH_DELAY of 3 days, currently the logic is for 3 days only; If I get a chance to improve, I will add a configuration where the 3 days logic will be parametrized and the 3 day period can be extended to n-days by just changing the paramter on the fly.

- The url param holds value for YYYY-MM-DD and can be extended to take all forms of timestamp like YYYY-MM-DD HH:MM or timestamp

- Can take timezone as parameter, currently it's hardcoded to EST.

- Optimize the API to handle large number of requests and make it more responsive by further optimizing the algorithm

- Take into consideration all the holidays such as Christmas and Thanksgiving to make sure the API reports precise results for any day of the year