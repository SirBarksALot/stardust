from rest_framework import serializers
from challenger.models import Challenge


class ChallengeSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        self.owner = kwargs.pop('owner')
        super(ChallengeSerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = Challenge
        fields = ['name']

    def create(self, validated_data):
        challenge = Challenge.objects.create(
            name=self.validated_data['name'],
            owner=self.owner
        )
        challenge.save()

        return challenge
