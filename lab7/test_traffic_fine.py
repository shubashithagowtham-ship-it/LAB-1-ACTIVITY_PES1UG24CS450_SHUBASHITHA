import pytest
from hypothesis import given, strategies as st
from traffic_fine import parse_ticket_id, total_fines, speed_excess

# ==============================================================================
# Property-Based Fuzz Testing for traffic_fine (Lab 7)
# Using Hypothesis to test robustness against unexpected, random, or malformed inputs
# ==============================================================================

@given(st.text() | st.none())
def test_parse_ticket_id_no_crash(s):
    try:
        parse_ticket_id(s)
    except Exception as e:
        assert False, f"parse_ticket_id crashed with: {e}"


@given(st.text() | st.none())
def test_total_fines_no_crash(s):
    try:
        total_fines(s)
    except Exception as e:
        assert False, f"total_fines crashed with: {e}"


@given(st.text() | st.none())
def test_speed_excess_no_crash(s):
    try:
        speed_excess(s)
    except Exception as e:
        assert False, f"speed_excess crashed with: {e}"


# ==============================================================================
# Unit & Regression Tests (Functional Correctness Verification)
# ==============================================================================

def test_parse_ticket_id_valid():
    assert parse_ticket_id("TF-2024-0456") == ("TF", 2024, 456)
    assert parse_ticket_id("ka-2023-100") == ("KA", 2023, 100)


def test_parse_ticket_id_invalid():
    assert parse_ticket_id("") is None
    assert parse_ticket_id(None) is None
    assert parse_ticket_id("INVALID") is None
    assert parse_ticket_id("TF-YEAR-0456") is None
    assert parse_ticket_id("TF-2024") is None


def test_total_fines_valid():
    assert total_fines("500,1200,300") == 2000
    assert total_fines("1000, 2000") == 3000


def test_total_fines_capped():
    assert total_fines("5000,6000") == 10000


def test_total_fines_malformed():
    assert total_fines("") == 0
    assert total_fines(None) == 0
    assert total_fines("500,,1200") == 1700
    assert total_fines("abc,def") == 0


def test_speed_excess_valid():
    assert speed_excess("72/60") == 20
    assert speed_excess("100/50") == 100


def test_speed_excess_within_limit():
    assert speed_excess("50/60") == 0


def test_speed_excess_edge_cases():
    assert speed_excess("70/0") == 0
    assert speed_excess("") == 0
    assert speed_excess(None) == 0
    assert speed_excess("invalid") == 0
