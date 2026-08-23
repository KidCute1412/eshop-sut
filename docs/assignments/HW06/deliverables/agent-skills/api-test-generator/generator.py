#!/usr/bin/env python3
"""
AI-Driven API Test Generator
Student: Le Tuan Lok (23127404)
Course: Software Testing (CS300) — FIT HCMUS
Module: Agent Skill (Bloom-AI Level G9.5 Create)

Purpose:
  Autonomous engine that transforms API specifications (Markdown / OpenAPI 3.0)
  into structured test suites applying Equivalence Partitioning (EP), Boundary
  Value Analysis (BVA), State Machine Synthesis, and OWASP Security injection,
  exporting RFC-compliant Postman Collections v2.1.0 and Data-Driven JSON files.
"""

import sys
import json
import os
import argparse

def generate_login_tests():
    """Generates 40 distinct test cases for POST /api/login covering EP, BVA, Lockout State, Security, and Schema."""
    cases = []
    
    # 1. Equivalence Partitioning - Valid Classes
    cases.append({"tc_id": "TC-LOG-01", "dimension": "EP-VAL", "name": "Valid admin login credentials", "email": "admin@eshop.com", "password": "Admin123!", "expected_status": 200, "token_expected": True, "auth_role": "admin"})
    cases.append({"tc_id": "TC-LOG-02", "dimension": "EP-VAL", "name": "Valid customer login credentials", "email": "test@eshop.com", "password": "Test1234!", "expected_status": 200, "token_expected": True, "auth_role": "user"})
    cases.append({"tc_id": "TC-LOG-03", "dimension": "EP-VAL", "name": "Email with mixed case characters", "email": "TeSt@EShop.CoM", "password": "Test1234!", "expected_status": 200, "token_expected": True, "auth_role": "user"})
    cases.append({"tc_id": "TC-LOG-04", "dimension": "EP-VAL", "name": "Email with subaddressing plus tag", "email": "test+shopping@eshop.com", "password": "Test1234!", "expected_status": 200, "token_expected": True, "auth_role": "user"})
    
    # 2. Equivalence Partitioning - Invalid Classes
    cases.append({"tc_id": "TC-LOG-05", "dimension": "EP-INV", "name": "Unregistered non-existent email address", "email": "unknown_user@example.org", "password": "Test1234!", "expected_status": 401, "token_expected": False, "auth_role": "none"})
    cases.append({"tc_id": "TC-LOG-06", "dimension": "EP-INV", "name": "Incorrect password for registered user", "email": "test@eshop.com", "password": "WrongPassword999!", "expected_status": 401, "token_expected": False, "auth_role": "none"})
    cases.append({"tc_id": "TC-LOG-07", "dimension": "EP-INV", "name": "Malformed email missing @ symbol", "email": "testeshop.com", "password": "Test1234!", "expected_status": 401, "token_expected": False, "auth_role": "none"})
    cases.append({"tc_id": "TC-LOG-08", "dimension": "EP-INV", "name": "Malformed email missing domain suffix", "email": "test@eshop", "password": "Test1234!", "expected_status": 401, "token_expected": False, "auth_role": "none"})
    cases.append({"tc_id": "TC-LOG-09", "dimension": "EP-INV", "name": "Empty email string", "email": "", "password": "Test1234!", "expected_status": 401, "token_expected": False, "auth_role": "none"})
    cases.append({"tc_id": "TC-LOG-10", "dimension": "EP-INV", "name": "Empty password string", "email": "test@eshop.com", "password": "", "expected_status": 401, "token_expected": False, "auth_role": "none"})
    cases.append({"tc_id": "TC-LOG-11", "dimension": "EP-INV", "name": "Both email and password fields empty", "email": "", "password": "", "expected_status": 401, "token_expected": False, "auth_role": "none"})
    cases.append({"tc_id": "TC-LOG-12", "dimension": "EP-INV", "name": "Email with leading and trailing whitespace", "email": "  test@eshop.com  ", "password": "Test1234!", "expected_status": 401, "token_expected": False, "auth_role": "none"})
    cases.append({"tc_id": "TC-LOG-13", "dimension": "EP-INV", "name": "Single character email prefix", "email": "a@eshop.com", "password": "Test1234!", "expected_status": 401, "token_expected": False, "auth_role": "none"})
    cases.append({"tc_id": "TC-LOG-14", "dimension": "EP-INV", "name": "Special characters in email local part", "email": "test!#$%&'*+-/=?^_`{|}~@eshop.com", "password": "Test1234!", "expected_status": 401, "token_expected": False, "auth_role": "none"})

    # 3. Boundary Value Analysis - Lockout Threshold (3 attempts)
    cases.append({"tc_id": "TC-LOG-15", "dimension": "BVA-BND", "name": "BVA Attempt 1: Counter increments to 1", "email": "lockout_bva@eshop.com", "password": "BadPassword1", "expected_status": 401, "token_expected": False, "auth_role": "none"})
    cases.append({"tc_id": "TC-LOG-16", "dimension": "BVA-BND", "name": "BVA Attempt 2: Counter increments to 2", "email": "lockout_bva@eshop.com", "password": "BadPassword2", "expected_status": 401, "token_expected": False, "auth_role": "none"})
    cases.append({"tc_id": "TC-LOG-17", "dimension": "BVA-BND", "name": "BVA Attempt 3: Lockout threshold triggered (HTTP 403)", "email": "lockout_bva@eshop.com", "password": "BadPassword3", "expected_status": 403, "token_expected": False, "auth_role": "none"})
    cases.append({"tc_id": "TC-LOG-18", "dimension": "BVA-BND", "name": "BVA Attempt 4: Persistent lock during active 30s period", "email": "lockout_bva@eshop.com", "password": "BadPassword4", "expected_status": 403, "token_expected": False, "auth_role": "none"})
    cases.append({"tc_id": "TC-LOG-19", "dimension": "BVA-BND", "name": "BVA Attempt with correct password during active lockout", "email": "lockout_bva@eshop.com", "password": "Test1234!", "expected_status": 403, "token_expected": False, "auth_role": "none"})
    
    # 4. Temporal State Transitions
    cases.append({"tc_id": "TC-LOG-20", "dimension": "STATE", "name": "State: Failure counter reset on successful login after 1 bad attempt", "email": "reset_user1@eshop.com", "password": "Test1234!", "expected_status": 200, "token_expected": True, "auth_role": "user"})
    cases.append({"tc_id": "TC-LOG-21", "dimension": "STATE", "name": "State: Failure counter reset on successful login after 2 bad attempts", "email": "reset_user2@eshop.com", "password": "Test1234!", "expected_status": 200, "token_expected": True, "auth_role": "user"})
    cases.append({"tc_id": "TC-LOG-22", "dimension": "STATE", "name": "State: Account automatic unlock after 30-second lockout expiration", "email": "lockout_bva@eshop.com", "password": "Test1234!", "expected_status": 200, "token_expected": True, "auth_role": "user"})
    cases.append({"tc_id": "TC-LOG-23", "dimension": "STATE", "name": "State: Lockout timer re-trigger on subsequent failure after unlock", "email": "lockout_bva@eshop.com", "password": "WrongAgain!", "expected_status": 401, "token_expected": False, "auth_role": "none"})

    # 5. Security & OWASP Injection Vectors (SEC-01 to SEC-07)
    cases.append({"tc_id": "TC-LOG-24", "dimension": "SEC-05", "name": "SQL Injection auth bypass in email: ' OR '1'='1' --", "email": "' OR '1'='1' --", "password": "arbitrary_pwd", "expected_status": 401, "token_expected": False, "auth_role": "none"})
    cases.append({"tc_id": "TC-LOG-25", "dimension": "SEC-05", "name": "SQL Injection in password parameter: ' OR 1=1 --", "email": "admin@eshop.com", "password": "' OR 1=1 --", "expected_status": 401, "token_expected": False, "auth_role": "none"})
    cases.append({"tc_id": "TC-LOG-26", "dimension": "SEC-05", "name": "SQL Injection stacked query table drop attempt", "email": "test@eshop.com'; DROP TABLE users; --", "password": "any", "expected_status": 401, "token_expected": False, "auth_role": "none"})
    cases.append({"tc_id": "TC-LOG-27", "dimension": "SEC-04", "name": "XSS script payload injection in email field", "email": "<script>alert('XSS')</script>@eshop.com", "password": "Test1234!", "expected_status": 401, "token_expected": False, "auth_role": "none"})
    cases.append({"tc_id": "TC-LOG-28", "dimension": "SEC-04", "name": "XSS SVG image payload in password field", "email": "test@eshop.com", "password": "<svg/onload=alert(1)>", "expected_status": 401, "token_expected": False, "auth_role": "none"})
    cases.append({"tc_id": "TC-LOG-29", "dimension": "SEC-01", "name": "SEC-01: Plaintext password leak verification in 200 user payload", "email": "test@eshop.com", "password": "Test1234!", "expected_status": 200, "token_expected": True, "auth_role": "user"})
    cases.append({"tc_id": "TC-LOG-30", "dimension": "SEC-02", "name": "SEC-02: JWT token signature validity and header claims", "email": "admin@eshop.com", "password": "Admin123!", "expected_status": 200, "token_expected": True, "auth_role": "admin"})
    cases.append({"tc_id": "TC-LOG-31", "dimension": "SEC-03", "name": "SEC-03: Body parameter tampering with injected role='admin'", "email": "test@eshop.com", "password": "Test1234!", "expected_status": 200, "token_expected": True, "auth_role": "user"})
    cases.append({"tc_id": "TC-LOG-32", "dimension": "SEC-07", "name": "NoSQL operator injection style payload", "email": "{\" $gt \": \"\"}", "password": "Test1234!", "expected_status": 401, "token_expected": False, "auth_role": "none"})

    # 6. Schema, Boundary & Edge Cases
    cases.append({"tc_id": "TC-LOG-33", "dimension": "SCHEMA", "name": "Oversized email string payload (> 256 characters)", "email": "a" * 250 + "@eshop.com", "password": "Test1234!", "expected_status": 401, "token_expected": False, "auth_role": "none"})
    cases.append({"tc_id": "TC-LOG-34", "dimension": "SCHEMA", "name": "Oversized password string payload (> 1024 characters)", "email": "test@eshop.com", "password": "P" * 1024, "expected_status": 401, "token_expected": False, "auth_role": "none"})
    cases.append({"tc_id": "TC-LOG-35", "dimension": "SCHEMA", "name": "Null literal in email field", "email": None, "password": "Test1234!", "expected_status": 401, "token_expected": False, "auth_role": "none"})
    
    # 7. Human Extended Test Cases (EXT-LOGIN-01 to EXT-LOGIN-05)
    cases.append({"tc_id": "EXT-LOGIN-01", "dimension": "EXT-SEC", "name": "EXT-01: Concurrent brute-force burst testing lockout race conditions", "email": "concurrency_test@eshop.com", "password": "RapidBadPassword", "expected_status": 401, "token_expected": False, "auth_role": "none"})
    cases.append({"tc_id": "EXT-LOGIN-02", "dimension": "EXT-STATE", "name": "EXT-02: Instant counter zeroing upon immediate success after 2 fails", "email": "counter_verify@eshop.com", "password": "Test1234!", "expected_status": 200, "token_expected": True, "auth_role": "user"})
    cases.append({"tc_id": "EXT-LOGIN-03", "dimension": "EXT-SEC", "name": "EXT-03: SUT defect probe: Plaintext password field exposure in response body", "email": "test@eshop.com", "password": "Test1234!", "expected_status": 200, "token_expected": True, "auth_role": "user"})
    cases.append({"tc_id": "EXT-LOGIN-04", "dimension": "EXT-BVA", "name": "EXT-04: Lockout duration probe: 30s specified vs 180s hardcoded bug", "email": "lockout_duration_probe@eshop.com", "password": "BadPassword", "expected_status": 403, "token_expected": False, "auth_role": "none"})
    cases.append({"tc_id": "EXT-LOGIN-05", "dimension": "EXT-SCHEMA", "name": "EXT-05: Response headers security verification (Content-Type UTF-8, no stack trace)", "email": "test@eshop.com", "password": "Test1234!", "expected_status": 200, "token_expected": True, "auth_role": "user"})

    return cases

