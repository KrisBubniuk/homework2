adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

#Task 1

text = adwentures_of_tom_sawer.replace("\n"," ")
print(f"Замінюємо на пробіл: {text}" )

#Task 2

text = text.replace("....", " ")
print(f"Замінюємо ...: {text}")

#Task 3

text = " ".join(text.split())
print(f"тільки один пробіл: {text}")

#Task 4

letters_h = text.count("h")
print("Кількість 'h':", letters_h)

#Task 5

words = text.split()
capitalized_count = sum(1 for word in words if word[0].isupper())
print("Слів з великої букви:", capitalized_count)

#Task 6

first_value = text.find("Tom")
second_value = text.find("Tom", first_value + 1)
print("Позиція другого Tom:", second_value)

#Task 7

adwentures_of_tom_sawer_sentences = [s.strip() for s in text.split(".") if s.strip()]
print(adwentures_of_tom_sawer_sentences)

#Task 8

if len(adwentures_of_tom_sawer_sentences) >= 4:
    print("Четверте речення (lowercase):", adwentures_of_tom_sawer_sentences[3].lower())

#Task 9

starts_by_time = any(s.startswith("By the time") for s in adwentures_of_tom_sawer_sentences)
print("Реченнящо починається з 'By the time'?:", starts_by_time)

#Task 10

last_sentence_words = len(adwentures_of_tom_sawer_sentences[-1].split())
print("Слів в останньому реченні:", last_sentence_words)



