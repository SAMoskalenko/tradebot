class MalformedRequest(Exception):
    """ HTTP 4XX return codes are used for for malformed requests; the issue is on the sender's side. """