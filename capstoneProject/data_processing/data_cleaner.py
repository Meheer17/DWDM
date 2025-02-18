def clean_data(scraped_data):
    """
    Clean and structure the scraped data.
    """
    cleaned_data = []
    for data in scraped_data:
        if data and "paragraphs" in data:
            # Example: Remove empty paragraphs
            cleaned_paragraphs = [p for p in data["paragraphs"] if p]
            cleaned_data.append({
                "url": data["url"],
                "cleaned_paragraphs": cleaned_paragraphs
            })
    return cleaned_data