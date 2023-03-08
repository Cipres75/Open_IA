FROM ubuntu:18.04
RUN apt-get -y update && apt -get install software-properties-common / && add-apt-repository ppa:deadsnakes/ppa && apt install python3.10
COPY grobid-0.7.2/ /grobid-0.7.2/
COPY grobid_client_python/ /grobid-0.7.2/grobid_client_python/
RUN pip install wordcloud && pip install requests
WORKDIR grobid-0.7.2/
CMD ./gradlew run && python3 grobid_client_python/OpenIA_Grobid.py
EXPOSE 80
