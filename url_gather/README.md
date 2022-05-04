## 说明文档 ##
### 介绍
* 使用该脚本，结合GoogleHack语法，可以快速搜集大量含有漏洞特征的URL
* 爬取的是baidu & bing的搜索结果
* 主要用于批量化寻找含有SQL注入的脆弱站点，结合sqlmap & sqlmapapi进行批量化验证.
* 参数说明
```
        -t  --threads           线程数
        -p  --page              爬取结果的页数
        -o  --outfile           结果的保存路径
        -h                      显示帮助信息     
```
### python环境
* python >=3.7
### 使用步骤
1.更新pip
- python -m pip install --upgrade pip 
2.安装依赖项
- pip install -r requirement.txt


