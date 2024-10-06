stock_api = "asdasdasdasdasdasdas"
news_api = "asdasdasdasdasdasd"

COMPANY_NAME = "Tesla Inc"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

account_sid = "asdasdasdasdads"
auth_token = "asdasdasdasd"

import requests
from twilio.rest import Client


stock_params = {
    "apikey": stock_api,
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "datatype": "json",
}
response_stock = requests.get("https://www.alphavantage.co/query", params=stock_params)
stock_data = response_stock.json()["Time Series (Daily)"]
stock_data_list = [value for (key,value) in stock_data.items()]
yesterday_data = stock_data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data = stock_data_list[1]
day_before_yesterday_data_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_data_price)



def check_diff():
    the_diff = abs(float(yesterday_closing_price) - float(day_before_yesterday_data_price))
    percentage = ((the_diff / float(yesterday_closing_price)) * 100)
    if percentage < 5:
        news_params = {
            "apiKey": news_api,
            "qInTitle": COMPANY_NAME
        }
        news_request = requests.get(NEWS_ENDPOINT, params=news_params)
        articles = news_request.json()["articles"]
        three_articles = articles[:3]

        formatted_articles = [f"Headline: {articles['title']}. \nBrief: {articles['description']} " for articles in three_articles]

        for article in formatted_articles:
            client = Client(account_sid, auth_token)

            message = client.messages.create(

                body=article,
                from_="+15017122661",
                to="+15558675310",
        )




check_diff()
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


#Optional: Format the SMS message like this: