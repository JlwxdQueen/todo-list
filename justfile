run:
    uvicorn main:app --reload

format:
	poetry run black .