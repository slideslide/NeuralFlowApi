class HttpStatus:
    HTTP_100_CONTINUE = 100
    HTTP_101_SWITCHING_PROTOCOLS = 101
    HTTP_102_PROCESSING = 102
    HTTP_103_EARLY_HINTS = 103
    HTTP_200_OK = 200
    HTTP_201_CREATED = 201
    HTTP_202_ACCEPTED = 202
    HTTP_203_NON_AUTHORITATIVE_INFORMATION = 203
    HTTP_204_NO_CONTENT = 204
    HTTP_205_RESET_CONTENT = 205
    HTTP_206_PARTIAL_CONTENT = 206
    HTTP_207_MULTI_STATUS = 207
    HTTP_208_ALREADY_REPORTED = 208
    HTTP_226_IM_USED = 226
    HTTP_300_MULTIPLE_CHOICES = 300
    HTTP_301_MOVED_PERMANENTLY = 301
    HTTP_302_FOUND = 302
    HTTP_303_SEE_OTHER = 303
    HTTP_304_NOT_MODIFIED = 304
    HTTP_305_USE_PROXY = 305
    HTTP_306_RESERVED = 306
    HTTP_307_TEMPORARY_REDIRECT = 307
    HTTP_308_PERMANENT_REDIRECT = 308
    HTTP_400_BAD_REQUEST = 400
    HTTP_401_UNAUTHORIZED = 401
    HTTP_402_PAYMENT_REQUIRED = 402
    HTTP_403_FORBIDDEN = 403
    HTTP_404_NOT_FOUND = 404
    HTTP_405_METHOD_NOT_ALLOWED = 405
    HTTP_406_NOT_ACCEPTABLE = 406
    HTTP_407_PROXY_AUTHENTICATION_REQUIRED = 407
    HTTP_408_REQUEST_TIMEOUT = 408
    HTTP_409_CONFLICT = 409
    HTTP_410_GONE = 410
    HTTP_411_LENGTH_REQUIRED = 411
    HTTP_412_PRECONDITION_FAILED = 412
    HTTP_413_REQUEST_ENTITY_TOO_LARGE = 413
    HTTP_414_REQUEST_URI_TOO_LONG = 414
    HTTP_415_UNSUPPORTED_MEDIA_TYPE = 415
    HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE = 416
    HTTP_417_EXPECTATION_FAILED = 417
    HTTP_418_IM_A_TEAPOT = 418
    HTTP_421_MISDIRECTED_REQUEST = 421
    HTTP_422_UNPROCESSABLE_ENTITY = 422
    HTTP_423_LOCKED = 423
    HTTP_424_FAILED_DEPENDENCY = 424
    HTTP_426_UPGRADE_REQUIRED = 426
    HTTP_428_PRECONDITION_REQUIRED = 428
    HTTP_429_TOO_MANY_REQUESTS = 429
    HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE = 431
    HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS = 451
    HTTP_500_INTERNAL_SERVER_ERROR = 500
    HTTP_501_NOT_IMPLEMENTED = 501
    HTTP_502_BAD_GATEWAY = 502
    HTTP_503_SERVICE_UNAVAILABLE = 503
    HTTP_504_GATEWAY_TIMEOUT = 504
    HTTP_505_HTTP_VERSION_NOT_SUPPORTED = 505
    HTTP_506_VARIANT_ALSO_NEGOTIATES = 506
    HTTP_507_INSUFFICIENT_STORAGE = 507
    HTTP_508_LOOP_DETECTED = 508
    HTTP_510_NOT_EXTENDED = 510
    HTTP_511_NETWORK_AUTHENTICATION_REQUIRED = 511

    _status_descriptions = {
        # Informational.
        HTTP_100_CONTINUE: 'Continue with the request.',
        HTTP_101_SWITCHING_PROTOCOLS: 'Server is switching to a different protocol.',
        HTTP_102_PROCESSING: 'Server has received and is processing the request, but no response is available yet.',

        # Success
        HTTP_200_OK: 'Request was successful.',
        HTTP_201_CREATED: 'Request was successful, and a new resource has been created.',
        HTTP_202_ACCEPTED: 'Request has been accepted but not yet acted upon.',
        HTTP_203_NON_AUTHORITATIVE_INFORMATION: 'Request was successful, but server is returning information that may '
                                                'be from another source.',
        HTTP_204_NO_CONTENT: 'There is no content to send for this request, but the headers may be useful.',
        HTTP_205_RESET_CONTENT: 'Server successfully processed the request, but is not returning any content.',
        HTTP_206_PARTIAL_CONTENT: 'Download is separated into multiple streams, due to range header.',
        HTTP_207_MULTI_STATUS: 'Message body that follows is an XML message and can contain a number of separate '
                               'response codes.',
        HTTP_208_ALREADY_REPORTED: (
                'Response is a representation of the result of one or more instance-manipulations applied to the '
                'current instance.'),
        HTTP_226_IM_USED: (
                'The server has fulfilled a GET request for the resource, and the response is a representation of the ' +
                'result of one or more instance-manipulations applied to the current instance.'),

        # Redirection.
        HTTP_300_MULTIPLE_CHOICES: 'Request has more than one possible response.',
        HTTP_301_MOVED_PERMANENTLY: 'URI of this resource has changed.',
        HTTP_302_FOUND: 'URI of this resource has changed, temporarily.',
        HTTP_303_SEE_OTHER: 'Client should get this resource from another URI.',
        HTTP_304_NOT_MODIFIED: 'Response has not been modified, client can continue to use a cached version.',
        HTTP_305_USE_PROXY: 'Requested resource may only be accessed through a given proxy.',
        HTTP_306_RESERVED: 'No longer used. Requested resource may only be accessed through a given proxy.',
        HTTP_307_TEMPORARY_REDIRECT: 'URI of this resource has changed, temporarily. Use the same HTTP method to '
                                     'access it.',
        HTTP_308_PERMANENT_REDIRECT: 'The request, and all future requests should be repeated using another URI.',

        # Client Error.
        HTTP_400_BAD_REQUEST: 'Server could not understand the request, due to invalid syntax.',
        HTTP_401_UNAUTHORIZED: 'Authentication is needed to access the given resource.',
        HTTP_402_PAYMENT_REQUIRED: 'Some form of payment is needed to access the given resource.',
        HTTP_403_FORBIDDEN: 'Client does not have rights to access the content.',
        HTTP_404_NOT_FOUND: 'Server cannot find requested resource.',
        HTTP_405_METHOD_NOT_ALLOWED: 'Server has disabled this request method and cannot be used.',
        HTTP_406_NOT_ACCEPTABLE: 'Requested resource is only capable of generating content not acceptable according '
                                 'to the Accept headers sent.',
        HTTP_407_PROXY_AUTHENTICATION_REQUIRED: 'Authentication by a proxy is needed to access the given resource.',
        HTTP_408_REQUEST_TIMEOUT: 'Server would like to shut down this unused connection.',
        HTTP_409_CONFLICT: 'Request could not be processed because of conflict in the request, such as an edit '
                           'conflict.',
        HTTP_410_GONE: 'Requested content has been delected from the server',
        HTTP_411_LENGTH_REQUIRED: 'Server requires the Content-Length header to be defined.',
        HTTP_412_PRECONDITION_FAILED: 'Client has indicated preconditions in its headers which the server does not '
                                      'meet.',
        HTTP_413_REQUEST_ENTITY_TOO_LARGE: 'Request entity is larger than limits defined by server.',
        HTTP_414_REQUEST_URI_TOO_LONG: 'URI requested by the client is too long for the server to handle.',
        HTTP_415_UNSUPPORTED_MEDIA_TYPE: 'Media format of the requested data is not supported by the server.',
        HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE: "Range specified by the Range header in the request can't be "
                                                  "fulfilled.",
        HTTP_417_EXPECTATION_FAILED: "Expectation indicated by the Expect header can't be met by the server.",
        HTTP_418_IM_A_TEAPOT: 'HTCPCP server is a teapot; the resulting entity body may be short and stout.',
        HTTP_422_UNPROCESSABLE_ENTITY: 'Request was well-formed but was unable to be followed due to semantic errors.',
        HTTP_423_LOCKED: 'Resource that is being accessed is locked.',
        HTTP_424_FAILED_DEPENDENCY: 'Request failed due to failure of a previous request (e.g. a PROPPATCH).',
        HTTP_426_UPGRADE_REQUIRED: 'Client should switch to a different protocol such as TLS/1.0.',
        HTTP_428_PRECONDITION_REQUIRED: 'Origin server requires the request to be conditional.',
        HTTP_429_TOO_MANY_REQUESTS: 'User has sent too many requests in a given amount of time.',
        HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE: 'Server rejected the request because either a header, or all the '
                                                  'headers collectively, are too large.',
        HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS: (
                'You attempted to access a Legally-restricted Resource. This could be due to censorship or ' +
                'government-mandated blocked access.'),

        # Server Error.
        HTTP_500_INTERNAL_SERVER_ERROR: "Server has encountered a situation it doesn't know how to handle.",
        HTTP_501_NOT_IMPLEMENTED: 'Request method is not supported by the server and cannot be handled.',
        HTTP_502_BAD_GATEWAY: 'Server, while working as a gateway to get a response needed to handle the request, '
                              'got an invalid response.',
        HTTP_503_SERVICE_UNAVAILABLE: 'Server is not yet ready to handle the request.',
        HTTP_504_GATEWAY_TIMEOUT: 'Server is acting as a gateway and cannot get a response in time.',
        HTTP_505_HTTP_VERSION_NOT_SUPPORTED: 'HTTP version used in the request is not supported by the server.',
        HTTP_506_VARIANT_ALSO_NEGOTIATES: 'Transparent content negotiation for the request results in acircular '
                                          'reference.',
        HTTP_507_INSUFFICIENT_STORAGE: 'Server is unable to store the representation needed to complete the request.',
        HTTP_508_LOOP_DETECTED: 'The server detected an infinite loop while processing the request',
        HTTP_510_NOT_EXTENDED: 'Further extensions to the request are required for the server to fulfill it.',
        HTTP_511_NETWORK_AUTHENTICATION_REQUIRED: 'The client needs to authenticate to gain network access.'
    }

    @classmethod
    def get_message(cls, status_code):
        return cls._status_descriptions.get(status_code, "Unknown status code.")
