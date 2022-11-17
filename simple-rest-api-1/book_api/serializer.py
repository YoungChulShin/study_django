from rest_framework import serializers

# JsonSerialize를 위한 클래스
class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    number_of_pages = serializers.IntegerField()
    publish_date = serializers.DateField()
    quantity = serializers.IntegerField()