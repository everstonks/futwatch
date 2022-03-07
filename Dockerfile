FROM python:slim

RUN useradd -m -d /home/futuser futuser &&\
    apt-get update && apt-get --no-install-recommends install -y locales &&\
    cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && echo "America/Sao_Paulo" > /etc/timezone
    # &&\ localedef -i pt_BR -c -f UTF-8 -A /usr/share/locale/locale.alias pt_BR.UTF-8

WORKDIR /home/futuser/app/service

COPY ./service/ .

ENV PATH $PATH:/home/futuser/.local/bin
ENV LANG pt_BR.UTF-8
ENV FLASK_DEBUG=1
ENV FLASK_ENV=development
ENV PYTHONDONTWRITEBYTECODE=1

RUN chown -R futuser:futuser /home/futuser/app/service &&\
    pip3 install --upgrade pip -r requirements.txt

EXPOSE 5000

USER futuser

CMD ["flask", "run", "--host=0.0.0.0"]
