FROM telegraf:alpine

ENV APP=barrenero-telegraf

RUN apk add --no-cache python3 && \
    rm -rf /var/cache/apk/*

# Create project dirs
RUN mkdir -p /srv/apps/$APP
WORKDIR /srv/apps/$APP

# Install python requirements
COPY requirements.txt /srv/apps/$APP/
RUN pip3 install -r requirements.txt

# Copy Telegraf config
COPY telegraf/telegraf.conf /etc/telegraf/telegraf.conf
COPY telegraf/plugins/ /etc/telegraf/plugins/

# Copy run_storj.py script
COPY . /srv/apps/$APP/

ENTRYPOINT ["telegraf"]
