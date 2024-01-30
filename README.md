# 项目说明文档


## 项目目录
```
/service_template
├── README.md                     # 项目说明文档      
├── app.py                        # 项目启动文件
├── config                        # 项目配置目录
│   └── default_config.py         # 项目配置文件
├── logs                          # 日志文件目录
├── mainapp                       # 项目主逻辑目录
│   └── routes                    # 接口文件目录
│       ├── __init__.py           # 路由管理初始化文件
│       └── test_route.py         # 接口文件
├── requirements.txt              # 项目依赖文件
├── service_template.ini          # supervisor 配置文件
├── utils                         # 工具类目录
│   ├── logger_handler.py         # 自定义日志文件
│   ├── resp_handler.py           # 请求钩子文件
│   └── shared.py                 # 公共方法文件
└── uwsgi.ini                     # uwsgi 配置文件
```