import shutil


from flask import Blueprint, Response, request
from marshmallow import Schema, fields, ValidationError
import json
from utility.storage import GCSStorageHandler
import pandas as pd

storage = GCSStorageHandler()

cloud_run = Blueprint('cloud_run', __name__, url_prefix='/api')


class CloudRunInputSchema(Schema):
    supplierName = fields.String(
        required=True,
        allow_none=False,
        data_key='supplierName',
        error_messages={"required": "supplierName is required"}
    )
    inputFile = fields.String(
        required=True,
        allow_none=False,
        data_key='inputFile',
        error_messages={"required": "inputFile is required"}
    )


@cloud_run.route('/cloud_run', methods=['POST'])
def get_cloud_run_input():
    request_data = request.json
    schema = CloudRunInputSchema()
    try:
        data = schema.load(request_data)
    except ValidationError as err:
        return Response(json.dumps(err.messages), content_type="application/json", status=400)
    supplier_name = data.get('supplierName').replace('/', '_')
    input_file = data.get('inputFile')
    cleaned_df = pd.DataFrame(eval(input_file))
    cleaned_file_path = f'{supplier_name}_input.csv'
    cleaned_df.to_csv(cleaned_file_path, index=False)
    blob_name, public_url = storage.upload_file(blob_name=cleaned_file_path, local_file_path=cleaned_file_path)
    result = {
        "publicInputFile": blob_name,
        "publicInputFUrl": public_url
    }
    shutil.rmtree(supplier_name, ignore_errors=True)
    return Response(json.dumps(result), mimetype="application/json", status=200)
