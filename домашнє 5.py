class MovaProgramuvannya:
    def __init__(self, ім_я):
        self.ім_я = ім_я

    def вивести_привітання(self):
        print(f"Привіт! Я мова програмування {self.ім_я}.")


class Python(MovaProgramuvannya):
    def __init__(self, ім_я="Python", призначення="Data Science, Web, AI"):
        super().__init__(ім_я)
        self.призначення = призначення

    def вивести_привітання(self):
        super().вивести_привітання()
        print(f"Особливість: синтаксис простий та зрозумілий. Сфера: {self.призначення}.\n")


class JavaScript(MovaProgramuvannya):
    def __init__(self, ім_я="JavaScript", тип_виконання="в браузері та Node.js"):
        super().__init__(ім_я)
        self.тип_виконання = тип_виконання

    def вивести_привітання(self):
        super().вивести_привітання()
        print(f"Особливість: використовується для розробки вебсайтів ({self.тип_виконання}).\n")


if __name__ == "__main__":
    mova_py = Python()
    mova_js = JavaScript()

    mova_py.вивести_привітання()
    mova_js.вивести_привітання()