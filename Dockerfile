FROM python:3.13-slim

WORKDIR /rickandmortyapi

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "src/main.py"]