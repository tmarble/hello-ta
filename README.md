# hello-ta

Hello Technical Agility

## Dependencies

python3

## Running

```
./run.py
```

open http://localhost:8000

## Docker

### Building the container

```
docker build -t hello-ta .
```

### Running the container

```
docker run --rm=true --publish 8080:8000 hello-ta
```

open http://localhost:8080

_NOTE:_ Port 8000 is running inside the container, but exposed locally as 8080

