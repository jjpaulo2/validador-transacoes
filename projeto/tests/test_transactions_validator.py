import pytest, unittest
from transactions_validator import validator, exceptions
from .fixtures.fixture_transaction_validator import ( ChallengeFixtures, 
                                                      CompromisedIncomeFixtures, 
                                                      LowScoreFixtures,
                                                      DoubleTransactionsFixtures,
                                                      MinimumInstallmentsFixtures ) 

class TestTransactionsValidatorExceptionExpected(unittest.TestCase):
    """
    Class de testes do módulo `transactions_validator` que contém os
    testes de casos onde é esperado o lançamento de exceções.
    """

    def setUp(self):
        """
        Configuração inicial antes da execução dos testes.
        """

        self.validator = validator.Validator()


    def test_low_score(self):
        """
        Método que testa os casos em que é esperada que a exceção
        `LowScoreException` seja lançada.
        """

        with pytest.raises(exceptions.LowScoreException):
            self.validator.validateMany(LowScoreFixtures.use_cases_exception)


    def test_compromised_income(self):
        """
        Método que testa os casos em que é esperada que a exceção
        `CompromisedIncomeException` seja lançada.
        """

        with pytest.raises(exceptions.CompromisedIncomeException):
            self.validator.validateMany(CompromisedIncomeFixtures.use_cases_exception)


    def test_minimum_installments(self):
        """
        Método que testa os casos em que é esperada que a exceção
        `MinimumInstallmentsException` seja lançada.
        """

        with pytest.raises(exceptions.MinimumInstallmentsException):
            self.validator.validateMany(MinimumInstallmentsFixtures.use_cases_exception)


    def test_double_transactions(self):
        """
        Método que testa os casos em que é esperada que a exceção
        `DoubleTransactionsException` seja lançada.
        """

        with pytest.raises(exceptions.DoubleTransactionsException):
            self.validator.validateMany(DoubleTransactionsFixtures.use_cases_exception)


class TestTransactionsValidatorExceptionNotExpected(unittest.TestCase):
    """
    Class de testes do módulo `transactions_validator` que contém os
    testes de casos onde não é esperado o lançamento de exceções.
    """

    def setUp(self):
        """
        Configuração inicial antes da execução dos testes.
        """

        self.validator = validator.Validator()


    def test_low_score(self):
        """
        Método que testa os casos em que é esperada que a exceção
        `LowScoreException` não seja lançada.
        """

        raised = False
        try:
            self.validator.validateMany(LowScoreFixtures.use_cases_no_exception)
        except exceptions.LowScoreException:
            raised = True

        self.assertFalse(raised)


    def test_compromised_income(self):
        """
        Método que testa os casos em que é esperada que a exceção
        `CompromisedIncomeException` não seja lançada.
        """

        raised = False
        try:
            self.validator.validateMany(CompromisedIncomeFixtures.use_cases_no_exception)
        except exceptions.CompromisedIncomeException:
            raised = True

        self.assertFalse(raised)


    def test_minimum_installments(self):
        """
        Método que testa os casos em que é esperada que a exceção
        `MinimumInstallmentsException` não seja lançada.
        """

        raised = False
        try:
            self.validator.validateMany(MinimumInstallmentsFixtures.use_cases_no_exception)
        except exceptions.MinimumInstallmentsException:
            raised = True

        self.assertFalse(raised)


    def test_double_transactions(self):
        """
        Método que testa os casos em que é esperada que a exceção
        `DoubleTransactionsException` não seja lançada.
        """

        raised = False
        try:
            self.validator.validateMany(DoubleTransactionsFixtures.use_cases_no_exception)
        except exceptions.DoubleTransactionsException:
            raised = True

        self.assertFalse(raised)

