from rest_framework import serializers

from .models import Status

class StatusSerialzer(serializers.ModelSerializer):
  class Meta:
    model   = Status
    fields  = [
      'user',
      'content',
      'image',
    ]

  def validate(self, data):

    content = data.get('content', None)

    content = None if content == "" else content
    image = data.get('image', None)

    if content == None and image == None:
      raise serializers.ValidationError('Content or image is required')

    return data