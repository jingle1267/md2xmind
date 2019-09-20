# md2xmind

![md2xmind](https://github.com/jingle1267/md2xmind/raw/master/md_xmind_preview.png)


markdown转思维导图基于python，实现把markdown格式的文档转换为xmind格式的文档。目前支持版本小于 8 的 xmind 。

### 安装

pip3 install md2xmind

### 升级

pip3 install -U md2xmind

### 使用方式

```python
import os
import md2xmind

# md格式的源文件路径
file_path = os.path.abspath(os.path.join(os.getcwd(), 'test2.md'))

# 第一个参数是源文件
# 第二个参数是生成的文件名称，生成的文件位于运行命令行的文件夹中
md2xmind.start_trans(file_path, 'test2')

```