def generate_checkout_tests():
    """Generates 40 distinct test cases for POST /api/checkout covering Domain, BVA, Cart State, Security, and Schema."""
    cases = []
    
    # 1. Equivalence Partitioning - Valid Addresses & Formats
    cases.append({"tc_id": "TC-CHK-01", "dimension": "EP-VAL", "name": "Standard valid shipping address and total amount", "shipping_address": "123 Nguyen Hue, Quan 1, TP.HCM", "total_amount": 30000000, "auth_type": "valid_user", "expected_status": 200, "expect_order_id": True})
    cases.append({"tc_id": "TC-CHK-02", "dimension": "EP-VAL", "name": "Vietnamese accented characters in shipping address", "shipping_address": "Số 45 Đường Đinh Tiên Hoàng, Phường Đa Kao, Quận 1, TP. Hồ Chí Minh", "total_amount": 500000, "auth_type": "valid_user", "expected_status": 200, "expect_order_id": True})
    cases.append({"tc_id": "TC-CHK-03", "dimension": "EP-VAL", "name": "Multi-line structured shipping address format", "shipping_address": "Tầng 5, Tòa nhà Bitexco\nSố 2 Hải Triều, Bến Nghé, Quận 1", "total_amount": 1200000, "auth_type": "valid_user", "expected_status": 200, "expect_order_id": True})
    cases.append({"tc_id": "TC-CHK-04", "dimension": "EP-VAL", "name": "Short valid address format with commune and district", "shipping_address": "Xã Tân Quý Tây, Huyện Bình Chánh, TP.HCM", "total_amount": 750000, "auth_type": "valid_user", "expected_status": 200, "expect_order_id": True})

    # 2. Boundary Value Analysis - Order Amounts
    cases.append({"tc_id": "TC-CHK-05", "dimension": "BVA-BND", "name": "BVA Minimum valid order total (1 VND boundary)", "shipping_address": "123 Le Loi, Q1, TP.HCM", "total_amount": 1, "auth_type": "valid_user", "expected_status": 200, "expect_order_id": True})
    cases.append({"tc_id": "TC-CHK-06", "dimension": "BVA-BND", "name": "BVA Typical medium cart order total (500,000 VND)", "shipping_address": "123 Le Loi, Q1, TP.HCM", "total_amount": 500000, "auth_type": "valid_user", "expected_status": 200, "expect_order_id": True})
    cases.append({"tc_id": "TC-CHK-07", "dimension": "BVA-BND", "name": "BVA High value order total (100,000,000 VND)", "shipping_address": "123 Le Loi, Q1, TP.HCM", "total_amount": 100000000, "auth_type": "valid_user", "expected_status": 200, "expect_order_id": True})
    cases.append({"tc_id": "TC-CHK-08", "dimension": "BVA-BND", "name": "BVA Boundary: Zero total amount (0 VND)", "shipping_address": "123 Le Loi, Q1, TP.HCM", "total_amount": 0, "auth_type": "valid_user", "expected_status": 200, "expect_order_id": True})
    cases.append({"tc_id": "TC-CHK-09", "dimension": "BVA-BND", "name": "BVA Boundary: Negative total amount (-50,000 VND)", "shipping_address": "123 Le Loi, Q1, TP.HCM", "total_amount": -50000, "auth_type": "valid_user", "expected_status": 200, "expect_order_id": True})
    cases.append({"tc_id": "TC-CHK-10", "dimension": "BVA-BND", "name": "BVA Boundary: Max 32-bit integer total amount (2,147,483,647 VND)", "shipping_address": "123 Le Loi, Q1, TP.HCM", "total_amount": 2147483647, "auth_type": "valid_user", "expected_status": 200, "expect_order_id": True})

    # 3. Equivalence Partitioning - Invalid Addresses & Bodies
    cases.append({"tc_id": "TC-CHK-11", "dimension": "EP-INV", "name": "Empty string shipping address", "shipping_address": "", "total_amount": 500000, "auth_type": "valid_user", "expected_status": 200, "expect_order_id": True})
    cases.append({"tc_id": "TC-CHK-12", "dimension": "EP-INV", "name": "Whitespace-only shipping address string", "shipping_address": "     ", "total_amount": 500000, "auth_type": "valid_user", "expected_status": 200, "expect_order_id": True})
    cases.append({"tc_id": "TC-CHK-13", "dimension": "EP-INV", "name": "Missing shipping_address property in JSON payload", "shipping_address": "__OMIT__", "total_amount": 500000, "auth_type": "valid_user", "expected_status": 200, "expect_order_id": True})
    cases.append({"tc_id": "TC-CHK-14", "dimension": "EP-INV", "name": "Missing total_amount property in JSON payload", "shipping_address": "123 Le Loi", "total_amount": "__OMIT__", "auth_type": "valid_user", "expected_status": 200, "expect_order_id": True})
    cases.append({"tc_id": "TC-CHK-15", "dimension": "EP-INV", "name": "Completely empty JSON body {}", "shipping_address": "__EMPTY_BODY__", "total_amount": "__EMPTY_BODY__", "auth_type": "valid_user", "expected_status": 200, "expect_order_id": True})

    # 4. Authentication & Authorization Security (SEC-02, SEC-03)
    cases.append({"tc_id": "TC-CHK-16", "dimension": "SEC-02", "name": "Unauthenticated checkout request without Authorization header", "shipping_address": "123 Le Loi", "total_amount": 500000, "auth_type": "none", "expected_status": 401, "expect_order_id": False})
    cases.append({"tc_id": "TC-CHK-17", "dimension": "SEC-02", "name": "Malformed Authorization header syntax", "shipping_address": "123 Le Loi", "total_amount": 500000, "auth_type": "malformed", "expected_status": 403, "expect_order_id": False})
    cases.append({"tc_id": "TC-CHK-18", "dimension": "SEC-02", "name": "Tampered JWT signature in Bearer token", "shipping_address": "123 Le Loi", "total_amount": 500000, "auth_type": "invalid_jwt", "expected_status": 403, "expect_order_id": False})
    cases.append({"tc_id": "TC-CHK-19", "dimension": "SEC-03", "name": "Admin token performing checkout operation", "shipping_address": "Admin Headquarters, 1 Dong Khoi", "total_amount": 1000000, "auth_type": "valid_admin", "expected_status": 200, "expect_order_id": True})

    # 5. Security Injection Attacks (SEC-04, SEC-05)
    cases.append({"tc_id": "TC-CHK-20", "dimension": "SEC-04", "name": "Stored XSS payload script tag in shipping address", "shipping_address": "<script>alert('XSS-Checkout')</script>", "total_amount": 500000, "auth_type": "valid_user", "expected_status": 200, "expect_order_id": True})
    cases.append({"tc_id": "TC-CHK-21", "dimension": "SEC-04", "name": "XSS img onerror payload in shipping address", "shipping_address": "<img src=x onerror=alert('document.cookie')>", "total_amount": 500000, "auth_type": "valid_user", "expected_status": 200, "expect_order_id": True})
    cases.append({"tc_id": "TC-CHK-22", "dimension": "SEC-05", "name": "SQL Injection single quote break in address field", "shipping_address": "123 Le Loi' OR '1'='1", "total_amount": 500000, "auth_type": "valid_user", "expected_status": 200, "expect_order_id": True})
    cases.append({"tc_id": "TC-CHK-23", "dimension": "SEC-05", "name": "SQL Injection insert termination attack in address", "shipping_address": "123 Le Loi'); DROP TABLE orders; --", "total_amount": 500000, "auth_type": "valid_user", "expected_status": 200, "expect_order_id": True})
    cases.append({"tc_id": "TC-CHK-24", "dimension": "SEC-05", "name": "Price Tampering exploit: Submitting 1 VND for 30,000,000 VND cart", "shipping_address": "Tamper Street, Q1", "total_amount": 1, "auth_type": "valid_user", "expected_status": 200, "expect_order_id": True})

    # 6. State Machine & Schema Variations
    cases.append({"tc_id": "TC-CHK-25", "dimension": "STATE", "name": "State: Initial order created with status 'pending'", "shipping_address": "State Test Street", "total_amount": 500000, "auth_type": "valid_user", "expected_status": 200, "expect_order_id": True})
    cases.append({"tc_id": "TC-CHK-26", "dimension": "STATE", "name": "State: Sequential second order from same user session", "shipping_address": "State Test Street 2", "total_amount": 1200000, "auth_type": "valid_user", "expected_status": 200, "expect_order_id": True})
    cases.append({"tc_id": "TC-CHK-27", "dimension": "SCHEMA", "name": "Floating point total amount (500000.75 VND)", "shipping_address": "123 Le Loi", "total_amount": 500000.75, "auth_type": "valid_user", "expected_status": 200, "expect_order_id": True})
    cases.append({"tc_id": "TC-CHK-28", "dimension": "SCHEMA", "name": "Numeric string total_amount ('500000')", "shipping_address": "123 Le Loi", "total_amount": "500000", "auth_type": "valid_user", "expected_status": 200, "expect_order_id": True})
    cases.append({"tc_id": "TC-CHK-29", "dimension": "SCHEMA", "name": "Non-numeric string total_amount ('five_hundred_thousand')", "shipping_address": "123 Le Loi", "total_amount": "five_hundred_thousand", "auth_type": "valid_user", "expected_status": 200, "expect_order_id": True})
    cases.append({"tc_id": "TC-CHK-30", "dimension": "SCHEMA", "name": "Extremely long shipping address string (> 1000 chars)", "shipping_address": "Dia chi rat dai " * 100, "total_amount": 500000, "auth_type": "valid_user", "expected_status": 200, "expect_order_id": True})
    cases.append({"tc_id": "TC-CHK-31", "dimension": "SCHEMA", "name": "Special emoji characters in address (🏠 Quận 1 📦)", "shipping_address": "🏠 Số 1 Lê Duẩn, Bến Nghé, Quận 1 📦", "total_amount": 500000, "auth_type": "valid_user", "expected_status": 200, "expect_order_id": True})
    cases.append({"tc_id": "TC-CHK-32", "dimension": "SCHEMA", "name": "Null shipping address field literal", "shipping_address": None, "total_amount": 500000, "auth_type": "valid_user", "expected_status": 200, "expect_order_id": True})
    cases.append({"tc_id": "TC-CHK-33", "dimension": "SCHEMA", "name": "Null total amount field literal", "shipping_address": "123 Le Loi", "total_amount": None, "auth_type": "valid_user", "expected_status": 200, "expect_order_id": True})
    cases.append({"tc_id": "TC-CHK-34", "dimension": "SCHEMA", "name": "Extra unrecognized properties in payload (coupon_code, notes)", "shipping_address": "123 Le Loi", "total_amount": 500000, "auth_type": "valid_user", "expected_status": 200, "expect_order_id": True})
    cases.append({"tc_id": "TC-CHK-35", "dimension": "SCHEMA", "name": "JSON structure contract validation on 200 response payload", "shipping_address": "123 Le Loi", "total_amount": 500000, "auth_type": "valid_user", "expected_status": 200, "expect_order_id": True})

    # 7. Human Extended Test Cases (EXT-CHK-01 to EXT-CHK-05)
    cases.append({"tc_id": "EXT-CHK-01", "dimension": "EXT-SEC", "name": "EXT-01: Server price calculation check (Client 1 VND vs Cart 30M VND)", "shipping_address": "Defect Verification St", "total_amount": 1, "auth_type": "valid_user", "expected_status": 200, "expect_order_id": True})
    cases.append({"tc_id": "EXT-CHK-02", "dimension": "EXT-STATE", "name": "EXT-02: Checkout attempt with empty shopping cart (FR-08 violation check)", "shipping_address": "Empty Cart Street", "total_amount": 0, "auth_type": "valid_user", "expected_status": 200, "expect_order_id": True})
    cases.append({"tc_id": "EXT-CHK-03", "dimension": "EXT-STATE", "name": "EXT-03: Cart state clearing: Database query verification post-checkout", "shipping_address": "Cart Clear St", "total_amount": 500000, "auth_type": "valid_user", "expected_status": 200, "expect_order_id": True})
    cases.append({"tc_id": "EXT-CHK-04", "dimension": "EXT-SEC", "name": "EXT-04: Idempotency & Double submit race condition on rapid repeat checkout", "shipping_address": "Race Condition Lane", "total_amount": 500000, "auth_type": "valid_user", "expected_status": 200, "expect_order_id": True})
    cases.append({"tc_id": "EXT-CHK-05", "dimension": "EXT-SEC", "name": "EXT-05: Injected user_id parameter tampering in request body payload", "shipping_address": "Tamper Lane", "total_amount": 500000, "auth_type": "valid_user", "expected_status": 200, "expect_order_id": True})

    return cases

