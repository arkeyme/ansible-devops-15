from python:rc-alpine3.13
WORKDIR /app
RUN pip install flask redis
ADD app.py /app/
EXPOSE 80
CMD ["python", "app.py"]