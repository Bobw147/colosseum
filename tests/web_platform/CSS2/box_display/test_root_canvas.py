from ....utils import W3CTestCase

class TestRootCanvas(W3CTestCase):
    vars().update(W3CTestCase.find_tests(__file__, 'root-canvas-'))
