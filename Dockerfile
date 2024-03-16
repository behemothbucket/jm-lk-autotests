FROM	--platform=linux/amd64 python:latest

ENV	PYTHONDONTWRITEBYTECODE=1
ENV	PYTHONUNBUFFERED=1

RUN	wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN	sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN	apt-get -y update
RUN	apt-get install -y google-chrome-stable
RUN	apt-get install -y unzip
RUN	wget -O /tmp/chromedriver.zip https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/`curl -sS https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_STABLE`/linux64/chromedriver-linux64.zip -q --show-progress
RUN	unzip -j /tmp/chromedriver.zip chromedriver-linux64/chromedriver -d /usr/bin/

RUN	python3 --version && \
    /usr/bin/google-chrome-stable --version && \
    /usr/bin/chromedriver --version

ARG	USERNAME=qa
RUN	useradd -m $USERNAME
USER	$USERNAME
ARG	HOMEPATH=/home/$USERNAME

ENV	PATH=$PATH:$HOMEPATH/.local/bin

RUN	mkdir $HOMEPATH/jm-landing/
WORKDIR	$HOMEPATH/jm-landing/
COPY	 . $HOMEPATH/jm-landing/
RUN	cd $HOMEPATH/jm-landing/
RUN	pip install --no-cache-dir --upgrade pip
RUN	pip install --no-cache-dir  -r requirements.txt
