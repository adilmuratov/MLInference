from mlmodels.spam_email_detection.spam_detection import spam_detection

def model_predict(
    model_name: str,
    text: str
):
    match model_name:
        case "spam_detection":
            return spam_detection(text)
        case _:
            return False