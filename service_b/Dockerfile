FROM python:3.9-slim

WORKDIR /usr/src/b

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5001

ENV FLASK_APP=app/app.py:create_app

CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]