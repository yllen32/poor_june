FROM joyzoursky/python-chromedriver:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /app
RUN python job_finder/db_handler.py
CMD [ "python", "job_finder/main.py" ]