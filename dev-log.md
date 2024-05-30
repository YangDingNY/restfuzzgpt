# Dev-Log

**4.18-4.23**

1. llm response -> http request
2. llm会一直不停的生成一个测试用例中的请求

**4.24-5.1**

重构了测试的逻辑，将测试序列的生成分为两步：

1. 生成测试序列；
2. 为测试序列中的每个请求构造具体的内容。

分步生成的好处在于可以让大模型更加聚焦于某一任务（给大模型时间去思考），不会再出现以前一个测试序列中不断生成请求的现象。

**5.3-5.7**

在warhhouse项目上进行了测试，发现了以下问题：

1. 不能得到正确的url；
2. 生成测试序列时找不到operationId
3. 生成具体请求时的格式问题

**5.8-5.13**
1. 修复了operationId问题
2. 格式化了warehouse项目的swagger
3. （进行中）读取分析swagger文档，识别其中的baseurl，path，opertionId等信息

**5.14-5.31**
1. blog docker 环境搭建
2. evomaster实验环境搭建
3. 使用tcpdump捕获http请求
```shell
tcpdump -i eth0 'tcp port 8080 and (((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2)) != 0)'
```
