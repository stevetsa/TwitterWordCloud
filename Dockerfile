FROM ubuntu:16.04
RUN \
apt-get update && apt-get install -y \
wget \
build-essential \
git \
libfreetype6-dev \
libxml2-dev \
libxslt-dev \
pkg-config \
python3 python3-numpy python3-nose python3-pandas python3-h5py python3-pip \
pep8 python-wheel \
python-sphinx
RUN pip3 install --upgrade setuptools
RUN pip3 install -U nltk tweepy wordcloud

ENV SRC /opt
ENV BIN /usr/local/bin

RUN [ "python3", "-c", "import nltk; nltk.download('all')" ]
WORKDIR $SRC
RUN git clone https://github.com/stevetsa/twitterwordcloud.git
WORKDIR /opt/twitterwordcloud

RUN cp *.py /usr/local/bin/.
COPY Dockerfile /opt/Dockerfile
