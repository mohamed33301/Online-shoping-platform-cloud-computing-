FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt /app/
COPY user_management.py /app/
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade markupsafe==2.0.1  
EXPOSE 5000
ENV FLASK_APP user_management.py
CMD ["flask", "run", "--host=0.0.0.0"]
