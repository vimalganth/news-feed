import feedparser
import os

# List of RSS feeds
RSS_FEEDS = [
    "https://news.google.com/rss?hl=en-US&gl=US&ceid=US:en",
    "https://www.aljazeera.com/xml/rss/all.xml"
]

# Create Markdown content
md_content = "# 📰 Latest News Updates\n\n"

# Track if any news was fetched
news_count = 0  

# Loop through each feed
for feed_url in RSS_FEEDS:
    print(f"📡 Fetching news from: {feed_url}")  # Debugging output

    feed = feedparser.parse(feed_url)

    # Check if feed has entries
    if not feed.entries:
        print(f"⚠️ WARNING: No news found in {feed_url}")
        continue  # Skip this feed if empty

    # Get feed title
    feed_title = feed.feed.get('title', 'No title available')
    md_content += f"## Source: {feed_title}\n\n"

    for entry in feed.entries[:5]:  # Fetch top 5 articles
        entry_title = getattr(entry, 'title', 'No title')
        entry_link = getattr(entry, 'link', '#')
        entry_published = getattr(entry, 'published', 'No date available')
        entry_summary = getattr(entry, 'summary', 'No summary available')

        md_content += f"### [{entry_title}]({entry_link})\n\n"
        md_content += f"📅 {entry_published}\n\n"
        md_content += f"{entry_summary}\n\n"
        md_content += "---\n\n"

        news_count += 1  # Track the number of articles added

# Ensure news.md is actually written
try:
    with open("news.md", "w", encoding="utf-8") as f:
        f.write(md_content)
    print("✅ News successfully written to news.md!")
except Exception as e:
    print(f"❌ ERROR: Failed to write news.md → {e}")
    exit(1)  # Exit with error

# Check if file is empty after writing
if os.path.getsize("news.md") == 0:
    print("❌ ERROR: news.md is empty! Something went wrong with writing.")
    exit(1)  # Exit with error
else:
    print("📄 news.md file successfully updated! 🚀")
