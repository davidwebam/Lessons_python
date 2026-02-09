import random
import smtplib
from email.message import EmailMessage


class BankUser:
    def __init__(self, name, surname, age, email, card_number, balance, pin):
        self.__blocked = False
        self.__pin_tries = 0
        self.__restore_code = None

        if not self.__is_valid_name(name):
            raise ValueError("Ajuny petq e lini menak tarer")

        if not self.__is_valid_name(surname):
            raise ValueError("Azganuny petq e parunaki miayn tarer")

        if not isinstance(age, int) or age <= 0:
            raise ValueError("Tariqy petq e lini irakan")

        if not self.__is_valid_email(email):
            raise ValueError("Sxal email")

        if not self.__is_valid_card(card_number):
            raise ValueError("Sxal qarti hamar")

        if balance < 0:
            raise ValueError("Gumary cheptq e lini bacasakan")

        if not (isinstance(pin, str) and pin.isdigit() and len(pin) == 4):
            raise ValueError("PIN kody petq e lini 4 tvanshanic backacats")

        self._name = name
        self._surname = surname
        self._age = age
        self._email = email

        self.__card_number = card_number.replace(" ", "")
        self.__balance = balance
        self.__pin = pin

    def __is_valid_name(self, value):
        return isinstance(value, str) and value.isalpha()

    def __is_valid_email(self, email):
        if not isinstance(email, str):
            return False
        if "@" not in email or "." not in email:
            return False
        if email.startswith("@") or email.endswith("@"):
            return False
        if email.count("@") != 1:
            return False
        return True

    def __is_valid_card(self, card):
        card = card.replace(" ", "")
        return card.isdigit() and len(card) == 16 and self.__luhn(card)

    def __luhn(self, card):
        digits = [int(x) for x in card]
        for i in range(len(digits) - 2, -1, -2):
            digits[i] *= 2
            if digits[i] > 9:
                digits[i] -= 9
        return sum(digits) % 10 == 0

    def __check_pin(self, pin):
        if self.__blocked:
            raise PermissionError("Ogtatery argelapakvats e")

        if pin == self.__pin:
            self.__pin_tries = 0
            return True

        self.__pin_tries += 1
        if self.__pin_tries >= 3:
            self.__blocked = True
            raise PermissionError("Hashivy argelapakvec")

        raise ValueError("Sxal PIN kod")

    def get_full_name(self):
        return f"{self._name} {self._surname}"

    def get_card_info(self, pin):
        self.__check_pin(pin)
        return self.__card_number, self.__balance

    def add_money(self, amount, pin):
        self.__check_pin(pin)
        if amount <= 0:
            raise ValueError("Gumary chpetq e lini bacasakan tiv")
        self.__balance += amount

    def withdraw_money(self, amount, pin):
        self.__check_pin(pin)
        if amount <= 0:
            raise ValueError("Gunary chpetq e lini bacasakan tiv")
        if amount > self.__balance:
            raise ValueError("Chka bavarar qanaki gumar")
        self.__balance -= amount

    def send_restore_code(self, smtp_email, smtp_password):
        self.__restore_code = str(random.randint(100000, 999999))

        msg = EmailMessage()
        msg.set_content(f"Dzer verakangman kodne {self.__restore_code}")
        msg["Subject"] = "PIN KODDDDD"
        msg["From"] = smtp_email
        msg["To"] = self._email

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(smtp_email, smtp_password)
            server.send_message(msg)

    def restore_access(self, code):
        if code == self.__restore_code:
            self.__blocked = False
            self.__pin_tries = 0
            self.__restore_code = None
            return "mutqy verajangvats e"
        raise ValueError("Sxal verakangman kod")


user = BankUser(
    "David", "Voskanyan", 25,
    "voskanyandavit83@gmail.com",
    "4539 1488 0343 6467",
    1000,
    "1234"
)

print(user.get_full_name())
print(user.get_card_info("1234"))
user.add_money(500, "1234")
user.withdraw_money(300, "1234")
