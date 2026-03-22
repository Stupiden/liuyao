import random
import inflect

# Store the Final Result
GUA = {}

# Refers to the upper and lower order of each "Yao"
YAOWEI = {
    1: '初爻',
    2: '二爻',
    3: '三爻',
    4: '四爻',
    5: '五爻',
    6: '上爻',
}


class CoinFlip:
    def __init__(self):
        """Initializes the CoinFlip with placeholders for result and transformation (bian)."""
        self.result = None
        self.bian = None

    def rolling_three_coins(self):
        """Simulates rolling three coins, returning a list of 'Bei' (Head) or 'Zi' (Tail)."""
        return [random.choice(["Bei", "Zi"]) for _ in range(3)]

    def sixiang(self):
        """Determines the 'sixiang(四象)' based on the result of rolling three coins."""
        coins = self.rolling_three_coins()
        yinyang_count = coins.count("Bei")

        match yinyang_count:
            case 0:
                self.result = "▅▅  ▅▅ ✖"
                self.bian = "▅▅▅▅▅▅"
            case 1:
                self.result = "▅▅▅▅▅▅"
                self.bian = "  ▅▅▅▅▅▅"
            case 2:
                self.result = "▅▅  ▅▅"
                self.bian = "  ▅▅  ▅▅"
            case 3:
                self.result = "▅▅▅▅▅▅ ◯"
                self.bian = "▅▅  ▅▅"


def rolling():
    """Performs the coin rolling process six times and prints the resulting hexagrams."""
    yao = CoinFlip()
    p = inflect.engine()

    for i in range(1, 7):
        input(
            f"Coin is rolling... Keep thinking... Press Enter to stop the {p.ordinal(i)} rolling!")
        yao.sixiang()

        order = YAOWEI[i]
        result = yao.result
        bian = yao.bian
        combo = f"{order} {result}"

        gua_result(i, combo, bian)
        print(combo)

    gua_print(GUA)
    print(f"      本卦     →     变卦")


def gua_result(n, yuan, bian):
    """Records the final result of each roll in the GUA dictionary."""
    GUA[n] = f"{yuan}       {bian}"


def gua_print(dic):
    """Prints the final hexagram in reverse order."""
    print("Done! Your final 'Gua' is:")
    for value in reversed(list(dic.values())):
        print(value)


def main():
    """Main entry point of the program, triggering the rolling process."""
    input("Focus on what you want to divine... Press Enter to continue.")
    rolling()


if __name__ == "__main__":
    main()
