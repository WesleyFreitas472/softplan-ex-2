import unittest
from API.app.validatorPayload import isValidPayload
from API.app.models import Value
from API import app


class TestValidator(unittest.TestCase):

    def testIfPayloadValidatorWorks(self):
        payloadExpected = {'name': str(), 'age': int()}
        payloadPassed = {'name': 'Wesley', 'age': 25}
        self.assertEqual(True, isValidPayload(payloadPassed, payloadExpected))

    def testIfModelCalculateRight(self):
        value = Value(amount=100)
        tax = 100.0
        self.assertEqual(200, value.getValueWithTaxes(tax))

    def testIfTaxIsNotFloatShowRaiseTypeError(self):
        value = Value(amount=100)
        tax = '100.0'
        with self.assertRaises(TypeError):
            value.getValueWithTaxes(tax)


class TestAPI(unittest.TestCase):

    def testIfAPIReturnsLikeProposedInChallenge(self):
        payload = {"amount": 10000, "tax": 2.2}
        with app.test_client() as client:
            response = client.post('/valueWithTaxes', json=payload)
        self.assertEqual(200, response.status_code)
        self.assertEqual(10220.00, response.json['valueWithTaxes'])

    def testIfClientPassParameterWithWrongType(self):
        payload = {"amount": 10000, "tax": 2}
        with app.test_client() as client:
            response = client.post('/valueWithTaxes', json=payload)
        self.assertEqual(400, response.status_code)

    def testIfClientDontPassPayload(self):
        with app.test_client() as client:
            response = client.post('/valueWithTaxes')
        self.assertEqual(400, response.status_code)


if __name__ == '__main__':
    unittest.main()
