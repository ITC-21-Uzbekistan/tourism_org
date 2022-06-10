from rest_framework import serializers
from rest_framework.utils.serializer_helpers import ReturnDict

from .models import Country, ContentCountry
from apps.gallery.serializers import ImageSerializer


class ContentCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentCountry
        exclude = ('country',)


class CountrySerializerForAll(serializers.ModelSerializer):
    country_name = serializers.SerializerMethodField('_get_country_name')
    country_info = serializers.SerializerMethodField('_get_country_info')
    country_images = ImageSerializer(read_only=True, many=True)

    class Meta:
        model = Country
        fields = ['id', 'country_name', 'country_info', 'country_url', 'country_meta_keywords', 'country_images']

    def _get_country_name(self, this):
        country_name = ContentCountry.objects.get(country=this, lang__short=str(self.context.get('lang')))
        return country_name.country_name

    def _get_country_info(self, this):
        country_info = ContentCountry.objects.get(country=this, lang__short=str(self.context.get('lang')))
        return country_info.country_info


class CountryCreateSerializerForAdmin(serializers.ModelSerializer):
    contents = ContentCountrySerializer(many=True)

    class Meta:
        model = Country
        fields = ['id', 'country_name', 'contents']

    def create(self, validated_data):
        contents_data = validated_data.pop("contents")
        country = Country.objects.create(**validated_data)
        for content_data in contents_data:
            ContentCountry.objects.create(country=country, **content_data)

        return country

    @property
    def data(self):
        ret = CountrySerializerForAdmin(self.instance).data
        return ReturnDict(ret, serializer=CountrySerializerForAdmin)


class CountrySerializerForAdmin(serializers.ModelSerializer):
    contents = serializers.SerializerMethodField('_get_contents')

    class Meta:
        model = Country
        fields = (
            'id',
            'country_name',
            'country_url',
            'country_meta_keywords',
            'country_images',
            'contents',
        )

    def _get_contents(self, this):
        contents = ContentCountry.objects.filter(country=this)
        serializer = ContentCountrySerializer(contents, many=True)
        return serializer.data

    def update(self, instance, validated_data):
        contents = validated_data.pop('contents')

        instance.country_name = validated_data.get('country_name', instance.country_name)
        instance.country_url = validated_data.get('country_url', instance.country_url)
        instance.country_meta_keywords = validated_data.get('country_meta_keywords', instance.country_meta_keywords)
        instance.country_images = validated_data.get('country_images', instance.country_images)

        for content in contents:
            instance_content = ContentCountry.objects.get(country=instance, lang_id=content['id'])
            instance_content.country_name = content.get('country_name', instance_content.country_name)
            instance_content.country_info = content.get('country_info', instance_content.country_info)

            instance_content.save()

        return instance
