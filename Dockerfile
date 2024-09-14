# *THIS IS JUST A TEMPLATE! DO NOT USE THIS FILE!*

# Use the official Python image as the base image.
FROM python:3.9-slim

# Set the working directory in the container.
WORKDIR /app

# Copy the current directory contents into the container.
COPY . /app

# Install any needed packages specified in requirements.txt.
RUN pip install --no-cache-dir -r requirements.txt

# Install ChromeDriver and dependencies for Selenium (for dynamic scraping).
RUN apt-get update && apt-get install -y wget gnupg && \
    wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' && \
    apt-get update && apt-get install -y google-chrome-stable && \
    wget -N https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip -d /usr/local/bin/ && rm chromedriver_linux64.zip

# Install additional tools and libraries for data processing, modeling, etc.
RUN apt-get install -y libpq-dev && pip install psycopg2-binary

# Expose port 80 to the outside world.
EXPOSE 80

# Run the default command.
CMD ["python", "src/scraping/scraper_static.py"]

# *THIS IS JUST A TEMPLATE! DO NOT USE THIS FILE!*
