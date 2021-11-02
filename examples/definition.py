import pandas


class Definition:
    def __init__(self, term):
        self.t = term

    def get(self):
        df = pandas.read_csv("data.csv")
        result = tuple(df.loc[df["word"] == self.t]["definition"])
        return result


if __name__ == "__main__":
    d = Definition(term=input("Your word or words:   "))
    print(d.get())
