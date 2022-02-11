FROM python:3.9

COPY . .

RUN pip3 install -r requirements.txt
RUN python3 -m nltk.downloader punkt
RUN python3 -m nltk.downloader stopwords

# ENV PYTHONPATH=/api
# WORKDIR /api

EXPOSE 8000

ENTRYPOINT ["python", "app.py"]