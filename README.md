<h1 align="center">HiFi (Hitaya Finance)</h1>

### PROBLEM STATEMENT

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


## 6. Project Requirements

<h4>Languages</h4>
<ul>
  <li>KeyCloak</li>
  <li>Python 3.12.1</li>
</ul>

## 8. Application Screenshots / <a href="">Demo.</a>


## 8. Components to be built (Work In Progress)

* [x] API Enhancement.

