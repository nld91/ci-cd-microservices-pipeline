# CI/CD Microservices Pipeline

This repository contains two simple Python Flask applications that simulate a microservices architecture. Each microservice (`service_a` and `service_b`) resides in its directory, complete with the application source code, unit tests, a Dockerfile, and a `requirements.txt` for managing dependencies. The repository's root directory includes a `docker-compose.yml` file to facilitate local testing and development.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

-   Docker
-   docker-compose
-   Python 3.8 or newer

### Installation

1.  Clone the repository:
       
    `git clone https://github.com/nld91/ci-cd-microservices-pipeline.git` 
    
2.  Navigate to the project directory:
       
    `cd ci-cd-microservices-pipeline` 
    
3.  Use docker-compose to build and run the services locally:
       
    `docker-compose up --build` 
    

## Usage

Once the services are running, you can access them through their respective ports.

-   **Service A** responds at `http://localhost:5000/` with a simple greeting from Microservice A.
-   **Service B** responds at `http://localhost:5001/`, with a string incorporating service A's message into its own.

## Building and Testing

To build and test each service individually, navigate to the service's directory and use Docker:

For **Service A**:

```
cd service_a
docker build -t service_a .
docker run service_a pytest
``` 

Repeat similar steps for **Service B**, adjusting for the correct directory and service names.

## Deployment

WIP

## Contributing

Contributions welcome! Please feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](https://chat.openai.com/c/LICENSE.md) file for details.