# TimeMama readme

## 本地开发

由于本项目采用serverless framework(sls)进行开发和部署,
与一般项目使用规范略有不同,请注意和遵循以下使用规范


### 1. 安装依赖

由于sls原因,部署不再使用外部env环境,所有依赖包会直接安装到当前根目录下;
需要注意,本项目git托管中,托管的文件夹仅含bin和time_mama_brains `两个` 文件夹;

本地安装依赖需要使用以下命令,把依赖包安装到当前项目目录下

`pip install -r requirements.txt -t .`

### 2. 本地dev
本地dev可以采用flask run方式运行

`flask run` 普通调试  
`flask run --debugger --reload` 热加载输出日志调试  

## 依赖约定

本项目采用的是Flask框架,所使用的依赖应该以Flask为核心的扩展或周边依赖即可;
尽量保持项目简单轻量

项目中现已安装了

`flask` [flask 1.1.1]('https://dormousehole.readthedocs.io/en/latest/index.html')

`flask_sqlalchemy` [flask_sqlalchemy]('https://flask-sqlalchemy.palletsprojects.com/en/2.x/')



## 代码结构

代码结构依旧遵循sls规范,根目录下仅保留一个app.py用于调用入口;
其余代码应放到time_mama_brains中

## 文件结构

.env    --  用于存放环境变量,一般用于部署阶段  
.gitignore  --  git 配置  
app.py  --  程序入口  
requirements.txt    --  依赖描述(所有依赖都需要在此描述后再安装)  
serverless.yml  --  自动部署配置文件  

## 其他

### 5.1 数据库

本项目基于腾讯云的Serverless云函数形式托管部署运行,数据库也采用sls形式实现;  
数据库采用postgres实例,链接驱动采用了pg8000  
具体可以咨询管理员

  @Project power by kevin,zico & harry - 2021