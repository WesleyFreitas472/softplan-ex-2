from flask import (
    Blueprint, jsonify, request, Response
)
from API.app.models import Value
from API.app.validatorPayload import (
    InvalidPayloadException, isValidPayload
)
from API.app.payloads import valueWithTaxesPayload

view = Blueprint('view', __name__)

@view.route('/valueWithTaxes', methods=['POST'])
def valueWithTaxes():
    try:
        if not request.json:
            raise InvalidPayloadException('Payload is required')
        isValidPayload(request.json, valueWithTaxesPayload)
        value = Value(request.json.get('amount'))
        valueWithTaxes = value.getValueWithTaxes(request.json.get('tax'))
        return jsonify({"valueWithTaxes": valueWithTaxes})
    except InvalidPayloadException as e:
        return {"error": e.args[0]},400
