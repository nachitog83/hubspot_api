# HubSpot API

HubSpot API project.

## Installation

Install Docker and docker-compose

1. Docker: https://docs.docker.com/get-docker/
2. docker-compose: https://docs.docker.com/compose/install/

## Run

Pull repo to local folder.
Place in root folder and execute docker-compose

.*command for build: docker-compose build
.*command for start: docker-compose up -d
.*command for logs: docker-compose logs -f -t

.*Backend server: http://localhost:5000

.*Frontend client: http://localhost:3000

## API Endpoints

**GET /api/oauth/authorize** - Perform OAuth flow to get HubSpot's access and refresh tokens.

**Header**
```
{
    "Content-Type": "application/json",
    "Authorization": "Bearer (Access Token)"
}
```

**Response**

If it's the first time accesing HubSpot,system will prompt a response with an external link to validate, which in turn will reply with an access code and execute a callback function in the local API, getting access and refresh tokens from Hubspot and persisting them in the MongoDB Collection.
```
{
    "data": http link,
    "msg": "msg"
}
```
If in turn, we already have an access and refresh token from Hubspot, the endpoint will refresh the access token if this is invalid.
```
{
    "data": espiration date,
    "msg": "Token refreshed"
}
```

**POST /api/auth/signup** - Sign Up new user

**Body**
```
{
    "email": "user@email.com",
    "password": "123456",
    "first_name": "user name",
    "last_name": "user last name"
}
```

**Response**
```
{
    "id": "User UUID"
}
```

**POST /api/auth/login** - Log in user

**Body**
```
{
    "email": "user@email.com",
    "password": "123456"
}
```

**Response**
```
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MDc0NjgwODUsIm5iZiI6MTYwNzQ2ODA4NSwianRpIjoiMDUzNjIxYmMtODQxNC00MWVkLThjMTktNDM4OGRmNDA2ZTlkIiwiZXhwIjoxNjA3NTU0NDg1LCJpZGVudGl0eSI6IjVmY2Y5ZDYwNDIzOTRkOTc0ZWNjNzZhZCIsImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.-32MgaQ1oTb9xx4drktBD2NHojJmdPolFGFCld60lmw",
    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MDc0NjgwODUsIm5iZiI6MTYwNzQ2ODA4NSwianRpIjoiNzRmMWM5MzMtZGVmZS00ZmU5LTk3ZjQtZDZkYTc0YzZjYTdhIiwiZXhwIjoxNjA4MDcyODg1LCJpZGVudGl0eSI6IjVmY2Y5ZDYwNDIzOTRkOTc0ZWNjNzZhZCIsInR5cGUiOiJyZWZyZXNoIn0.S_1VU9Q5r7l4RYnrNqa8DPTqSkDBk-9Fnsx115FODs0"
}
```

**GET /api/deals/update** - Get Deals from Hubspot

**Header**
```
{
    "Content-Type": "application/json",
    "Authorization": "Bearer (Access Token)"
}
```

**Body**

If Update is successful, system will send the following response, with deals added or updated, and deals deleted from MongoDB
```
{
    "deals_deleted": 6,
    "deals_updated": 1
}
```


**GET /api/deals/show** - Show Deals

**Header**
```
{
    "Content-Type": "application/json",
    "Authorization": "Bearer (Access Token)"
}
```
**Body**

This will show the list of Deals stored in MongoDB
```
[
    {
        "dealtype": "existingbusiness",
        "dealid": "3576978050",
        "dealstage": "qualifiedtobuy",
        "dealname": "Test Deal 2",
        "amount": "20000",
        "closedate": "2021-01-06T16:17:33.916000"
    },
]
```

## Considerations

This API is developed using Flask with Flask-restful.
I use Marshmallow to serialize data, incoming and outgoing.

Flask-restful doesn't provide flexibility in terms of error handling (this was noticed far into the development process). So I opted for generating fixed custom exceptions for handling HubSpot API exceptions and our own exceptions.

Flask jwt was used to login and persist users within the API. Users cannot access the API endpoints without being logged to the backend.

Front End was my first React project, so it's very basic and lacks some common features (such as hiding components or disabling parts of the UI,  based on the app state) due to time constrains. I plan on continuing developing the frondend client for fun purposes.


