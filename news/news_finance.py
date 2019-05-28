import tushare as ts
import pandas  as pd

print(ts.__version__)

pd.set_option('max_colwidth', 500)

# 默认获取最近80条新闻数据，只提供新闻类型、链接和标题
ds = ts.get_latest_news()
print(ds)
ds = ts.get_latest_news(top=5, show_content=True)  # 显示最新5条新闻，并打印出新闻内容
print(ds['title'])
print(ds['url'])
print(ds['content'])

ds = ts.get_notices()
print(ds)
