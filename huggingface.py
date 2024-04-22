from transformers import pipeline

# Load the pipeline for text classification
metadata_pipeline = pipeline("text-classification")

# Read the file and preprocess it
with open(r"C:\Users\TSATYAWA\Downloads\sample2.json", "r") as file:
    text = file.read()

# Extract metadata using the model
metadata = metadata_pipeline(text)

# Print the extracted metadata
print(metadata)
