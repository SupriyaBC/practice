import pytest

from model_evaluator import(
    is_eligible,
    evaluate_model,
    evaluate_models,
    select_release_candidate

)

def test_valid_model():
    model = {
        "name": "Model_A",
        "accuracy": 0.92,
        "latency": 120
    }

    assert is_eligible(model)==[]

def test_invalid_accuracy():
    model = {
        "name": "Model_B",
        "accuracy": 1.20,
        "latency": 100
    }

    errors = is_eligible(model)

    assert "accuracy must be greater than 0 and at most 1" in errors

def test_empty_model_name():
    model = {
        "name": "",
        "accuracy": 1.20,
        "latency": 100
    }
    errors = is_eligible(model)
    assert "name should not be empty" in errors


def test_negative_latency():
    model = {
        "name": "Model_C",
        "accuracy": 0.95,
        "latency": -5
    }

    errors = is_eligible(model)

    assert "latency must be between 0 and 200" in errors

def test_evaluate_model():
    model = {
        "name": "Model_A",
        "accuracy": 0.92,
        "latency": 120
    }

    result = evaluate_model(model)

    assert result["name"] == "Model_A"
    assert result["passed"] is True
    assert result["errors"] == []


def test_evaluate_models():
    models = [
        {"name": "Model_A", "accuracy": 0.92, "latency": 120},
        {"name": "Model_B", "accuracy": 1.20, "latency": 100},
        {"name": "Model_D", "accuracy": 0.98, "latency": 150}
    ]

    results = evaluate_models(models)

    assert len(results) == 3
    assert results[0]["passed"] is True
    assert results[1]["passed"] is False
    assert results[2]["passed"] is True


def test_select_release_candidate():
    models = [
        {"name": "Model_A", "accuracy": 0.92, "latency": 120},
        {"name": "Model_B", "accuracy": 1.20, "latency": 100},
        {"name": "", "accuracy": 0.85, "latency": -5},
        {"name": "Model_D", "accuracy": 0.98, "latency": 150}
    ]

    candidate = select_release_candidate(models)

    assert candidate is not None
    assert candidate["name"] == "Model_D"
    assert candidate["accuracy"] == 0.98

def test_no_eligible_release_candidate():
    models = [
        {"name": "Model_A", "accuracy": 1.20, "latency": 120},
        {"name": "Model_B", "accuracy": 0.80, "latency": 100}
    ]

    candidate = select_release_candidate(models)

    assert candidate is None