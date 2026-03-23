from pathlib import Path

import pickle

BASE_DIR = Path(__file__).resolve().parent

def spam_detection(text: str) -> bool:
    vectorizer_path = BASE_DIR / "spam_detection_files" / "vectorizer.pkl"
    model_path = BASE_DIR / "spam_detection_files" / "SVM_model.pkl"

    with open(vectorizer_path, "rb") as f:
        vectorizer = pickle.load(f)

    with open(model_path, "rb") as f:
        model = pickle.load(f)

    X = vectorizer.transform(text)

    prediction = model.predict(X)

    if prediction[0] == 0:
        return True
    else: 
        return False