import pytest
from traffic_fine import speeding_fine, license_action, total_penalty

# ==============================================================================
# Code Coverage (Statement Coverage) Tests for traffic_fine
# Designed to execute all lines and statements (Target: 100% Statement Coverage)
# ==============================================================================

def test_speeding_fine_no_speeding():
    # Covers: speed <= limit -> return 0
    assert speeding_fine(50, 60, "city") == 0


def test_speeding_fine_school_high_excess():
    # Covers: excess = speed - limit, zone == "school", base = 2000, excess > 40 -> return base * 3
    assert speeding_fine(100, 50, "school") == 6000


def test_speeding_fine_highway_medium_excess():
    # Covers: zone == "highway", base = 1000, excess > 20 -> return base * 2
    assert speeding_fine(75, 50, "highway") == 2000


def test_speeding_fine_other_zone_low_excess():
    # Covers: else (default base = 500), return base
    assert speeding_fine(65, 50, "residential") == 500


def test_license_commercial_12_or_more_points():
    # Covers: points >= 12, is_commercial True -> return "revoke"
    assert license_action(14, True, False) == "revoke"


def test_license_non_commercial_12_or_more_points():
    # Covers: points >= 12, is_commercial False -> return "suspend"
    assert license_action(12, False, False) == "suspend"


def test_license_repeat_offender_8_to_11_points():
    # Covers: points >= 8, repeat_offender True -> return "suspend"
    assert license_action(10, False, True) == "suspend"


def test_license_standard_8_to_11_points():
    # Covers: points >= 8, repeat_offender False -> return "warning"
    assert license_action(8, False, False) == "warning"


def test_license_notice_4_to_7_points():
    # Covers: points >= 4 -> return "notice"
    assert license_action(5, False, False) == "notice"


def test_license_clean_record_under_4_points():
    # Covers: return "none"
    assert license_action(2, False, False) == "none"


def test_total_penalty_valid_capped():
    # Covers: total = 0, loop iteration, total += fine, total > 10000 -> total = 10000
    assert total_penalty([4000, 7000]) == 10000


def test_total_penalty_negative_fine_raises():
    # Covers: if fine < 0: raise ValueError("negative fine")
    with pytest.raises(ValueError, match="negative fine"):
        total_penalty([500, -100])
