import re

INPUT_FILE = "questions.txt"
OUTPUT_FILE = "quiz.md"

ANSWER_RE = re.compile(r"^([A-Da-d])[.)\-]\s*(.+)")
CORRECT_RE = re.compile(r"(✓|\(Đúng\))")

def clean_markdown(text: str) -> str:
    # remove bold / italic
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"\*(.*?)\*", r"\1", text)

    # remove inline code
    text = re.sub(r"`(.*?)`", r"\1", text)

    return text.strip()


def convert(text: str) -> str:
    lines = [l.rstrip() for l in text.splitlines() if l.strip()]

    quizzes = []
    question = None
    answers = []

    def flush():
        if question and answers:
            block = ["<quiz>", question]
            for text, correct in answers:
                block.append(f"- [{'x' if correct else ' '}] {text}")
            block.append("</quiz>\n")
            quizzes.append("\n".join(block))

    for line in lines:
        a = ANSWER_RE.match(line)
        if a:
            # ans_text = a.group(2).replace("✓", "").replace("(Đúng)", "").strip()
            raw_text = a.group(2).replace("✓", "").replace("(Đúng)", "")
            ans_text = clean_markdown(raw_text)

            is_correct = bool(CORRECT_RE.search(line))
            answers.append((ans_text, is_correct))
        else:
            # gặp dòng mới KHÔNG phải đáp án
            if answers:
                flush()
                answers = []
            question = line

    flush()
    return "\n".join(quizzes)

if __name__ == "__main__":
    with open(INPUT_FILE, encoding="utf-8") as f:
        raw = f.read()

    output = convert(raw)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"Generated quiz.md ({output.count('<quiz>')} questions)")
