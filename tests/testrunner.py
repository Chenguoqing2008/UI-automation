#! /usr/bin/python3
# _*_ coding:utf-8 _*_


from unittest import TestLoader, TestSuite, TextTestRunner
from tests.SM.sm_dashboard import SMDashBoardPage
from concurrencytest import ConcurrentTestSuite, fork_for_tests
from testtools import ConcurrentStreamTestSuite
import testtools as testtools


def main():

    loader = TestLoader()
    suite = TestSuite(loader.loadTestsFromTestCase(SMDashBoardPage))
    runner = TextTestRunner(verbosity=2)

    runner.run(suite)

    # concurrent_suite = ConcurrentTestSuite(suite, fork_for_tests(1))
    # runner.run(concurrent_suite)

    # concurrent_suite = ConcurrentStreamTestSuite(lambda: ((case, None) for case in suite))
    # concurrent_suite.run(testtools.StreamResult)


if __name__ == "__main__":
    main()
