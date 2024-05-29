### cwa-verification-server
- jdk: 11
- maven: 3.6.3
- project version: 1.5.0
- port: 8080
```shell
cd ./cwa-verification-server
docker build -t cwa .
docker run -d -p 8080:8080 --name cwa cwa
```

### features-service
- jdk: 11
- maven: 3.6.3
- project version: 1.5.0
- port: 8081
```shell
cd ./features-service
docker build -t features .
docker run -d -p 8081:8081 --name features features
```

### blog
- jdk: 11
- maven: 3.6.3
- project version: demo
- port: 8082 3306
```shell
cd ./blog
chmod +x ./reset.sh
docker compose build --no-cache
docker compose up
```
