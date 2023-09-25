# -*- coding: utf-8 -*-

from ConversationTree.Common.parameterize_util import read_case
from ConversationTree.Common import parameterize_util
from ConversationTree.Common.requests_util import RequestsUtil
import allure
import pytest


@pytest.fixture(scope='class')
@allure.story("用户接入")
def connection2112():
    data = read_case('./TestCases/2112/connection2112.yaml')[0]
    RequestsUtil(parameterize_util).standard_yaml(data)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-01')
class TestConversationTreeXj01:
    """Q1"""
    @allure.story("第1流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_1_flow.yaml'))
<<<<<<< HEAD
    @pytest.mark.debug
=======
    @pytest.mark.all
>>>>>>> 9994d9dd41a8e38ef027d55d24b2a205292cfbf4
    @pytest.mark.t2112
    def test_2112_1_flow(self, case_info):
        """1-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-02')
class TestConversationTreeXj02:
    @allure.story("第2流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_2_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_2_flow(self, case_info):
        """1-2-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-03')
class TestConversationTreeXj03:
    @allure.story("第3流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_3_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_3_flow(self, case_info):
        """1-2-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-04')
class TestConversationTreeXj04:
    @allure.story("第4流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_4_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_4_flow(self, case_info):
        """1-2-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-05')
class TestConversationTreeXj05:
    @allure.story("第5流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_5_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_5_flow(self, case_info):
        """1-2-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-06')
class TestConversationTreeXj06:
    @allure.story("第6流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_6_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_6_flow(self, case_info):
        """1-2-4"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-07')
class TestConversationTreeXj07:
    @allure.story("第7流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_7_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_7_flow(self, case_info):
        """1-2-5"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-08')
class TestConversationTreeXj08:
    @allure.story("第8流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_8_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_8_flow(self, case_info):
        """1-2-6"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-09')
class TestConversationTreeXj09:
    @allure.story("第9流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_9_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_9_flow(self, case_info):
        """1-2-7"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-10')
class TestConversationTreeXj10:
    @allure.story("第10流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_10_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_10_flow(self, case_info):
        """1-2-8"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-11')
class TestConversationTreeXj11:
    @allure.story("第11流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_11_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_11_flow(self, case_info):
        """1-2-9"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-12')
class TestConversationTreeXj12:
    @allure.story("第12流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_12_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_12_flow(self, case_info):
        """1-2-10"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-13')
class TestConversationTreeXj13:
    @allure.story("第13流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_13_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_13_flow(self, case_info):
        """1-2-11"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-14')
class TestConversationTreeXj14:
    @allure.story("第14流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_14_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_14_flow(self, case_info):
        """1-2-12"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-15')
class TestConversationTreeXj15:
    @allure.story("第15流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_15_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_15_flow(self, case_info):
        """1-2-13"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-16')
class TestConversationTreeXj16:
    @allure.story("第16流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_16_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_16_flow(self, case_info):
        """1-2-14"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-17')
class TestConversationTreeXj17:
    @allure.story("第17流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_17_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_17_flow(self, case_info):
        """1-2-15"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-18')
class TestConversationTreeXj18:
    @allure.story("第18流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_18_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_18_flow(self, case_info):
        """1-2-16"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-19')
class TestConversationTreeXj19:
    @allure.story("第19流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_19_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_19_flow(self, case_info):
        """1-2-17"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-221')
class TestConversationTreeXj221:
    @allure.story("第221流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_221_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_221_flow(self, case_info):
        """1-2-18"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-222')
class TestConversationTreeXj222:
    @allure.story("第222流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_222_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_222_flow(self, case_info):
        """1-2-19"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-223')
class TestConversationTreeXj223:
    @allure.story("第223流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_223_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_223_flow(self, case_info):
        """1-2-20"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-224')
class TestConversationTreeXj224:
    @allure.story("第224流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_224_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_224_flow(self, case_info):
        """1-2-21"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-225')
class TestConversationTreeXj225:
    @allure.story("第225流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_225_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_225_flow(self, case_info):
        """1-2-22"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-226')
class TestConversationTreeXj226:
    @allure.story("第226流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_226_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_226_flow(self, case_info):
        """1-2-23"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-227')
class TestConversationTreeXj227:
    @allure.story("第227流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_227_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_227_flow(self, case_info):
        """1-2-24"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-20')
class TestConversationTreeXj20:
    @allure.story("第20流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_20_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_20_flow(self, case_info):
        """1-3-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-21')
class TestConversationTreeXj21:
    @allure.story("第21流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_21_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_21_flow(self, case_info):
        """1-3-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-22')
class TestConversationTreeXj22:
    @allure.story("第22流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_22_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_22_flow(self, case_info):
        """1-3-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-23')
class TestConversationTreeXj23:
    @allure.story("第23流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_23_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_23_flow(self, case_info):
        """1-3-4"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-24')
class TestConversationTreeXj24:
    @allure.story("第24流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_24_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_24_flow(self, case_info):
        """1-3-5"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-25')
class TestConversationTreeXj25:
    @allure.story("第25流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_25_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_25_flow(self, case_info):
        """1-3-6"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-26')
class TestConversationTreeXj26:
    @allure.story("第26流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_26_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_26_flow(self, case_info):
        """1-3-7"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-27')
class TestConversationTreeXj27:
    @allure.story("第27流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_27_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_27_flow(self, case_info):
        """1-3-8"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-28')
class TestConversationTreeXj28:
    @allure.story("第28流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_28_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_28_flow(self, case_info):
        """1-3-9"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-29')
class TestConversationTreeXj29:
    @allure.story("第29流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_29_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_29_flow(self, case_info):
        """1-3-10"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-30')
class TestConversationTreeXj30:
    @allure.story("第30流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_30_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_30_flow(self, case_info):
        """1-3-11"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-31')
class TestConversationTreeXj31:
    @allure.story("第31流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_31_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_31_flow(self, case_info):
        """1-3-12"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-32')
class TestConversationTreeXj32:
    @allure.story("第32流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_32_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_32_flow(self, case_info):
        """1-3-13"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-33')
class TestConversationTreeXj33:
    @allure.story("第33流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_33_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_33_flow(self, case_info):
        """1-3-14"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-34')
class TestConversationTreeXj34:
    @allure.story("第34流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_34_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_34_flow(self, case_info):
        """1-3-15"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-35')
class TestConversationTreeXj35:
    @allure.story("第35流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_35_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_35_flow(self, case_info):
        """1-3-16"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-36')
class TestConversationTreeXj36:
    @allure.story("第36流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_36_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_36_flow(self, case_info):
        """1-3-17"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-350')
class TestConversationTreeXj350:
    @allure.story("第350流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_350_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_350_flow(self, case_info):
        """1-3-18"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-351')
class TestConversationTreeXj351:
    @allure.story("第351流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_351_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_351_flow(self, case_info):
        """1-3-19"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-352')
class TestConversationTreeXj352:
    @allure.story("第352流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_352_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_352_flow(self, case_info):
        """1-3-20"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-353')
class TestConversationTreeXj353:
    @allure.story("第353流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_353_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_353_flow(self, case_info):
        """1-3-21"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-354')
class TestConversationTreeXj354:
    @allure.story("第354流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_354_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_354_flow(self, case_info):
        """1-3-22"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-355')
class TestConversationTreeXj355:
    @allure.story("第355流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_355_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_355_flow(self, case_info):
        """1-3-23"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-356')
class TestConversationTreeXj356:
    @allure.story("第356流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_356_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_356_flow(self, case_info):
        """1-3-24"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-37')
class TestConversationTreeXj37:
    @allure.story("第37流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_37_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_37_flow(self, case_info):
        """1-4"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-38')
class TestConversationTreeXj38:
    @allure.story("第38流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_38_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_38_flow(self, case_info):
        """1-5"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-39')
class TestConversationTreeXj39:
    @allure.story("第39流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_39_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_39_flow(self, case_info):
        """1-6"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-40')
class TestConversationTreeXj40:
    @allure.story("第40流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_40_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_40_flow(self, case_info):
        """1-7"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-41')
class TestConversationTreeXj41:
    @allure.story("第41流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_41_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_41_flow(self, case_info):
        """1-8"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-42')
class TestConversationTreeXj42:
    @allure.story("第42流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_42_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_42_flow(self, case_info):
        """1-9-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-43')
class TestConversationTreeXj43:
    @allure.story("第43流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_43_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_43_flow(self, case_info):
        """1-9-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-44')
class TestConversationTreeXj44:
    @allure.story("第44流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_44_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_44_flow(self, case_info):
        """1-9-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-45')
class TestConversationTreeXj45:
    @allure.story("第45流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_45_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_45_flow(self, case_info):
        """1-9-4"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-46')
class TestConversationTreeXj46:
    @allure.story("第46流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_46_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_46_flow(self, case_info):
        """1-9-5"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-47')
class TestConversationTreeXj47:
    @allure.story("第47流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_47_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_47_flow(self, case_info):
        """1-9-6"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-48')
class TestConversationTreeXj48:
    @allure.story("第48流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_48_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_48_flow(self, case_info):
        """1-9-7"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-49')
class TestConversationTreeXj49:
    @allure.story("第49流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_49_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_49_flow(self, case_info):
        """1-9-8"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-50')
class TestConversationTreeXj50:
    @allure.story("第50流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_50_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_50_flow(self, case_info):
        """1-9-9"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-51')
class TestConversationTreeXj51:
    @allure.story("第51流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_51_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_51_flow(self, case_info):
        """1-9-10"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-52')
class TestConversationTreeXj52:
    @allure.story("第52流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_52_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_52_flow(self, case_info):
        """1-9-11"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-53')
class TestConversationTreeXj53:
    @allure.story("第53流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_53_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_53_flow(self, case_info):
        """1-9-12"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-54')
class TestConversationTreeXj54:
    @allure.story("第54流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_54_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_54_flow(self, case_info):
        """1-9-13"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-55')
class TestConversationTreeXj55:
    @allure.story("第55流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_55_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_55_flow(self, case_info):
        """1-9-14"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-56')
class TestConversationTreeXj56:
    @allure.story("第56流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_56_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_56_flow(self, case_info):
        """1-9-15"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-57')
class TestConversationTreeXj57:
    @allure.story("第57流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_57_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_57_flow(self, case_info):
        """1-9-16"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-58')
class TestConversationTreeXj58:
    @allure.story("第58流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_58_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_58_flow(self, case_info):
        """1-9-17"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-228')
class TestConversationTreeXj228:
    @allure.story("第228流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_228_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_228_flow(self, case_info):
        """1-9-18"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-229')
class TestConversationTreeXj229:
    @allure.story("第229流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_229_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_229_flow(self, case_info):
        """1-9-19"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-230')
class TestConversationTreeXj230:
    @allure.story("第230流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_230_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_230_flow(self, case_info):
        """1-9-20"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-231')
class TestConversationTreeXj231:
    @allure.story("第231流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_231_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_231_flow(self, case_info):
        """1-9-21"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-232')
class TestConversationTreeXj232:
    @allure.story("第232流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_232_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_232_flow(self, case_info):
        """1-9-22"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-233')
class TestConversationTreeXj233:
    @allure.story("第233流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_233_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_233_flow(self, case_info):
        """1-9-23"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-234')
class TestConversationTreeXj234:
    @allure.story("第234流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_234_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_234_flow(self, case_info):
        """1-9-24"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-59')
class TestConversationTreeXj59:
    @allure.story("第59流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_59_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_59_flow(self, case_info):
        """1-10-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-60')
class TestConversationTreeXj60:
    @allure.story("第60流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_60_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_60_flow(self, case_info):
        """1-10-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-61')
class TestConversationTreeXj61:
    @allure.story("第61流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_61_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_61_flow(self, case_info):
        """1-10-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-62')
class TestConversationTreeXj62:
    @allure.story("第62流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_62_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_62_flow(self, case_info):
        """1-10-4"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-63')
class TestConversationTreeXj63:
    @allure.story("第63流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_63_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_63_flow(self, case_info):
        """1-10-5"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-64')
class TestConversationTreeXj64:
    @allure.story("第64流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_64_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_64_flow(self, case_info):
        """1-10-6"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-65')
class TestConversationTreeXj65:
    @allure.story("第65流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_65_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_65_flow(self, case_info):
        """1-10-7"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-66')
class TestConversationTreeXj66:
    @allure.story("第66流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_66_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_66_flow(self, case_info):
        """1-10-8"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-67')
class TestConversationTreeXj67:
    @allure.story("第67流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_67_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_67_flow(self, case_info):
        """1-10-9"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-68')
class TestConversationTreeXj68:
    @allure.story("第68流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_68_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_68_flow(self, case_info):
        """1-10-10"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-69')
class TestConversationTreeXj69:
    @allure.story("第69流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_69_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_69_flow(self, case_info):
        """1-10-11"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-70')
class TestConversationTreeXj70:
    @allure.story("第70流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_70_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_70_flow(self, case_info):
        """1-10-12"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-71')
class TestConversationTreeXj71:
    @allure.story("第71流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_71_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_71_flow(self, case_info):
        """1-10-13"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-72')
class TestConversationTreeXj72:
    @allure.story("第72流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_72_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_72_flow(self, case_info):
        """1-10-14"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-73')
class TestConversationTreeXj73:
    @allure.story("第73流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_73_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_73_flow(self, case_info):
        """1-10-15"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-74')
class TestConversationTreeXj74:
    @allure.story("第74流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_74_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_74_flow(self, case_info):
        """1-10-16"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-75')
class TestConversationTreeXj75:
    @allure.story("第75流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_75_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_75_flow(self, case_info):
        """1-10-17"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-235')
class TestConversationTreeXj235:
    @allure.story("第235流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_235_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_235_flow(self, case_info):
        """1-10-18"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-236')
class TestConversationTreeXj236:
    @allure.story("第236流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_236_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_236_flow(self, case_info):
        """1-10-19"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-237')
class TestConversationTreeXj237:
    @allure.story("第237流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_237_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_237_flow(self, case_info):
        """1-10-20"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-238')
class TestConversationTreeXj238:
    @allure.story("第238流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_238_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_238_flow(self, case_info):
        """1-10-21"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-239')
class TestConversationTreeXj239:
    @allure.story("第239流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_239_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_239_flow(self, case_info):
        """1-10-22"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-240')
class TestConversationTreeXj240:
    @allure.story("第240流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_240_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_240_flow(self, case_info):
        """1-10-23"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-241')
class TestConversationTreeXj241:
    @allure.story("第241流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_241_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_241_flow(self, case_info):
        """1-10-24"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-76')
class TestConversationTreeXj76:
    @allure.story("第76流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_76_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_76_flow(self, case_info):
        """1-11-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-77')
class TestConversationTreeXj77:
    @allure.story("第77流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_77_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_77_flow(self, case_info):
        """1-11-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-78')
class TestConversationTreeXj78:
    @allure.story("第78流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_78_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_78_flow(self, case_info):
        """1-11-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-79')
class TestConversationTreeXj79:
    @allure.story("第79流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_79_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_79_flow(self, case_info):
        """1-11-4"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-80')
class TestConversationTreeXj80:
    @allure.story("第80流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_80_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_80_flow(self, case_info):
        """1-11-5"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-81')
class TestConversationTreeXj81:
    @allure.story("第81流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_81_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_81_flow(self, case_info):
        """1-11-6"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-82')
class TestConversationTreeXj82:
    @allure.story("第82流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_82_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_82_flow(self, case_info):
        """1-11-7"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-83')
class TestConversationTreeXj83:
    @allure.story("第83流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_83_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_83_flow(self, case_info):
        """1-11-8"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-84')
class TestConversationTreeXj84:
    @allure.story("第84流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_84_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_84_flow(self, case_info):
        """1-11-9"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-85')
class TestConversationTreeXj85:
    @allure.story("第85流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_85_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_85_flow(self, case_info):
        """1-11-10"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-86')
class TestConversationTreeXj86:
    @allure.story("第86流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_86_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_86_flow(self, case_info):
        """1-11-11"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-87')
class TestConversationTreeXj87:
    @allure.story("第87流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_87_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_87_flow(self, case_info):
        """1-11-12"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-88')
class TestConversationTreeXj88:
    @allure.story("第88流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_88_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_88_flow(self, case_info):
        """1-11-13"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-89')
class TestConversationTreeXj89:
    @allure.story("第89流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_89_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_89_flow(self, case_info):
        """1-11-14"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-90')
class TestConversationTreeXj90:
    @allure.story("第90流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_90_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_90_flow(self, case_info):
        """1-11-15"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-91')
class TestConversationTreeXj91:
    @allure.story("第91流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_91_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_91_flow(self, case_info):
        """1-11-16"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-92')
class TestConversationTreeXj92:
    @allure.story("第92流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_92_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_92_flow(self, case_info):
        """1-11-17"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-242')
class TestConversationTreeXj242:
    @allure.story("第242流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_242_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_242_flow(self, case_info):
        """1-11-18"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-243')
class TestConversationTreeXj243:
    @allure.story("第243流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_243_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_243_flow(self, case_info):
        """1-11-19"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-244')
class TestConversationTreeXj244:
    @allure.story("第244流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_244_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_244_flow(self, case_info):
        """1-11-20"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-245')
class TestConversationTreeXj245:
    @allure.story("第245流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_245_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_245_flow(self, case_info):
        """1-11-21"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-246')
class TestConversationTreeXj246:
    @allure.story("第246流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_246_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_246_flow(self, case_info):
        """1-11-22"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-247')
class TestConversationTreeXj247:
    @allure.story("第247流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_247_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_247_flow(self, case_info):
        """1-11-23"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-248')
class TestConversationTreeXj248:
    @allure.story("第248流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_248_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_248_flow(self, case_info):
        """1-11-24"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-93')
class TestConversationTreeXj93:
    @allure.story("第93流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_93_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_93_flow(self, case_info):
        """1-12-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-94')
class TestConversationTreeXj94:
    @allure.story("第94流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_94_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_94_flow(self, case_info):
        """1-12-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-95')
class TestConversationTreeXj95:
    @allure.story("第95流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_95_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_95_flow(self, case_info):
        """1-12-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-96')
class TestConversationTreeXj96:
    @allure.story("第96流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_96_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_96_flow(self, case_info):
        """1-12-4"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-97')
class TestConversationTreeXj97:
    @allure.story("第97流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_97_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_97_flow(self, case_info):
        """1-12-5"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-98')
class TestConversationTreeXj98:
    @allure.story("第98流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_98_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_98_flow(self, case_info):
        """1-12-6"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-99')
class TestConversationTreeXj99:
    @allure.story("第99流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_99_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_99_flow(self, case_info):
        """1-12-7"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-100')
class TestConversationTreeXj100:
    @allure.story("第100流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_100_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_100_flow(self, case_info):
        """1-12-8"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-101')
class TestConversationTreeXj101:
    @allure.story("第101流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_101_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_101_flow(self, case_info):
        """1-12-9"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-102')
class TestConversationTreeXj102:
    @allure.story("第102流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_102_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_102_flow(self, case_info):
        """1-12-10"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-103')
class TestConversationTreeXj103:
    @allure.story("第103流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_103_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_103_flow(self, case_info):
        """1-12-11"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-104')
class TestConversationTreeXj104:
    @allure.story("第104流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_104_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_104_flow(self, case_info):
        """1-12-12"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-105')
class TestConversationTreeXj105:
    @allure.story("第105流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_105_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_105_flow(self, case_info):
        """1-12-13"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-106')
class TestConversationTreeXj106:
    @allure.story("第106流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_106_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_106_flow(self, case_info):
        """1-12-14"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-107')
class TestConversationTreeXj107:
    @allure.story("第107流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_107_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_107_flow(self, case_info):
        """1-12-15"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-108')
class TestConversationTreeXj108:
    @allure.story("第108流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_108_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_108_flow(self, case_info):
        """1-12-16"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-109')
class TestConversationTreeXj109:
    @allure.story("第109流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_109_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_109_flow(self, case_info):
        """1-12-17"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-249')
class TestConversationTreeXj249:
    @allure.story("第249流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_249_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_249_flow(self, case_info):
        """1-12-18"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-250')
class TestConversationTreeXj250:
    @allure.story("第250流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_250_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_250_flow(self, case_info):
        """1-12-19"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-251')
class TestConversationTreeXj251:
    @allure.story("第251流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_251_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_251_flow(self, case_info):
        """1-12-20"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-252')
class TestConversationTreeXj252:
    @allure.story("第252流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_252_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_252_flow(self, case_info):
        """1-12-21"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-253')
class TestConversationTreeXj253:
    @allure.story("第253流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_253_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_253_flow(self, case_info):
        """1-12-22"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-254')
class TestConversationTreeXj254:
    @allure.story("第254流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_254_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_254_flow(self, case_info):
        """1-12-23"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-255')
class TestConversationTreeXj255:
    @allure.story("第255流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_255_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_255_flow(self, case_info):
        """1-12-24"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-110')
class TestConversationTreeXj110:
    @allure.story("第110流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_110_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_110_flow(self, case_info):
        """1-13"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-111')
class TestConversationTreeXj111:
    @allure.story("第111流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_111_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_111_flow(self, case_info):
        """1-14-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-112')
class TestConversationTreeXj112:
    @allure.story("第112流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_112_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_112_flow(self, case_info):
        """1-14-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-113')
class TestConversationTreeXj113:
    @allure.story("第113流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_113_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_113_flow(self, case_info):
        """1-14-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-114')
class TestConversationTreeXj114:
    @allure.story("第114流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_114_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_114_flow(self, case_info):
        """1-14-4"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-115')
class TestConversationTreeXj115:
    @allure.story("第115流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_115_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_115_flow(self, case_info):
        """1-14-5"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-116')
class TestConversationTreeXj116:
    @allure.story("第116流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_116_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_116_flow(self, case_info):
        """1-14-6"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-117')
class TestConversationTreeXj117:
    @allure.story("第117流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_117_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_117_flow(self, case_info):
        """1-14-7"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-118')
class TestConversationTreeXj118:
    @allure.story("第118流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_118_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_118_flow(self, case_info):
        """1-14-8"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-119')
class TestConversationTreeXj119:
    @allure.story("第119流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_119_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_119_flow(self, case_info):
        """1-14-9"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-120')
class TestConversationTreeXj120:
    @allure.story("第120流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_120_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_120_flow(self, case_info):
        """1-14-10"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-121')
class TestConversationTreeXj121:
    @allure.story("第121流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_121_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_121_flow(self, case_info):
        """1-14-11"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-122')
class TestConversationTreeXj122:
    @allure.story("第122流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_122_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_122_flow(self, case_info):
        """1-14-12"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-123')
class TestConversationTreeXj123:
    @allure.story("第123流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_123_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_123_flow(self, case_info):
        """1-14-13"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-124')
class TestConversationTreeXj124:
    @allure.story("第124流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_124_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_124_flow(self, case_info):
        """1-14-14"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-125')
class TestConversationTreeXj125:
    @allure.story("第125流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_125_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_125_flow(self, case_info):
        """1-14-15"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-126')
class TestConversationTreeXj126:
    @allure.story("第126流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_126_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_126_flow(self, case_info):
        """1-14-16"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-127')
class TestConversationTreeXj127:
    @allure.story("第127流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_127_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_127_flow(self, case_info):
        """1-14-17"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-256')
class TestConversationTreeXj256:
    @allure.story("第256流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_256_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_256_flow(self, case_info):
        """1-14-18"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-257')
class TestConversationTreeXj257:
    @allure.story("第257流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_257_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_257_flow(self, case_info):
        """1-14-19"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-258')
class TestConversationTreeXj258:
    @allure.story("第258流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_258_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_258_flow(self, case_info):
        """1-14-20"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-259')
class TestConversationTreeXj259:
    @allure.story("第259流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_259_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_259_flow(self, case_info):
        """1-14-21"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-260')
class TestConversationTreeXj260:
    @allure.story("第260流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_260_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_260_flow(self, case_info):
        """1-14-22"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-261')
class TestConversationTreeXj261:
    @allure.story("第261流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_261_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_261_flow(self, case_info):
        """1-14-23"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-262')
class TestConversationTreeXj262:
    @allure.story("第262流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_262_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_262_flow(self, case_info):
        """1-14-24"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-128')
class TestConversationTreeXj128:
    @allure.story("第128流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_128_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_128_flow(self, case_info):
        """1-15"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-129')
class TestConversationTreeXj129:
    @allure.story("第129流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_129_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_129_flow(self, case_info):
        """1-16"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-130')
class TestConversationTreeXj130:
    @allure.story("第130流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_130_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_130_flow(self, case_info):
        """1-17"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-263')
class TestConversationTreeXj263:
    @allure.story("第263流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_263_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_263_flow(self, case_info):
        """1-18"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-264')
class TestConversationTreeXj264:
    @allure.story("第264流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_264_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_264_flow(self, case_info):
        """1-19"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-265')
class TestConversationTreeXj265:
    @allure.story("第265流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_265_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_265_flow(self, case_info):
        """1-20"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-266')
class TestConversationTreeXj266:
    @allure.story("第266流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_266_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_266_flow(self, case_info):
        """1-21"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-267')
class TestConversationTreeXj267:
    @allure.story("第267流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_267_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_267_flow(self, case_info):
        """1-22"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-268')
class TestConversationTreeXj268:
    @allure.story("第268流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_268_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_268_flow(self, case_info):
        """1-23"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-269')
class TestConversationTreeXj269:
    @allure.story("第269流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_269_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_269_flow(self, case_info):
        """1-24"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-131')
class TestConversationTreeXj131:
    """Q2"""
    @allure.story("第131流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_131_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_131_flow(self, case_info):
        """1-6-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-132')
class TestConversationTreeXj132:
    @allure.story("第132流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_132_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_132_flow(self, case_info):
        """1-6-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-133')
class TestConversationTreeXj133:
    @allure.story("第133流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_133_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_133_flow(self, case_info):
        """1-6-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-134')
class TestConversationTreeXj134:
    @allure.story("第134流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_134_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_134_flow(self, case_info):
        """1-6-4-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-135')
class TestConversationTreeXj135:
    @allure.story("第135流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_135_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_135_flow(self, case_info):
        """1-6-4-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-136')
class TestConversationTreeXj136:
    @allure.story("第136流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_136_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_136_flow(self, case_info):
        """1-6-4-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-137')
class TestConversationTreeXj137:
    @allure.story("第137流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_137_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_137_flow(self, case_info):
        """1-6-4-4"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-138')
class TestConversationTreeXj138:
    @allure.story("第138流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_138_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_138_flow(self, case_info):
        """1-6-4-5"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-139')
class TestConversationTreeXj139:
    @allure.story("第139流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_139_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_139_flow(self, case_info):
        """1-6-4-6-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-140')
class TestConversationTreeXj140:
    @allure.story("第140流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_140_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_140_flow(self, case_info):
        """1-6-4-6-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-141')
class TestConversationTreeXj141:
    @allure.story("第141流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_141_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_141_flow(self, case_info):
        """1-6-4-6-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-142')
class TestConversationTreeXj142:
    @allure.story("第142流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_142_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_142_flow(self, case_info):
        """1-6-4-6-4-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-143')
class TestConversationTreeXj143:
    @allure.story("第143流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_143_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_143_flow(self, case_info):
        """1-6-4-6-4-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-144')
class TestConversationTreeXj144:
    @allure.story("第144流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_144_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_144_flow(self, case_info):
        """1-6-4-6-4-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-145')
class TestConversationTreeXj145:
    @allure.story("第145流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_145_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_145_flow(self, case_info):
        """1-6-4-6-4-4"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-146')
class TestConversationTreeXj146:
    @allure.story("第146流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_146_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_146_flow(self, case_info):
        """1-6-4-6-4-5"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-147')
class TestConversationTreeXj147:
    @allure.story("第147流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_147_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_147_flow(self, case_info):
        """1-6-4-6-4-6"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-148')
class TestConversationTreeXj148:
    @allure.story("第148流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_148_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_148_flow(self, case_info):
        """1-6-4-6-4-7"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-149')
class TestConversationTreeXj149:
    @allure.story("第149流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_149_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_149_flow(self, case_info):
        """1-6-4-6-4-8"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-150')
class TestConversationTreeXj150:
    @allure.story("第150流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_150_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_150_flow(self, case_info):
        """1-6-4-6-4-9"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-151')
class TestConversationTreeXj151:
    @allure.story("第151流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_151_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_151_flow(self, case_info):
        """1-6-4-6-4-10"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-152')
class TestConversationTreeXj152:
    @allure.story("第152流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_152_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_152_flow(self, case_info):
        """1-6-4-6-4-11"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-153')
class TestConversationTreeXj153:
    @allure.story("第153流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_153_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_153_flow(self, case_info):
        """1-6-4-6-4-12"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-154')
class TestConversationTreeXj154:
    @allure.story("第154流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_154_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_154_flow(self, case_info):
        """1-6-4-6-4-13"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-155')
class TestConversationTreeXj155:
    @allure.story("第155流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_155_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_155_flow(self, case_info):
        """1-6-4-6-4-14"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-156')
class TestConversationTreeXj156:
    @allure.story("第156流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_156_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_156_flow(self, case_info):
        """1-6-4-6-4-15"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-270')
class TestConversationTreeXj270:
    @allure.story("第270流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_270_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_270_flow(self, case_info):
        """1-6-4-6-4-16"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-271')
class TestConversationTreeXj271:
    @allure.story("第271流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_271_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_271_flow(self, case_info):
        """1-6-4-6-4-17"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-272')
class TestConversationTreeXj272:
    @allure.story("第272流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_272_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_272_flow(self, case_info):
        """1-6-4-6-4-18"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-273')
class TestConversationTreeXj273:
    @allure.story("第273流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_273_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_273_flow(self, case_info):
        """1-6-4-6-4-19"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-274')
class TestConversationTreeXj274:
    @allure.story("第274流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_274_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_274_flow(self, case_info):
        """1-6-4-6-4-20"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-275')
class TestConversationTreeXj275:
    @allure.story("第275流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_275_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_275_flow(self, case_info):
        """1-6-4-6-4-21"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-276')
class TestConversationTreeXj276:
    @allure.story("第276流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_276_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_276_flow(self, case_info):
        """1-6-4-6-4-22"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-277')
class TestConversationTreeXj277:
    @allure.story("第277流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_277_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_277_flow(self, case_info):
        """1-6-4-6-4-23"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-278')
class TestConversationTreeXj278:
    @allure.story("第278流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_278_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_278_flow(self, case_info):
        """1-6-4-6-4-24"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-157')
class TestConversationTreeXj157:
    @allure.story("第157流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_157_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_157_flow(self, case_info):
        """1-6-4-6-5"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-158')
class TestConversationTreeXj158:
    @allure.story("第158流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_158_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_158_flow(self, case_info):
        """1-6-4-6-6"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-159')
class TestConversationTreeXj159:
    @allure.story("第159流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_159_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_159_flow(self, case_info):
        """1-6-4-6-7"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-160')
class TestConversationTreeXj160:
    @allure.story("第160流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_160_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_160_flow(self, case_info):
        """1-6-4-6-8"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-161')
class TestConversationTreeXj161:
    @allure.story("第161流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_161_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_161_flow(self, case_info):
        """1-6-4-6-9"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-162')
class TestConversationTreeXj162:
    @allure.story("第162流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_162_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_162_flow(self, case_info):
        """1-6-4-6-10"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-163')
class TestConversationTreeXj163:
    @allure.story("第163流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_163_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_163_flow(self, case_info):
        """1-6-4-6-11"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-164')
class TestConversationTreeXj164:
    @allure.story("第164流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_164_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_164_flow(self, case_info):
        """1-6-4-6-12"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-165')
class TestConversationTreeXj165:
    @allure.story("第165流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_165_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_165_flow(self, case_info):
        """1-6-4-6-13"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-166')
class TestConversationTreeXj166:
    @allure.story("第166流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_166_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_166_flow(self, case_info):
        """1-6-4-6-14"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-167')
class TestConversationTreeXj167:
    @allure.story("第167流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_167_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_167_flow(self, case_info):
        """1-6-4-6-15"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-279')
class TestConversationTreeXj279:
    @allure.story("第279流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_279_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_279_flow(self, case_info):
        """1-6-4-6-16"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-280')
class TestConversationTreeXj280:
    @allure.story("第280流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_280_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_280_flow(self, case_info):
        """1-6-4-6-17"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-281')
class TestConversationTreeXj281:
    @allure.story("第281流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_281_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_281_flow(self, case_info):
        """1-6-4-6-18"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-282')
class TestConversationTreeXj282:
    @allure.story("第282流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_282_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_282_flow(self, case_info):
        """1-6-4-6-19"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-283')
class TestConversationTreeXj283:
    @allure.story("第283流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_283_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_283_flow(self, case_info):
        """1-6-4-6-20"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-284')
class TestConversationTreeXj284:
    @allure.story("第284流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_284_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_284_flow(self, case_info):
        """1-6-4-6-21"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-285')
class TestConversationTreeXj285:
    @allure.story("第285流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_285_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_285_flow(self, case_info):
        """1-6-4-6-22"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-286')
class TestConversationTreeXj286:
    @allure.story("第286流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_286_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_286_flow(self, case_info):
        """1-6-4-6-23"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-287')
class TestConversationTreeXj287:
    @allure.story("第287流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_287_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_287_flow(self, case_info):
        """1-6-4-6-24"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-168')
class TestConversationTreeXj168:
    @allure.story("第168流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_168_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_168_flow(self, case_info):
        """1-6-4-7"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-169')
class TestConversationTreeXj169:
    @allure.story("第169流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_169_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_169_flow(self, case_info):
        """1-6-4-8"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-170')
class TestConversationTreeXj170:
    @allure.story("第170流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_170_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_170_flow(self, case_info):
        """1-6-4-9"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-171')
class TestConversationTreeXj171:
    @allure.story("第171流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_171_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_171_flow(self, case_info):
        """1-6-4-10"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-172')
class TestConversationTreeXj172:
    @allure.story("第172流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_172_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_172_flow(self, case_info):
        """1-6-4-11"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-173')
class TestConversationTreeXj173:
    @allure.story("第173流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_173_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_173_flow(self, case_info):
        """1-6-4-12"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-174')
class TestConversationTreeXj174:
    @allure.story("第174流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_174_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_174_flow(self, case_info):
        """1-6-4-13"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-175')
class TestConversationTreeXj175:
    @allure.story("第175流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_175_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_175_flow(self, case_info):
        """1-6-4-14"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-176')
class TestConversationTreeXj176:
    @allure.story("第176流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_176_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_176_flow(self, case_info):
        """1-6-4-15"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-288')
class TestConversationTreeXj288:
    @allure.story("第288流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_288_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_288_flow(self, case_info):
        """1-6-4-16"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-289')
class TestConversationTreeXj289:
    @allure.story("第289流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_289_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_289_flow(self, case_info):
        """1-6-4-17"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-290')
class TestConversationTreeXj290:
    @allure.story("第290流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_290_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_290_flow(self, case_info):
        """1-6-4-18"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-291')
class TestConversationTreeXj291:
    @allure.story("第291流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_291_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_291_flow(self, case_info):
        """1-6-4-19"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-292')
class TestConversationTreeXj292:
    @allure.story("第292流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_292_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_292_flow(self, case_info):
        """1-6-4-20"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-293')
class TestConversationTreeXj293:
    @allure.story("第293流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_293_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_293_flow(self, case_info):
        """1-6-4-21"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-294')
class TestConversationTreeXj294:
    @allure.story("第294流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_294_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_294_flow(self, case_info):
        """1-6-4-22"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-295')
class TestConversationTreeXj295:
    @allure.story("第295流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_295_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_295_flow(self, case_info):
        """1-6-4-23"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-296')
class TestConversationTreeXj296:
    @allure.story("第296流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_296_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_296_flow(self, case_info):
        """1-6-4-24"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-177')
class TestConversationTreeXj177:
    @allure.story("第177流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_177_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_177_flow(self, case_info):
        """1-6-5"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-178')
class TestConversationTreeXj178:
    @allure.story("第178流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_178_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_178_flow(self, case_info):
        """1-6-6"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-179')
class TestConversationTreeXj179:
    @allure.story("第179流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_179_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_179_flow(self, case_info):
        """1-6-7"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-180')
class TestConversationTreeXj180:
    @allure.story("第180流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_180_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_180_flow(self, case_info):
        """1-6-8"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-181')
class TestConversationTreeXj181:
    @allure.story("第181流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_181_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_181_flow(self, case_info):
        """1-6-9"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-182')
class TestConversationTreeXj182:
    @allure.story("第182流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_182_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_182_flow(self, case_info):
        """1-6-10"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-183')
class TestConversationTreeXj183:
    @allure.story("第183流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_183_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_183_flow(self, case_info):
        """1-6-11"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-184')
class TestConversationTreeXj184:
    @allure.story("第184流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_184_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_184_flow(self, case_info):
        """1-6-12"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-185')
class TestConversationTreeXj185:
    @allure.story("第185流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_185_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_185_flow(self, case_info):
        """1-6-13"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-186')
class TestConversationTreeXj186:
    @allure.story("第186流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_186_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_186_flow(self, case_info):
        """1-6-14"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-187')
class TestConversationTreeXj187:
    @allure.story("第187流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_187_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_187_flow(self, case_info):
        """1-6-15"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-297')
class TestConversationTreeXj297:
    @allure.story("第297流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_297_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_297_flow(self, case_info):
        """1-6-16"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-298')
class TestConversationTreeXj298:
    @allure.story("第298流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_298_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_298_flow(self, case_info):
        """1-6-17"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-299')
class TestConversationTreeXj299:
    @allure.story("第299流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_299_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_299_flow(self, case_info):
        """1-6-18"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-300')
class TestConversationTreeXj300:
    @allure.story("第300流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_300_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_300_flow(self, case_info):
        """1-6-19"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-301')
class TestConversationTreeXj301:
    @allure.story("第301流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_301_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_301_flow(self, case_info):
        """1-6-20"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-302')
class TestConversationTreeXj302:
    @allure.story("第302流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_302_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_302_flow(self, case_info):
        """1-6-21"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-303')
class TestConversationTreeXj303:
    @allure.story("第303流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_303_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_303_flow(self, case_info):
        """1-6-22"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-304')
class TestConversationTreeXj304:
    @allure.story("第304流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_304_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_304_flow(self, case_info):
        """1-6-23"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-305')
class TestConversationTreeXj305:
    @allure.story("第305流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_305_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_305_flow(self, case_info):
        """1-6-24"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-188')
class TestConversationTreeXj188:
    """Q4"""
    @allure.story("第188流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_188_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_188_flow(self, case_info):
        """1-6-1-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-189')
class TestConversationTreeXj189:
    @allure.story("第189流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_189_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_189_flow(self, case_info):
        """1-6-1-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-190')
class TestConversationTreeXj190:
    @allure.story("第190流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_190_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_190_flow(self, case_info):
        """1-6-1-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-191')
class TestConversationTreeXj191:
    @allure.story("第191流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_191_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_191_flow(self, case_info):
        """1-6-1-4"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-192')
class TestConversationTreeXj192:
    @allure.story("第192流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_192_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_192_flow(self, case_info):
        """1-6-1-5-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-193')
class TestConversationTreeXj193:
    @allure.story("第193流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_193_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_193_flow(self, case_info):
        """1-6-1-5-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-194')
class TestConversationTreeXj194:
    @allure.story("第194流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_194_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_194_flow(self, case_info):
        """1-6-1-5-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-195')
class TestConversationTreeXj195:
    @allure.story("第195流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_195_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_195_flow(self, case_info):
        """1-6-1-5-4"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-196')
class TestConversationTreeXj196:
    @allure.story("第196流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_196_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_196_flow(self, case_info):
        """1-6-1-5-5"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-197')
class TestConversationTreeXj197:
    @allure.story("第197流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_197_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_197_flow(self, case_info):
        """1-6-1-5-6"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-198')
class TestConversationTreeXj198:
    @allure.story("第198流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_198_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_198_flow(self, case_info):
        """1-6-1-5-7"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-199')
class TestConversationTreeXj199:
    @allure.story("第199流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_199_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_199_flow(self, case_info):
        """1-6-1-5-8"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-200')
class TestConversationTreeXj200:
    @allure.story("第200流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_200_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_200_flow(self, case_info):
        """1-6-1-5-9"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-201')
class TestConversationTreeXj201:
    @allure.story("第201流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_201_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_201_flow(self, case_info):
        """1-6-1-5-10"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-202')
class TestConversationTreeXj202:
    @allure.story("第202流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_202_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_202_flow(self, case_info):
        """1-6-1-5-11"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-203')
class TestConversationTreeXj203:
    @allure.story("第203流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_203_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_203_flow(self, case_info):
        """1-6-1-5-12"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-204')
class TestConversationTreeXj204:
    @allure.story("第204流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_204_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_204_flow(self, case_info):
        """1-6-1-5-13"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-205')
class TestConversationTreeXj205:
    @allure.story("第205流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_205_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_205_flow(self, case_info):
        """1-6-1-5-14"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-206')
class TestConversationTreeXj206:
    @allure.story("第206流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_206_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_206_flow(self, case_info):
        """1-6-1-5-15"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-207')
class TestConversationTreeXj207:
    @allure.story("第207流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_207_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_207_flow(self, case_info):
        """1-6-1-5-16"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-208')
class TestConversationTreeXj208:
    @allure.story("第208流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_208_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_208_flow(self, case_info):
        """1-6-1-5-17"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-306')
class TestConversationTreeXj306:
    @allure.story("第306流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_306_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_306_flow(self, case_info):
        """1-6-1-5-18"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-307')
class TestConversationTreeXj307:
    @allure.story("第307流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_307_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_307_flow(self, case_info):
        """1-6-1-5-19"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-308')
class TestConversationTreeXj308:
    @allure.story("第308流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_308_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_308_flow(self, case_info):
        """1-6-1-5-20"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-309')
class TestConversationTreeXj309:
    @allure.story("第309流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_309_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_309_flow(self, case_info):
        """1-6-1-5-21"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-310')
class TestConversationTreeXj310:
    @allure.story("第310流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_310_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_310_flow(self, case_info):
        """1-6-1-5-22"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-311')
class TestConversationTreeXj311:
    @allure.story("第311流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_311_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_311_flow(self, case_info):
        """1-6-1-5-23"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-312')
class TestConversationTreeXj312:
    @allure.story("第312流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_312_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_312_flow(self, case_info):
        """1-6-1-5-24"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-209')
class TestConversationTreeXj209:
    @allure.story("第209流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_209_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_209_flow(self, case_info):
        """1-6-1-6-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-357')
class TestConversationTreeXj357:
    @allure.story("第357流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_357_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_357_flow(self, case_info):
        """1-6-1-6-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-358')
class TestConversationTreeXj358:
    @allure.story("第358流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_358_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_358_flow(self, case_info):
        """1-6-1-6-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-359')
class TestConversationTreeXj359:
    @allure.story("第359流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_359_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_359_flow(self, case_info):
        """1-6-1-6-4"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-360')
class TestConversationTreeXj360:
    @allure.story("第360流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_360_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_360_flow(self, case_info):
        """1-6-1-6-5"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-361')
class TestConversationTreeXj361:
    @allure.story("第361流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_361_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_361_flow(self, case_info):
        """1-6-1-6-6"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-362')
class TestConversationTreeXj362:
    @allure.story("第362流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_362_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_362_flow(self, case_info):
        """1-6-1-6-7"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-363')
class TestConversationTreeXj363:
    @allure.story("第363流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_363_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_363_flow(self, case_info):
        """1-6-1-6-8"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-364')
class TestConversationTreeXj364:
    @allure.story("第364流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_364_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_364_flow(self, case_info):
        """1-6-1-6-9"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-365')
class TestConversationTreeXj365:
    @allure.story("第365流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_365_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_365_flow(self, case_info):
        """1-6-1-6-10"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-366')
class TestConversationTreeXj366:
    @allure.story("第366流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_366_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_366_flow(self, case_info):
        """1-6-1-6-11"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-367')
class TestConversationTreeXj367:
    @allure.story("第367流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_367_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_367_flow(self, case_info):
        """1-6-1-6-12"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-368')
class TestConversationTreeXj368:
    @allure.story("第368流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_368_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_368_flow(self, case_info):
        """1-6-1-6-13"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-369')
class TestConversationTreeXj369:
    @allure.story("第369流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_369_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_369_flow(self, case_info):
        """1-6-1-6-14"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-370')
class TestConversationTreeXj370:
    @allure.story("第370流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_370_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_370_flow(self, case_info):
        """1-6-1-6-15"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-371')
class TestConversationTreeXj371:
    @allure.story("第371流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_371_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_371_flow(self, case_info):
        """1-6-1-6-16"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-372')
class TestConversationTreeXj372:
    @allure.story("第372流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_372_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_372_flow(self, case_info):
        """1-6-1-6-17"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-373')
class TestConversationTreeXj373:
    @allure.story("第373流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_373_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_373_flow(self, case_info):
        """1-6-1-6-18"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-374')
class TestConversationTreeXj374:
    @allure.story("第374流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_374_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_374_flow(self, case_info):
        """1-6-1-6-19"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-375')
class TestConversationTreeXj375:
    @allure.story("第375流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_375_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_375_flow(self, case_info):
        """1-6-1-6-20"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-376')
class TestConversationTreeXj376:
    @allure.story("第376流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_376_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_376_flow(self, case_info):
        """1-6-1-6-21"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-377')
class TestConversationTreeXj377:
    @allure.story("第377流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_377_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_377_flow(self, case_info):
        """1-6-1-6-22"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-378')
class TestConversationTreeXj378:
    @allure.story("第378流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_378_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_378_flow(self, case_info):
        """1-6-1-6-23"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-379')
class TestConversationTreeXj379:
    @allure.story("第379流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_379_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_379_flow(self, case_info):
        """1-6-1-6-24"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-210')
class TestConversationTreeXj210:
    @allure.story("第210流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_210_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_210_flow(self, case_info):
        """1-6-1-7-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-380')
class TestConversationTreeXj380:
    @allure.story("第380流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_380_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_380_flow(self, case_info):
        """1-6-1-7-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-381')
class TestConversationTreeXj381:
    @allure.story("第381流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_381_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_381_flow(self, case_info):
        """1-6-1-7-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-382')
class TestConversationTreeXj382:
    @allure.story("第382流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_382_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_382_flow(self, case_info):
        """1-6-1-7-4"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-383')
class TestConversationTreeXj383:
    @allure.story("第383流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_383_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_383_flow(self, case_info):
        """1-6-1-7-5"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-384')
class TestConversationTreeXj384:
    @allure.story("第384流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_384_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_384_flow(self, case_info):
        """1-6-1-7-6"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-385')
class TestConversationTreeXj385:
    @allure.story("第385流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_385_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_385_flow(self, case_info):
        """1-6-1-7-7"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-386')
class TestConversationTreeXj386:
    @allure.story("第386流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_386_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_386_flow(self, case_info):
        """1-6-1-7-8"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-387')
class TestConversationTreeXj387:
    @allure.story("第387流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_387_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_387_flow(self, case_info):
        """1-6-1-7-9"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-388')
class TestConversationTreeXj388:
    @allure.story("第388流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_388_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_388_flow(self, case_info):
        """1-6-1-7-10"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-389')
class TestConversationTreeXj389:
    @allure.story("第389流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_389_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_389_flow(self, case_info):
        """1-6-1-7-11"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-390')
class TestConversationTreeXj390:
    @allure.story("第390流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_390_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_390_flow(self, case_info):
        """1-6-1-7-12"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-391')
class TestConversationTreeXj391:
    @allure.story("第391流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_391_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_391_flow(self, case_info):
        """1-6-1-7-13"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-392')
class TestConversationTreeXj392:
    @allure.story("第392流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_392_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_392_flow(self, case_info):
        """1-6-1-7-14"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-393')
class TestConversationTreeXj393:
    @allure.story("第393流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_393_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_393_flow(self, case_info):
        """1-6-1-7-15"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-394')
class TestConversationTreeXj394:
    @allure.story("第394流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_394_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_394_flow(self, case_info):
        """1-6-1-7-16"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-395')
class TestConversationTreeXj395:
    @allure.story("第395流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_395_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_395_flow(self, case_info):
        """1-6-1-7-17"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-396')
class TestConversationTreeXj396:
    @allure.story("第396流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_396_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_396_flow(self, case_info):
        """1-6-1-7-18"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-397')
class TestConversationTreeXj397:
    @allure.story("第397流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_397_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_397_flow(self, case_info):
        """1-6-1-7-19"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-398')
class TestConversationTreeXj398:
    @allure.story("第398流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_398_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_398_flow(self, case_info):
        """1-6-1-7-20"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-399')
class TestConversationTreeXj399:
    @allure.story("第399流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_399_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_399_flow(self, case_info):
        """1-6-1-7-21"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-400')
class TestConversationTreeXj400:
    @allure.story("第400流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_400_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_400_flow(self, case_info):
        """1-6-1-7-22"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-401')
class TestConversationTreeXj401:
    @allure.story("第401流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_401_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_401_flow(self, case_info):
        """1-6-1-7-23"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-402')
class TestConversationTreeXj402:
    @allure.story("第402流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_402_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_402_flow(self, case_info):
        """1-6-1-7-24"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-211')
class TestConversationTreeXj211:
    @allure.story("第211流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_211_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_211_flow(self, case_info):
        """1-6-1-8-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-403')
class TestConversationTreeXj403:
    @allure.story("第403流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_403_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_403_flow(self, case_info):
        """1-6-1-8-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-404')
class TestConversationTreeXj404:
    @allure.story("第404流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_404_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_404_flow(self, case_info):
        """1-6-1-8-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-405')
class TestConversationTreeXj405:
    @allure.story("第405流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_405_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_405_flow(self, case_info):
        """1-6-1-8-4"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-406')
class TestConversationTreeXj406:
    @allure.story("第406流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_406_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_406_flow(self, case_info):
        """1-6-1-8-5"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-407')
class TestConversationTreeXj407:
    @allure.story("第407流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_407_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_407_flow(self, case_info):
        """1-6-1-8-6"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-408')
class TestConversationTreeXj408:
    @allure.story("第408流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_408_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_408_flow(self, case_info):
        """1-6-1-8-7"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-409')
class TestConversationTreeXj409:
    @allure.story("第409流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_409_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_409_flow(self, case_info):
        """1-6-1-8-8"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-410')
class TestConversationTreeXj410:
    @allure.story("第410流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_410_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_410_flow(self, case_info):
        """1-6-1-8-9"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-411')
class TestConversationTreeXj411:
    @allure.story("第411流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_411_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_411_flow(self, case_info):
        """1-6-1-8-10"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-412')
class TestConversationTreeXj412:
    @allure.story("第412流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_412_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_412_flow(self, case_info):
        """1-6-1-8-11"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-413')
class TestConversationTreeXj413:
    @allure.story("第413流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_413_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_413_flow(self, case_info):
        """1-6-1-8-12"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-414')
class TestConversationTreeXj414:
    @allure.story("第414流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_414_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_414_flow(self, case_info):
        """1-6-1-8-13"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-415')
class TestConversationTreeXj415:
    @allure.story("第415流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_415_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_415_flow(self, case_info):
        """1-6-1-8-14"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-416')
class TestConversationTreeXj416:
    @allure.story("第416流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_416_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_416_flow(self, case_info):
        """1-6-1-8-15"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-417')
class TestConversationTreeXj417:
    @allure.story("第417流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_417_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_417_flow(self, case_info):
        """1-6-1-8-16"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-418')
class TestConversationTreeXj418:
    @allure.story("第418流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_418_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_418_flow(self, case_info):
        """1-6-1-8-17"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-419')
class TestConversationTreeXj419:
    @allure.story("第419流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_419_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_419_flow(self, case_info):
        """1-6-1-8-18"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-420')
class TestConversationTreeXj420:
    @allure.story("第420流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_420_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_420_flow(self, case_info):
        """1-6-1-8-19"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-421')
class TestConversationTreeXj421:
    @allure.story("第421流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_421_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_421_flow(self, case_info):
        """1-6-1-8-20"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-422')
class TestConversationTreeXj422:
    @allure.story("第422流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_422_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_422_flow(self, case_info):
        """1-6-1-8-21"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-423')
class TestConversationTreeXj423:
    @allure.story("第423流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_423_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_423_flow(self, case_info):
        """1-6-1-8-22"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-424')
class TestConversationTreeXj424:
    @allure.story("第424流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_424_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_424_flow(self, case_info):
        """1-6-1-8-23"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-425')
class TestConversationTreeXj425:
    @allure.story("第425流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_425_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_425_flow(self, case_info):
        """1-6-1-8-24"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-212')
class TestConversationTreeXj212:
    @allure.story("第212流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_212_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_212_flow(self, case_info):
        """1-6-1-9-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-426')
class TestConversationTreeXj426:
    @allure.story("第426流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_426_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_426_flow(self, case_info):
        """1-6-1-9-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-427')
class TestConversationTreeXj427:
    @allure.story("第427流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_427_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_427_flow(self, case_info):
        """1-6-1-9-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-428')
class TestConversationTreeXj428:
    @allure.story("第428流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_428_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_428_flow(self, case_info):
        """1-6-1-9-4"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-429')
class TestConversationTreeXj429:
    @allure.story("第429流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_429_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_429_flow(self, case_info):
        """1-6-1-9-5"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-430')
class TestConversationTreeXj430:
    @allure.story("第430流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_430_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_430_flow(self, case_info):
        """1-6-1-9-6"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-431')
class TestConversationTreeXj431:
    @allure.story("第431流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_431_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_431_flow(self, case_info):
        """1-6-1-9-7"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-432')
class TestConversationTreeXj432:
    @allure.story("第432流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_432_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_432_flow(self, case_info):
        """1-6-1-9-8"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-433')
class TestConversationTreeXj433:
    @allure.story("第433流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_433_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_433_flow(self, case_info):
        """1-6-1-9-9"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-434')
class TestConversationTreeXj434:
    @allure.story("第434流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_434_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_434_flow(self, case_info):
        """1-6-1-9-10"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-435')
class TestConversationTreeXj435:
    @allure.story("第435流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_435_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_435_flow(self, case_info):
        """1-6-1-9-11"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-436')
class TestConversationTreeXj436:
    @allure.story("第436流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_436_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_436_flow(self, case_info):
        """1-6-1-9-12"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-437')
class TestConversationTreeXj437:
    @allure.story("第437流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_437_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_437_flow(self, case_info):
        """1-6-1-9-13"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-438')
class TestConversationTreeXj438:
    @allure.story("第438流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_438_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_438_flow(self, case_info):
        """1-6-1-9-14"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-439')
class TestConversationTreeXj439:
    @allure.story("第439流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_439_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_439_flow(self, case_info):
        """1-6-1-9-15"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-440')
class TestConversationTreeXj440:
    @allure.story("第440流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_440_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_440_flow(self, case_info):
        """1-6-1-9-16"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-441')
class TestConversationTreeXj441:
    @allure.story("第441流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_441_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_441_flow(self, case_info):
        """1-6-1-9-17"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-442')
class TestConversationTreeXj442:
    @allure.story("第442流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_442_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_442_flow(self, case_info):
        """1-6-1-9-18"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-443')
class TestConversationTreeXj443:
    @allure.story("第443流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_443_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_443_flow(self, case_info):
        """1-6-1-9-19"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-444')
class TestConversationTreeXj444:
    @allure.story("第444流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_444_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_444_flow(self, case_info):
        """1-6-1-9-20"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-445')
class TestConversationTreeXj445:
    @allure.story("第445流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_445_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_445_flow(self, case_info):
        """1-6-1-9-21"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-446')
class TestConversationTreeXj446:
    @allure.story("第446流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_446_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_446_flow(self, case_info):
        """1-6-1-9-22"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-447')
class TestConversationTreeXj447:
    @allure.story("第447流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_447_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_447_flow(self, case_info):
        """1-6-1-9-23"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-448')
class TestConversationTreeXj448:
    @allure.story("第448流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_448_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_448_flow(self, case_info):
        """1-6-1-9-24"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-213')
class TestConversationTreeXj213:
    @allure.story("第213流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_213_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_213_flow(self, case_info):
        """1-6-1-10-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-449')
class TestConversationTreeXj449:
    @allure.story("第449流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_449_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_449_flow(self, case_info):
        """1-6-1-10-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-450')
class TestConversationTreeXj450:
    @allure.story("第450流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_450_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_450_flow(self, case_info):
        """1-6-1-10-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-451')
class TestConversationTreeXj451:
    @allure.story("第451流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_451_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_451_flow(self, case_info):
        """1-6-1-10-4"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-452')
class TestConversationTreeXj452:
    @allure.story("第452流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_452_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_452_flow(self, case_info):
        """1-6-1-10-5"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-453')
class TestConversationTreeXj453:
    @allure.story("第453流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_453_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_453_flow(self, case_info):
        """1-6-1-10-6"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-454')
class TestConversationTreeXj454:
    @allure.story("第454流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_454_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_454_flow(self, case_info):
        """1-6-1-10-7"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-455')
class TestConversationTreeXj455:
    @allure.story("第455流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_455_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_455_flow(self, case_info):
        """1-6-1-10-8"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-456')
class TestConversationTreeXj456:
    @allure.story("第456流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_456_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_456_flow(self, case_info):
        """1-6-1-10-9"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-457')
class TestConversationTreeXj457:
    @allure.story("第457流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_457_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_457_flow(self, case_info):
        """1-6-1-10-10"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-458')
class TestConversationTreeXj458:
    @allure.story("第458流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_458_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_458_flow(self, case_info):
        """1-6-1-10-11"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-459')
class TestConversationTreeXj459:
    @allure.story("第459流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_459_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_459_flow(self, case_info):
        """1-6-1-10-12"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-460')
class TestConversationTreeXj460:
    @allure.story("第460流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_460_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_460_flow(self, case_info):
        """1-6-1-10-13"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-461')
class TestConversationTreeXj461:
    @allure.story("第461流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_461_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_461_flow(self, case_info):
        """1-6-1-10-14"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-462')
class TestConversationTreeXj462:
    @allure.story("第462流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_462_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_462_flow(self, case_info):
        """1-6-1-10-15"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-463')
class TestConversationTreeXj463:
    @allure.story("第463流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_463_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_463_flow(self, case_info):
        """1-6-1-10-16"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-464')
class TestConversationTreeXj464:
    @allure.story("第464流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_464_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_464_flow(self, case_info):
        """1-6-1-10-17"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-465')
class TestConversationTreeXj465:
    @allure.story("第465流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_465_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_465_flow(self, case_info):
        """1-6-1-10-18"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-466')
class TestConversationTreeXj466:
    @allure.story("第466流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_466_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_466_flow(self, case_info):
        """1-6-1-10-19"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-467')
class TestConversationTreeXj467:
    @allure.story("第467流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_467_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_467_flow(self, case_info):
        """1-6-1-10-20"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-468')
class TestConversationTreeXj468:
    @allure.story("第468流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_468_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_468_flow(self, case_info):
        """1-6-1-10-21"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-469')
class TestConversationTreeXj469:
    @allure.story("第469流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_469_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_469_flow(self, case_info):
        """1-6-1-10-22"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-470')
class TestConversationTreeXj470:
    @allure.story("第470流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_470_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_470_flow(self, case_info):
        """1-6-1-10-23"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-471')
class TestConversationTreeXj471:
    @allure.story("第471流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_471_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_471_flow(self, case_info):
        """1-6-1-10-24"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-214')
class TestConversationTreeXj214:
    @allure.story("第214流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_214_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_214_flow(self, case_info):
        """1-6-1-11-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-472')
class TestConversationTreeXj472:
    @allure.story("第472流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_472_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_472_flow(self, case_info):
        """1-6-1-11-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-473')
class TestConversationTreeXj473:
    @allure.story("第473流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_473_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_473_flow(self, case_info):
        """1-6-1-11-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-474')
class TestConversationTreeXj474:
    @allure.story("第474流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_474_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_474_flow(self, case_info):
        """1-6-1-11-4"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-475')
class TestConversationTreeXj475:
    @allure.story("第475流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_475_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_475_flow(self, case_info):
        """1-6-1-11-5"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-476')
class TestConversationTreeXj476:
    @allure.story("第476流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_476_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_476_flow(self, case_info):
        """1-6-1-11-6"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-477')
class TestConversationTreeXj477:
    @allure.story("第477流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_477_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_477_flow(self, case_info):
        """1-6-1-11-7"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-478')
class TestConversationTreeXj478:
    @allure.story("第478流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_478_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_478_flow(self, case_info):
        """1-6-1-11-8"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-479')
class TestConversationTreeXj479:
    @allure.story("第479流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_479_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_479_flow(self, case_info):
        """1-6-1-11-9"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-480')
class TestConversationTreeXj480:
    @allure.story("第480流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_480_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_480_flow(self, case_info):
        """1-6-1-11-10"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-481')
class TestConversationTreeXj481:
    @allure.story("第481流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_481_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_481_flow(self, case_info):
        """1-6-1-11-11"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-482')
class TestConversationTreeXj482:
    @allure.story("第482流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_482_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_482_flow(self, case_info):
        """1-6-1-11-12"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-483')
class TestConversationTreeXj483:
    @allure.story("第483流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_483_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_483_flow(self, case_info):
        """1-6-1-11-13"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-484')
class TestConversationTreeXj484:
    @allure.story("第484流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_484_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_484_flow(self, case_info):
        """1-6-1-11-14"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-485')
class TestConversationTreeXj485:
    @allure.story("第485流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_485_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_485_flow(self, case_info):
        """1-6-1-11-15"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-486')
class TestConversationTreeXj486:
    @allure.story("第486流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_486_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_486_flow(self, case_info):
        """1-6-1-11-16"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-487')
class TestConversationTreeXj487:
    @allure.story("第487流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_487_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_487_flow(self, case_info):
        """1-6-1-11-17"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-488')
class TestConversationTreeXj488:
    @allure.story("第488流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_488_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_488_flow(self, case_info):
        """1-6-1-11-18"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-489')
class TestConversationTreeXj489:
    @allure.story("第489流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_489_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_489_flow(self, case_info):
        """1-6-1-11-19"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-490')
class TestConversationTreeXj490:
    @allure.story("第490流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_490_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_490_flow(self, case_info):
        """1-6-1-11-20"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-491')
class TestConversationTreeXj491:
    @allure.story("第491流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_491_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_491_flow(self, case_info):
        """1-6-1-11-21"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-492')
class TestConversationTreeXj492:
    @allure.story("第492流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_492_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_492_flow(self, case_info):
        """1-6-1-11-22"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-493')
class TestConversationTreeXj493:
    @allure.story("第493流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_493_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_493_flow(self, case_info):
        """1-6-1-11-23"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-494')
class TestConversationTreeXj494:
    @allure.story("第494流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_494_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_494_flow(self, case_info):
        """1-6-1-11-24"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-215')
class TestConversationTreeXj215:
    @allure.story("第215流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_215_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_215_flow(self, case_info):
        """1-6-1-12"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-216')
class TestConversationTreeXj216:
    @allure.story("第216流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_216_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_216_flow(self, case_info):
        """1-6-1-13"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-217')
class TestConversationTreeXj217:
    @allure.story("第217流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_217_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_217_flow(self, case_info):
        """1-6-1-14-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-495')
class TestConversationTreeXj495:
    @allure.story("第495流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_495_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_495_flow(self, case_info):
        """1-6-1-14-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-496')
class TestConversationTreeXj496:
    @allure.story("第496流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_496_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_496_flow(self, case_info):
        """1-6-1-14-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-497')
class TestConversationTreeXj497:
    @allure.story("第497流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_497_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_497_flow(self, case_info):
        """1-6-1-14-4"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-498')
class TestConversationTreeXj498:
    @allure.story("第498流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_498_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_498_flow(self, case_info):
        """1-6-1-14-5"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-499')
class TestConversationTreeXj499:
    @allure.story("第499流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_499_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_499_flow(self, case_info):
        """1-6-1-14-6"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-500')
class TestConversationTreeXj500:
    @allure.story("第500流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_500_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_500_flow(self, case_info):
        """1-6-1-14-7"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-501')
class TestConversationTreeXj501:
    @allure.story("第501流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_501_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_501_flow(self, case_info):
        """1-6-1-14-8"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-502')
class TestConversationTreeXj502:
    @allure.story("第502流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_502_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_502_flow(self, case_info):
        """1-6-1-14-9"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-503')
class TestConversationTreeXj503:
    @allure.story("第503流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_503_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_503_flow(self, case_info):
        """1-6-1-14-10"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-504')
class TestConversationTreeXj504:
    @allure.story("第504流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_504_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_504_flow(self, case_info):
        """1-6-1-14-11"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-505')
class TestConversationTreeXj505:
    @allure.story("第505流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_505_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_505_flow(self, case_info):
        """1-6-1-14-12"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-506')
class TestConversationTreeXj506:
    @allure.story("第506流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_506_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_506_flow(self, case_info):
        """1-6-1-14-13"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-507')
class TestConversationTreeXj507:
    @allure.story("第507流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_507_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_507_flow(self, case_info):
        """1-6-1-14-14"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-508')
class TestConversationTreeXj508:
    @allure.story("第508流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_508_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_508_flow(self, case_info):
        """1-6-1-14-15"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-509')
class TestConversationTreeXj509:
    @allure.story("第509流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_509_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_509_flow(self, case_info):
        """1-6-1-14-16"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-510')
class TestConversationTreeXj510:
    @allure.story("第510流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_510_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_510_flow(self, case_info):
        """1-6-1-14-17"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-511')
class TestConversationTreeXj511:
    @allure.story("第511流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_511_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_511_flow(self, case_info):
        """1-6-1-14-18"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-512')
class TestConversationTreeXj512:
    @allure.story("第512流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_512_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_512_flow(self, case_info):
        """1-6-1-14-19"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-513')
class TestConversationTreeXj513:
    @allure.story("第513流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_513_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_513_flow(self, case_info):
        """1-6-1-14-20"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-514')
class TestConversationTreeXj514:
    @allure.story("第514流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_514_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_514_flow(self, case_info):
        """1-6-1-14-21"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-515')
class TestConversationTreeXj515:
    @allure.story("第515流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_515_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_515_flow(self, case_info):
        """1-6-1-14-22"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-516')
class TestConversationTreeXj516:
    @allure.story("第516流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_516_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_516_flow(self, case_info):
        """1-6-1-14-23"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-517')
class TestConversationTreeXj517:
    @allure.story("第517流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_517_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_517_flow(self, case_info):
        """1-6-1-14-24"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-218')
class TestConversationTreeXj218:
    @allure.story("第218流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_218_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_218_flow(self, case_info):
        """1-6-1-15"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-219')
class TestConversationTreeXj219:
    @allure.story("第219流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_219_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_219_flow(self, case_info):
        """1-6-1-16"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-220')
class TestConversationTreeXj220:
    @allure.story("第220流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_220_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_220_flow(self, case_info):
        """1-6-1-17"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-313')
class TestConversationTreeXj313:
    @allure.story("第313流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_313_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_313_flow(self, case_info):
        """1-6-1-18"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-314')
class TestConversationTreeXj314:
    @allure.story("第314流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_314_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_314_flow(self, case_info):
        """1-6-1-19"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-315')
class TestConversationTreeXj315:
    @allure.story("第315流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_315_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_315_flow(self, case_info):
        """1-6-1-20"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-316')
class TestConversationTreeXj316:
    @allure.story("第316流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_316_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_316_flow(self, case_info):
        """1-6-1-21"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-317')
class TestConversationTreeXj317:
    @allure.story("第317流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_317_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_317_flow(self, case_info):
        """1-6-1-22"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-318')
class TestConversationTreeXj318:
    @allure.story("第318流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_318_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_318_flow(self, case_info):
        """1-6-1-23"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-319')
class TestConversationTreeXj319:
    @allure.story("第319流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_319_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_319_flow(self, case_info):
        """1-6-1-24"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-320')
class TestConversationTreeXj320:
    """Q5"""
    @allure.story("第320流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_320_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_320_flow(self, case_info):
        """1-6-1-1-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-321')
class TestConversationTreeXj321:
    @allure.story("第321流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_321_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_321_flow(self, case_info):
        """1-6-1-1-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-322')
class TestConversationTreeXj322:
    @allure.story("第322流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_322_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_322_flow(self, case_info):
        """1-6-1-1-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-323')
class TestConversationTreeXj323:
    @allure.story("第323流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_323_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_323_flow(self, case_info):
        """1-6-1-1-4"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-324')
class TestConversationTreeXj324:
    @allure.story("第324流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_324_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_324_flow(self, case_info):
        """1-6-1-1-5"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-325')
class TestConversationTreeXj325:
    @allure.story("第325流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_325_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_325_flow(self, case_info):
        """1-6-1-1-6"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-326')
class TestConversationTreeXj326:
    @allure.story("第326流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_326_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_326_flow(self, case_info):
        """1-6-1-1-7-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-327')
class TestConversationTreeXj327:
    @allure.story("第327流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_327_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_327_flow(self, case_info):
        """1-6-1-1-7-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-328')
class TestConversationTreeXj328:
    @allure.story("第328流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_328_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_328_flow(self, case_info):
        """1-6-1-1-7-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-329')
class TestConversationTreeXj329:
    @allure.story("第329流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_329_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_329_flow(self, case_info):
        """1-6-1-1-7-4"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-330')
class TestConversationTreeXj330:
    @allure.story("第330流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_330_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_330_flow(self, case_info):
        """1-6-1-1-7-5"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-331')
class TestConversationTreeXj331:
    @allure.story("第331流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_331_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_331_flow(self, case_info):
        """1-6-1-1-7-6"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-332')
class TestConversationTreeXj332:
    @allure.story("第332流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_332_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_332_flow(self, case_info):
        """1-6-1-1-7-7"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-333')
class TestConversationTreeXj333:
    @allure.story("第333流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_333_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_333_flow(self, case_info):
        """1-6-1-1-7-8"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-334')
class TestConversationTreeXj334:
    @allure.story("第334流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_334_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_334_flow(self, case_info):
        """1-6-1-1-7-9"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-335')
class TestConversationTreeXj335:
    @allure.story("第335流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_335_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_335_flow(self, case_info):
        """1-6-1-1-7-10"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-336')
class TestConversationTreeXj336:
    @allure.story("第336流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_336_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_336_flow(self, case_info):
        """1-6-1-1-7-11"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-337')
class TestConversationTreeXj337:
    @allure.story("第337流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_337_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_337_flow(self, case_info):
        """1-6-1-1-7-12"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-338')
class TestConversationTreeXj338:
    @allure.story("第338流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_338_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_338_flow(self, case_info):
        """1-6-1-1-7-13"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-339')
class TestConversationTreeXj339:
    @allure.story("第339流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_339_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_339_flow(self, case_info):
        """1-6-1-1-7-14"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-340')
class TestConversationTreeXj340:
    @allure.story("第340流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_340_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_340_flow(self, case_info):
        """1-6-1-1-7-15"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-341')
class TestConversationTreeXj341:
    @allure.story("第341流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_341_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_341_flow(self, case_info):
        """1-6-1-1-7-16"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-342')
class TestConversationTreeXj342:
    @allure.story("第342流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_342_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_342_flow(self, case_info):
        """1-6-1-1-7-17"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-343')
class TestConversationTreeXj343:
    @allure.story("第343流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_343_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_343_flow(self, case_info):
        """1-6-1-1-7-18"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-344')
class TestConversationTreeXj344:
    @allure.story("第344流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_344_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_344_flow(self, case_info):
        """1-6-1-1-7-19"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-345')
class TestConversationTreeXj345:
    @allure.story("第345流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_345_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_345_flow(self, case_info):
        """1-6-1-1-7-20"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-346')
class TestConversationTreeXj346:
    @allure.story("第346流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_346_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_346_flow(self, case_info):
        """1-6-1-1-7-21"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-347')
class TestConversationTreeXj347:
    @allure.story("第347流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_347_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_347_flow(self, case_info):
        """1-6-1-1-7-22"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-348')
class TestConversationTreeXj348:
    @allure.story("第348流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_348_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_348_flow(self, case_info):
        """1-6-1-1-7-23"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-349')
class TestConversationTreeXj349:
    @allure.story("第349流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_349_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_349_flow(self, case_info):
        """1-6-1-1-7-24"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-518')
class TestConversationTreeXj518:
    @allure.story("第518流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_518_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_518_flow(self, case_info):
        """1-6-1-1-8-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-519')
class TestConversationTreeXj519:
    @allure.story("第519流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_519_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_519_flow(self, case_info):
        """1-6-1-1-8-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-520')
class TestConversationTreeXj520:
    @allure.story("第520流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_520_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_520_flow(self, case_info):
        """1-6-1-1-8-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-521')
class TestConversationTreeXj521:
    @allure.story("第521流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_521_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_521_flow(self, case_info):
        """1-6-1-1-8-4"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-522')
class TestConversationTreeXj522:
    @allure.story("第522流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_522_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_522_flow(self, case_info):
        """1-6-1-1-8-5"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-523')
class TestConversationTreeXj523:
    @allure.story("第523流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_523_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_523_flow(self, case_info):
        """1-6-1-1-8-6"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-524')
class TestConversationTreeXj524:
    @allure.story("第524流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_524_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_524_flow(self, case_info):
        """1-6-1-1-8-7"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-525')
class TestConversationTreeXj525:
    @allure.story("第525流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_525_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_525_flow(self, case_info):
        """1-6-1-1-8-8"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-526')
class TestConversationTreeXj526:
    @allure.story("第526流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_526_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_526_flow(self, case_info):
        """1-6-1-1-8-9"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-527')
class TestConversationTreeXj527:
    @allure.story("第527流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_527_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_527_flow(self, case_info):
        """1-6-1-1-8-10"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-528')
class TestConversationTreeXj528:
    @allure.story("第528流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_528_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_528_flow(self, case_info):
        """1-6-1-1-8-11"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-529')
class TestConversationTreeXj529:
    @allure.story("第529流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_529_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_529_flow(self, case_info):
        """1-6-1-1-8-12"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-530')
class TestConversationTreeXj530:
    @allure.story("第530流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_530_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_530_flow(self, case_info):
        """1-6-1-1-8-13"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-531')
class TestConversationTreeXj531:
    @allure.story("第531流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_531_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_531_flow(self, case_info):
        """1-6-1-1-8-14"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-532')
class TestConversationTreeXj532:
    @allure.story("第532流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_532_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_532_flow(self, case_info):
        """1-6-1-1-8-15"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-533')
class TestConversationTreeXj533:
    @allure.story("第533流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_533_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_533_flow(self, case_info):
        """1-6-1-1-8-16"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-534')
class TestConversationTreeXj534:
    @allure.story("第534流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_534_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_534_flow(self, case_info):
        """1-6-1-1-8-17"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-535')
class TestConversationTreeXj535:
    @allure.story("第535流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_535_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_535_flow(self, case_info):
        """1-6-1-1-8-18"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-536')
class TestConversationTreeXj536:
    @allure.story("第536流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_536_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_536_flow(self, case_info):
        """1-6-1-1-8-19"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-537')
class TestConversationTreeXj537:
    @allure.story("第537流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_537_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_537_flow(self, case_info):
        """1-6-1-1-8-20"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-538')
class TestConversationTreeXj538:
    @allure.story("第538流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_538_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_538_flow(self, case_info):
        """1-6-1-1-8-21"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-539')
class TestConversationTreeXj539:
    @allure.story("第539流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_539_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_539_flow(self, case_info):
        """1-6-1-1-8-22"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-540')
class TestConversationTreeXj540:
    @allure.story("第540流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_540_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_540_flow(self, case_info):
        """1-6-1-1-8-23"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-541')
class TestConversationTreeXj541:
    @allure.story("第541流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_541_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_541_flow(self, case_info):
        """1-6-1-1-8-24"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-542')
class TestConversationTreeXj542:
    @allure.story("第542流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_542_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_542_flow(self, case_info):
        """1-6-1-1-9"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-543')
class TestConversationTreeXj543:
    @allure.story("第543流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_543_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_543_flow(self, case_info):
        """1-6-1-1-10-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-544')
class TestConversationTreeXj544:
    @allure.story("第544流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_544_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_544_flow(self, case_info):
        """1-6-1-1-10-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-545')
class TestConversationTreeXj545:
    @allure.story("第545流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_545_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_545_flow(self, case_info):
        """1-6-1-1-10-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-546')
class TestConversationTreeXj546:
    @allure.story("第546流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_546_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_546_flow(self, case_info):
        """1-6-1-1-10-4"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-547')
class TestConversationTreeXj547:
    @allure.story("第547流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_547_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_547_flow(self, case_info):
        """1-6-1-1-10-5"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-548')
class TestConversationTreeXj548:
    @allure.story("第548流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_548_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_548_flow(self, case_info):
        """1-6-1-1-10-6"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-549')
class TestConversationTreeXj549:
    @allure.story("第549流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_549_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_549_flow(self, case_info):
        """1-6-1-1-10-7"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-550')
class TestConversationTreeXj550:
    @allure.story("第550流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_550_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_550_flow(self, case_info):
        """1-6-1-1-10-8"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-551')
class TestConversationTreeXj551:
    @allure.story("第551流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_551_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_551_flow(self, case_info):
        """1-6-1-1-10-9"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-552')
class TestConversationTreeXj552:
    @allure.story("第552流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_552_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_552_flow(self, case_info):
        """1-6-1-1-10-10"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-553')
class TestConversationTreeXj553:
    @allure.story("第553流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_553_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_553_flow(self, case_info):
        """1-6-1-1-10-11"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-554')
class TestConversationTreeXj554:
    @allure.story("第554流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_554_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_554_flow(self, case_info):
        """1-6-1-1-10-12"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-555')
class TestConversationTreeXj555:
    @allure.story("第555流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_555_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_555_flow(self, case_info):
        """1-6-1-1-10-13"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-556')
class TestConversationTreeXj556:
    @allure.story("第556流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_556_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_556_flow(self, case_info):
        """1-6-1-1-10-14"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-557')
class TestConversationTreeXj557:
    @allure.story("第557流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_557_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_557_flow(self, case_info):
        """1-6-1-1-10-15"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-558')
class TestConversationTreeXj558:
    @allure.story("第558流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_558_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_558_flow(self, case_info):
        """1-6-1-1-10-16"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-559')
class TestConversationTreeXj559:
    @allure.story("第559流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_559_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_559_flow(self, case_info):
        """1-6-1-1-10-17"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-560')
class TestConversationTreeXj560:
    @allure.story("第560流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_560_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_560_flow(self, case_info):
        """1-6-1-1-10-18"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-561')
class TestConversationTreeXj561:
    @allure.story("第561流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_561_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_561_flow(self, case_info):
        """1-6-1-1-10-19"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-562')
class TestConversationTreeXj562:
    @allure.story("第562流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_562_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_562_flow(self, case_info):
        """1-6-1-1-10-20"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-563')
class TestConversationTreeXj563:
    @allure.story("第563流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_563_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_563_flow(self, case_info):
        """1-6-1-1-10-21"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-564')
class TestConversationTreeXj564:
    @allure.story("第564流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_564_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_564_flow(self, case_info):
        """1-6-1-1-10-22"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-565')
class TestConversationTreeXj565:
    @allure.story("第565流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_565_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_565_flow(self, case_info):
        """1-6-1-1-10-23"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-566')
class TestConversationTreeXj566:
    @allure.story("第566流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_566_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_566_flow(self, case_info):
        """1-6-1-1-10-24"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-567')
class TestConversationTreeXj567:
    @allure.story("第567流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_567_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_567_flow(self, case_info):
        """1-6-1-1-11-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-568')
class TestConversationTreeXj568:
    @allure.story("第568流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_568_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_568_flow(self, case_info):
        """1-6-1-1-11-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-569')
class TestConversationTreeXj569:
    @allure.story("第569流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_569_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_569_flow(self, case_info):
        """1-6-1-1-11-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-570')
class TestConversationTreeXj570:
    @allure.story("第570流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_570_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_570_flow(self, case_info):
        """1-6-1-1-11-4"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-571')
class TestConversationTreeXj571:
    @allure.story("第571流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_571_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_571_flow(self, case_info):
        """1-6-1-1-11-5"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-572')
class TestConversationTreeXj572:
    @allure.story("第572流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_572_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_572_flow(self, case_info):
        """1-6-1-1-11-6"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-573')
class TestConversationTreeXj573:
    @allure.story("第573流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_573_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_573_flow(self, case_info):
        """1-6-1-1-11-7"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-574')
class TestConversationTreeXj574:
    @allure.story("第574流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_574_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_574_flow(self, case_info):
        """1-6-1-1-11-8"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-575')
class TestConversationTreeXj575:
    @allure.story("第575流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_575_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_575_flow(self, case_info):
        """1-6-1-1-11-9"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-576')
class TestConversationTreeXj576:
    @allure.story("第576流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_576_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_576_flow(self, case_info):
        """1-6-1-1-11-10"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-577')
class TestConversationTreeXj577:
    @allure.story("第577流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_577_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_577_flow(self, case_info):
        """1-6-1-1-11-11"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-578')
class TestConversationTreeXj578:
    @allure.story("第578流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_578_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_578_flow(self, case_info):
        """1-6-1-1-11-12"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-579')
class TestConversationTreeXj579:
    @allure.story("第579流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_579_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_579_flow(self, case_info):
        """1-6-1-1-11-13"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-580')
class TestConversationTreeXj580:
    @allure.story("第580流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_580_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_580_flow(self, case_info):
        """1-6-1-1-11-14"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-581')
class TestConversationTreeXj581:
    @allure.story("第581流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_581_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_581_flow(self, case_info):
        """1-6-1-1-11-15"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-582')
class TestConversationTreeXj582:
    @allure.story("第582流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_582_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_582_flow(self, case_info):
        """1-6-1-1-11-16"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-583')
class TestConversationTreeXj583:
    @allure.story("第583流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_583_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_583_flow(self, case_info):
        """1-6-1-1-11-17"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-584')
class TestConversationTreeXj584:
    @allure.story("第584流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_584_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_584_flow(self, case_info):
        """1-6-1-1-11-18"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-585')
class TestConversationTreeXj585:
    @allure.story("第585流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_585_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_585_flow(self, case_info):
        """1-6-1-1-11-19"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-586')
class TestConversationTreeXj586:
    @allure.story("第586流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_586_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_586_flow(self, case_info):
        """1-6-1-1-11-20"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-587')
class TestConversationTreeXj587:
    @allure.story("第587流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_587_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_587_flow(self, case_info):
        """1-6-1-1-11-21"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-588')
class TestConversationTreeXj588:
    @allure.story("第588流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_588_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_588_flow(self, case_info):
        """1-6-1-1-11-22"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-589')
class TestConversationTreeXj589:
    @allure.story("第589流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_589_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_589_flow(self, case_info):
        """1-6-1-1-11-23"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-590')
class TestConversationTreeXj590:
    @allure.story("第590流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_590_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_590_flow(self, case_info):
        """1-6-1-1-11-24"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-591')
class TestConversationTreeXj591:
    @allure.story("第591流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_591_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_591_flow(self, case_info):
        """1-6-1-1-12"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-592')
class TestConversationTreeXj592:
    @allure.story("第592流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_592_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_592_flow(self, case_info):
        """1-6-1-1-13-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-593')
class TestConversationTreeXj593:
    @allure.story("第593流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_593_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_593_flow(self, case_info):
        """1-6-1-1-13-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-594')
class TestConversationTreeXj594:
    @allure.story("第594流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_594_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_594_flow(self, case_info):
        """1-6-1-1-13-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-595')
class TestConversationTreeXj595:
    @allure.story("第595流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_595_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_595_flow(self, case_info):
        """1-6-1-1-13-4"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-596')
class TestConversationTreeXj596:
    @allure.story("第596流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_596_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_596_flow(self, case_info):
        """1-6-1-1-13-5"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-597')
class TestConversationTreeXj597:
    @allure.story("第597流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_597_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_597_flow(self, case_info):
        """1-6-1-1-13-6"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-598')
class TestConversationTreeXj598:
    @allure.story("第598流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_598_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_598_flow(self, case_info):
        """1-6-1-1-13-7"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-599')
class TestConversationTreeXj599:
    @allure.story("第599流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_599_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_599_flow(self, case_info):
        """1-6-1-1-13-8"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-600')
class TestConversationTreeXj600:
    @allure.story("第600流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_600_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_600_flow(self, case_info):
        """1-6-1-1-13-9"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-601')
class TestConversationTreeXj601:
    @allure.story("第601流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_601_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_601_flow(self, case_info):
        """1-6-1-1-13-10"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-602')
class TestConversationTreeXj602:
    @allure.story("第602流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_602_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_602_flow(self, case_info):
        """1-6-1-1-13-11"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-603')
class TestConversationTreeXj603:
    @allure.story("第603流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_603_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_603_flow(self, case_info):
        """1-6-1-1-13-12"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-604')
class TestConversationTreeXj604:
    @allure.story("第604流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_604_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_604_flow(self, case_info):
        """1-6-1-1-13-13"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-605')
class TestConversationTreeXj605:
    @allure.story("第605流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_605_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_605_flow(self, case_info):
        """1-6-1-1-13-14"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-606')
class TestConversationTreeXj606:
    @allure.story("第606流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_606_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_606_flow(self, case_info):
        """1-6-1-1-13-15"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-607')
class TestConversationTreeXj607:
    @allure.story("第607流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_607_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_607_flow(self, case_info):
        """1-6-1-1-13-16"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-608')
class TestConversationTreeXj608:
    @allure.story("第608流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_608_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_608_flow(self, case_info):
        """1-6-1-1-13-17"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-609')
class TestConversationTreeXj609:
    @allure.story("第609流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_609_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_609_flow(self, case_info):
        """1-6-1-1-13-18"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-610')
class TestConversationTreeXj610:
    @allure.story("第610流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_610_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_610_flow(self, case_info):
        """1-6-1-1-13-19"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-611')
class TestConversationTreeXj611:
    @allure.story("第611流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_611_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_611_flow(self, case_info):
        """1-6-1-1-13-20"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-612')
class TestConversationTreeXj612:
    @allure.story("第612流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_612_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_612_flow(self, case_info):
        """1-6-1-1-13-21"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-613')
class TestConversationTreeXj613:
    @allure.story("第613流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_613_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_613_flow(self, case_info):
        """1-6-1-1-13-22"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-614')
class TestConversationTreeXj614:
    @allure.story("第614流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_614_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_614_flow(self, case_info):
        """1-6-1-1-13-23"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-615')
class TestConversationTreeXj615:
    @allure.story("第615流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_615_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_615_flow(self, case_info):
        """1-6-1-1-13-24"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-616')
class TestConversationTreeXj616:
    @allure.story("第616流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_616_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_616_flow(self, case_info):
        """1-6-1-1-14-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-617')
class TestConversationTreeXj617:
    @allure.story("第617流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_617_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_617_flow(self, case_info):
        """1-6-1-1-14-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-618')
class TestConversationTreeXj618:
    @allure.story("第618流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_618_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_618_flow(self, case_info):
        """1-6-1-1-14-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-619')
class TestConversationTreeXj619:
    @allure.story("第619流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_619_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_619_flow(self, case_info):
        """1-6-1-1-14-4"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-620')
class TestConversationTreeXj620:
    @allure.story("第620流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_620_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_620_flow(self, case_info):
        """1-6-1-1-14-5"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-621')
class TestConversationTreeXj621:
    @allure.story("第621流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_621_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_621_flow(self, case_info):
        """1-6-1-1-14-6"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-622')
class TestConversationTreeXj622:
    @allure.story("第622流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_622_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_622_flow(self, case_info):
        """1-6-1-1-14-7"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-623')
class TestConversationTreeXj623:
    @allure.story("第623流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_623_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_623_flow(self, case_info):
        """1-6-1-1-14-8"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-624')
class TestConversationTreeXj624:
    @allure.story("第624流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_624_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_624_flow(self, case_info):
        """1-6-1-1-14-9"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-625')
class TestConversationTreeXj625:
    @allure.story("第625流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_625_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_625_flow(self, case_info):
        """1-6-1-1-14-10"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-626')
class TestConversationTreeXj626:
    @allure.story("第626流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_626_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_626_flow(self, case_info):
        """1-6-1-1-14-11"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-627')
class TestConversationTreeXj627:
    @allure.story("第627流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_627_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_627_flow(self, case_info):
        """1-6-1-1-14-12"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-628')
class TestConversationTreeXj628:
    @allure.story("第628流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_628_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_628_flow(self, case_info):
        """1-6-1-1-14-13"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-629')
class TestConversationTreeXj629:
    @allure.story("第629流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_629_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_629_flow(self, case_info):
        """1-6-1-1-14-14"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-630')
class TestConversationTreeXj630:
    @allure.story("第630流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_630_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_630_flow(self, case_info):
        """1-6-1-1-14-15"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-631')
class TestConversationTreeXj631:
    @allure.story("第631流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_631_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_631_flow(self, case_info):
        """1-6-1-1-14-16"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-632')
class TestConversationTreeXj632:
    @allure.story("第632流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_632_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_632_flow(self, case_info):
        """1-6-1-1-14-17"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-633')
class TestConversationTreeXj633:
    @allure.story("第633流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_633_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_633_flow(self, case_info):
        """1-6-1-1-14-18"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-634')
class TestConversationTreeXj634:
    @allure.story("第634流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_634_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_634_flow(self, case_info):
        """1-6-1-1-14-19"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-635')
class TestConversationTreeXj635:
    @allure.story("第635流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_635_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_635_flow(self, case_info):
        """1-6-1-1-14-20"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-636')
class TestConversationTreeXj636:
    @allure.story("第636流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_636_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_636_flow(self, case_info):
        """1-6-1-1-14-21"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-637')
class TestConversationTreeXj637:
    @allure.story("第637流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_637_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_637_flow(self, case_info):
        """1-6-1-1-14-22"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-638')
class TestConversationTreeXj638:
    @allure.story("第638流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_638_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_638_flow(self, case_info):
        """1-6-1-1-14-23"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-639')
class TestConversationTreeXj639:
    @allure.story("第639流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_639_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_639_flow(self, case_info):
        """1-6-1-1-14-24"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-640')
class TestConversationTreeXj640:
    @allure.story("第640流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_640_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_640_flow(self, case_info):
        """1-6-1-1-15-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-641')
class TestConversationTreeXj641:
    @allure.story("第641流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_641_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_641_flow(self, case_info):
        """1-6-1-1-15-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-642')
class TestConversationTreeXj642:
    @allure.story("第642流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_642_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_642_flow(self, case_info):
        """1-6-1-1-15-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-643')
class TestConversationTreeXj643:
    @allure.story("第643流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_643_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_643_flow(self, case_info):
        """1-6-1-1-15-4"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-644')
class TestConversationTreeXj644:
    @allure.story("第644流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_644_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_644_flow(self, case_info):
        """1-6-1-1-15-5"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-645')
class TestConversationTreeXj645:
    @allure.story("第645流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_645_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_645_flow(self, case_info):
        """1-6-1-1-15-6"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-646')
class TestConversationTreeXj646:
    @allure.story("第646流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_646_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_646_flow(self, case_info):
        """1-6-1-1-15-7"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-647')
class TestConversationTreeXj647:
    @allure.story("第647流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_647_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_647_flow(self, case_info):
        """1-6-1-1-15-8"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-648')
class TestConversationTreeXj648:
    @allure.story("第648流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_648_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_648_flow(self, case_info):
        """1-6-1-1-15-9"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-649')
class TestConversationTreeXj649:
    @allure.story("第649流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_649_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_649_flow(self, case_info):
        """1-6-1-1-15-10"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-650')
class TestConversationTreeXj650:
    @allure.story("第650流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_650_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_650_flow(self, case_info):
        """1-6-1-1-15-11"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-651')
class TestConversationTreeXj651:
    @allure.story("第651流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_651_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_651_flow(self, case_info):
        """1-6-1-1-15-12"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-652')
class TestConversationTreeXj652:
    @allure.story("第652流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_652_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_652_flow(self, case_info):
        """1-6-1-1-15-13"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-653')
class TestConversationTreeXj653:
    @allure.story("第653流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_653_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_653_flow(self, case_info):
        """1-6-1-1-15-14"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-654')
class TestConversationTreeXj654:
    @allure.story("第654流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_654_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_654_flow(self, case_info):
        """1-6-1-1-15-15"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-655')
class TestConversationTreeXj655:
    @allure.story("第655流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_655_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_655_flow(self, case_info):
        """1-6-1-1-15-16"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-656')
class TestConversationTreeXj656:
    @allure.story("第656流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_656_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_656_flow(self, case_info):
        """1-6-1-1-15-17"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-657')
class TestConversationTreeXj657:
    @allure.story("第657流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_657_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_657_flow(self, case_info):
        """1-6-1-1-15-18"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-658')
class TestConversationTreeXj658:
    @allure.story("第658流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_658_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_658_flow(self, case_info):
        """1-6-1-1-15-19"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-659')
class TestConversationTreeXj659:
    @allure.story("第659流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_659_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_659_flow(self, case_info):
        """1-6-1-1-15-20"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-660')
class TestConversationTreeXj660:
    @allure.story("第660流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_660_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_660_flow(self, case_info):
        """1-6-1-1-15-21"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-661')
class TestConversationTreeXj661:
    @allure.story("第661流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_661_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_661_flow(self, case_info):
        """1-6-1-1-15-22"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-662')
class TestConversationTreeXj662:
    @allure.story("第662流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_662_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_662_flow(self, case_info):
        """1-6-1-1-15-23"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-663')
class TestConversationTreeXj663:
    @allure.story("第663流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_663_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_663_flow(self, case_info):
        """1-6-1-1-15-24"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-664')
class TestConversationTreeXj664:
    @allure.story("第664流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_664_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_664_flow(self, case_info):
        """1-6-1-1-16"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-665')
class TestConversationTreeXj665:
    @allure.story("第665流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_665_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_665_flow(self, case_info):
        """1-6-1-1-17-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-666')
class TestConversationTreeXj666:
    @allure.story("第666流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_666_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_666_flow(self, case_info):
        """1-6-1-1-17-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-667')
class TestConversationTreeXj667:
    @allure.story("第667流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_667_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_667_flow(self, case_info):
        """1-6-1-1-17-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-668')
class TestConversationTreeXj668:
    @allure.story("第668流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_668_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_668_flow(self, case_info):
        """1-6-1-1-17-4"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-669')
class TestConversationTreeXj669:
    @allure.story("第669流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_669_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_669_flow(self, case_info):
        """1-6-1-1-17-5"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-670')
class TestConversationTreeXj670:
    @allure.story("第670流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_670_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_670_flow(self, case_info):
        """1-6-1-1-17-6"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-671')
class TestConversationTreeXj671:
    @allure.story("第671流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_671_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_671_flow(self, case_info):
        """1-6-1-1-17-7"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-672')
class TestConversationTreeXj672:
    @allure.story("第672流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_672_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_672_flow(self, case_info):
        """1-6-1-1-17-8"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-673')
class TestConversationTreeXj673:
    @allure.story("第673流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_673_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_673_flow(self, case_info):
        """1-6-1-1-17-9"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-674')
class TestConversationTreeXj674:
    @allure.story("第674流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_674_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_674_flow(self, case_info):
        """1-6-1-1-17-10"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-675')
class TestConversationTreeXj675:
    @allure.story("第675流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_675_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_675_flow(self, case_info):
        """1-6-1-1-17-11"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-676')
class TestConversationTreeXj676:
    @allure.story("第676流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_676_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_676_flow(self, case_info):
        """1-6-1-1-17-12"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-677')
class TestConversationTreeXj677:
    @allure.story("第677流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_677_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_677_flow(self, case_info):
        """1-6-1-1-17-13"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-678')
class TestConversationTreeXj678:
    @allure.story("第678流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_678_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_678_flow(self, case_info):
        """1-6-1-1-17-14"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-679')
class TestConversationTreeXj679:
    @allure.story("第679流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_679_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_679_flow(self, case_info):
        """1-6-1-1-17-15"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-680')
class TestConversationTreeXj680:
    @allure.story("第680流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_680_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_680_flow(self, case_info):
        """1-6-1-1-17-16"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-681')
class TestConversationTreeXj681:
    @allure.story("第681流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_681_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_681_flow(self, case_info):
        """1-6-1-1-17-17"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-682')
class TestConversationTreeXj682:
    @allure.story("第682流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_682_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_682_flow(self, case_info):
        """1-6-1-1-17-18"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-683')
class TestConversationTreeXj683:
    @allure.story("第683流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_683_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_683_flow(self, case_info):
        """1-6-1-1-17-19"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-684')
class TestConversationTreeXj684:
    @allure.story("第684流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_684_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_684_flow(self, case_info):
        """1-6-1-1-17-20"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-685')
class TestConversationTreeXj685:
    @allure.story("第685流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_685_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_685_flow(self, case_info):
        """1-6-1-1-17-21"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-686')
class TestConversationTreeXj686:
    @allure.story("第686流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_686_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_686_flow(self, case_info):
        """1-6-1-1-17-22"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-687')
class TestConversationTreeXj687:
    @allure.story("第687流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_687_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_687_flow(self, case_info):
        """1-6-1-1-17-23"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-688')
class TestConversationTreeXj688:
    @allure.story("第688流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_688_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_688_flow(self, case_info):
        """1-6-1-1-17-24"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-689')
class TestConversationTreeXj689:
    @allure.story("第689流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_689_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_689_flow(self, case_info):
        """1-6-1-1-18"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-690')
class TestConversationTreeXj690:
    @allure.story("第690流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_690_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_690_flow(self, case_info):
        """1-6-1-1-19"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-691')
class TestConversationTreeXj691:
    @allure.story("第691流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_691_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_691_flow(self, case_info):
        """1-6-1-1-20"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-692')
class TestConversationTreeXj692:
    @allure.story("第692流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_692_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_692_flow(self, case_info):
        """1-6-1-1-21"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-693')
class TestConversationTreeXj693:
    @allure.story("第693流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_693_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_693_flow(self, case_info):
        """1-6-1-1-22"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-694')
class TestConversationTreeXj694:
    @allure.story("第694流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_694_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_694_flow(self, case_info):
        """1-6-1-1-23"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-695')
class TestConversationTreeXj695:
    @allure.story("第695流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_695_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_695_flow(self, case_info):
        """1-6-1-1-24"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-696')
class TestConversationTreeXj696:
    """Q6"""
    @allure.story("第696流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_696_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_696_flow(self, case_info):
        """1-6-1-1-4-1"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-697')
class TestConversationTreeXj697:
    @allure.story("第697流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_697_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_697_flow(self, case_info):
        """1-6-1-1-4-2"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-698')
class TestConversationTreeXj698:
    @allure.story("第698流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_698_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_698_flow(self, case_info):
        """1-6-1-1-4-3"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-699')
class TestConversationTreeXj699:
    @allure.story("第699流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_699_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_699_flow(self, case_info):
        """1-6-1-1-4-4"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-700')
class TestConversationTreeXj700:
    @allure.story("第700流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_700_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_700_flow(self, case_info):
        """1-6-1-1-4-5"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-701')
class TestConversationTreeXj701:
    @allure.story("第701流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_701_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_701_flow(self, case_info):
        """1-6-1-1-4-6"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-702')
class TestConversationTreeXj702:
    @allure.story("第702流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_702_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_702_flow(self, case_info):
        """1-6-1-1-4-7"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-703')
class TestConversationTreeXj703:
    @allure.story("第703流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_703_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_703_flow(self, case_info):
        """1-6-1-1-4-8"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-704')
class TestConversationTreeXj704:
    @allure.story("第704流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_704_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_704_flow(self, case_info):
        """1-6-1-1-4-9"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-705')
class TestConversationTreeXj705:
    @allure.story("第705流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_705_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_705_flow(self, case_info):
        """1-6-1-1-4-10"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-706')
class TestConversationTreeXj706:
    @allure.story("第706流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_706_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_706_flow(self, case_info):
        """1-6-1-1-4-11"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-707')
class TestConversationTreeXj707:
    @allure.story("第707流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_707_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_707_flow(self, case_info):
        """1-6-1-1-4-12"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-708')
class TestConversationTreeXj708:
    @allure.story("第708流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_708_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_708_flow(self, case_info):
        """1-6-1-1-4-13"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-709')
class TestConversationTreeXj709:
    @allure.story("第709流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_709_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_709_flow(self, case_info):
        """1-6-1-1-4-14"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-710')
class TestConversationTreeXj710:
    @allure.story("第710流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_710_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_710_flow(self, case_info):
        """1-6-1-1-4-15"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-711')
class TestConversationTreeXj711:
    @allure.story("第711流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_711_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_711_flow(self, case_info):
        """1-6-1-1-4-16"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-712')
class TestConversationTreeXj712:
    @allure.story("第712流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_712_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_712_flow(self, case_info):
        """1-6-1-1-4-17"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-713')
class TestConversationTreeXj713:
    @allure.story("第713流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_713_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_713_flow(self, case_info):
        """1-6-1-1-4-18"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-714')
class TestConversationTreeXj714:
    @allure.story("第714流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_714_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_714_flow(self, case_info):
        """1-6-1-1-4-19"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-715')
class TestConversationTreeXj715:
    @allure.story("第715流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_715_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_715_flow(self, case_info):
        """1-6-1-1-4-20"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-716')
class TestConversationTreeXj716:
    @allure.story("第716流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_716_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_716_flow(self, case_info):
        """1-6-1-1-4-21"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-717')
class TestConversationTreeXj717:
    @allure.story("第717流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_717_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_717_flow(self, case_info):
        """1-6-1-1-4-22"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-718')
class TestConversationTreeXj718:
    @allure.story("第718流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_718_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_718_flow(self, case_info):
        """1-6-1-1-4-23"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)


@pytest.mark.usefixtures("connection2112")
@allure.feature('测试对话树2112-719')
class TestConversationTreeXj719:
    @allure.story("第719流程")
    @pytest.mark.parametrize('case_info', read_case('./TestCases/2112/test_2112_719_flow.yaml'))
    @pytest.mark.all
    @pytest.mark.t2112
    def test_2112_719_flow(self, case_info):
        """1-6-1-1-4-24"""
        RequestsUtil(parameterize_util).standard_yaml(case_info)

