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

/api/oauth/authorize - Perform OAuth flow to get HubSpot's access and refresh tokens.

/api/auth/signup - Sign Up new user
```
{
    "email": "user@email.com",
    "password": "123456",
    "first_name": "user name",
    "last_name": "user last name"
}
```

/api/auth/login - Sign In user

/api/deals/update - GET Deals from Hubspot

/api/deals/show - Show Deals

## Considerations

This API is developed using Flask with Flask-restful.
I use Marshmallow to serialize data, incoming and outgoing.

Flask-restful doesn't provide flexibility in terms of error handling (this was noticed far into the development process). So I opted for generating fixed custom exceptions for handling HubSpot API exceptions and our own exceptions.

Flask jwt was used to login and persist users within the API. Users cannot access the API endpoints without being logged to the backend.

Front End was my first React project, so it's very basic and lacks some common features (such as hiding components or disabling parts of the UI,  based on the app state) due to time constrains. I plan on continuing developing the frondend client for fun purposes.


