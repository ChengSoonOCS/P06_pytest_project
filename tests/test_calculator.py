from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_sub(self):
        #arrange
        a = 5555
        b = 4321
        cal = Calculator()

        #act
        result = cal.subtract(a, b)

        #assert
        expected = 1234
        assert result == expected
    
    def test_mul(self):
        #arrange
        a = 1234
        b = 4.5016207455429497568881685575365
        cal = Calculator()

        #act
        result = cal.multiply(a, b)

        #assert
        expected = 5555
        assert result == expected

    def test_div(self):
        #arrange
        a = 5555
        b = 4.5016207455429497568881685575365
        cal = Calculator()

        #act
        result = cal.divide(a,b)

        #assert
        excepted = 1234
        assert result == excepted