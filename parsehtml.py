from bs4 import BeautifulSoup

with open("videos.html") as f:
    videos_html = f.read()

soup = BeautifulSoup(videos_html, "html.parser")

# vids = soup.div.contents[0].contents[4].contents
vids = soup.find_all("a", id="video-title")
parsed = []
for vid in vids:
    title = vid.get("title")
    href = vid.get("href")
    code = href[9:20]
    parsed.append((code, title))

with open("parsed.txt", "w") as f:
    for p in parsed:
        print(*p, file=f)
