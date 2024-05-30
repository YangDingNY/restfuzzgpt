构建镜像
```shell
docker build -t evomaster .
docker run -it --name evomaster -v /path/to/restfuzzgpt/benchmark/docs:/root/evomaster/docs -v /path/to/restfuzzgpt/experiments/baselines/evomaster/src/em:/root/evomaster/src/em --network network-benchmark evomaster
```

运行evomaster（blackbox）
```shell
java -jar ./evomaster.jar  --blackBox true --bbSwaggerUrl ./docs/swagger.json  --outputFormat JAVA_JUNIT_4 --maxTime 60s --ratePerMinute 60
```
