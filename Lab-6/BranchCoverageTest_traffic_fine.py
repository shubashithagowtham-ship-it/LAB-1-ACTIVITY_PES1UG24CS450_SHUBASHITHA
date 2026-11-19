import pytest
from traffic_fine import speeding_fine, license_action, total_penalty

# ==============================================================================
# Branch Coverage Tests for traffic_fine
# Designed to test all decision branches (True & False) and boundary conditions.
# Target: 100% Branch Coverage and 100% Statement Coverage.
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Tests for speeding_fine(speed, limit, zone)
# Decision 1: if speed <= limit (True / False)
# Decision 2: if zone == "school" elif zone == "highway" else (3 branches)
# Decision 3: if excess > 40 elif excess > 20 else (3 branches)
# Boundaries tested: speed == limit, speed < limit, excess = 41, 40, 21, 20, 1
# ------------------------------------------------------------------------------

def test_speeding_fine_at_exact_limit():
    # Boundary: speed == limit (Decision 1: True)
    assert speeding_fine(60, 60, "city") == 0


def test_speeding_fine_below_limit():
    # speed < limit (Decision 1: True)
    assert speeding_fine(45, 60, "highway") == 0


def test_speeding_fine_school_zone_excess_over_40():
    # zone == "school", excess = 45 > 40 -> 2000 * 3 = 6000
    assert speeding_fine(85, 40, "school") == 6000


def test_speeding_fine_school_zone_excess_boundary_40():
    # zone == "school", excess = 40 (not > 40, but > 20) -> 2000 * 2 = 4000
    assert speeding_fine(80, 40, "school") == 4000


def test_speeding_fine_school_zone_excess_over_20():
    # zone == "school", excess = 25 > 20 -> 2000 * 2 = 4000
    assert speeding_fine(65, 40, "school") == 4000


def test_speeding_fine_school_zone_excess_boundary_20():
    # zone == "school", excess = 20 (not > 20) -> base = 2000
    assert speeding_fine(60, 40, "school") == 2000


def test_speeding_fine_school_zone_excess_under_20():
    # zone == "school", excess = 10 <= 20 -> base = 2000
    assert speeding_fine(50, 40, "school") == 2000


def test_speeding_fine_highway_zone_excess_over_40():
    # zone == "highway", excess = 50 > 40 -> 1000 * 3 = 3000
    assert speeding_fine(110, 60, "highway") == 3000


def test_speeding_fine_highway_zone_excess_over_20():
    # zone == "highway", excess = 25 > 20 -> 1000 * 2 = 2000
    assert speeding_fine(85, 60, "highway") == 2000


def test_speeding_fine_highway_zone_excess_under_20():
    # zone == "highway", excess = 15 <= 20 -> base = 1000
    assert speeding_fine(75, 60, "highway") == 1000


def test_speeding_fine_default_zone_excess_over_40():
    # other zone (e.g., "residential"), excess = 42 > 40 -> 500 * 3 = 1500
    assert speeding_fine(92, 50, "residential") == 1500


def test_speeding_fine_default_zone_excess_over_20():
    # other zone, excess = 21 > 20 -> 500 * 2 = 1000
    assert speeding_fine(71, 50, "rural") == 1000


def test_speeding_fine_default_zone_excess_under_20():
    # other zone, excess = 5 <= 20 -> base = 500
    assert speeding_fine(55, 50, "residential") == 500


# ------------------------------------------------------------------------------
# 2. Tests for license_action(points, is_commercial, repeat_offender)
# Decision 1: points >= 12 (True / False)
#   Sub-decision: is_commercial (True: revoke / False: suspend)
# Decision 2: points >= 8 (True / False)
#   Sub-decision: repeat_offender (True: suspend / False: warning)
# Decision 3: points >= 4 (True: notice / False: none)
# Boundaries tested: 12, 11, 8, 7, 4, 3, 0
# ------------------------------------------------------------------------------

def test_license_commercial_driver_12_points():
    # Boundary: points == 12, commercial -> revoke
    assert license_action(12, True, False) == "revoke"


def test_license_commercial_driver_high_points():
    # points > 12, commercial -> revoke
    assert license_action(20, True, True) == "revoke"


def test_license_non_commercial_12_points():
    # Boundary: points == 12, non-commercial -> suspend
    assert license_action(12, False, False) == "suspend"


def test_license_non_commercial_high_points():
    # points > 12, non-commercial -> suspend
    assert license_action(15, False, True) == "suspend"


def test_license_repeat_offender_8_points():
    # Boundary: points == 8, repeat offender -> suspend
    assert license_action(8, False, True) == "suspend"


def test_license_repeat_offender_11_points():
    # Upper boundary under 12: points == 11, repeat offender -> suspend
    assert license_action(11, False, True) == "suspend"


def test_license_standard_offender_8_points():
    # Boundary: points == 8, non-repeat offender -> warning
    assert license_action(8, False, False) == "warning"


def test_license_standard_offender_11_points():
    # Upper boundary under 12: points == 11, non-repeat offender -> warning
    assert license_action(11, False, False) == "warning"


def test_license_notice_4_points():
    # Boundary: points == 4 -> notice
    assert license_action(4, False, False) == "notice"


def test_license_notice_7_points():
    # Upper boundary under 8: points == 7 -> notice
    assert license_action(7, True, True) == "notice"


def test_license_clean_record_3_points():
    # Upper boundary under 4: points == 3 -> none
    assert license_action(3, False, False) == "none"


def test_license_clean_record_zero_points():
    # Boundary: points == 0 -> none
    assert license_action(0, False, False) == "none"


# ------------------------------------------------------------------------------
# 3. Tests for total_penalty(fines)
# Decision 1: for fine in fines (0 iterations / 1+ iterations)
# Decision 2: if fine < 0 (True: raise ValueError / False: add)
# Decision 3: if total > 10000 (True: cap at 10000 / False: keep total)
# Boundaries tested: fines=[], fine < 0, total < 10000, total == 10000, total > 10000
# ------------------------------------------------------------------------------

def test_total_penalty_empty_list():
    # Decision: loop does not execute (0 iterations)
    assert total_penalty([]) == 0


def test_total_penalty_single_fine():
    # Normal iteration under cap
    assert total_penalty([500]) == 500


def test_total_penalty_under_cap():
    # Decision: total <= 10000 (False branch of if total > 10000)
    assert total_penalty([1500, 2500, 1000]) == 5000


def test_total_penalty_exact_cap():
    # Boundary: total == 10000
    assert total_penalty([5000, 5000]) == 10000


def test_total_penalty_exceeding_cap():
    # Decision: total > 10000 (True branch of if total > 10000)
    assert total_penalty([6000, 5000]) == 10000


def test_total_penalty_negative_fine_first_item():
    # Decision: fine < 0 (True branch)
    with pytest.raises(ValueError, match="negative fine"):
        total_penalty([-100])


def test_total_penalty_negative_fine_subsequent_item():
    # Decision: fine < 0 after valid fine
    with pytest.raises(ValueError, match="negative fine"):
        total_penalty([500, 1000, -200])
