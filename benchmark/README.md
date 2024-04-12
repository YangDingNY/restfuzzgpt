### cwa-verification-server
- jdk: 11
- maven: 3.6.3
- project version: 1.5.0
```dockerfile
docker build -t cwa .
docker run -d -p 8080:8080 --name cwa cwa
```
