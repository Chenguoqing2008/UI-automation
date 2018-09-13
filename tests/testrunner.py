#! /usr/bin/python3
# _*_ coding:utf-8 _*_


from unittest import TestLoader, TestSuite, TextTestRunner
# from tests.SM.test_sm_dashboard import SMDashBoardTest
from tests.IM.im_mainpage import IMMainPageTest
from tests.DM.dm_dashboard import DMDashBoardTest
from tests.SA.sa_homepage import SAHomePageTest
# from concurrencytest import ConcurrentTestSuite, fork_for_tests
# from testtools import ConcurrentStreamTestSuite
# import testtools as testtools


def main():

    loader = TestLoader()
    suite = TestSuite((loader.loadTestsFromTestCase(SAHomePageTest),
                       # loader.loadTestsFromTestCase(SMDashBoardTest),
                       loader.loadTestsFromTestCase(IMMainPageTest),
                       loader.loadTestsFromTestCase(DMDashBoardTest)
                       ))

    with open('UnittestTextReport.html', 'a') as f:
        runner = TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)

    # concurrent_suite = ConcurrentTestSuite(suite, fork_for_tests(1))
    # runner.run(concurrent_suite)

    # concurrent_suite = ConcurrentStreamTestSuite(lambda: ((case, None) for case in suite))
    # concurrent_suite.run(testtools.StreamResult())


if __name__ == "__main__":
    main()
