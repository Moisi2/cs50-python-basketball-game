import pytest
from project import simulate_possession, calculate_score, display_score, overtime

# --- Tests for calculate_score ---
def test_calculate_score(monkeypatch):
    # Test Case 1: Successful 2-point shot
    mock_values = iter([0.3, 0.6])
    monkeypatch.setattr('project.random.random', lambda: next(mock_values))
    assert calculate_score(0.4) == 2

    # Test Case 2: Successful 3-point shot
    mock_values = iter([0.3, 0.8])
    monkeypatch.setattr('project.random.random', lambda: next(mock_values))
    assert calculate_score(0.4) == 3

    # Test Case 3: Missed shot
    monkeypatch.setattr('project.random.random', lambda: 0.5)
    assert calculate_score(0.4) == 0


# --- Tests for simulate_possession ---
def test_simulate_possession(monkeypatch):
    # Test Case 1: No shot is attempted
    monkeypatch.setattr('project.random.random', lambda: 0.7)
    assert simulate_possession("Team A", "Team B") == 0

    # Test Case 2: A shot is attempted and it's a 2-pointer
    mock_values = iter([0.5, 0.3, 0.6]) # Shot taken, shot made, 2-pointer
    monkeypatch.setattr('project.random.random', lambda: next(mock_values))
    assert simulate_possession("Team A", "Team B") == 2


# --- Test for display_score ---
def test_display_score(capsys):
    display_score("Lakers", 10, "Celtics", 8)
    captured = capsys.readouterr()
    assert captured.out == "Score: Lakers - 10, Celtics - 8\n"


# --- Test for overtime ---
def test_overtime(monkeypatch):
    # Starting tied score
    initial_scores = (10, 10)

    # Control possessions: Team 1 (True), Team 1 (True), Team 2 (False)
    mock_choices = iter([True, True, False])
    monkeypatch.setattr('project.random.choice', lambda _: next(mock_choices))

    # Mock simulate_possession to always return 2 points
    monkeypatch.setattr('project.simulate_possession', lambda offense, defense: 2)

    # Mock display functions to prevent printing during test
    monkeypatch.setattr('project.display_score', lambda *args: None)
    monkeypatch.setattr('project.display_winner_ascii', lambda *args: None)

    # Expected outcome:
    # Team A: 10 + 2 + 2 = 14
    # Team B: 10 + 2 = 102
    expected_final_score = (14, 12)

    # Run the function and check its return value
    final_score = overtime("Team A", "Team B", initial_scores[0], initial_scores[1])
    assert final_score == expected_final_score
