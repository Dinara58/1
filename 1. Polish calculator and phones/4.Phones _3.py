try:
    phone_num = input().replace(" ", "").replace("\t", "")
    if "(" in phone_num and ")" in phone_num:
        st_index = phone_num.index("(")
        en_index = phone_num.index(")")
        phone_num = phone_num[:st_index] + phone_num[st_index + 1:en_index] + phone_num[en_index + 1:]
    if "--" not in phone_num and "-" in phone_num:
        phone_num = phone_num[0] + phone_num[1:-1].replace("-", "") + phone_num[-1]
    if phone_num.startswith("+7"):
        phone_num = "+7" + phone_num[2:]
    elif phone_num.startswith("8"):
        phone_num = "+7" + phone_num[1:]
    else:
        raise TypeError()
    if not phone_num[1:].isdigit():
        raise TypeError()
    if len(phone_num[1:]) != 11:
        raise ValueError()
    print(phone_num)
except ValueError:
    print("Неверное количество цифр")
except TypeError:
    print("Неверный формат")
