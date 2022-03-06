FROM python:slim

WORKDIR /app/service

RUN useradd -u 9999 futuser && apt-get update && apt-get --no-install-recommends install -y locales &&\
    cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && echo "America/Sao_Paulo" > /etc/timezone &&\
    localedef -i pt_BR -c -f UTF-8 -A /usr/share/locale/locale.alias pt_BR.UTF-8

COPY requirements.txt /app/service
RUN pip3 install --upgrade pip -r requirements.txt

USER futuser

COPY . /app/service

ENV LANG pt_BR.UTF-8
ENV FLASK_DEBUG=1
ENV PYTHONDONTWRITEBYTECODE=1

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["app.py"]
