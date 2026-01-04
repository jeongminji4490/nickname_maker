# Nickname Maker
LLM-based Nickname Recommendation Web Service

http://13.238.182.199:8501/

<img width="2814" height="1918" alt="image" src="https://github.com/user-attachments/assets/a9f9e9c8-5db2-4866-a297-6a7475a22aea" />

## Stacks

- Python-based Streamlit and FastAPI were used to quickly develop a web client (UI) and a backend API server with a clear separation of concerns.
    - Although the API is relatively simple, FastAPI was intentionally chosen to gain experience designing a structure that can support additional clients in the future, such as Flutter.
- Docker and Docker Compose were used to containerize the server and standardize the execution environment, improving deployment stability.
    - By building and running the application using Docker images, a consistent runtime environment can be maintained without manual package installation or local environment setup.
    - Docker Compose was used to separate API server testing and Web UI testing by running each service in its own container.
- AWS EC2 was used to provision and operate the cloud environment for deploying the FastAPI server.
- OpenAI GPT-4o-mini was used as the LLM to generate nickname recommendation responses.

| Layer  | Stacks             |
| ------ | ------------------------ |
| Client | Streamlit (Web UI)       |
| Server | FastAPI, Docker, AWS EC2 |
| LLM    | OpenAI GPT-4o-mini       |