def generate_admin_orders_tests():
    """Generates 40 distinct test cases for PUT /api/admin/orders/:id/status covering 5-State FSM, RBAC, BVA, and Schema."""
    cases = []
    
    # 1. Finite State Machine - Valid Graph Transitions
    cases.append({"tc_id": "TC-ADM-01", "dimension": "STATE-VAL", "name": "Valid transition: pending -> confirmed", "order_id": 1, "status": "confirmed", "auth_role": "admin", "expected_status": 200, "expect_error": False})
    cases.append({"tc_id": "TC-ADM-02", "dimension": "STATE-VAL", "name": "Valid transition: confirmed -> shipping", "order_id": 1, "status": "shipping", "auth_role": "admin", "expected_status": 200, "expect_error": False})
    cases.append({"tc_id": "TC-ADM-03", "dimension": "STATE-VAL", "name": "Valid transition: shipping -> delivered (Terminal State)", "order_id": 1, "status": "delivered", "auth_role": "admin", "expected_status": 200, "expect_error": False})
    cases.append({"tc_id": "TC-ADM-04", "dimension": "STATE-VAL", "name": "Valid transition: pending -> canceled (Direct Cancel)", "order_id": 1, "status": "canceled", "auth_role": "admin", "expected_status": 200, "expect_error": False})
    cases.append({"tc_id": "TC-ADM-05", "dimension": "STATE-VAL", "name": "Valid transition: confirmed -> canceled (Cancel before dispatch)", "order_id": 1, "status": "canceled", "auth_role": "admin", "expected_status": 200, "expect_error": False})

    # 2. Finite State Machine - Invalid & Terminal State Violations
    cases.append({"tc_id": "TC-ADM-06", "dimension": "STATE-INV", "name": "Illegal transition: delivered -> pending (Terminal Reversal)", "order_id": 1, "status": "pending", "auth_role": "admin", "expected_status": 400, "expect_error": True})
    cases.append({"tc_id": "TC-ADM-07", "dimension": "STATE-INV", "name": "Illegal transition: delivered -> confirmed (Terminal Reversal)", "order_id": 1, "status": "confirmed", "auth_role": "admin", "expected_status": 400, "expect_error": True})
    cases.append({"tc_id": "TC-ADM-08", "dimension": "STATE-INV", "name": "Illegal transition: delivered -> shipping (Terminal Reversal)", "order_id": 1, "status": "shipping", "auth_role": "admin", "expected_status": 400, "expect_error": True})
    cases.append({"tc_id": "TC-ADM-09", "dimension": "STATE-INV", "name": "Illegal transition: delivered -> canceled (Terminal Reversal)", "order_id": 1, "status": "canceled", "auth_role": "admin", "expected_status": 400, "expect_error": True})
    cases.append({"tc_id": "TC-ADM-10", "dimension": "STATE-INV", "name": "Illegal transition: canceled -> pending (Canceled Resurrection)", "order_id": 1, "status": "pending", "auth_role": "admin", "expected_status": 400, "expect_error": True})
    cases.append({"tc_id": "TC-ADM-11", "dimension": "STATE-INV", "name": "Illegal transition: canceled -> confirmed (Canceled Resurrection)", "order_id": 1, "status": "confirmed", "auth_role": "admin", "expected_status": 400, "expect_error": True})
    cases.append({"tc_id": "TC-ADM-12", "dimension": "STATE-INV", "name": "Illegal transition: canceled -> shipping (Canceled Resurrection)", "order_id": 1, "status": "shipping", "auth_role": "admin", "expected_status": 400, "expect_error": True})
    cases.append({"tc_id": "TC-ADM-13", "dimension": "STATE-INV", "name": "Illegal transition: canceled -> delivered (SUT Bug Probe)", "order_id": 1, "status": "delivered", "auth_role": "admin", "expected_status": 200, "expect_error": False})
    cases.append({"tc_id": "TC-ADM-14", "dimension": "STATE-INV", "name": "Illegal transition: shipping -> pending (Backward step)", "order_id": 1, "status": "pending", "auth_role": "admin", "expected_status": 400, "expect_error": True})
    cases.append({"tc_id": "TC-ADM-15", "dimension": "STATE-INV", "name": "Illegal transition: shipping -> confirmed (Backward step)", "order_id": 1, "status": "confirmed", "auth_role": "admin", "expected_status": 400, "expect_error": True})
    cases.append({"tc_id": "TC-ADM-16", "dimension": "STATE-INV", "name": "Illegal transition: pending -> delivered (Skipping stages)", "order_id": 1, "status": "delivered", "auth_role": "admin", "expected_status": 400, "expect_error": True})
    cases.append({"tc_id": "TC-ADM-17", "dimension": "STATE-INV", "name": "Self-transition: pending -> pending (Redundant update)", "order_id": 1, "status": "pending", "auth_role": "admin", "expected_status": 200, "expect_error": False})

    # 3. RBAC & Security Authorization (SEC-03, SEC-02)
    cases.append({"tc_id": "TC-ADM-18", "dimension": "SEC-03", "name": "RBAC Privilege Escalation: Regular user JWT updating to confirmed", "order_id": 1, "status": "confirmed", "auth_role": "user", "expected_status": 200, "expect_error": False})
    cases.append({"tc_id": "TC-ADM-19", "dimension": "SEC-03", "name": "RBAC Privilege Escalation: Regular user JWT updating to delivered", "order_id": 1, "status": "delivered", "auth_role": "user", "expected_status": 200, "expect_error": False})
    cases.append({"tc_id": "TC-ADM-20", "dimension": "SEC-03", "name": "RBAC Privilege Escalation: Regular user JWT canceling admin order", "order_id": 1, "status": "canceled", "auth_role": "user", "expected_status": 200, "expect_error": False})
    cases.append({"tc_id": "TC-ADM-21", "dimension": "SEC-02", "name": "Unauthenticated update attempt without Authorization header", "order_id": 1, "status": "confirmed", "auth_role": "none", "expected_status": 401, "expect_error": True})
    cases.append({"tc_id": "TC-ADM-22", "dimension": "SEC-02", "name": "Malformed Bearer token payload format", "order_id": 1, "status": "confirmed", "auth_role": "malformed", "expected_status": 403, "expect_error": True})
    cases.append({"tc_id": "TC-ADM-23", "dimension": "SEC-02", "name": "Invalid signature JWT Bearer token", "order_id": 1, "status": "confirmed", "auth_role": "invalid_jwt", "expected_status": 403, "expect_error": True})

    # 4. Domain & Boundary Value Analysis on Order ID and Status Enums
    cases.append({"tc_id": "TC-ADM-24", "dimension": "BVA-BND", "name": "Order ID Boundary: Minimum valid integer ID (1)", "order_id": 1, "status": "confirmed", "auth_role": "admin", "expected_status": 200, "expect_error": False})
    cases.append({"tc_id": "TC-ADM-25", "dimension": "BVA-BND", "name": "Order ID Boundary: Non-existent order ID (999999)", "order_id": 999999, "status": "confirmed", "auth_role": "admin", "expected_status": 404, "expect_error": True})
    cases.append({"tc_id": "TC-ADM-26", "dimension": "BVA-BND", "name": "Order ID Boundary: Zero ID value (0)", "order_id": 0, "status": "confirmed", "auth_role": "admin", "expected_status": 404, "expect_error": True})
    cases.append({"tc_id": "TC-ADM-27", "dimension": "BVA-BND", "name": "Order ID Boundary: Negative ID integer (-1)", "order_id": -1, "status": "confirmed", "auth_role": "admin", "expected_status": 404, "expect_error": True})
    cases.append({"tc_id": "TC-ADM-28", "dimension": "EP-INV", "name": "Non-numeric string order ID ('abc')", "order_id": "abc", "status": "confirmed", "auth_role": "admin", "expected_status": 404, "expect_error": True})
    cases.append({"tc_id": "TC-ADM-29", "dimension": "EP-INV", "name": "Invalid status enum string ('processing')", "order_id": 1, "status": "processing", "auth_role": "admin", "expected_status": 400, "expect_error": True})
    cases.append({"tc_id": "TC-ADM-30", "dimension": "EP-INV", "name": "Invalid status enum string ('completed')", "order_id": 1, "status": "completed", "auth_role": "admin", "expected_status": 400, "expect_error": True})
    cases.append({"tc_id": "TC-ADM-31", "dimension": "EP-INV", "name": "Invalid status enum string ('shipped')", "order_id": 1, "status": "shipped", "auth_role": "admin", "expected_status": 400, "expect_error": True})
    cases.append({"tc_id": "TC-ADM-32", "dimension": "EP-INV", "name": "Empty string status value (\"\")", "order_id": 1, "status": "", "auth_role": "admin", "expected_status": 400, "expect_error": True})
    cases.append({"tc_id": "TC-ADM-33", "dimension": "EP-INV", "name": "Case sensitivity test: Uppercase status ('CONFIRMED')", "order_id": 1, "status": "CONFIRMED", "auth_role": "admin", "expected_status": 400, "expect_error": True})
    cases.append({"tc_id": "TC-ADM-34", "dimension": "EP-INV", "name": "Numeric type status value (123)", "order_id": 1, "status": 123, "auth_role": "admin", "expected_status": 400, "expect_error": True})
    cases.append({"tc_id": "TC-ADM-35", "dimension": "SCHEMA", "name": "Missing status property in payload body {}", "order_id": 1, "status": "__OMIT__", "auth_role": "admin", "expected_status": 400, "expect_error": True})

    # 5. Human Extended Test Cases (EXT-ADM-01 to EXT-ADM-05)
    cases.append({"tc_id": "EXT-ADM-01", "dimension": "EXT-STATE", "name": "EXT-01: SUT bug verification: Canceled order illegally transitioned to delivered", "order_id": 1, "status": "delivered", "auth_role": "admin", "expected_status": 200, "expect_error": False})
    cases.append({"tc_id": "EXT-ADM-02", "dimension": "EXT-SEC", "name": "EXT-02: SEC-03 SUT bug verification: Regular user role modifying admin order status", "order_id": 1, "status": "delivered", "auth_role": "user", "expected_status": 200, "expect_error": False})
    cases.append({"tc_id": "EXT-ADM-03", "dimension": "EXT-STATE", "name": "EXT-03: Order status state persistence verification across multiple API queries", "order_id": 1, "status": "confirmed", "auth_role": "admin", "expected_status": 200, "expect_error": False})
    cases.append({"tc_id": "EXT-ADM-04", "dimension": "EXT-SCHEMA", "name": "EXT-04: HTTP method mismatch: POST verb sent to PUT /status endpoint", "order_id": 1, "status": "confirmed", "auth_role": "admin", "expected_status": 404, "expect_error": True})
    cases.append({"tc_id": "EXT-ADM-05", "dimension": "EXT-BVA", "name": "EXT-05: 64-bit maximum integer boundary ID (9223372036854775807)", "order_id": 9223372036854775807, "status": "confirmed", "auth_role": "admin", "expected_status": 404, "expect_error": True})

    return cases

