from pyquery import PyQuery

html = """
    <div id='content'>
        <ul class='list'>
            <li class='one'>One</li>
            <li class='two'>Two</li>
            <li class='three'>Three</li>
            <li class='four'>Four</li>
            <div id='inner'>
                <a href='http://www.baidu.com'>百度一下</a>
                <p>第一段</p>
                <p>第2段</p>
                <p>第3段</p>
                <p>
                    第4段
                    <span>法大师傅大师傅</span>
                </p>
                <p>第5段</p>
                <p>第6段</p>
            </div>
        </ul>
    </div>
"""

# 创建对象
doc_obj = PyQuery(html)
# print(doc_obj)

ul = doc_obj('p')

# ul是一个对象
print(ul)
print(type(ul))





























