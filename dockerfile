# 
FROM python:3.11-slim-bullseye

# Set working directory
WORKDIR /code

# copy requirements to working directory
COPY ./requirements.txt /code/requirements.txt

# Install newest version of pip
RUN python -m pip install --upgrade pip

# Install app packages from requirements
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# copy the application code to working directory
COPY ./app /code/app

# execute run api command
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]