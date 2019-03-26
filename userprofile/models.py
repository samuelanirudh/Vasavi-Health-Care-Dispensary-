from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

# Create your models here.
class PatientDetails(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    ILLNESS_CHOICES = (
        ('anemia', 'Anemia'),
        ('asthma', 'Asthma'),
        ('arthiritis', 'Arthritis'),
        ('cancer', 'Cancer'),
        ('gout', 'Gout'),
        ('diabetes', 'Diabetes'),
        ('emotional_disorder', 'Emotional Disorder'),
        ('epilepsy_seizures', 'Epilepsy Seizures'),
        ('fainting_spells', 'Fainting Spells'),
        ('gallstones', 'Gallstones'),
        ('heart_disease', 'Heart Disease'),
        ('heart_attack', 'Heart Attack'),
        ('rheumatic_fever', 'Rheumatic Fever'),
        ('high_blood_pressure', 'High Blood Pressure'),
        ('digestive_problems', 'Digestive Problems'),
        ('ulcerative_colitis', 'Ulcerative Colitis'),
        ('ulcer_disease', 'Ulcer Disease'),
        ('hepatitis', 'Hepatitis'),
        ('kidney_disease', 'Kidney Disease'),
        ('liver_disease', 'Liver Disease'),
        ('sleep_apnea', 'Sleep Apnea'),
        ('use_a_c_pap_machine', 'Use a C-PAP machine'),
        ('thyroid_problems', 'Thyroid Problems'),
        ('tuberculosis', 'Tuberculosis'),
        ('venereal_disease', 'Venereal Disease'),
        ('neurological_disorders', 'Neurological Disorders'),
        ('bleeding_disorders', 'Bleeding Disorders'),
        ('lung_disease', 'Lung Disease'),
        ('emphysema', 'Emphysema'),
    )
    MONTH_CHOICES = (
        ('jan', 'January'),
        ('feb', 'February'),
        ('mar', 'March'),
        ('apr', 'April'),
        ('may', 'May'),
        ('jun', 'June'),
        ('jul', 'July'),
        ('aug', 'August'),
        ('sep', 'September'),
        ('oct', 'October'),
        ('nov', 'November'),
        ('dec', 'December'),
    )
    DATE_CHOICES = tuple([(str(x),str(x))for x in range(1,31)])
    YEAR_CHOICES = tuple([(str(x),str(x))for x in range(1900,2019)])
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    date = models.CharField(max_length=6, choices=DATE_CHOICES, default='01')
    month = models.CharField(max_length=6, choices=MONTH_CHOICES, default='January')
    year = models.CharField(max_length=6, choices=YEAR_CHOICES, default='1970')
    height = models.CharField(max_length=4, default='172')
    weight = models.CharField(max_length=4, default='70')
    email = models.EmailField(max_length=128, default='abc@example.com', primary_key=True)
    reason = models.CharField(max_length=1024, default='')
    prescribed_tablets = models.CharField(max_length=1024, null=True)
    drug_allergies = models.CharField(max_length=1024, null=True)
    illnesses = MultiSelectField(choices=ILLNESS_CHOICES, max_choices=10, max_length=4096, default='x')
    other_illnesses = models.CharField(max_length=1024, null=True)
    operations = models.CharField(max_length=1024, null=True)
    current_medications = models.CharField(max_length=1024, null=True)

    def __str__(self):
        return str(self.first_name)
