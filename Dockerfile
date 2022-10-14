
FROM python:3.7-slim AS compile-image
RUN apt-get update
RUN apt-get -y install git
RUN apt-get install -y --no-install-recommends build-essential gcc wget

# Make sure we use the virtualenv:
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install numpy

# TA-Lib
RUN wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz && \
  tar -xvzf ta-lib-0.4.0-src.tar.gz && \
  cd ta-lib/ && \
  ./configure --prefix=/opt/venv && \
  make && \
  make install

RUN pip install --global-option=build_ext --global-option="-L/opt/venv/lib" TA-Lib==0.4.16
RUN rm -R ta-lib ta-lib-0.4.0-src.tar.gz

COPY req.txt .
RUN pip install -r req.txt

FROM python:3.7-slim AS build-image
COPY --from=compile-image /opt/venv /opt/venv

# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"
ENV LD_LIBRARY_PATH="/opt/venv/lib"

RUN mkdir -p /app/src

WORKDIR /app/src

COPY . .
EXPOSE 8000

CMD [ "supervisord" ]

