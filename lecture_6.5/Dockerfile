FROM centos:7

RUN yum update ; \
    yum install -y wget \
    sudo \
    perl-Digest-SHA

RUN wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.13.4-linux-x86_64.tar.gz && \
    wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.13.4-linux-x86_64.tar.gz.sha512 && \
    shasum -a 512 -c elasticsearch-7.13.4-linux-x86_64.tar.gz.sha512 && \
    tar -xzf elasticsearch-7.13.4-linux-x86_64.tar.gz
RUN mkdir /var/lib/nodes && \
    useradd es && \
    chown -R es /var/lib/nodes && \
    chown -R es /elasticsearch-7.13.4
EXPOSE 9200
COPY elasticsearch.yml /elasticsearch-7.13.4/config/

ENTRYPOINT ["/bin/sudo", "-u", "es"]
CMD ["/elasticsearch-7.13.4/bin/elasticsearch"]
#CMD ["/bin/bash"]

#EXPOSE 9200-9400

#RUN rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch

#COPY elasticsearch.repo /etc/yum.repos.d/

#RUN yum update ; \
#    yum install -y sudo ; \
#    yum install --enablerepo=elasticsearch -y elasticsearch
#RUN mkdir /var/lib/nodes && chown -R elasticsearch /var/lib/nodes
#COPY elasticsearch.yml /etc/elasticsearch/

#CMD ["sudo", "-u", "elasticsearch", "/usr/share/elasticsearch/bin/systemd-entrypoint", "--quiet"]
#CMD ["/bin/bash"]
