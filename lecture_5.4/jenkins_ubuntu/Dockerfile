FROM ubuntu:latest

ARG http_port=8080

RUN apt update && \
    apt install -y openjdk-11-jdk \
    wget \
    gnupg2 && \
    wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | apt-key add - && \
    echo 'deb https://pkg.jenkins.io/debian-stable binary/' > \
    /etc/apt/sources.list.d/jenkins.list && \
    apt update && \
    apt install -y jenkins

EXPOSE ${http_port}

USER root

CMD ["/usr/bin/java", "-jar", "/usr/share/jenkins/jenkins.war", "--httpPort=8080"]