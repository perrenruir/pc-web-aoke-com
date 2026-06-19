SITE_NAME = "Aoke"
SITE_URL = "https://pc-web-aoke.com"
TAGS = ["aoke", "web", "pc", "online", "services"]
KEYWORDS = ["aoke platform", "aoke web", "pc aoke", "aoke services"]
DESCRIPTION = "A professional web-based platform for PC users, offering various online services and tools under the Aoke brand."

def generate_header():
    lines = []
    lines.append("=" * 50)
    lines.append(f"  Site Summary Report — {SITE_NAME}")
    lines.append("=" * 50)
    return "\n".join(lines)

def build_metadata_block():
    block = {
        "title": SITE_NAME,
        "url": SITE_URL,
        "tags": TAGS,
        "keywords": KEYWORDS,
        "summary": DESCRIPTION
    }
    return block

def format_tag_list(tags):
    return ", ".join(f"#{tag}" for tag in tags)

def format_keywords(kw_list):
    return " | ".join(kw_list)

def render_summary(meta):
    lines = []
    lines.append(f"Site Title: {meta['title']}")
    lines.append(f"URL:        {meta['url']}")
    lines.append(f"Tags:       {format_tag_list(meta['tags'])}")
    lines.append(f"Keywords:   {format_keywords(meta['keywords'])}")
    lines.append(f"")
    lines.append(f"Description:")
    lines.append(f"  {meta['summary']}")
    return "\n".join(lines)

def count_stats(meta):
    return {
        "tag_count": len(meta["tags"]),
        "keyword_count": len(meta["keywords"]),
        "desc_length": len(meta["summary"])
    }

def print_statistics(stats):
    print(f"  [Stats] Tags: {stats['tag_count']}, Keywords: {stats['keyword_count']}, Desc Length: {stats['desc_length']} chars")

def export_to_text(meta, stats):
    filename = "aoke_summary.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(generate_header() + "\n")
        f.write(render_summary(meta) + "\n")
        f.write(f"\nStatistics:\n")
        f.write(f"  Tags: {stats['tag_count']}, Keywords: {stats['keyword_count']}, Description Length: {stats['desc_length']} chars\n")
    print(f"  Exported summary to {filename}")

def main():
    print(generate_header())
    print()
    meta = build_metadata_block()
    print(render_summary(meta))
    print()
    stats = count_stats(meta)
    print_statistics(stats)
    print()
    export_to_text(meta, stats)
    print()
    print("Done.")

if __name__ == "__main__":
    main()