name = "Anton"
age = 15
Hobbies = ["гитара", "ролики", "поспать"]

person = {
    "name": "Anton",
    "age": 15,
    "hobbies": ["гитара", "ролики", "поспать"],

}

print(person["hobbies"][1])

questions = {
    1: {
        "text": "Текст вопроса 1",
        "variants": ["ответ 1", "ответ 2", "ответ 3", "ответ 4"]
    },
    2: {
        "text": "Текст вопроса 2",
        "variants": ["ответ 1", "ответ 2", "ответ 3", "ответ 4"]
    }
}

print(questions[1]["text"])