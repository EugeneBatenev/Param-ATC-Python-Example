import json
import os


import allure
from datetime import datetime
import pytest
from allure import attachment_type
from allure_commons.types import Severity
RESULTS_DIR = "allure-results"
os.makedirs(RESULTS_DIR, exist_ok=True)

@allure.id("484711")

@pytest.fixture(scope="module")
def setup_environment():
    print("Setting up the test environment.")
    yield
    print("Tearing down the test environment.")

@pytest.mark.parametrize("test_input, expected_output", [
    ("input1", "output1"),
    ("input2", "output2"),
    ("input3", "output"),
])
@allure.label("jira", "BPDND-1")
def test_generate_result_files(setup_environment, test_input, expected_output):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    # Генерация JSON результата
    json_result = {
        "test_input": test_input,
        "expected_output": expected_output,
        "status": "passed",
        "timestamp": timestamp
    }

    json_file_path = os.path.join(RESULTS_DIR, f"result_{test_input}.json")
    with open(json_file_path, "w") as json_file:
        json.dump(json_result, json_file, indent=4)

    # Генерация текстового результата
    text_file_path = os.path.join(RESULTS_DIR, f"result_{test_input}.txt")
    with open(text_file_path, "w") as text_file:
        text_file.write(f"Test Input: {test_input}\n")
        text_file.write(f"Expected Output: {expected_output}\n")
        text_file.write(f"Status: passed\n")
        text_file.write(f"Timestamp: {timestamp}\n")

    # Проверка, что файлы созданы
    assert os.path.exists(json_file_path)
    assert os.path.exists(text_file_path)












