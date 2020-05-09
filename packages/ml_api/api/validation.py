from marshmallow import Schema, fields
from marshmallow import ValidationError

import typing as t
import json


class InvalidInputError(Exception):
    """Invalid model input."""


SYNTAX_ERROR_FIELD_MAP = {
    '1stFlrSF': 'FirstFlrSF',
    '2ndFlrSF': 'SecondFlrSF',
    '3SsnPorch': 'ThreeSsnPortch'
}


class CarsDataRequestSchema(Schema):
    year = fields.Integer()
    manufacturer = fields.Str()
    odometer = fields.Integer()
    transmission = fields.Str()
    type = fields.Str()
    ori_cost_prc = fields.Integer()
    # id = fields.Integer(allow_none=True)
    # url = fields.Str(allow_none=True)
    # region = fields.Str(allow_none=True)
    # region_url = fields.Str(allow_none=True)
    # model = fields.Str(allow_none=True)
    # condition = fields.Str(allow_none=True)
    # cylinders = fields.Str(allow_none=True)
    # fuel = fields.Str(allow_none=True)
    # title_status = fields.Str(allow_none=True)
    # vin = fields.Str(allow_none=True)
    # drive = fields.Str(allow_none=True)
    # size = fields.Str(allow_none=True)
    # paint_color = fields.Str(allow_none=True)
    # image_url = fields.Str(allow_none=True)
    # description = fields.Str(allow_none=True)
    # county = fields.Str(allow_none=True)
    # state =fields.Str(allow_none=True)
    # lat = fields.Str(allow_none=True)
    # long = fields.Str(allow_none=True)
    


def _filter_error_rows(errors: dict,
                       validated_input: t.List[dict]
                       ) -> t.List[dict]:
    """Remove input data rows with errors."""

    indexes = errors.keys()
    # delete them in reverse order so that you
    # don't throw off the subsequent indexes.
    for index in sorted(indexes, reverse=True):
        del validated_input[index]

    return validated_input


def validate_inputs(input_data):
    """Check prediction inputs against schema."""

    # set many=True to allow passing in a list
    schema = CarsDataRequestSchema(many=True)
    input_data = json.loads(input_data)

    errors = None
    try:
        schema.load(input_data)
    except ValidationError as exc:
        errors = exc.messages

    if errors:
        validated_input = _filter_error_rows(
            errors=errors,
            validated_input=input_data)
    else:
        validated_input = input_data

    return validated_input, errors
