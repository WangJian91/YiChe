# -*- coding: utf-8 -*-

from ConversationTree.Common.parameterize_util import read_case
from ConversationTree.Common import parameterize_util
from ConversationTree.Common.requests_util import RequestsUtil
import allure
import pytest


@pytest.fixture(scope='class')
@allure.story("用户接入")
def connection31():
    data = read_case('./TestCases/31/connection31.yaml')[0]
    RequestsUtil(parameterize_util).standard_yaml(data)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-01')
class TestConversationTreeWw01:
    """王伟外呼"""

    @allure.story("第1流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_1_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_1_flow(self, case_info):
        """1-1-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-02')
class TestConversationTreeWw02:
    @allure.story("第2流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_2_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_2_flow(self, case_info):
        """1-1-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-03')
class TestConversationTreeWw03:
    @allure.story("第3流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_3_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_3_flow(self, case_info):
        """1-1-4-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-04')
class TestConversationTreeWw04:
    @allure.story("第4流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_4_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_4_flow(self, case_info):
        """1-1-4-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-05')
class TestConversationTreeWw05:
    @allure.story("第5流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_5_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_5_flow(self, case_info):
        """1-1-4-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-06')
class TestConversationTreeWw06:
    @allure.story("第6流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_6_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_6_flow(self, case_info):
        """1-1-4-4-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-07')
class TestConversationTreeWw07:
    @allure.story("第7流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_7_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_7_flow(self, case_info):
        """1-1-4-4-2-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-08')
class TestConversationTreeWw08:
    @allure.story("第8流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_8_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_8_flow(self, case_info):
        """1-1-4-4-2-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-09')
class TestConversationTreeWw09:
    @allure.story("第9流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_9_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_9_flow(self, case_info):
        """1-1-4-4-2-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-10')
class TestConversationTreeWw10:
    @allure.story("第10流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_10_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_10_flow(self, case_info):
        """1-1-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-11')
class TestConversationTreeWw11:
    @allure.story("第11流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_11_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_11_flow(self, case_info):
        """1-1-4-4-2-4-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-12')
class TestConversationTreeWw12:
    @allure.story("第12流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_12_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_12_flow(self, case_info):
        """1-1-4-4-2-4-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-13')
class TestConversationTreeWw13:
    @allure.story("第13流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_13_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_13_flow(self, case_info):
        """1-1-4-4-2-4-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-14')
class TestConversationTreeWw14:
    @allure.story("第14流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_14_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_14_flow(self, case_info):
        """1-1-4-4-2-4-4"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-15')
class TestConversationTreeWw15:
    @allure.story("第15流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_15_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_15_flow(self, case_info):
        """1-1-4-4-3-1-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-16')
class TestConversationTreeWw16:
    @allure.story("第16流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_16_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_16_flow(self, case_info):
        """1-1-4-4-3-1-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-17')
class TestConversationTreeWw17:
    @allure.story("第17流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_17_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_17_flow(self, case_info):
        """1-1-4-4-3-1-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-18')
class TestConversationTreeWw18:
    @allure.story("第18流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_18_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_18_flow(self, case_info):
        """1-1-4-4-3-1-4-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-19')
class TestConversationTreeWw19:
    @allure.story("第19流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_19_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_19_flow(self, case_info):
        """1-1-4-4-3-1-4-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-20')
class TestConversationTreeWw20:
    @allure.story("第20流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_20_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_20_flow(self, case_info):
        """1-1-4-4-3-1-4-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-21')
class TestConversationTreeWw21:
    @allure.story("第21流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_21_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_21_flow(self, case_info):
        """1-1-4-4-3-1-4-4"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-22')
class TestConversationTreeWw22:
    @allure.story("第22流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_22_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_22_flow(self, case_info):
        """1-1-4-4-3-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-23')
class TestConversationTreeWw23:
    @allure.story("第23流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_23_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_23_flow(self, case_info):
        """1-1-4-4-3-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-24')
class TestConversationTreeWw24:
    @allure.story("第24流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_24_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_24_flow(self, case_info):
        """1-1-4-5-1-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-25')
class TestConversationTreeWw25:
    @allure.story("第25流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_25_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_25_flow(self, case_info):
        """1-1-4-5-1-2-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-26')
class TestConversationTreeWw26:
    @allure.story("第26流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_26_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_26_flow(self, case_info):
        """1-1-4-5-1-2-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-27')
class TestConversationTreeWw27:
    @allure.story("第27流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_27_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_27_flow(self, case_info):
        """1-1-4-5-1-2-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-28')
class TestConversationTreeWw28:
    @allure.story("第28流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_28_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_28_flow(self, case_info):
        """1-1-4-5-1-2-4-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-29')
class TestConversationTreeWw29:
    @allure.story("第29流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_29_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_29_flow(self, case_info):
        """1-1-4-5-1-2-4-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-30')
class TestConversationTreeWw30:
    @allure.story("第30流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_30_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_30_flow(self, case_info):
        """1-1-4-5-1-2-4-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-31')
class TestConversationTreeWw31:
    @allure.story("第31流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_31_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_31_flow(self, case_info):
        """1-1-4-5-1-2-4-4"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-32')
class TestConversationTreeWw32:
    @allure.story("第32流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_32_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_32_flow(self, case_info):
        """1-1-4-5-1-3-1-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-33')
class TestConversationTreeWw33:
    @allure.story("第33流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_33_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_33_flow(self, case_info):
        """1-1-4-5-1-3-1-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-34')
class TestConversationTreeWw34:
    @allure.story("第34流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_34_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_34_flow(self, case_info):
        """1-1-4-5-1-3-1-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-35')
class TestConversationTreeWw35:
    @allure.story("第35流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_35_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_35_flow(self, case_info):
        """1-1-4-5-1-3-1-4-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-36')
class TestConversationTreeWw36:
    @allure.story("第36流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_36_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_36_flow(self, case_info):
        """1-1-4-5-1-3-1-4-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-37')
class TestConversationTreeWw37:
    @allure.story("第37流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_37_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_37_flow(self, case_info):
        """1-1-4-5-1-3-1-4-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-38')
class TestConversationTreeWw38:
    @allure.story("第38流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_38_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_38_flow(self, case_info):
        """1-1-4-5-1-3-1-4-4"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-39')
class TestConversationTreeWw39:
    @allure.story("第39流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_39_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_39_flow(self, case_info):
        """1-1-4-5-1-3-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-40')
class TestConversationTreeWw40:
    @allure.story("第40流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_40_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_40_flow(self, case_info):
        """1-1-4-5-1-3-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-41')
class TestConversationTreeWw41:
    @allure.story("第41流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_41_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_41_flow(self, case_info):
        """1-1-4-5-2-1-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-42')
class TestConversationTreeWw42:
    @allure.story("第42流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_42_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_42_flow(self, case_info):
        """1-1-4-5-2-1-2-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-43')
class TestConversationTreeWw43:
    @allure.story("第43流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_43_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_43_flow(self, case_info):
        """1-1-4-5-2-1-2-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-44')
class TestConversationTreeWw44:
    @allure.story("第44流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_44_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_44_flow(self, case_info):
        """1-1-4-5-2-1-2-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-45')
class TestConversationTreeWw45:
    @allure.story("第45流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_45_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_45_flow(self, case_info):
        """1-1-4-5-2-1-2-4-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-46')
class TestConversationTreeWw46:
    @allure.story("第46流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_46_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_46_flow(self, case_info):
        """1-1-4-5-2-1-2-4-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-47')
class TestConversationTreeWw47:
    @allure.story("第47流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_47_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_47_flow(self, case_info):
        """1-1-4-5-2-1-2-4-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-48')
class TestConversationTreeWw48:
    @allure.story("第48流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_48_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_48_flow(self, case_info):
        """1-1-4-5-2-1-2-4-4"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-49')
class TestConversationTreeWw49:
    @allure.story("第49流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_49_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_49_flow(self, case_info):
        """1-1-4-5-2-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-50')
class TestConversationTreeWw50:
    @allure.story("第50流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_50_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_50_flow(self, case_info):
        """1-1-4-5-2-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-51')
class TestConversationTreeWw51:
    @allure.story("第51流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_51_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_51_flow(self, case_info):
        """1-1-4-5-4"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-52')
class TestConversationTreeWw52:
    @allure.story("第52流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_52_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_52_flow(self, case_info):
        """1-1-4-6-1-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-53')
class TestConversationTreeWw53:
    @allure.story("第53流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_53_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_53_flow(self, case_info):
        """1-1-4-6-1-2-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-54')
class TestConversationTreeWw54:
    @allure.story("第54流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_54_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_54_flow(self, case_info):
        """1-1-4-6-1-2-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-55')
class TestConversationTreeWw55:
    @allure.story("第55流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_55_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_55_flow(self, case_info):
        """1-1-4-6-1-2-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-56')
class TestConversationTreeWw56:
    @allure.story("第56流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_56_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_56_flow(self, case_info):
        """1-1-4-6-1-2-4-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-57')
class TestConversationTreeWw57:
    @allure.story("第57流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_57_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_57_flow(self, case_info):
        """1-1-4-6-1-2-4-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-58')
class TestConversationTreeWw58:
    @allure.story("第58流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_58_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_58_flow(self, case_info):
        """1-1-4-6-1-2-4-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-59')
class TestConversationTreeWw59:
    @allure.story("第59流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_59_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_59_flow(self, case_info):
        """1-1-4-6-1-2-4-4"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-60')
class TestConversationTreeWw60:
    @allure.story("第60流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_60_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_60_flow(self, case_info):
        """1-1-4-6-1-3-1-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-61')
class TestConversationTreeWw61:
    @allure.story("第61流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_61_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_61_flow(self, case_info):
        """1-1-4-6-1-3-1-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-62')
class TestConversationTreeWw62:
    @allure.story("第62流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_62_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_62_flow(self, case_info):
        """1-1-4-6-1-3-1-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-63')
class TestConversationTreeWw63:
    @allure.story("第63流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_63_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_63_flow(self, case_info):
        """1-1-4-6-1-3-1-4-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-64')
class TestConversationTreeWw64:
    @allure.story("第64流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_64_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_64_flow(self, case_info):
        """1-1-4-6-1-3-1-4-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-65')
class TestConversationTreeWw65:
    @allure.story("第65流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_65_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_65_flow(self, case_info):
        """1-1-4-6-1-3-1-4-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-66')
class TestConversationTreeWw66:
    @allure.story("第66流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_66_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_66_flow(self, case_info):
        """1-1-4-6-1-3-1-4-4"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-67')
class TestConversationTreeWw67:
    @allure.story("第67流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_67_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_67_flow(self, case_info):
        """1-1-4-6-1-3-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-68')
class TestConversationTreeWw68:
    @allure.story("第68流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_68_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_68_flow(self, case_info):
        """1-1-4-6-1-3-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-69')
class TestConversationTreeWw69:
    @allure.story("第69流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_69_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_69_flow(self, case_info):
        """1-1-4-6-2-1-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-70')
class TestConversationTreeWw70:
    @allure.story("第70流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_70_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_70_flow(self, case_info):
        """1-1-4-6-2-1-2-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-71')
class TestConversationTreeWw71:
    @allure.story("第71流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_71_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_71_flow(self, case_info):
        """1-1-4-6-2-1-2-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-72')
class TestConversationTreeWw72:
    @allure.story("第72流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_72_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_72_flow(self, case_info):
        """1-1-4-6-2-1-2-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-73')
class TestConversationTreeWw73:
    @allure.story("第73流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_73_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_73_flow(self, case_info):
        """1-1-4-6-2-1-2-4-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-74')
class TestConversationTreeWw74:
    @allure.story("第74流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_74_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_74_flow(self, case_info):
        """1-1-4-6-2-1-2-4-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-75')
class TestConversationTreeWw75:
    @allure.story("第75流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_75_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_75_flow(self, case_info):
        """1-1-4-6-2-1-2-4-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-76')
class TestConversationTreeWw76:
    @allure.story("第76流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_76_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_76_flow(self, case_info):
        """1-1-4-6-2-1-2-4-4"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-77')
class TestConversationTreeWw77:
    @allure.story("第77流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_77_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_77_flow(self, case_info):
        """1-1-4-6-2-1-3-1-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-78')
class TestConversationTreeWw78:
    @allure.story("第78流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_78_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_78_flow(self, case_info):
        """1-1-4-6-2-1-3-1-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-79')
class TestConversationTreeWw79:
    @allure.story("第79流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_79_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_79_flow(self, case_info):
        """1-1-4-6-2-1-3-1-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-80')
class TestConversationTreeWw80:
    @allure.story("第80流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_80_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_80_flow(self, case_info):
        """1-1-4-6-2-1-3-1-4-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-81')
class TestConversationTreeWw81:
    @allure.story("第81流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_81_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_81_flow(self, case_info):
        """1-1-4-6-2-1-3-1-4-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-82')
class TestConversationTreeWw82:
    @allure.story("第82流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_82_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_82_flow(self, case_info):
        """1-1-4-6-2-1-3-1-4-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-83')
class TestConversationTreeWw83:
    @allure.story("第83流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_83_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_83_flow(self, case_info):
        """1-1-4-6-2-1-3-1-4-4"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-84')
class TestConversationTreeWw84:
    @allure.story("第84流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_84_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_84_flow(self, case_info):
        """1-1-4-6-2-1-3-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-85')
class TestConversationTreeWw85:
    @allure.story("第85流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_85_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_85_flow(self, case_info):
        """1-1-4-6-2-1-3-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-86')
class TestConversationTreeWw86:
    @allure.story("第86流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_86_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_86_flow(self, case_info):
        """1-1-4-6-2-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-87')
class TestConversationTreeWw87:
    @allure.story("第87流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_87_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_87_flow(self, case_info):
        """1-1-4-6-2-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-88')
class TestConversationTreeWw88:
    @allure.story("第88流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_88_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_88_flow(self, case_info):
        """1-1-4-6-4"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-89')
class TestConversationTreeWw89:
    @allure.story("第89流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_89_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_89_flow(self, case_info):
        """1-1-4-7-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-90')
class TestConversationTreeWw90:
    @allure.story("第90流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_90_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_90_flow(self, case_info):
        """1-1-5"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-91')
class TestConversationTreeWw91:
    @allure.story("第91流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_91_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_91_flow(self, case_info):
        """1-1-7"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-92')
class TestConversationTreeWw92:
    @allure.story("第92流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_92_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_92_flow(self, case_info):
        """1-1-8"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-93')
class TestConversationTreeWw93:
    @allure.story("第93流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_93_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_93_flow(self, case_info):
        """1-1-9"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-94')
class TestConversationTreeWw94:
    @allure.story("第94流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_94_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_94_flow(self, case_info):
        """1-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-95')
class TestConversationTreeWw95:
    @allure.story("第95流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_95_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_95_flow(self, case_info):
        """1-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-96')
class TestConversationTreeWw96:
    @allure.story("第96流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_96_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_96_flow(self, case_info):
        """1-4"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-97')
class TestConversationTreeWw97:
    @allure.story("第97流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_97_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_97_flow(self, case_info):
        """1-5"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-98')
class TestConversationTreeWw98:
    @allure.story("第98流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_98_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_98_flow(self, case_info):
        """1-6"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-99')
class TestConversationTreeWw99:
    @allure.story("第99流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_99_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_99_flow(self, case_info):
        """1-7"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-100')
class TestConversationTreeWw100:
    @allure.story("第100流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_100_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_100_flow(self, case_info):
        """1-9"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-101')
class TestConversationTreeWw101:
    @allure.story("第101流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_101_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_101_flow(self, case_info):
        """1-10"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-102')
class TestConversationTreeWw102:
    @allure.story("第102流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_102_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_102_flow(self, case_info):
        """1-11"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection31")
@allure.feature('测试对话树31-103')
class TestConversationTreeWw103:
    @allure.story("第103流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/31/test_31_103_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t31
    def test_31_103_flow(self, case_info):
        """2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)
