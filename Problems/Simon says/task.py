def what_to_do(instructions):
    simon = "Simon says"
    if instructions.startswith(simon) or instructions.endswith(simon):
        return f"I {instructions.replace(simon, '').strip()}"
    else:
        return "I won't do it!"
