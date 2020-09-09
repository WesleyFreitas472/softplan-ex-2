class InvalidPayloadException(Exception):
    pass


def isValidPayload(payloadPassed: dict, payloadExpected: dict) -> bool:
    for key, value in payloadExpected.items():
        if key not in payloadPassed.keys():
            raise InvalidPayloadException(f'Parameter \'{key}\' is required')
        elif type(payloadPassed[key]) != type(payloadExpected[key]):
            typeNeeded = str(type(payloadExpected[key]))
            raise InvalidPayloadException(
                f'Parameter \'{key}\' must be a {typeNeeded}')
    for key in payloadPassed.keys():
        if key not in payloadExpected.keys():
            raise InvalidPayloadException(f'Parameter \'{key}\' is not needed')
    return True
