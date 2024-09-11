from main import blackjack_score
import pytest

#@pytest.mark.skip(reason="no way of currently testing this")
def test_score_for_pair_of_number_cards():
  # Arrange
  hand = [3, 4]
  expected_result = 7
  # Act
  score = blackjack_score(hand)

  # Assert <-- Write assert statement here
  assert score == expected_result

# @pytest.mark.skip(reason="no way of currently testing this")
def test_facecards_have_values_calculated_correctly():
  hand = ["Queen", "Jack"]
  expected_result = 20

  score = blackjack_score(hand)
  assert score == expected_result

#@pytest.mark.skip(reason="no way of currently testing this")
def test_calculates_aces_as_11_where_it_does_not_go_over_21():
  hand = ['Ace', 6]
  expected_result = 17

  score = blackjack_score(hand)
  assert score == expected_result

#@pytest.mark.skip(reason="no way of currently testing this")
def test_calculates_aces_as_1_where_11_would_bust():
  hand =['Ace', 10, 5]
  expected_result = 16

  score = blackjack_score(hand)
  assert score == expected_result

#@pytest.mark.skip(reason="no way of currently testing this")
def test_returns_invalid_for_invalid_cards():
  hand = [11, 'Ace']
  expected_result = 'Invalid'

  score = blackjack_score(hand)
  assert score == expected_result


# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_invalid_for_list_length_greater_than_5():
  hand = [2, 3, 5, 'Jack', 'Queen', 'Queen']
  expected_result = 'Invalid'

  score = blackjack_score(hand)
  assert score == expected_result

# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_bust_for_scores_over_21():
  hand = [2, 'Jack', 'Queen']
  expected_result = 'Bust'

  score = blackjack_score(hand)
  assert score == expected_result

# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_12_for_ace_ace_king():
  hand = ['Ace', 'Ace', 'King']
  expected_result = 12

  score = blackjack_score(hand)
  assert score == expected_result

# @pytest.mark.skip(reason="logic not yet implemented")
def test_returns_14_for_ace_ace_ace_ace():
  hand = ['Ace', 'Ace', 'Ace', 'Ace']
  expected_result = 14

  score = blackjack_score(hand)
  assert score == expected_result