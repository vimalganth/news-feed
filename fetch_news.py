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
    
    # Check if the feed has a title
    feed_title = feed.feed.get('title', 'No title available')
    md_content += f"## Source: {feed_title}\n\n"

    for entry in feed.entries[:5]:  # Fetch top 5 articles per feed
        entry_title = getattr(entry, 'title', 'No title')
        entry_link = getattr(entry, 'link', '#')
        entry_published = getattr(entry, 'published', 'No date available')
        entry_summary = getattr(entry, 'summary', 'No summary available')

        md_content += f"### [{entry_title}]({entry_link})\n\n"
        md_content += f"📅 {entry_published}\n\n"
        md_content += f"{entry_summary}\n\n"
        md_content += "---\n\n"

# Save Markdown file
with open("news.md", "w", encoding="utf-8") as f:
    f.write(md_content)

print("✅ News fetched and saved to news.md")
