def chunk_text(text, chunk_size=500):
    """
    Splits text into manageable pieces for indexing.
    """

    chunks = []

    text = text.replace("\n", " ")

    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)

    return chunks
