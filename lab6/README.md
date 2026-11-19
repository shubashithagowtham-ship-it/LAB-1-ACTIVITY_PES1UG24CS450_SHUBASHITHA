# Lab 6: Code and Branch Coverage Analysis

**Student Name:** Shubashitha Gowtham  
**SRN:** PES1UG24CS450  
**Section:** 5H  
**Course:** Software Engineering Lab (UE24CS251B)  
**Problem Statement:** Scenario 27 — Traffic Fine Calculator (`traffic_fine.py`)  

---

## Objective
- Understand the difference between **Statement (Line) Coverage** and **Branch Coverage**.
- Use Python's `coverage` tool to measure, analyze, and optimize test completeness.
- Identify untested decision branches and logical paths.
- Design targeted test cases achieving **100% Line Coverage** and **100% Branch Coverage**.

---

## Problem Overview

The application under test is `traffic_fine.py`, which provides three functions:
1. `speeding_fine(speed, limit, zone)`: Calculates fines based on road zone (`school`, `highway`, or default) and excess speed categories (`> 40`, `> 20`, or `<= 20`).
2. `license_action(points, is_commercial, repeat_offender)`: Determines license penalties (`revoke`, `suspend`, `warning`, `notice`, `none`) based on points threshold (`>= 12`, `>= 8`, `>= 4`) and driver classification.
3. `total_penalty(fines)`: Calculates cumulative penalties, validates against negative values (`ValueError`), and caps maximum fine at 10,000.

---

## Coverage Analysis Progression

### 1. Initial Baseline Coverage
Running the initial starter test case with branch coverage enabled:
```bash
coverage run --branch -m pytest test_traffic_fine.py
coverage report -m
```
- **Line Coverage:** 21% (26 missed statements out of 35)
- **Branch Coverage:** 21% (22 missed branches out of 26)

---

### 2. Statement (Code) Coverage Suite (`CodeCoverageTest_traffic_fine.py`)
Designed 12 targeted unit tests exercising all execution paths:
```bash
coverage run -m pytest CodeCoverageTest_traffic_fine.py
coverage report -m
```
- **Statements:** 35 / 35 (100% Statement Coverage)
- **Status:** 12 passed in 0.40s
- *Note:* While line coverage is 100%, branch coverage at this stage was 98% because the False branch for `if total > 10000` (penalty sum <= 10000) was not taken, demonstrating why line coverage alone is insufficient.

---

### 3. Branch Coverage Suite (`BranchCoverageTest_traffic_fine.py`)
Engineered 32 comprehensive tests applying Boundary Value Analysis (BVA) and Equivalence Partitioning:
```bash
coverage run --branch -m pytest BranchCoverageTest_traffic_fine.py
coverage report -m
```
- **Statements:** 35 / 35 (100%)
- **Branches:** 26 / 26 (100% Branch Coverage)
- **Missed Branches:** 0
- **Status:** 32 passed in 0.78s

---

## Coverage Metrics Summary Table

| Metric / Stage | Total Stmts | Missed Stmts | Total Branches | Missed Branches | Overall Coverage |
|---|---|---|---|---|---|
| **Initial Baseline** | 35 | 26 | 26 | 22 | **21%** |
| **Code Coverage Test** | 35 | 0 | 26 | 1 | **100% Line / 98% Branch** |
| **Branch Coverage Test** | 35 | 0 | 26 | 0 | **100% Line & Branch** |

---

## Deliverables Checklist
- [x] `traffic_fine.py`: Application module under test
- [x] `CodeCoverageTest_traffic_fine.py`: Dedicated test suite for code/statement coverage (>90%)
- [x] `BranchCoverageTest_traffic_fine.py`: Dedicated test suite for branch coverage (100%)
- [x] `test_traffic_fine.py`: Unified full test suite
- [x] `screenshots/`: Terminal output verification screenshots
  - `lab6_initial_coverage.png`
  - `lab6_code_coverage.png`
  - `lab6_branch_coverage.png`
- [x] `Lab_6_Code_and_Branch_Coverage_Analysis_PES1UG24CS450.pdf`: Comprehensive lab report document
- [x] Minimum 2 distinct commits in Git history for evaluation rubric compliance
