FROM ubuntu:16.04

ENV LANG=C.UTF-8

RUN \
  apt-get -y update && \
  apt-get install -y software-properties-common vim unzip curl

# Java 설치
RUN \
  echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
  add-apt-repository -y ppa:webupd8team/java && \
  apt-get update && \
  apt-get install -y oracle-java8-installer && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /var/cache/oracle-jdk8-installer

# Define commonly used JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle
# ENV CLASSPATH .:${CLASSPATH}
ENV PATH ${JAVA_HOME}/bin:${PATH}


RUN \
  apt-get install -y software-properties-common && \
  add-apt-repository -y ppa:fkrull/deadsnakes && \
  apt-get -y update


RUN apt-get install -y --no-install-recommends build-essential python3.6 python3-pip python3-setuptools git

RUN python3.6 -m pip install pip --upgrade

ADD . /app

WORKDIR /app

RUN pip3.6 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "./run.sh" ]
