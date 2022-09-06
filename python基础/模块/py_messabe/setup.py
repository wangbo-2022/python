from distutils.core import setup

setup(
    name="py_message",
    version="1.0",
    author="pypy",
    author_email="pypy@163.com",
    description="pypy",

    # 项目主页
    url="pypypy",

    # 你要安装的包，通过 setuptools.find_packages 找到当前目录下有哪些包
    py_modules=["py_messabe.send_message", "py_messabe.receive_message"])