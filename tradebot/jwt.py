from __future__ import unicode_literals

from datetime import datetime

from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.utils import unix_epoch


def jwt_create_payload(user):
    """
    Create JWT claims token.

    To be more standards-compliant please refer to the official JWT standards
    specification: https://tools.ietf.org/html/rfc7519#section-4.1
    """

    issued_at_time = datetime.utcnow()
    expiration_time = issued_at_time + api_settings.JWT_EXPIRATION_DELTA

    payload = {
        'username': user.get_username(),
        'is_staff': user.is_staff,
        'iat': unix_epoch(issued_at_time),
        'exp': expiration_time
    }

    if api_settings.JWT_PAYLOAD_INCLUDE_USER_ID:
        payload['user_id'] = user.pk

    # It's common practice to have user object attached to profile objects.
    # If you have some other implementation feel free to create your own
    # `jwt_create_payload` method with custom payload.
    if hasattr(user, 'profile'):
        payload['user_profile_id'] = user.profile.pk if user.profile else None,

    # Include original issued at time for a brand new token
    # to allow token refresh
    if api_settings.JWT_ALLOW_REFRESH:
        payload['orig_iat'] = unix_epoch(issued_at_time)

    if api_settings.JWT_AUDIENCE is not None:
        payload['aud'] = api_settings.JWT_AUDIENCE

    if api_settings.JWT_ISSUER is not None:
        payload['iss'] = api_settings.JWT_ISSUER

    return payload
