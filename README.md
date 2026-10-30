# AWS Lambda & Serverless: Module 05

**Intern:** Raheem Noorul Nazla
**Program:** AWS Cloud & DevOps Internship, Codomax Digital Solutions
**Module:** 05 (Day 21-24), AWS Lambda & Serverless

## Project overview

A simple serverless API. A static web page stored in Amazon S3 calls an Amazon API Gateway HTTP API, which runs an AWS Lambda function written in Python and returns a JSON message.

```
Browser -> S3 static page -> API Gateway (GET /hello) -> Lambda function -> JSON response
```

**Live website:** `<your S3 website endpoint>/serverless.html`
**API endpoint:** `<your API Gateway invoke URL>/hello?name=Nazla`

## Objectives covered

1. Understand serverless computing
2. Learn AWS Lambda fundamentals
3. Create and test a Lambda function
4. Learn Amazon API Gateway basics
5. Connect API Gateway with Lambda
6. Build a simple serverless API

## Key concepts

| Concept | Meaning |
|---------|---------|
| Serverless | You run code without managing servers. AWS handles provisioning and scaling, and you pay only for usage. |
| Lambda function | A small piece of code that runs in response to an event. |
| Handler | The function Lambda calls first (`lambda_handler(event, context)`). |
| Event | The input data (here, the HTTP request from API Gateway). |
| API Gateway | A managed service that creates HTTP endpoints and sends requests to backends such as Lambda. |
| Route | A method and path, for example `GET /hello`. |
| Integration | The connection between a route and its backend (Lambda). |
| Stage | A deployed version of the API (`$default` with auto-deploy). |

## Steps performed

### 1. Create the Lambda function
- Lambda > Create function > Author from scratch
- Name: `nazla-hello-api`, runtime: Python 3.x, architecture: x86_64
- Pasted `lambda_function.py` into the code editor and clicked **Deploy**.

### 2. Test the function
- Test tab > created a test event > **Test**
- Execution result: succeeded, with the JSON response.

### 3. Create the API with API Gateway
- API Gateway > Create API > **HTTP API**
- Integration: Lambda > `nazla-hello-api`
- Route: `GET /hello`
- Stage: `$default` (auto-deploy)
- Copied the **Invoke URL**.

### 4. Test the API
Opened `<Invoke URL>/hello?name=Nazla` in a browser and received the JSON message.

### 5. Host the web page on S3
- Set `API_URL` in `serverless.html` to the invoke URL.
- Uploaded `serverless.html` to the S3 bucket with static website hosting enabled.
- Opened the page, entered a name, and clicked **Call API**.

## Screenshots

(Add your screenshots to a `screenshots/` folder and link them here.)

- Lambda function with code deployed
- Lambda test result (succeeded)
- API Gateway route and integration
- API response in the browser
- Web page calling the API

## Key learnings

- Serverless means no server management: Lambda scales automatically and bills per request.
- API Gateway gives Lambda a public HTTPS URL.
- The Lambda handler receives the request as an `event` and returns a response with a status code, headers and body.
- Always handle user input safely: the web page shows the response with `textContent`, not `innerHTML`.

## Files

- `lambda_function.py`: the Lambda function code
- `serverless.html`: the web page that calls the API
- `README.md`: project documentation
