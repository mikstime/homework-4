# Тестирование взаимодействий с контактами

*Добавление контакта*
 * Ошибка при добавлении контакта с пустыми полями
 * Ошибка при вводе невалидной почты: подойдет любая почта не содержащая кириллические символы, без знака @, с некорректным указанием домена, содержащая недопустимые символы(например: это_имейл@mail.ru, email@email, email.ru)
 * Ошибка при вводе даты из будущего(например, 31 декабрь 2020 года)
 * Корректноне сохранение контакта при вводе всех полей в валидной форме, перечисление полей:

 * 
 ** Имя
 ** Фамилия
 ** Псевдоним
 ** Компания
 ** Email
 ** Мобильный номер телефона
 ** Примечание
 ** Должность 
 ** Руководитель
 ** Адрес
 ** Пол
 ** Вконтакте + другой
 * Ввод только имени(остальное оставить пустым)
 * Ввод только email(остальное оставить пустым)
 * Ввод только псевдонима(остальное оставить пустым)
 * Ввод всех полей(перечислены выше), с полем “другое”, оставленным пустым
 * Создание двух идентичных контактов(например, с идентичными именами и идентичными email'ами)
 * Создание контакта с кириллическим именем 
 * Создание контакта с латинскими символами
 * Создание контакта с нетипичным unicode символами в фамилии, например: ђћ∆

 

*Изменение контакта*
 * Изменить email на валидный
 * Ошибка при смене на email с кириллицей
 * Ошибка при смене на email без точки
 * Изменение всех полей на пустые
 * Изменение имени и фамилии для совпадения с уже существующим контактом
 * Изменение данных на корректные
 * Изменение телефона на пустой
 * Изменение имени контакта с кириллических символов на латинские
 * Изменение имени контакта с латинских символов на кириллические
 * Ошибка при смены даты из будущего(например, 31 декабрь 2020 года)

*Удалить контакт*
 * Удаление контакта со страницы просмотра контакта
 * Удаление контакта путем выделения(нажатия на фотографию) из списка контактов
 * Удаление всех контактов
 * Удаление контакта после выделения и перехода на другую страницу

 

*Избранное*
 * Добавление в избранное со страницы просмотра контакта
 * Добавление в избранное через группы
 * Удаление из избранного
### Выполнил: Болдин Дмитрий