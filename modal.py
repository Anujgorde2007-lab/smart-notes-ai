def classify_note(text):
    text = text.lower()

    if any(word in text for word in ["derivative", "integral", "algebra"]):
        return "Math"
    elif any(word in text for word in ["force", "energy", "motion"]):
        return "Physics"
    elif any(word in text for word in ["algorithm", "python", "data"]):
        return "Computer Science"
    else:
        return "General"


def summarize_note(text):
    return text[:60] + "..." if len(text) > 60 else text
