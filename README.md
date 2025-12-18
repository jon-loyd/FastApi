# FastApi
A production ready FastAPI backend.

## Create and activate virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

## Installing dependencies
pip install -r requirements.txt

## Maintaining dependencies
pip install pip-tools
pip-compile requirements.in

## Start the docker container
docker-compose up -d

## Run the app
python -m uvicorn app.main:app --reload