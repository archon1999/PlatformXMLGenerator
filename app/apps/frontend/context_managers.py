from apps.backend.models import Platform


def from_platforms(request):
    platforms = Platform.platforms.all()
    return {
        'platforms': platforms,
    }
