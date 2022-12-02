FROM python:3.10
WORKDIR /Autistic Children
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["uvicorn", "app:app", "--reload"]