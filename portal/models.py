from django.db import models
from django.utils import timezone

class news(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	head = models.TextField(help_text = 'O Cabeçalho será mostrado apenas no portal!')
	text = models.TextField()
	foto = models.ImageField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	legenda = models.CharField(max_length=255, help_text ='Digite a legenda da foto')

class Meta:
	verbose_name, verbose_name_plural = u"map", u"cidade, estado, position"
	ordering = ('cidade',)
      

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return "%s" % (self.title)




"""	def __init__(self, *args, **kwargs):
		kwargs['max_length']=42
		super(GeopositionField, self).__init__(*args, **kwargs)



	def get_internal_type(self):	
		return 'CharField'

	def to_python(self, value):
		if not value or value=='None':
			return None

		if isinstance(value, Geoposition):
			return value

		if isinstance(value, list):
			return Geoposition(value[0], value[1])


		value_parts = value.rsplit(',')
		try:
			latitude = value_parts[0]
		except IndexError:
			latitude = '0.0'
		try:
			longitude = value_parts[1]
		except IndexError:
			longitude = '0.0'
		return Geoposition(latitude, longitude)

	def from_db_value(self, value, expression, connection, context):
		return self.to_python(value)

	def get_prep_value(self, value):
		return str(value)

	def value_to_string(self, obj):
		value = self._get_val_from_obj(obj)
		return smart_text(value)

	def formfield(self, **kwargs):
		defaults={
			'form_class':GeopositionFormField
		}
		defaults.update(kwargs)
		return super(GeopositionField, self).formfield(**defaults)"""


