from rest_framework.versioning import BaseVersioning


class BuildHeaderVersioning(BaseVersioning):
    def determine_version(self, request, *args, **kwargs):
        return request.META.get('HTTP_X_BUILD_VERSION', '1.0')
