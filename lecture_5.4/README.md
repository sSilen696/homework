### Задание 1

```dockerfile
FROM archlinux:latest

RUN pacman -Sy

RUN pacman -S --noconfirm ponysay

ENTRYPOINT ["/usr/bin/ponysay"]
CMD ["Hey, netology”]
```

### Задание 2

Для Amazon так же есть в директории jenkins_amazoncorreto
```dockerfile
FROM amazonlinux

ARG version=11.0.11.9-1
# In addition to installing the Amazon corretto, we also install
# fontconfig. The folks who manage the docker hub's
# official image library have found that font management
# is a common usecase, and painpoint, and have
# recommended that Java images include font support.
#
# See:
#  https://github.com/docker-library/official-images/blob/master/test/tests/java-uimanager-font/container.java

# The logic and code related to Fingerprint is contributed by @tianon in a Github PR's Conversation
# Comment = https://github.com/docker-library/official-images/pull/7459#issuecomment-592242757
# PR = https://github.com/docker-library/official-images/pull/7459
RUN set -eux \
    && export GNUPGHOME="$(mktemp -d)" \
    && curl -fL -o corretto.key https://yum.corretto.aws/corretto.key \
    && gpg --batch --import corretto.key \
    && gpg --batch --export --armor '6DC3636DAE534049C8B94623A122542AB04F24E3' > corretto.key \
    && rpm --import corretto.key \
    && rm -r "$GNUPGHOME" corretto.key \
    && curl -fL -o /etc/yum.repos.d/corretto.repo https://yum.corretto.aws/corretto.repo \
    && grep -q '^gpgcheck=1' /etc/yum.repos.d/corretto.repo \
    && yum install -y java-11-amazon-corretto-devel-$version \
    && (find /usr/lib/jvm/java-11-amazon-corretto -name src.zip -delete || true) \
    && yum install -y fontconfig \
    wget \
    && yum clean all

ENV LANG C.UTF-8
ENV JAVA_HOME=/usr/lib/jvm/java-11-amazon-corretto

RUN wget -O /etc/yum.repos.d/jenkins.repo \
    https://pkg.jenkins.io/redhat-stable/jenkins.repo
RUN rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
RUN yum upgrade && \
    yum install -y jenkins


CMD ["/usr/lib/jvm/java-11-amazon-corretto/bin/java", "-jar", "/usr/lib/jenkins/jenkins.war", "--httpPort=8080"]

```
Для Ubuntu аналогично лежит в jenkins_ubuntu
```dockerfile
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

```
### Задание 3
Файл лежит nodejs
```dockerfile
FROM node



RUN git clone https://github.com/simplicitesoftware/nodejs-demo.git

WORKDIR /nodejs-demo
EXPOSE 3000
RUN sed -i "s/localhost/0.0.0.0/" app.js
RUN npm install


CMD  ["npm", "start"]
```