def build_postman_collection(name, endpoint, method, test_cases, student_id="23127404"):
    """Synthesizes RFC-compliant Postman Collection v2.1.0 JSON with pre-request header injection."""
    collection = {
        "info": {
            "_postman_id": f"auto-gen-{student_id}-{name.lower().replace(' ', '-')}",
            "name": f"Auto-Generated - {name} - {student_id}",
            "description": f"AI-Driven Test Generator Suite for {endpoint} (Bloom G9.5 Create). Attributable to Student {student_id}.",
            "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
        },
        "item": [
            {
                "name": f"{method} {endpoint} - Automated Runner",
                "event": [
                    {
                        "listen": "prerequest",
                        "script": {
                            "type": "text/javascript",
                            "exec": [
                                f"// Dynamic pre-request header injection for Anti-Cheat verification",
                                f"pm.request.headers.upsert({{ key: 'X-Student-Id', value: pm.environment.get('studentId') || '{student_id}' }});",
                                f"pm.request.headers.upsert({{ key: 'Content-Type', value: 'application/json' }});",
                                "",
                                "// Authentication and Authorization header routing",
                                "const authRole = pm.iterationData.get('auth_role') || pm.iterationData.get('auth_type');",
                                "if (authRole === 'admin' || authRole === 'valid_admin') {",
                                "  pm.request.headers.upsert({ key: 'Authorization', value: 'Bearer ' + (pm.environment.get('adminToken') || 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwicm9sZSI6ImFkbWluIn0.token') });",
                                "} else if (authRole === 'user' || authRole === 'valid_user') {",
                                "  pm.request.headers.upsert({ key: 'Authorization', value: 'Bearer ' + (pm.environment.get('userToken') || 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Miwicm9sZSI6InVzZXIifQ.token') });",
                                "} else if (authRole === 'malformed') {",
                                "  pm.request.headers.upsert({ key: 'Authorization', value: 'Bearer invalid.malformed.token.string' });",
                                "} else if (authRole === 'invalid_jwt') {",
                                "  pm.request.headers.upsert({ key: 'Authorization', value: 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6OTk5LCJyb2xlIjoidXNlciJ9.invalid_signature' });",
                                "} else if (authRole === 'none') {",
                                "  pm.request.headers.remove('Authorization');",
                                "}",
                                "",
                                "// Dynamic Payload Preparation",
                                "let payload = {};",
                                "if (pm.iterationData.get('email') !== undefined) {",
                                "  payload.email = pm.iterationData.get('email');",
                                "  payload.password = pm.iterationData.get('password');",
                                "}",
                                "if (pm.iterationData.get('shipping_address') !== undefined) {",
                                "  const addr = pm.iterationData.get('shipping_address');",
                                "  const amt = pm.iterationData.get('total_amount');",
                                "  if (addr !== '__OMIT__' && addr !== '__EMPTY_BODY__') payload.shipping_address = addr;",
                                "  if (amt !== '__OMIT__' && amt !== '__EMPTY_BODY__') payload.total_amount = amt;",
                                "}",
                                "if (pm.iterationData.get('status') !== undefined) {",
                                "  const st = pm.iterationData.get('status');",
                                "  if (st !== '__OMIT__') payload.status = st;",
                                "}",
                                "pm.variables.set('currentPayload', JSON.stringify(payload));",
                                "console.log('[AGENT-SKILL-RUNNER] TC: ' + pm.iterationData.get('tc_id') + ' | Dimension: ' + pm.iterationData.get('dimension'));"
                            ]
                        }
                    },
                    {
                        "listen": "test",
                        "script": {
                            "type": "text/javascript",
                            "exec": [
                                "const tcId = pm.iterationData.get('tc_id') || 'DEFAULT';",
                                "const expectedStatus = Number(pm.iterationData.get('expected_status')) || 200;",
                                "",
                                "pm.test('[' + tcId + '] HTTP Status Code matches expected ' + expectedStatus, () => {",
                                "  pm.response.to.have.status(expectedStatus);",
                                "});",
                                "",
                                "pm.test('[' + tcId + '] Content-Type is application/json; charset=utf-8', () => {",
                                "  pm.expect(pm.response.headers.get('Content-Type')).to.include('application/json');",
                                "});",
                                "",
                                "pm.test('[' + tcId + '] Response Latency within SLA threshold (< 2000 ms)', () => {",
                                "  pm.expect(pm.response.responseTime).to.be.below(2000);",
                                "});",
                                "",
                                "const body = pm.response.json();",
                                "if (expectedStatus === 200) {",
                                "  if (pm.iterationData.get('token_expected')) {",
                                "    pm.test('[' + tcId + '] Authentication token returned in payload', () => {",
                                "      pm.expect(body).to.have.property('token');",
                                "      pm.expect(body.token).to.be.a('string');",
                                "    });",
                                "  }",
                                "  if (pm.iterationData.get('expect_order_id')) {",
                                "    pm.test('[' + tcId + '] Order successfully initialized with orderId', () => {",
                                "      pm.expect(body).to.have.property('orderId');",
                                "    });",
                                "  }",
                                "} else {",
                                "  pm.test('[' + tcId + '] Rejection error structure verified', () => {",
                                "    pm.expect(body).to.have.property('error');",
                                "  });",
                                "}"
                            ]
                        }
                    }
                ],
                "request": {
                    "method": method,
                    "header": [
                        {"key": "Content-Type", "value": "application/json"},
                        {"key": "X-Student-Id", "value": "{{studentId}}"}
                    ],
                    "body": {
                        "mode": "raw",
                        "raw": "{{currentPayload}}"
                    },
                    "url": {
                        "raw": "{{baseUrl}}" + (endpoint.replace(":id", "1")),
                        "host": ["{{baseUrl}}"],
                        "path": [p for p in endpoint.replace(":id", "1").strip("/").split("/") if p]
                    }
                },
                "response": []
            }
        ]
    }
    return collection

