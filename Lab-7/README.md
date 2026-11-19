# Lab 7: Fuzzing for Input Validation Bugs

**Student Name:** Shubashitha Gowtham  
**SRN:** PES1UG24CS450  
**Section:** 5H  
**Course:** Software Engineering Lab (UE24CS251B)  
**Problem Statement:** Scenario 27 — Traffic Ticket Processing System (`traffic_fine.py`)  

---

## Objective
- Explore fuzz testing as a dynamic security and quality assurance technique.
- Identify input validation flaws, edge cases, and crash bugs using Python's `Hypothesis` library.
- Apply defensive programming to harden Python applications against unexpected or hostile inputs.

---

## Problem Overview

The application `traffic_fine.py` processes traffic ticket data:
1. `parse_ticket_id(ticket_id)`: Parses ticket IDs formatted as `'PREFIX-YEAR-SERIAL'`.
2. `total_fines(amounts_csv)`: Computes sum of fine amounts from comma-separated string, capped at 10,000.
3. `speed_excess(reading)`: Calculates percentage over speed limit from `'speed/limit'` format.

---

## Lab Execution Steps

### Step 1: Environment Setup
Installed property-based testing and fuzzing dependencies:
```bash
pip install pytest hypothesis
```

### Step 2: Running Application on Normal Sample Inputs
Executed initial application using standard valid inputs:
```bash
python traffic_fine.py
```
- Inputs tested: `TF-2024-0456` (returns `('TF', 2024, 456)`), `500,1200,300` (returns `2000`), `72/60` (returns `20`).
- *Observation:* Works properly on expected formats, but lacks input validation.

### Step 3: Fuzz Test Implementation with Hypothesis
Implemented property tests in `test_traffic_fine.py` using `@given(st.text() | st.none())`:
- Asserts that none of the functions crash on arbitrary Unicode strings or `None`.

### Step 4: Fuzz Testing Buggy Code (Vulnerabilities Discovered)
Running `pytest test_traffic_fine.py` uncovered multiple severe bugs:
- **`parse_ticket_id`:** `AttributeError` on `None`; `ValueError` on empty string `""` and inputs with missing hyphen delimiters.
- **`total_fines`:** `AttributeError` on `None`; `ValueError: invalid literal for int()` on empty string `""` or trailing commas.
- **`speed_excess`:** `AttributeError` on `None`; `ValueError` on missing `/`; `ZeroDivisionError: integer division by zero` when speed limit is 0 (e.g. `'70/0'`).

### Step 5: Defensive Code Hardening
Refactored `traffic_fine.py` to defensively guard against all invalid inputs:
- Added `isinstance(..., str)` checks and null guards.
- Protected string splits with token length assertions.
- Wrapped integer conversions in guarded `try-except (ValueError, TypeError, OverflowError)` blocks.
- Added strict divisor checks (`limit <= 0`) to prevent division by zero.
- Graceful return values: returns `None` or `0` on invalid inputs rather than crashing.

### Step 6: Verification with Fuzz Testing
Re-ran test suite on hardened code:
```bash
pytest test_traffic_fine.py
```
- **Result:** All 11 property and regression tests **PASSED** (exercised against hundreds of randomized inputs by Hypothesis).

---

## Deliverables Checklist
- [x] `traffic_fine.py`: Fully hardened application resilient to fuzzing
- [x] `test_traffic_fine.py`: Complete test suite with Hypothesis property tests and regression cases
- [x] `screenshots/`: Step-by-step verification screenshots:
  - `lab7_step2_initial_run.png`: Normal run on sample inputs
  - `lab7_step4_fuzz_failures.png`: Hypothesis failure output on unhardened code
  - `lab7_step5_fixed_run.png`: Normal run on hardened code
  - `lab7_step6_fuzz_passed.png`: All fuzz tests passing on hardened code
- [x] `Lab_7_Fuzz_Testing_PES1UG24CS450.pdf`: Comprehensive PDF report documenting methodology, findings, and fixes
