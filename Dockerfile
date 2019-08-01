FROM python
RUN apt-get update && \
  apt-get install sqlite3 -y && \
  apt-get install vim -y
WORKDIR /usr/src/app
RUN pip install --upgrade pip && \
    pip install --no-cache-dir rasa 
COPY data data
RUN rasa init --no-prompt
ENTRYPOINT [ "rasa", "run", "--enable-api","--cors", "*"]

