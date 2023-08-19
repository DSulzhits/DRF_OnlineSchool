from rest_framework import serializers


class ScamValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value.get('video_url'):
            if 'youtube.com' not in value.get('video_url'):
                raise serializers.ValidationError('Видео можно предоставлять только с youtube.com')

# def validator_scam_links(value):
#     if value.get('url_video'):
#         if 'youtube.com' not in value.get('url_video'):
#             raise serializers.ValidationError('Видео можно предоставлять только с youtube.com')
