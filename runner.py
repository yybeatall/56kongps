import loginsucc,pickup
import unittest

#mysuite = unittest.TestSuite()
#mysuite.addTest(unittestdemo.MyTestCase("testLogInFailed"))
#mysuite.addTest(unittestdemo.MyTestCase("testLogInOK"))
cases = unittest.TestLoader().loadTestsFromTestCase(loginsucc.MyTestCase)
cases2 = unittest.TestLoader().loadTestsFromTestCase(pickup.MyTestCase)

mysuite = unittest.TestSuite([cases,cases2])
#mysuite.addTest(unittestdemo.MyTestCase("testLogIn"))

myrunner = unittest.TextTestRunner(verbosity=2)
myrunner.run(mysuite)