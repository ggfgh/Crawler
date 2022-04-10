## 说明文档 ##
### 介绍
* 这是两个搜集URL的脚本，爬取的是baidu & bing的搜索结果.
* 主要用于SQL注入的批量化，结合sqlmap.
* 参数说明
    -  -t  --threads  线程数
    -  -p  --page     爬取结果的页数
    -  -o             结果的保存路径
    -  -h             显示帮助信息     

### 使用
pip install -r requirement.txt
environment: python >=3.7
