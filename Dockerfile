FROM python:3.6
EXPOSE 34251
ADD . /root/psite
WORKDIR /root/psite
RUN pip install -r requirements.txt
CMD ["python", "webui.py"]
