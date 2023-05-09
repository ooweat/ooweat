import feedparser
import time

URL = "https://ooweat.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

markdown_text = """### Welcome My Github :) 👋

📬  Contact Email : ooweat@kakao.com

👨🏻‍💻  Tech & Daily Blog : <a href="https://ooweat.tistory.com">ooweat 블로그 바로가기 :)</a>

[![github stats](https://github-readme-stats.vercel.app/api?username=ooweat&show_icons=true&hide_border=False)](https://ooweat.tistory.com)

🤩 Latest Blog Post

""" # list of blog posts will be appended here

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"[{time.strftime('[%Y.%m.%d]', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"
        
f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
