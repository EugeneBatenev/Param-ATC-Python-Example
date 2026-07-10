import json
import os
import random
from datetime import datetime

import allure
import pytest

RESULTS_DIR = "allure-results"
os.makedirs(RESULTS_DIR, exist_ok=True)


@pytest.fixture(scope="module")
def setup_environment():
    print("Setting up the test environment.")
    yield
    print("Tearing down the test environment.")


def generate_mock_result(test_name, test_input, expected_output):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    json_result = {
        "test_name": test_name,
        "test_input": test_input,
        "expected_output": expected_output,
        "status": "passed",
        "timestamp": timestamp,
    }

    json_file_path = os.path.join(RESULTS_DIR, f"{test_name}_{test_input}.json")
    with open(json_file_path, "w") as json_file:
        json.dump(json_result, json_file, indent=4)

    text_file_path = os.path.join(RESULTS_DIR, f"{test_name}_{test_input}.txt")
    with open(text_file_path, "w") as text_file:
        text_file.write(f"Test Name: {test_name}\n")
        text_file.write(f"Test Input: {test_input}\n")
        text_file.write(f"Expected Output: {expected_output}\n")
        text_file.write("Status: passed\n")
        text_file.write(f"Timestamp: {timestamp}\n")

    allure.attach.file(
        json_file_path,
        name=f"{test_name} JSON result",
        attachment_type=allure.attachment_type.JSON,
    )

    allure.attach.file(
        text_file_path,
        name=f"{test_name} text result",
        attachment_type=allure.attachment_type.TEXT,
    )

    assert os.path.exists(json_file_path)
    assert os.path.exists(text_file_path)


def maybe_fail():
    if random.random() < 0.25:
        pytest.fail("Random mock failure for Allure Report testing")


@allure.label("jira", "AE-2")
def test_generate_user_result(setup_environment):
    generate_mock_result("test_generate_user_result", "user_input", "user_output")
    maybe_fail()


@allure.label("jira", "BPDND-2")
def test_generate_order_result(setup_environment):
    generate_mock_result("test_generate_order_result", "order_input", "order_output")
    maybe_fail()


@allure.label("jira", "BPDND-3")
def test_generate_payment_result(setup_environment):
    generate_mock_result("test_generate_payment_result", "payment_input", "payment_output")
    maybe_fail()


@allure.label("jira", "BPDND-4")
def test_generate_invoice_result(setup_environment):
    generate_mock_result("test_generate_invoice_result", "invoice_input", "invoice_output")
    maybe_fail()


@allure.label("jira", "BPDND-5")
def test_generate_notification_result(setup_environment):
    generate_mock_result("test_generate_notification_result", "notification_input", "notification_output")
    maybe_fail()
