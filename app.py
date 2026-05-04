from model import classify_note, summarize_note

print("📘 AI Notes Organizer")
print("----------------------")

note = input("Enter your study note:\n")

category = classify_note(note)
summary = summarize_note(note)

print("\n🔹 Category:", category)
print("🔹 Summary:", summary)
