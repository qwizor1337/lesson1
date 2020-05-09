answers = {
	"привет": "И тебе привет!",
	"как дела": "Лучше всех",
	"пока": "Увидимся"
}

question = input()
def get_answer(question,answers):
	return str(answers[question])

x = answers.get(question).lower()
print(x)
