FROM obtest/base
MAINTAINER Y12STUDIO <y12studio@gmail.com>

RUN apt-get install -y python-pip

ADD requirements.txt /opt/pyrest/requirements.txt
RUN cd /opt/pyrest && pip install -r requirements.txt

CMD ["/sbin/my_init"]
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*