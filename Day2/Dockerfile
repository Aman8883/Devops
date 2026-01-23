FROM python:3.9-slim
LABEL maintainer="kanojiaaman9@gmail.com"
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_ENV=production

CMD ["python","app.py"]
