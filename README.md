# ВВПД Практическая №5. Документация программиста
## Find Palindrome

Все мы сталкивались с проблемой нахождения [палиндрома](https://ru.wikipedia.org/wiki/Палиндром) числа путем суммирования этого числа с самим собой, но в развернутом виде. Годами люди трудились, бились головами, просили Бога, заключали сделки с демонами, проводили годы, медитируя, но ни один из них даже не приблизился к тому, чтобы узнать как написать программу, которая будет искать палиндромы. Со временем люди утратили веру в то, что это возможно, но случилось событие масштабы которого сопоставимы со [вторым пришествием Иисуса](https://en.wikipedia.org/wiki/Second_Coming) - в интернете появился код, который полностью отвечает необходимым требованиям. Были смельчаки, которые не верили этому, отрицали, пытались доказать, что это невозможно, говорили: "*Погодите, это реально?*". Отвечаю всем им: "*:sunglasses:Да, это реально*" и подкрепляю свои слова этим проектом. При помощи этого кода, написанного на языке программирования **PYTHON** вы можете:

* Проводить время с пользой, изучая палиндромы чисел.
* Решать задачи на нахождение палиндрома
* Читать документацию к этому коду

Ниже можно увидеть план разработчика, можно заметить, что выполнены почти все пункты, что вызывает уважение к программисту, ведь старание всегда вызывает уважение.
- [x] Написать код
- [x] Написать документацию
- [x] Написать README файл
- [x] Анжумания
- [x] Посмотреть 10 серию Человека-Бензопилы
- [ ] Купить комбо-усилитель для новой бас гитары
- [ ] Сдать экзамен по ВВПД (ну или хотя бы все практические)
 
 Я понимаю, что каждому читателю уже нетерпится посмотретья на это гениальное творение, поэтому необходимо перестать чесать языком и начать демонстрировать код.
 
 ## Демонстрация кода
Ниже внимательный читатель может увидеть сердце программы - алгоритм нахождения палиндрома числа.
```python
for n in range(iteration_count + 1):
    if str(palindrome) == str(palindrome)[::-1]:
        print(f"Палиндром - {palindrome}. Число итераций: {n}")
        return True
    palindrome = str(int(palindrome) + int(str(palindrome)[::-1]))
else:
    print("Палиндром не найден")
    return False
```
## Перерыв на приколы
Ниже я прикрепил фотоприкол, чтобы немного отдохнуть от интеллектуальной деятельности.
![image](https://user-images.githubusercontent.com/120565896/207591544-13e88201-84eb-4314-8441-f8f1953d0461.png)

После минуты смеха предлагаю решить легкую математическую задачу, чтобы снова вернуться к интеллектуальной деятельности.
```math
\int_{}^{}\sqrt{x^{5x-4}} *\frac{^{145^{x}}}{\sqrt{4}} dx
```
Если решение этого интеграла занимает больше 15 секунд, то, *возможно*, у вас есть проблемы с математикой и поэтому вам стоит закрыть данный проект и заняться математическим анализом.

~Тут мне уже надоело ну и затянулось как-то немного по ощущениям~

## Долгожданный финал

На этом моменте ознакомительная часть заканчивается, спасибо за внимание!
