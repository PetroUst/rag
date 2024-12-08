import os
import glob


class Chunker:
    def __init__(self, folder="RFC-snap", chunk_size=512):
        self.folder = folder
        self.chunk_size = chunk_size
        self.docs = []
        self.doc_names = []

        # Load all documents
        for path in glob.glob(f"{self.folder}/*.txt"):
            with open(path, encoding="utf-8", errors="ignore") as f:
                self.docs.append(f.read())
                self.doc_names.append(os.path.basename(path).split('.')[0])  # Store file name without extension

        self.chunks = []

    def create_chunks(self):
        os.makedirs("CHUNKS", exist_ok=True)  # Ensure CHUNKS folder exists

        for doc, doc_name in zip(self.docs, self.doc_names):
            start_idx = 0
            doc_len = len(doc)
            chunk_index = 0

            while start_idx < doc_len:
                end_idx = min(start_idx + self.chunk_size, doc_len)

                # Adjust to avoid splitting a word
                while end_idx < doc_len and doc[end_idx] not in (' ', '\n'):
                    end_idx -= 1

                # Extract the chunk
                chunk = doc[start_idx:end_idx].strip()

                # Save the chunk to the CHUNKS folder
                chunk_filename = f"CHUNKS/{doc_name}_{chunk_index}.txt"
                with open(chunk_filename, "w", encoding="utf-8") as chunk_file:
                    chunk_file.write(chunk)

                chunk_index += 1

                # Move start_idx to maxsize/2 from the end of the current chunk
                start_idx = end_idx - self.chunk_size // 2

                # Avoid cutting words for the next chunk
                while start_idx < doc_len and start_idx > 0 and doc[start_idx] not in (' ', '\n'):
                    start_idx += 1


# Usage example
chunker = Chunker(chunk_size=512)
chunker.create_chunks()
print("Chunking complete!")
