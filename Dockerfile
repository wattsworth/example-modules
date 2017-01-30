FROM jdonnal/joule:latest

MAINTAINER John Donnal <donnal@usna.edu>

ADD . /joule-modules
ADD ./e2e /etc/joule

CMD /usr/local/bin/jouled


