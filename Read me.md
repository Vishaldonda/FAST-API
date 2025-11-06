# 1. Virtual Env Set Up
python3 -m venv myenv

Mac: source myenv/bin/activate

On Windows : myenv\Scripts\activate

TO Deactivate : deactivate

Save packages into a file : pip freeze > requirements.txt


# 2. Install dependencies
1. Install FastAPI and Uvicorn :
pip3 install fastapi uvicorn
pip3 install sqlalchemy

2. Run your FastAPI app:
uvicorn main:app --reload


# Docs
1. Swagger Docs
Swagger UI:
http://127.0.0.1:8000/docs


2. Alternative (ReDoc UI):
http://127.0.0.1:8000/redoc