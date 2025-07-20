# ERA5-Data-Download-Script
这是一个ERA5再分析数据集的下载脚本<br>
This is a download script for an ERA5 reanalysis dataset
# 项目结构
- ERA5.py：用于实现下载逻辑的类
- main.py：下载入口（简单实现）
- main_multi_processing.py：下载入口（多进程/带重复请求机制的实现）
# 依赖库
- cdsapi
```
pip install cdsapi
```
# 使用说明
请参考https://cds.climate.copernicus.eu/how-to-api<br>
1. 需要登录ECMWF账号
2. 查看令牌信息
3. 将.cdsapirc令牌文件置于Home目录（用户目录）
