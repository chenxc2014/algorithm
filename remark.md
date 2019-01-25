# 如何切换默认的pypi源（国外的pypi源）
国内的pypi源有  
````
阿里云：http://mirrors.aliyun.com/pypi/simple/  
中国科技大学：https://pypi.mirrors.ustc.edu.cn/simple/
豆瓣(douban): http://pypi.douban.com/simple/
清华大学: https://pypi.tuna.tsinghua.edu.cn/simple/
中国科学技术大学: http://pypi.mirrors.ustc.edu.cn/simple/
````
- 手动指定  
如：安装pandas  
``
pip install pandas -i http://pypi.douban.com/simple/
``  
如果出现  
``pypi.douban.com is not a trusted or secure host and is being ignored...``  
则执行下面命令  
``pip install pandas -i http://pypi.douban.com/simple --trusted-host pypi.douban.com``  
- 修改默认pypi源  
  - 在liunx环境下，在当前的虚拟环境下面新建pip.conf文件  
  ``~/.pip/pip.conf``  
  - 在windows环境下，在当前的虚拟环境下面的pip文件夹新建pip.ini，并配置系统环境变量  
  ``%HOMEPATH%\pip\pip.ini``  
  - 在上面2个文件夹里面写入这些代码  
  ````
  [global]  
  index-url=http://pypi.douban.com/simple/   
  [install]  
  trusted-host=pypi.douban.com    
  ````
  
  
