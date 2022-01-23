import requests
import bin.variables as v


def calculate(input_value, output_value, output_code):
    data = {
        'number': input_value
    }
    response = requests.post(v.url_factorial, data=data)
    if response.status_code == output_code:
        answer = response.json().get("answer")
        if answer == output_value:
            return True
        else:
            return answer
    else:
        return response.status_code
