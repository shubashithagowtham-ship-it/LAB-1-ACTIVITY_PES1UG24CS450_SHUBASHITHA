import pytest
from traffic_fine import speeding_fine, license_action, total_penalty

# ==============================================================================
# Comprehensive Test Suite for traffic_fine (Lab 6)
# Student: Shubashitha Gowtham (PES1UG24CS450)
# Covers 100% Line Coverage and 100% Branch Coverage
# ==============================================================================

# --- Speeding Fine Tests ---

def test_no_speeding():
    # Boundary: speed == limit
    assert speeding_fine(60, 60, "city") == 0


def test_speed_below_limit():
    # speed < limit
    assert speeding_fine(50, 60, "highway") == 0


def test_speeding_school_high_excess():
    # zone == "school", excess > 40
    assert speeding_fine(100, 50, "school") == 6000


def test_speeding_school_boundary_40():
    # zone == "school", excess == 40 (not > 40, but > 20)
    assert speeding_fine(90, 50, "school") == 4000


def test_speeding_school_medium_excess():
    # zone == "school", excess > 20
    assert speeding_fine(75, 50, "school") == 4000


def test_speeding_school_boundary_20():
    # zone == "school", excess == 20 (not > 20)
    assert speeding_fine(70, 50, "school") == 2000


def test_speeding_school_low_excess():
    # zone == "school", excess <= 20
    assert speeding_fine(60, 50, "school") == 2000


def test_speeding_highway_high_excess():
    # zone == "highway", excess > 40
    assert speeding_fine(110, 60, "highway") == 3000


def test_speeding_highway_medium_excess():
    # zone == "highway", excess > 20
    assert speeding_fine(85, 60, "highway") == 2000


def test_speeding_highway_low_excess():
    # zone == "highway", excess <= 20
    assert speeding_fine(75, 60, "highway") == 1000


def test_speeding_default_zone_high_excess():
    # default zone, excess > 40
    assert speeding_fine(95, 50, "residential") == 1500


def test_speeding_default_zone_medium_excess():
    # default zone, excess > 20
    assert speeding_fine(75, 50, "rural") == 1000


def test_speeding_default_zone_low_excess():
    # default zone, excess <= 20
    assert speeding_fine(65, 50, "residential") == 500


# --- License Action Tests ---

def test_license_commercial_12_points():
    # Boundary: points == 12, commercial -> revoke
    assert license_action(12, True, False) == "revoke"


def test_license_commercial_high_points():
    # points > 12, commercial -> revoke
    assert license_action(18, True, True) == "revoke"


def test_license_noncommercial_12_points():
    # Boundary: points == 12, non-commercial -> suspend
    assert license_action(12, False, False) == "suspend"


def test_license_noncommercial_high_points():
    # points > 12, non-commercial -> suspend
    assert license_action(15, False, False) == "suspend"


def test_license_repeat_offender_8_points():
    # Boundary: points == 8, repeat offender -> suspend
    assert license_action(8, False, True) == "suspend"


def test_license_repeat_offender_11_points():
    # points == 11, repeat offender -> suspend
    assert license_action(11, False, True) == "suspend"


def test_license_standard_8_points():
    # Boundary: points == 8, non-repeat offender -> warning
    assert license_action(8, False, False) == "warning"


def test_license_standard_11_points():
    # points == 11, non-repeat offender -> warning
    assert license_action(11, False, False) == "warning"


def test_license_notice_4_points():
    # Boundary: points == 4 -> notice
    assert license_action(4, False, False) == "notice"


def test_license_notice_7_points():
    # points == 7 -> notice
    assert license_action(7, True, True) == "notice"


def test_license_clean_record_3_points():
    # points == 3 -> none
    assert license_action(3, False, False) == "none"


def test_license_clean_record_zero_points():
    # points == 0 -> none
    assert license_action(0, False, False) == "none"


# --- Total Penalty Tests ---

def test_total_penalty_empty():
    # Empty fines list
    assert total_penalty([]) == 0


def test_total_penalty_single():
    # Single fine
    assert total_penalty([500]) == 500


def test_total_penalty_under_cap():
    # Total <= 10000
    assert total_penalty([1000, 2500, 1500]) == 5000


def test_total_penalty_exact_cap():
    # Total == 10000
    assert total_penalty([4000, 6000]) == 10000


def test_total_penalty_over_cap():
    # Total > 10000
    assert total_penalty([6000, 7000]) == 10000


def test_total_penalty_negative_raises():
    # Negative fine raises ValueError
    with pytest.raises(ValueError, match="negative fine"):
        total_penalty([500, -50, 1000])
