![image](https://github.com/IntelegixLabs/HiFi/assets/34819268/6447dcaf-62fc-4292-aa1b-a21264411d1f)<h1 align="center">HiFi (Hitaya Finance)</h1>

### PROBLEM STATEMENT

<strong> 1. Providing stock analytics data, news feeds, and event information. </strong>

Gather stock fundamental details like about the company, quarter results, profit and loss, balance sheets cash flow  ratios, shareholding patterns, news about the company, and events. Using GenAI LLMs to make informed decisions.  Peer-to-peer stock comparison related to the same category.

<strong> 2. Generating buy-sell decisions based on Market sentiments.</strong>

User-defined questions to identify risk management based on input, leveraging LLMs based on the above company data  and user data to understand the current situation and predict the future price of the stock, and show whether the user should  buy, neutral, or sell the stock from user portfolio to minimize maximize the risk.

# Features 

- Provide stock analytics data, news feeds, and event information.
- Generating buy-sell decisions based on Market sentiments.
- Generating buy-sell signals for intraday trades, and equity investments.
- LLMs to minimize risk and maximize profit.
- Kill switch option for intraday & F&O.
- Portfolio Dashboard.
- Option to automate trade from the wallet.
- Connect with a broker.

  # Advance Features

  - Users can opt for premium plans to secure their data by using <strong> blockchain technology under the hood to make it decentralized and safeguard their information. </strong>
  - LLMs for personalized recommendations and portfolio management, risk management using RAG models.
  - Enabling follow trading for users who want to make trading data public that others can utilize to <strong>create/replicate trading strategies.</strong>




















## 1. Project Architecture

<p align="center">
  <img src="data/HiFi.png" />
</p> 

## 2. Getting Started With The Fast API Application

```sh
$ git clone https://github.com/IntelegixLabs/HiFi.git
$ cd HiFi
$ pip install -r requirements.txt
$ python main.py
```

Swagger UI `http://localhost:5000/docs`

Run `uvicorn main:app --reload`


#### Listen to Stripe events

<span>Use Stripe CLI to simulate Stripe events in your local environment or <a href="https://stripe.com/docs/webhooks" target="__blank" rel="noopener noreferrer">learn more about Webhooks</a>.</span>

1. <span><a href="https://stripe.com/docs/stripe-cli" target="__blank" rel="noopener noreferrer">Download the CLI</a> and log in with your Stripe account</span>

```commandline
stripe login
```

2. Forward events to your webhook

```commandline
stripe listen --forward-to localhost:5000/payments/stripe/webhook
```

3. Trigger events with the CLI

```commandline
stripe trigger payment_intent.succeeded

stripe trigger subscription_schedule.canceled

stripe trigger invoice.upcoming

stripe trigger charge.captured

stripe trigger invoice.payment_succeeded
```

## 3. Running the Test Cases

```sh
$ cd HiFi
$ pytest --disable-warnings  
```

## 4. Run this project with docker locally

```sh
$ cd HiFi
$ docker system prune 
$ docker-compose -f docker-compose.yml up -d --build
```



## 5. Getting Started With UI Application

```sh
$ git clone https://github.com/IntelegixLabs/HiFi_UI.git
$ cd HiFi_UI
$ npm i
```


## 6. Project Requirements

<h4>Languages</h4>
<ul>
  <li>KeyCloak 24.0.0</li>
  <li>Python 3.12.1</li>
</ul>

## 8. Application Screenshots / <a href="">Demo.</a>


## 8. Components to be built (Work In Progress)

* [x] API Enhancement.

