# 打包上传步骤

### 1. 修改版本等信息

### 2. 打包

```
python setup.py sdist bdist_wheel
```

### 3. 发布上传

```
twine upload dist/*
```

参考 https://github.com/pypa/twine

