import os
from unittest import TestSuite, TestLoader

from HTMLTestRunner.HTMLTestRunner import HTMLTestRunner

s = TestSuite()

s.addTests(TestLoader().discover(os.getcwd()))

print(os.getcwd())
# with open(os.getcwd() + 'test_report.html', 'w', encoding="utf-8") as fp:
#     run = HTMLTestRunner(
#         stream=fp,
#         verbosity=1,
#         title="测试报告标题",
#         description="测试报告描述信息"
#     )
#     run.run(s)
