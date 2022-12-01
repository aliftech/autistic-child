FROM python:3.10-slim-buster
WORKDIR /Autistic Children
COPY . .

ADD . /app
RUN pip install -r requirements.txt

EXPOSE 9001

CMD ["uvicorn", "app:app", "--reload"]