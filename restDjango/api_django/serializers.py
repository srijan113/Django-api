from .models import Book
from time import timezone

from rest_framework import serializers



#if we use serializer only
# class BookSerializer(serializers.Serializer):
#     title=serializers.CharField(max_length=50)
#     author=serializers.CharField(max_length=50)
#     image=serializers.ImageField()
#     email=serializers.CharField(max_length=254)
#     date=serializers.DateTimeField()


#     def create(self, validated_data):
#         return Book.objects.create(validated_data)

#     def update(self, instance, validated_data):
#         instance.title=validated_data.get('title',instance.title)
#         instance.author=validated_data.get('author',instance.author)
#         instance.image=validated_data.get('image',instance.image)
#         instance.email=validated_data.get('email',instance.email)
#         instance.date=validated_data.get('date',instance.date)
#         instance.save()
#         return instance


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=['id','title','author','image','email','date']