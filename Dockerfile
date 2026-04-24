#python 
FROM python:3.9.7

#workdir 
WORKDIR /app 

#copy files 
COPY requirements.txt ./

#run install 
RUN pip install --no-cache-dir -r requirements.txt

#copy everything 
COPY . . 

#expose port 

#serve 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"] 
