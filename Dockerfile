FROM python:3.9-slim
WORKDIR /usr/src/app
COPY hello.py .
CMD ["python", "./hello.py"]d