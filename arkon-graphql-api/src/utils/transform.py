import base64

class Convert():

    def base64ToString(id):
        base64_string = id
        base64_bytes = base64_string.encode("ascii")
        sample_string_bytes = base64.b64decode(base64_bytes)
        sample_string = sample_string_bytes.decode("ascii")
        return sample_string.split(':')[1]
    
