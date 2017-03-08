import unittest
import fstrings
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
from fstrings import f, fdocstring, printf


URL = '/api/v1.0'
NUM = 10
class OBJ: NUM = 20
STRING = 'STRING'


class Test_f(unittest.TestCase):

    def test_args_kwargs(self):
        '''f format with args kwargs'''

        class LCLOBJ: NUM = 20
        expected = '/api/v1.0/10/STRING/020'
        result = f(
            '{}/{}/{STRING}/{OBJ.NUM:0>3}',
            '/api/v1.0',
            '10',
            STRING='STRING',
            OBJ=LCLOBJ
        )
        assert result == expected

    def test_locals(self):
        '''f format with locals'''

        URL = '/api/v2.0'
        NUM = 20
        class OBJ: NUM = 40
        STRING = 'LCLSTRING'

        expected = '/api/v2.0/20/LCLSTRING/040'
        result = f('{URL}/{NUM}/{STRING}/{OBJ.NUM:0>3}')
        assert result == expected

    def test_globals(self):
        '''f format with globals'''

        expected = '/api/v1.0/10/STRING/020'
        result = f('{URL}/{NUM}/{STRING}/{OBJ.NUM:0>3}')
        assert result == expected

    def test_override(self):
        '''f format with keyword override'''

        expected = '/api/v1.0/10/FUNKY/020'
        result = f('{URL}/{NUM}/{STRING}/{OBJ.NUM:0>3}', STRING='FUNKY')
        assert result == expected


class Test_fdocstring(unittest.TestCase):

    def test_fn_args_kwargs(self):
        '''fdocstring func with args kwargs'''

        class OOBJ: NUM = 40

        expected = '/api/v2.0/20/OVRSTRING/040'

        @fdocstring('/api/v2.0', 20, STRING='OVRSTRING', OBJ=OOBJ)
        def func():
            '''{}/{}/{STRING}/{OBJ.NUM:0>3}'''

        assert func.__doc__ == expected

    def test_cls_args_kwargs(self):
        '''fdocstring class with args kwargs'''

        class OOBJ: NUM = 40

        expected = '/api/v2.0/20/OVRSTRING/040'

        @fdocstring('/api/v2.0', 20, STRING='OVRSTRING', OBJ=OOBJ)
        class obj(object):
            '''{}/{}/{STRING}/{OBJ.NUM:0>3}'''

            def method(self):
                '''{}/{}/{STRING}/{OBJ.NUM:0>3}'''

        assert obj.__doc__ == expected
        assert obj.method.__doc__ == expected

    def test_fn_locals(self):
        '''fdocstring func with locals'''

        URL = '/api/v2.0'
        NUM = 20
        class OBJ: NUM = 40
        STRING = 'LCLSTRING'

        expected = '/api/v2.0/20/LCLSTRING/040'

        @fdocstring()
        def func():
            '''{URL}/{NUM}/{STRING}/{OBJ.NUM:0>3}'''

        assert func.__doc__ == expected

    def test_fn_globals(self):
        '''fdocstring func with globals'''

        expected = '/api/v1.0/10/STRING/020'

        @fdocstring()
        def func():
            '''{URL}/{NUM}/{STRING}/{OBJ.NUM:0>3}'''

        assert func.__doc__ == expected

    def test_cls_globals(self):
        '''fdocstring class with globals'''

        expected = '/api/v1.0/10/STRING/020'

        @fdocstring()
        class obj(object):
            '''{URL}/{NUM}/{STRING}/{OBJ.NUM:0>3}'''

            def method(self):
                '''{URL}/{NUM}/{STRING}/{OBJ.NUM:0>3}'''

        assert obj.__doc__ == expected
        assert obj.method.__doc__ == expected

    def test_cls_locals(self):
        '''fdocstring class with locals'''

        URL = '/api/v2.0'
        NUM = 20
        class OBJ: NUM = 40
        STRING = 'LCLSTRING'

        expected = '/api/v2.0/20/LCLSTRING/040'

        @fdocstring()
        class obj(object):
            '''{URL}/{NUM}/{STRING}/{OBJ.NUM:0>3}'''

            def method(self):
                '''{URL}/{NUM}/{STRING}/{OBJ.NUM:0>3}'''

        assert obj.__doc__ == expected
        assert obj.method.__doc__ == expected


class Test_printf(unittest.TestCase):

    def setUp(self):
        self.stream = StringIO()

    def tearDown(self):
        self.stream.close()
        self.stream = None

    def test_printf_args_kwargs(self):
        '''printf args kwargs'''

        class OOBJ: NUM = 40
        expected = '/api/v2.0/20/LCLSTRING/040\n'
        printf(
            '{}/{}/{STRING}/{OBJ.NUM:0>3}',
            '/api/v2.0',
            20,
            STRING='OVRSTRING',
            OBJ=OOBJ,
            _stream_=self.stream,
        )


    def test_printf_locals(self):
        '''printf locals'''

        URL = '/api/v2.0'
        NUM = 20
        class OBJ: NUM = 40
        STRING = 'LCLSTRING'

        expected = '/api/v2.0/20/LCLSTRING/040\n'
        printf('{URL}/{NUM}/{STRING}/{OBJ.NUM:0>3}', _stream_=self.stream)
        result = self.stream.getvalue()
        assert result == expected

    def test_printf_globals(self):
        '''printf globals'''

        expected = '/api/v1.0/10/STRING/020\n'
        printf('{URL}/{NUM}/{STRING}/{OBJ.NUM:0>3}', _stream_=self.stream)
        assert self.stream.getvalue() == expected


if __name__ == '__main__':

    doctest.testmod(fstrings)
    unittest.main(verbosity=2)
