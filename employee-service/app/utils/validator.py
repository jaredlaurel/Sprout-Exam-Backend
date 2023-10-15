import uuid
from datetime import datetime


class BaseValidator:
    """
    Base Class for Validators
    """

    def is_default_id_or_new_id(self, v):
        return v or uuid.uuid4()

    def is_required(self, v, values):
        if not v:
            raise ValueError(
                f"Value is required. "
                f"id: {str(values.get('nsItemId', values.get('id')))}"
            )

        return v

    def is_valid_string(self, v, values):
        if not isinstance(v, str):
            raise ValueError(
                f"Value should be string. "
                f"id: {str(values.get('nsItemId', values.get('id')))}"
            )
        return v

    def is_valid_date_string(self, v, values):
        try:
            return None if not v else datetime.strptime(v, "%m/%d/%Y").date()
        except ValueError:
            raise ValueError(
                f"Incorrect date format, should be MM/dd/yyyy. "
                f"id: {values.get('nsItemId', values.get('id'))}"
            )

    def is_valid_number(self, v, values):
        if isinstance(v, str) and not v.isnumeric():
            raise ValueError(
                f"{v} value should be numeric. "
                f"id: {str(values.get('nsItemId', values.get('id')))}"
            )

        if not v:
            return 0

        return int(v)

    def is_valid_float(self, v, values):
        try:
            return float(v)
        except ValueError:
            raise ValueError(
                f"{v} value should be numeric. "
                f"id: {str(values.get('nsItemId', values.get('id')))}"
            )

    def is_valid_string_and_not_null(self, v, values):
        if self.is_required(v, values) and self.is_valid_string(v, values):
            return v
