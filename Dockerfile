FROM python
WORKDIR /app
ENV PORT=8000

COPY run.py /app/
COPY resources/public/ /app/resources/public/

RUN echo "Technical Agility PORT = ${PORT}"
EXPOSE ${PORT}

CMD [ "./run.py" ]

