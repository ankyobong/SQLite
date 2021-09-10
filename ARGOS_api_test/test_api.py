import xml.etree.ElementTree as elemTree
import requests
import sys
# a = open("https://api-rpa.argos-labs.com///openapi/v1/pam/list?apiKey=140781f9a6e354edf86a")
# root = elemTree.fromstring()
# a = elemTree.parse("https://api-rpa.argos-labs.com///openapi/v1/pam/list?apiKey=140781f9a6e354edf86a")
# a=root.findall("https://api-rpa.argos-labs.com///openapi/v1/pam/list?apiKey=140781f9a6e354edf86a")
a = requests.post("https://api-rpa.argos-labs.com///openapi/v1/uxrobot/remote_command/ondemandrun/api?apiKey=2c4e34ba47674e5fd295",
                  json={
    "userId":"akb0930@vivans.net",
    "apiScenarioId":"004987801c6a4d0c8071",
    "timeOut":10,
    "apiPamId":"c1e8a7d977f5d9ace632",
    "endPoint":"http://127.0.0.1:5000/",
    "workId":"input_work_id",
    "botParameters" :
    [
        {
            "variable_text":"{{my.a}}",
            "value":"hello, world"
        },
        {
            "variable_text":"{{my.b}}",
            "value": "hello, world2"
        },
        {
            "variable_text":"{{AAAAA.aaab}}",
          "value": ["1", "2", "3", "A", "B", "C"]
        },
        {
            "variable_text":"{{param.searchText}}",
            "value": "hello world"
        }
    ]
})
# url = "https://api-rpa.argos-labs.com///openapi/v1/scenario/list?apiKey="
# a = requests.get(url+"2c4e34ba47674e5fd295")
# if a.json()['status']//10 == 20:
#     for i in a.json()['data']:
#         for k, v in i.items():
#             sys.stdout.write("%s, %s \n" % (k, v))
# else:
#     sys.stderr.write("status : %d" % a.json()['status'])
    # print(",".join(a.json()['data']))
# sys.stdout.write(a.text)
