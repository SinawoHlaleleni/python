FROM python:3.7.2
RUN pip install Flask==0.11.1
RUN useradd -ms /bin/bash admin
USER admin
WORKDIR /ex40
CMD ["python", "ex40.py"]
