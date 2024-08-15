from src.constants.api_constants import APIconstants

def test_testing():
    url=APIconstants().base_url()
    return url

print(test_testing())