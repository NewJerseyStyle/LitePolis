/**
 * FastAPI
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * OpenAPI spec version: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { Detail2 } from '../models/Detail2';
import { HttpFile } from '../http/http';

export class ResponseMessage {
    'detail': Detail2;
    'error'?: string | null;
    'message'?: string | null;
    'statusCode'?: number;

    static readonly discriminator: string | undefined = undefined;

    static readonly attributeTypeMap: Array<{name: string, baseName: string, type: string, format: string}> = [
        {
            "name": "detail",
            "baseName": "detail",
            "type": "Detail2",
            "format": ""
        },
        {
            "name": "error",
            "baseName": "error",
            "type": "string",
            "format": ""
        },
        {
            "name": "message",
            "baseName": "message",
            "type": "string",
            "format": ""
        },
        {
            "name": "statusCode",
            "baseName": "status_code",
            "type": "number",
            "format": ""
        }    ];

    static getAttributeTypeMap() {
        return ResponseMessage.attributeTypeMap;
    }

    public constructor() {
    }
}

