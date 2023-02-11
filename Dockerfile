FROM python:3.11.2-bullseye

COPY dist /home/app
ENV WORDLIST=/usr/share/wordlist.txt
COPY wordlist.txt /usr/share


RUN pip install /home/app/contentscanner-0.1.0.tar.gz
RUN rm /home/app/contentscanner-0.1.0.tar.gz /home/app/contentscanner-0.1.0-py3-none-any.whl


