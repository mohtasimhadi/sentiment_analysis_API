# app.py
from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForSequenceClassification

app = Flask(__name__)

# Load pre-trained model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("StatsGary/setfit-ft-sentinent-eval")
model = AutoModelForSequenceClassification.from_pretrained("StatsGary/setfit-ft-sentinent-eval")

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    text = data.get('text')

    if not text:
        return jsonify({'error': 'Invalid request'}), 400

    # Tokenize input text and truncate/pad to a fixed length
    inputs = tokenizer.encode_plus(text, add_special_tokens=True, return_tensors='pt', max_length=512, truncation=True, padding=True)
    
    # Perform sentiment analysis
    outputs = model(**inputs)
    predictions = outputs.logits.argmax(dim=1)
    sentiment = "positive" if predictions.item() == 1 else "negative" if predictions.item() == 0 else "neutral"

    result = {'sentiment': sentiment}
    return jsonify(result)

if __name__ == '__main__':
    app.run()