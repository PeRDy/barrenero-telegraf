FROM telegraf:alpine
LABEL maintainer="José Antonio Perdiguero López <perdy.hh@gmail.com>"

ENV APP=barrenero-telegraf

RUN apk add --no-cache python3 && \
    rm -rf /var/cache/apk/*

# Create project dirs
RUN mkdir -p /srv/apps/$APP
WORKDIR /srv/apps/$APP

# Install python requirements
COPY requirements.txt constraints.txt /srv/apps/$APP/
RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt -c constraints.txt && \
    rm -rf $HOME/.cache/pip/*

COPY . /srv/apps/$APP/

ENTRYPOINT ["telegraf"]
