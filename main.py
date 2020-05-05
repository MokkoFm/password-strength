import urwid

def is_very_long(password):
    return len(password) >=12

def has_digit(password):
    return any(letter.isdigit() for letter in password)

def has_letters(password):
    return any(not letter.isdigit() for letter in password)

def has_upper_letters(password):
    return any(letter.isupper() for letter in password)

def has_lower_letters(password):
    return any(has_upper_letters(password) and letter.islower() for letter in password)

def has_symbols(password):
    return any(not letter.isdigit() and not letter.isalpha() for letter in password)

def doesnt_consist_of_symbols(password):
    return any(has_symbols(password) and letter.isdigit() or letter.isalpha() for letter in password)

def on_ask_change(edit, new_edit_text):
    score = 0
    conditions = [is_very_long(password), has_digit(password), has_letters(password), has_upper_letters(password), has_lower_letters(password), has_symbols(password), doesnt_consist_of_symbols(password)]
    
    for condition in conditions:
      if condition is True:
        score +=2

    reply.set_text("Рейтинг этого пароля: %s" % score)

if __name__ == '__main__':
    password = input('Введите пароль:')
    ask = urwid.Edit('Введите пароль: ', mask='*')
    reply = urwid.Text("")
    menu = urwid.Pile([ask, reply])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(ask, 'change', on_ask_change)
    urwid.MainLoop(menu).run()
    on_ask_change()