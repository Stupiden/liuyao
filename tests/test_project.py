import pytest
from unittest.mock import patch, call
from yixchange.core import CoinFlip, rolling, gua_result, gua_print, GUA, YAOWEI


# ─────────────────────────────────────────────
# Fixtures
# ─────────────────────────────────────────────

@pytest.fixture(autouse=True)
def clear_gua():
    """Clear the shared GUA dict before every test."""
    GUA.clear()
    yield
    GUA.clear()


# ─────────────────────────────────────────────
# CoinFlip.rolling_three_coins
# ─────────────────────────────────────────────

class TestRollingThreeCoins:
    def test_returns_three_items(self):
        cf = CoinFlip()
        coins = cf.rolling_three_coins()
        assert len(coins) == 3

    def test_values_are_bei_or_zi(self):
        cf = CoinFlip()
        for _ in range(20):
            coins = cf.rolling_three_coins()
            assert all(c in ("Bei", "Zi") for c in coins)

    def test_uses_random_choice(self):
        cf = CoinFlip()
        with patch("random.choice", return_value="Bei") as mock_choice:
            coins = cf.rolling_three_coins()
        assert mock_choice.call_count == 3
        assert coins == ["Bei", "Bei", "Bei"]


# ─────────────────────────────────────────────
# CoinFlip.sixiang — all four branches
# ─────────────────────────────────────────────

class TestSixiang:
    """Tests for all four 四象 outcomes."""

    def _run(self, sides):
        """Helper: patch rolling_three_coins and return a CoinFlip after sixiang()."""
        cf = CoinFlip()
        with patch.object(cf, "rolling_three_coins", return_value=sides):
            cf.sixiang()
        return cf

    # 0 Bei → Old Yin (变阳)
    def test_zero_bei_old_yin(self):
        cf = self._run(["Zi", "Zi", "Zi"])
        assert cf.result == "▅▅  ▅▅ ✖"
        assert cf.bian == "▅▅▅▅▅▅"

    # 1 Bei → Young Yang (少阳)
    def test_one_bei_young_yang(self):
        cf = self._run(["Bei", "Zi", "Zi"])
        assert cf.result == "▅▅▅▅▅▅"
        assert cf.bian == "  ▅▅▅▅▅▅"

    # 2 Bei → Young Yin (少阴)
    def test_two_bei_young_yin(self):
        cf = self._run(["Bei", "Bei", "Zi"])
        assert cf.result == "▅▅  ▅▅"
        assert cf.bian == "  ▅▅  ▅▅"

    # 3 Bei → Old Yang (变阴)
    def test_three_bei_old_yang(self):
        cf = self._run(["Bei", "Bei", "Bei"])
        assert cf.result == "▅▅▅▅▅▅ ◯"
        assert cf.bian == "▅▅  ▅▅"

    def test_initial_state_is_none(self):
        cf = CoinFlip()
        assert cf.result is None
        assert cf.bian is None


# ─────────────────────────────────────────────
# gua_result
# ─────────────────────────────────────────────

class TestGuaResult:
    def test_stores_combined_string(self):
        gua_result(1, "初爻 ▅▅▅▅▅▅", "▅▅  ▅▅")
        assert GUA[1] == "初爻 ▅▅▅▅▅▅       ▅▅  ▅▅"

    def test_stores_changing_line(self):
        gua_result(2, "二爻 ▅▅  ▅▅ ✖", "▅▅▅▅▅▅")
        assert GUA[2] == "二爻 ▅▅  ▅▅ ✖       ▅▅▅▅▅▅"

    def test_stores_all_six_positions(self):
        entries = [
            (1, "初爻 ▅▅▅▅▅▅", "▅▅  ▅▅"),
            (2, "二爻 ▅▅  ▅▅", "  ▅▅  ▅▅"),
            (3, "三爻 ▅▅▅▅▅▅ ◯", "▅▅  ▅▅"),
            (4, "四爻 ▅▅▅▅▅▅", "  ▅▅▅▅▅▅"),
            (5, "五爻 ▅▅  ▅▅ ✖", "▅▅▅▅▅▅"),
            (6, "上爻 ▅▅▅▅▅▅", "  ▅▅▅▅▅▅"),
        ]
        for n, yuan, bian in entries:
            gua_result(n, yuan, bian)
        assert len(GUA) == 6

    def test_overwrites_existing_key(self):
        gua_result(1, "初爻 ▅▅▅▅▅▅", "▅▅  ▅▅")
        gua_result(1, "初爻 ▅▅  ▅▅", "  ▅▅  ▅▅")
        assert GUA[1] == "初爻 ▅▅  ▅▅       　  ▅▅  ▅▅".replace("　", "")


# ─────────────────────────────────────────────
# gua_print
# ─────────────────────────────────────────────

class TestGuaPrint:
    def _populate(self):
        gua_result(1, "初爻 ▅▅▅▅▅▅", "▅▅  ▅▅")
        gua_result(2, "二爻 ▅▅  ▅▅ ✖", "▅▅▅▅▅▅")

    def test_prints_header(self, capsys):
        self._populate()
        gua_print(GUA)
        captured = capsys.readouterr()
        assert "Done! Your final 'Gua' is:" in captured.out

    def test_prints_in_reverse_order(self, capsys):
        self._populate()
        gua_print(GUA)
        captured = capsys.readouterr()
        lines = captured.out.strip().splitlines()
        # Line 1 (index 1 in output) should be position-2 entry (reversed)
        assert "二爻" in lines[1]
        assert "初爻" in lines[2]

    def test_both_entries_present(self, capsys):
        self._populate()
        gua_print(GUA)
        captured = capsys.readouterr()
        assert "二爻 ▅▅  ▅▅ ✖       ▅▅▅▅▅▅" in captured.out
        assert "初爻 ▅▅▅▅▅▅       ▅▅  ▅▅" in captured.out

    def test_empty_gua(self, capsys):
        gua_print({})
        captured = capsys.readouterr()
        assert "Done! Your final 'Gua' is:" in captured.out


# ─────────────────────────────────────────────
# YAOWEI constant
# ─────────────────────────────────────────────

class TestYaowei:
    def test_has_six_entries(self):
        assert len(YAOWEI) == 6

    def test_keys_one_to_six(self):
        assert set(YAOWEI.keys()) == {1, 2, 3, 4, 5, 6}

    def test_correct_labels(self):
        assert YAOWEI[1] == '初爻'
        assert YAOWEI[6] == '上爻'


# ─────────────────────────────────────────────
# rolling (integration-level)
# ─────────────────────────────────────────────

class TestRolling:
    def test_rolling_populates_gua_with_six_entries(self, capsys):
        coin_sides = ["Bei", "Zi", "Zi"] * 6  # 1 Bei → Young Yang, repeated 6×

        with patch("builtins.input", return_value=""), \
             patch("random.choice", side_effect=coin_sides * 3):
            rolling()

        assert len(GUA) == 6

    def test_rolling_calls_input_six_times(self, capsys):
        with patch("builtins.input", return_value="") as mock_input, \
             patch("random.choice", return_value="Bei"):
            rolling()

        # 6 rolling prompts (main() adds one more, but rolling() itself: 6)
        assert mock_input.call_count == 6

    def test_rolling_prints_legend(self, capsys):
        with patch("builtins.input", return_value=""), \
             patch("random.choice", return_value="Bei"):
            rolling()

        captured = capsys.readouterr()
        assert "本卦" in captured.out
        assert "变卦" in captured.out
