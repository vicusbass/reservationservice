# ReservationService

Reservation service build with FastAPI and Postgres

![Continuous Integration and Delivery](https://github.com/vicusbass/reservationservice/workflows/Continuous%20Integration%20and%20Delivery/badge.svg?branch=master)

## Run in development mode

`docker` and `docker-compose` are assumed to be installed on the development machine.

### Start the service and a Postgres dev db

```shell script
cd src
docker-compose up -d web web-db
```

### Run DB migrations

`docker-compose exec web python app/db.py`

## API documentation

The API documentation is located [here](http://localhost:8002/docs)

## Performance benchmark

Create 100 reservations with high load, with 10 concurrent users

```shell script
cd performance_tests
docker run -i loadimpact/k6 run --vus 10 --iterations 100 - <create_reservations.js
```

The service is running in Docker container, Postgres DB as well, on Ubuntu laptop. Performance tests are based on `k6.io` and are located in `performance_tests` folder.
Here are the tests results, the request rate goes over 1000 RPS, with a response time of 8.26 ms.

```text
    checks.....................: 100.00% ✓ 100  ✗ 0   
    data_received..............: 24 kB   288 kB/s
    data_sent..................: 22 kB   261 kB/s
    http_req_blocked...........: avg=43.99µs min=1.58µs  med=2.58µs  max=627.84µs p(90)=35.93µs p(95)=425.23µs
    http_req_connecting........: avg=30.93µs min=0s      med=0s      max=560.07µs p(90)=8.66µs  p(95)=222.57µs
    http_req_duration..........: avg=8.08ms  min=4.49ms  med=7.79ms  max=17.3ms   p(90)=10.54ms p(95)=11.27ms 
    http_req_receiving.........: avg=41.01µs min=23.19µs med=40.12µs max=87.61µs  p(90)=58.36µs p(95)=64.46µs 
    http_req_sending...........: avg=19.69µs min=9µs     med=12.15µs max=314.45µs p(90)=30.45µs p(95)=49.31µs 
    http_req_tls_handshaking...: avg=0s      min=0s      med=0s      max=0s       p(90)=0s      p(95)=0s      
    http_req_waiting...........: avg=8.02ms  min=4.44ms  med=7.75ms  max=17.26ms  p(90)=10.46ms p(95)=11.22ms 
    http_reqs..................: 100     1189.575597/s
    iteration_duration.........: avg=8.26ms  min=4.64ms  med=7.91ms  max=17.43ms  p(90)=10.68ms p(95)=11.46ms 
    iterations.................: 100     1189.575597/s
    vus........................: 10      min=10 max=10
    vus_max....................: 10      min=10 max=10

```