# -*- coding: utf-8 -*-

from IMRobot.Common.parameterize_util import read_case
from IMRobot.Common import parameterize_util
from IMRobot.Common.requests_util import RequestsUtil
import allure
import pytest


# @allure.feature('测试对话树2112-01')
# class TestConversationTreeXj01:
#     @allure.story("第1流程")
#     @pytest.mark.parametrize('case_info', read_case('/TestCases/test1.yaml'))
#     @pytest.mark.debug
#     def test_2112_1_flow(self, case_info):
#         """1-1"""
#         RequestsUtil(parameterize_util).standard_yaml(case_info)


# @allure.feature('测试对话树2112-01')
# @allure.story("第1流程")
# @pytest.mark.parametrize('case_info', read_case('/TestCases/test1.yaml'))
# @pytest.mark.debug
# def test_2112_1_flow(case_info):
#     """1-1"""
#     RequestsUtil(parameterize_util).standard_yaml(case_info)


@allure.feature('测试对话树2112-01')
@allure.story("第1流程")
@pytest.mark.parametrize('case_info', read_case('/TestCases/test1.yaml'))
@pytest.mark.debug
@pytest.mark.asyncio
async def test_2112_1_flow(case_info):
    """1-1"""
    RequestsUtil(parameterize_util).standard_yaml(case_info)
