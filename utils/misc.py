from collections import defaultdict
import random

def group_entries_by_month(entries):
    """Group entries by month."""
    grouped_entries = defaultdict(list)
    for entry in entries:
        month = entry.created_at.strftime('%B %Y')
        grouped_entries[month].append(entry)
    return grouped_entries

greetings = [
    "Hello, {name}! How are you feeling today?",
    "Good day, {name}! Ready to reflect?",
    "Hey there, {name}! What's on your mind?",
    "Greetings, {name}! Let's dive into your thoughts.",
    "Welcome, {name}! It's time to write.",
    "Hi, {name}! Let's capture today's moments.",
    "Hey, {name}! How's your day unfolding?",
    "Hey there, {name}! Ready to jot down your feelings?",
    "Good vibes, {name}! What will today's entry bring?",
    "Hello, {name}! Let's reflect on today's journey.",
    "A warm welcome, {name}! Time to write your story.",
    "How are you today, {name}? Let's begin your entry.",
    "Hi, {name}! Let's capture today's reflections."
]

def get_personalized_greeting(name: str):
    greeting = random.choice(greetings) 
    return greeting.format(name=name)

def processContent(content: str):
    paras = content.split("\n\n")
    processedContent = "\n>\n".join([f"> {para}" for para in paras])
    return processedContent