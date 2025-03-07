# SPDX-FileCopyrightText: (c) 2025 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0

from typing import Callable

import pytest
from infra import RunMode
from utils import compile_fail, record_model_test_properties

from ..tester import BloomTester

MODEL_PATH = "bigscience/bloom-3b"
MODEL_NAME = "bloom-3b"


# ----- Fixtures -----


@pytest.fixture
def inference_tester() -> BloomTester:
    return BloomTester(MODEL_PATH)


@pytest.fixture
def training_tester() -> BloomTester:
    return BloomTester(MODEL_PATH, run_mode=RunMode.TRAINING)


# ----- Tests -----


@pytest.mark.model_test
@pytest.mark.skip(reason=compile_fail("Unsupported data type"))  # segfault
def test_bloom_3b_inference(
    inference_tester: BloomTester,
    record_tt_xla_property: Callable,
):
    record_model_test_properties(record_tt_xla_property, MODEL_NAME)

    inference_tester.test()


@pytest.mark.model_test
@pytest.mark.skip(reason="Support for training not implemented")
def test_bloom_3b_training(
    training_tester: BloomTester,
    record_tt_xla_property: Callable,
):
    record_model_test_properties(record_tt_xla_property, MODEL_NAME)

    training_tester.test()
