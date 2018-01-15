FROM telegraf:alpine
LABEL maintainer="José Antonio Perdiguero López <perdy.hh@gmail.com>"

ENV APP=barrenero-telegraf

RUN apk add --no-cache python3 && \
    rm -rf /var/cache/apk/*

# Create project dirs
RUN mkdir -p /srv/apps/$APP
WORKDIR /srv/apps/$APP

# Install python requirements
COPY requirements.txt /srv/apps/$APP/
RUN pip3 install -r requirements.txt && \
    rm -rf $HOME/.cache/pip/*

ENTRYPOINT ["telegraf"]
