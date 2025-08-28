# you will also find guides on how best to write your Dockerfile

FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
 PATH=/home/user/.local/bin:$PATH

WORKDIR $HOME/app

COPY --chown=user . $HOME/app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
