FROM python
WORKDIR app
ARG TOKEN
ARG URL
ENV CONSUL_METRICS_ENDPOINT=${URL}}
ENV CONSUL_TOKEN=${TOKEN}}
COPY metrics.py  .
COPY requirments.txt .
RUN pip3 install -r requirments.txt
CMD ["python", "metrics.py"]
EXPOSE 5000
