.PHONY: all build up install clean

all: up

install:
	uv pip install -r requirements.txt

up:
	uv run streamlit run app.py

dev:
	uv run streamlit run app.py --server.runOnSave true

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
