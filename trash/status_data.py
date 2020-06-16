status_codes = {
    "1xx" : [
        100,
        101,
        102
    ],
    "2xx" : [
        200,
        201,
        202,
        203,
        204,
        205,
        206,
        207,
        208,
        226
    ],
    "3xx" : [ 
        300,
        301,
        302,
        303,
        304,
        305,
        307,
        308,
    ],
    "4xx" : [
        400,
        401,
        402,
        403,
        404,
        405,
        406,
        407,
        408,
        409,
        410,
        411,
        412,
        413,
        414,
        415,
        416,
        417,
        418,
        421,
        422,
        423,
        424,
        426,
        428,
        429,
        431,
        444,
        451,
        499,
    ],
    "40x" : [
        400,
        401,
        402,
        403,
        404,
        405,
        406,
        407,
        408,
        409,
    ],
    "41x" : [
        410,
        411,
        412,
        413,
        414,
        415,
        416,
        417,
        418,
    ],
    "42x" : [
        421,
        422,
        423,
        424,
        426,
        428,
        429,
    ],
    "5xx" : [
        500,
        501,
        502,
        503,
        504,
        505,
        506,
        507,
        508,
        510,
        511,
        599,
    ],
    "50x": [
        500,
        501,
        502,
        503,
        504,
        505,
        506,
        507,
        508,
    ]
}

# if 410 in status_code["41x"]:
#     print("yes")
# else:
#     print("no")
# print(status_code["41x"
import re
def get_status_codes(status_code):
    rex = re.search(r'([1-5][0-9x]{2})',status_code)
    
    # if rex == None:
    #     print("yes")
    # else:
    #     print("no")
    # val = []
    # if status_code in status_codes:
    #     val = status_codes[status_code]
    # elif status_code.split(",") != []:
    #     val = status_code.split(",")
    # else:
    #     return [200,204,301,302,307,401,403]
    # return rex
    return "ngu vl"

print(get_status_codes("5xx"))