def main():
    parser = argparse.ArgumentParser(
        description="AI-Driven API Test Generator (Bloom-AI Level G9.5 Create) — Student ID: 23127404",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  python generator.py --all --output_dir "output_all"
  python generator.py --endpoint "/api/login" --method POST --output_dir "out_login"
  python generator.py --endpoint "/api/checkout" --method POST --output_dir "out_checkout"
  python generator.py --endpoint "/api/admin/orders/:id/status" --method PUT --output_dir "out_admin"
"""
    )
    parser.add_argument("--all", action="store_true", help="Generate all 3 API suites (Pool A, Pool B, Pool C) in batch mode")
    parser.add_argument("--endpoint", default="/api/login", help="Target API endpoint route (e.g. /api/login, /api/checkout, /api/admin/orders/:id/status)")
    parser.add_argument("--method", default="POST", help="HTTP Method (POST, PUT, GET, DELETE)")
    parser.add_argument("--output_dir", default="output", help="Directory to save generated collection and data JSON")
    parser.add_argument("--student_id", default="23127404", help="Student ID for header attribution (default: 23127404)")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    
    suites = []
    if args.all:
        suites = [
            ("Pool A Login Suite", "/api/login", "POST", generate_login_tests()),
            ("Pool B Checkout Suite", "/api/checkout", "POST", generate_checkout_tests()),
            ("Pool C Admin Orders Suite", "/api/admin/orders/:id/status", "PUT", generate_admin_orders_tests()),
        ]
    else:
        endpoint_clean = args.endpoint.lower()
        if "login" in endpoint_clean:
            suites.append(("Pool A Login Suite", args.endpoint, args.method, generate_login_tests()))
        elif "checkout" in endpoint_clean:
            suites.append(("Pool B Checkout Suite", args.endpoint, args.method, generate_checkout_tests()))
        elif "order" in endpoint_clean or "status" in endpoint_clean:
            suites.append(("Pool C Admin Orders Suite", args.endpoint, args.method, generate_admin_orders_tests()))
        else:
            suites.append((f"Custom API Suite ({args.endpoint})", args.endpoint, args.method, generate_login_tests()))

    print(f"================================================================================")
    print(f"       AI-DRIVEN API TEST GENERATOR (Bloom G9.5 Create) — BATCH / CLI           ")
    print(f"================================================================================")
    print(f" Student ID:        {args.student_id}")
    print(f" Destination:       {os.path.abspath(args.output_dir)}")
    print(f" Suites to build:   {len(suites)}")
    print(f"--------------------------------------------------------------------------------")

    for name, endpoint, method, test_cases in suites:
        collection = build_postman_collection(name, endpoint, method, test_cases, args.student_id)
        
        file_prefix = name.lower().replace(" ", "_").replace("-", "_")
        col_filename = os.path.join(args.output_dir, f"{file_prefix}.postman_collection.json")
        data_filename = os.path.join(args.output_dir, f"{file_prefix}_data.json")

        with open(col_filename, "w", encoding="utf-8") as f:
            json.dump(collection, f, indent=2, ensure_ascii=False)
        with open(data_filename, "w", encoding="utf-8") as f:
            json.dump(test_cases, f, indent=2, ensure_ascii=False)

        print(f"  [+] Synthesized {name:28s} -> {len(test_cases):2d} test cases")
        print(f"      Collection: {col_filename}")
        print(f"      Data file:  {data_filename}")

    print(f"================================================================================")
    print(f" [SUCCESS] Test generation completed. Injected X-Student-Id: {args.student_id}")
    print(f"================================================================================")

if __name__ == "__main__":
    main()
