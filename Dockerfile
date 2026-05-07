FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install flask numpy scikit-learn gunicorn

EXPOSE 7860

CMD ["python", "app.py"]