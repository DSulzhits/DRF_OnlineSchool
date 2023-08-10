from rest_framework import serializers


def validator_scam_links(value):
    if value.get('url_video'):
        if 'youtube.com' not in value.get('url_video'):
            raise serializers.ValidationError('Видео можно предоставлять только с youtube.com')
