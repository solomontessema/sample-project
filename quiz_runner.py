import ipywidgets as widgets
from IPython.display import display, clear_output

def run_quiz(questions):
    radios = []
    output = widgets.Output()
    submit_button = widgets.Button(description="Submit Quiz", button_style="success")

    # Display all questions with radio buttons
    for q in questions:
        print(q["question"])
        radio = widgets.RadioButtons(options=q["options"], value=None)
        radios.append((q, radio))
        display(radio)

    display(submit_button, output)

    def on_submit(b):
        with output:
            clear_output()
            incorrect = []
            score = 0

            for q, radio in radios:
                selected = radio.value
                correct = q["options"][q["answer"]]
                if selected == correct:
                    score += 1
                else:
                    incorrect.append({
                        "question": q["question"],
                        "selected": selected,
                        "correct": correct
                    })

            print(f"✅ Your score: {score} out of {len(questions)}\n")

            if incorrect:
                print("❌ Review the incorrect answers:\n")
                for item in incorrect:
                    print(f"Question: {item['question']}")
                    print(f"Your answer: {item['selected']}")
                    print(f"Correct answer: {item['correct']}\n")
            else:
                print("🎉 Perfect score! Well done.")

    submit_button.on_click(on_submit)
