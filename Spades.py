import unittest
def check_straight(card1, card2, card3):
    card_values = {'S2': 2, 'S3': 3, 'S4': 4, 'S5': 5, 'S6': 6, 'S7': 7,
                   'S8': 8, 'S9': 9, 'S10': 10, 'SJ': 11, 'SQ': 12, 'SK': 13, 'SA': 14}
    values = [card_values[card1], card_values[card2], card_values[card3]]
    values.sort()
    if values[1] == values[0] + 1 and values[2] == values[1] + 1:
        return max(values)
    else:
        return 0


def check_3ofa_kind(card1, card2, card3):
    card_values = {'S2': 2, 'S3': 3, 'S4': 4, 'S5': 5, 'S6': 6, 'S7': 7,
                   'S8': 8, 'S9': 9, 'S10': 10, 'SJ': 11, 'SQ': 12, 'SK': 13, 'SA': 14}
    values = [card_values[card1], card_values[card2], card_values[card3]]
    if values[0] == values[1] == values[2]:
        return values[0]
    else:
        return 0


def check_royal_flush(card1, card2, card3):
    if check_straight(card1, card2, card3) == 14:
        return 14
    else:
        return 0


def play_cards(left1, left2, left3, right1, right2, right3):
    left_straight = check_straight(left1, left2, left3)
    right_straight = check_straight(right1, right2, right3)
    left_three_of_a_kind = check_3ofa_kind(left1, left2, left3)
    right_three_of_a_kind = check_3ofa_kind(right1, right2, right3)
    left_royal_flush = check_royal_flush(left1, left2, left3)
    right_royal_flush = check_royal_flush(right1, right2, right3)

    if left_royal_flush and not right_royal_flush:
        return -1
    if right_royal_flush and not left_royal_flush:
        return 1
    if left_straight and right_straight:
        if left_straight > right_straight:
            return -1
        elif right_straight > left_straight:
            return 1
        else:
            return 0
    if left_three_of_a_kind and right_three_of_a_kind:
        if left_three_of_a_kind > right_three_of_a_kind:
            return -1
        elif right_three_of_a_kind > left_three_of_a_kind:
            return 1
        else:
            return 0
    if left_straight and right_three_of_a_kind:
        return -1
    if right_straight and left_three_of_a_kind:
        return 1
    return 0


# Unit tests for the functions
class TestPokerFunctions(unittest.TestCase):

    def test_check_straight(self):
        self.assertEqual(check_straight('S5', 'S6', 'S7'), 7)
        self.assertEqual(check_straight('S6', 'S5', 'S7'), 7)
        self.assertEqual(check_straight('S3', 'SQ', 'SK'), 0)
        self.assertEqual(check_straight('S2', 'SK', 'SA'), 0)
        self.assertEqual(check_straight('S4', 'S4', 'S4'), 0)
        self.assertEqual(check_straight('SQ', 'SK', 'SJ'), 13)

    def test_check_3ofa_kind(self):
        self.assertEqual(check_3ofa_kind('S9', 'S9', 'S9'), 9)
        self.assertEqual(check_3ofa_kind('S2', 'S4', 'S2'), 0)
        self.assertEqual(check_3ofa_kind('SK', 'SK', 'SK'), 13)
        self.assertEqual(check_3ofa_kind('S7', 'S8', 'S9'), 0)
        self.assertEqual(check_3ofa_kind('S5', 'S5', 'S6'), 0)

    def test_check_royal_flush(self):
        self.assertEqual(check_royal_flush('S10', 'SJ', 'SA'), 14)
        self.assertEqual(check_royal_flush('S9', 'S10', 'SJ'), 0)
        self.assertEqual(check_royal_flush('SK', 'SK', 'SK'), 0)

    def test_play_cards(self):
        self.assertEqual(play_cards('S5', 'S6', 'S7', 'S2', 'S3', 'S4'), -1)
        self.assertEqual(play_cards('S2', 'S3', 'S4', 'SK', 'SK', 'SK'), 1)
        self.assertEqual(play_cards('SJ', 'SJ', 'SJ', 'SJ', 'SJ', 'SJ'), 0)
        self.assertEqual(play_cards('S10', 'SJ', 'SA', 'S2', 'S3', 'S4'), -1)
        self.assertEqual(play_cards('S2', 'S2', 'S2', 'SK', 'SK', 'SK'), 1)
        self.assertEqual(play_cards('S5', 'S6', 'S7', 'S10', 'SJ', 'SA'), 1)
        self.assertEqual(play_cards('S2', 'S4', 'S6', 'S3', 'S5', 'S7'), 0)
        self.assertEqual(play_cards('S5', 'S6', 'S7', 'S7', 'S5', 'S6'), 0)


# Run the unit tests
if __name__ == '__main__':
    unittest.main()
