FROM python:slim

RUN useradd -m -d /home/futuser futuser &&\
    apt-get update && apt-get --no-install-recommends install -y locales &&\
    cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && echo "America/Sao_Paulo" > /etc/timezone
    # &&\ localedef -i pt_BR -c -f UTF-8 -A /usr/share/locale/locale.alias pt_BR.UTF-8

USER futuser
WORKDIR /home/futuser/app/service

ENV PATH $PATH:/home/futuser/.local/bin
ENV LANG pt_BR.UTF-8
ENV FLASK_DEBUG=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY requirements.txt /home/futuser/app/service
RUN pip3 install --upgrade pip -r requirements.txt
COPY . /home/futuser/app/service

EXPOSE 5000

CMD ["python", "app.py"]
