import feedparser

# List of multiple RSS feeds
RSS_FEEDS = [
    "https://news.google.com/rss?hl=en-US&gl=US&ceid=US:en",
    "https://rss.cnn.com/rss/edition.rss",
    "https://www.aljazeera.com/xml/rss/all.xml"
]

# Create a Markdown file
md_content = "# 📰 Latest News Updates\n\n"

# Loop through each feed
for feed_url in RSS_FEEDS:
    feed = feedparser.parse(feed_url)
    md_content += f"## Source: {feed.feed.title}\n\n"

    for entry in feed.entries[:5]:  # Fetch top 5 articles per feed
        md_content += f"### [{entry.title}]({entry.link})\n\n"
        md_content += f"📅 {entry.published}\n\n"
        md_content += f"{entry.summary}\n\n"
        md_content += "---\n\n"

# Save Markdown file
with open("news.md", "w", encoding="utf-8") as f:
    f.write(md_content)

print("✅ News fetched and saved to news.md")
