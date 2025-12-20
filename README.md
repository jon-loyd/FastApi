# FastApi
A production ready FastAPI backend.

## Create and activate virtual environment
```
python -m venv venv
.\venv\Scripts\Activate.ps1
```

## Installing dependencies
```
pip install -r requirements.txt
```

## Start the docker container
```
docker-compose up -d
```

## Run the app
```
python -m uvicorn app.main:app --reload
```

## Maintaining dependencies
```
pip install pip-tools
pip-compile requirements.in
```

## Testing
```
pytest --cov=app --cov-report=html
start htmlcov\index.html
```
