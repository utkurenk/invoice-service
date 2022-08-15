FROM python:3.10

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "./main.py", "--host", "0.0.0.0"]