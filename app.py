from model import classify_note, summarize_note

print("📘 AI Notes Organizer")
print("----------------------")

note = input("Enter your study note:\n")

category = classify_note(note)
summary = summarize_note(note)

print("\n🔹 Category:", category)
print("🔹 Summary:", summary)
if __name__ == "__main__":
    text = input("Enter your note: ")

    category = classify_note(text)
    summary = summarize_note(text)

    print("\nCategory:", category)
    print("Summary:", summary)
