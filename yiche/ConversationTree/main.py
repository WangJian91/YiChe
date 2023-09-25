import os
import time
import pytest

# pytest.main(['-m all'])
# pytest.main(['-m t2112'])
pytest.main(['-m debug'])
# pytest.main(['-m t31'])
# times = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
# os.system("allure generate ./Reports/temps -o ./Reports/reports_" + '_' + times + " --clean")
