from django.db.models import (
    Model,
    IntegerChoices,
    DateTimeField,
    IntegerField,
    BigIntegerField,
    TextField,
    BooleanField,
    URLField,
    ForeignKey,
    CASCADE,
)
from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
)
from backend.srvs.camp.camp._settings import (
    AGE_MIN,
    AGE_MAX,
    SALARY_MIN,
    SALARY_MAX,
    DESCRIPTION_MAX,
    WORK_EXPERIENCE_MIN,
    WORK_EXPERIENCE_MAX,
    EMPLOYEES_MIN,
    EMPLOYEES_MAX,
    BUILT_YEAR_MIN,
    BUILT_YEAR_MAX,
    URL_LENGTH,
)


class BaseCompany(Model):
    class Industry(IntegerChoices):
        COMPUTER_AND_INFORMATION_TECHNOLOGY_AND_INTERNET = 1
        PRODUCTION_AND_INDUSTRIES = 2
        ADVERTISING_AND_RECOVERY_AND_BRANDING = 3
        MEDICAL_AND_HEALTH_SERVICES = 4
        ARCHITECTURE_AND_CIVIL_ENGINEERING = 5
        EDUCATION_AND_SCHOOLS_AND_UNIVERSITIES = 6
        MEDIA_AND_PUBLICATIONS = 7
        OIL_AND_GAS = 8
        TOURISM_AND_HOTEL = 9
        FINANCIAL_AND_CREDIT = 10
        TELECOM = 11
        REAL_ESTATE = 12
        INSURANCE = 13
        HUMAN_RESOURCES = 14
        FORCE = 15
        ADVOCACY_AND_LEGAL = 16
        GOVERNMENT = 17
        OTHER = 18

    created_at = DateTimeField(
        auto_now_add=True,
        db_index=True,
    )
    modified_at = DateTimeField(
        auto_now=True,
        db_index=True,
    )
    published_at = DateTimeField(
        null=True,
        blank=True,
    )
    destroyed_at = DateTimeField(
        null=True,
        blank=True,
    )

    industry_id = IntegerField(
        null=True,
        choices=Industry.choices,
    )
    title = TextField(
        null=False,
        blank=False,
    )
    min_employees = IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(EMPLOYEES_MIN),
            MaxValueValidator(EMPLOYEES_MAX),
        ],
    )
    max_employees = IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(EMPLOYEES_MIN),
            MaxValueValidator(EMPLOYEES_MAX),
        ],
    )
    built_year = IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(BUILT_YEAR_MIN),
            MaxValueValidator(BUILT_YEAR_MAX),
        ],
    )
    website = URLField(
        max_length=URL_LENGTH,
        unique=False,
    )
    description = TextField(
        null=True,
        blank=True,
        max_length=DESCRIPTION_MAX,
    )
    public_address = TextField(
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True


class CompanyPage(BaseCompany):
    url = URLField(
        max_length=URL_LENGTH,
        unique=True,
    )


class BaseJob(Model):
    class Category(IntegerChoices):
        SALES_AND_MARKETING = 1
        WEB_AND_PROGRAMMING_AND_SOFTWARE = 2
        FINANCE_AND_ACCOUNTING = 3
        EXECUTIVE_AND_ADMINISTRATIVE_OFFICE_MANAGER = 4
        DIGITAL_MARKETING = 5
        CONTENT_PRODUCTION_AND_MANAGEMENT = 6
        SUPPORT_AND_FINANCE = 7
        IT_DEVOPS_SERVER = 8
        DESIGN = 9
        INDUSTRIAL_ENGINEERING_AND_INDUSTRIAL_MANAGEMENT = 10
        EDUCATION = 11
        SIMPLE_WORKER_AND_SERVICE_FORCE = 12
        SHOPPING_AND_BUSINESS = 13
        ELECTRICAL_AND_ELECTRONIC_ENGINEERING = 14
        HUMAN_RESOURCES_AND_RECRUITMENT = 15
        CIVIL_ENGINEERING_AND_ARCHITECTURE = 16
        THE_FIELD_OF_CINEMA_AND_IMAGE = 17
        WAREHOUSING = 18
        TECHNICAL_TECHNICIAN_AND_REPAIRMAN = 19
        TOURISM = 20
        MECHANICAL_AND_AEROSPACE_ENGINEERING = 21
        PRODUCT_MANAGER = 22
        MARKET_RESEARCH_AND_ECONOMIC_ANALYSIS = 23
        Medicine_nursing_and_medicine = 24
        TRANSPORTATION = 25
        RESEARCH_AND_DEVELOPMENT = 26
        FOOD_INDUSTRY = 27
        SKILLED_LABORER_AND_INDUSTRIAL_WORKER = 28
        HOTEL_MANAGEMENT = 29
        LEGAL_EXPERT_AND_LAWYER = 30
        CAR_AND_MOTOR_COURIER = 31
        PUBLIC_RELATIONS = 32
        INSURANCE_MANAGEMENT = 33
        GUARD = 34
        CHEMICAL_AND_PETROLEUM_ENGINEERING = 35
        TRANSLATION = 36
        HSE = 37
        MINING_AND_METALLURGY_ENGINEERING = 38
        TEXTILE_ENGINEERING_AND_FABRIC_AND_CLOTHING_DESIGN = 39
        CHEMISTRY_AND_PHARMACEUTICALS = 40
        MEDICAL_ENGINEERING = 41
        BIOLOGICAL_AND_LABORATORY_SCIENCES = 42
        JOURNALIST = 43
        AGRICULTURAL_ENGINEERING = 44
        POLYMER_ENGINEERING = 45
        PHYSICAL_EDUCATION = 46
        CEO = 47
        MUSIC_AND_SOUND = 48

    class PlaceType(IntegerChoices):
        IN_PERSON = 1
        REMOTE = 2
        SEMI_ATTENDANCE = 3

    class EmploymentType(IntegerChoices):
        FULL_TIME = 1
        PART_TIME = 2
        CONTRACTUAL = 3

    class Seniority(IntegerChoices):
        EMPLOYEE = 1
        EXPERT = 2
        SENIOR = 3
        MIDDLE_MANAGER = 4
        TOP_MANAGER = 5

    class Gender(IntegerChoices):
        MAN = 1
        WOMAN = 2
        NOT_IMPORTANT = 3

    class MilitaryStatus(IntegerChoices):
        NOT_IMPORTANT = 1
        FINISHED_OR_PERMANENT_EXEMPTION = 2
        EDUCATIONAL_EXEMPTION = 3

    class Status(IntegerChoices):
        ALIVE = 1
        EXPIRED = 2

    class SalaryType(IntegerChoices):
        AGREED = 1
        HOURLY = 2
        DAILY = 3
        WEEKLY = 4
        MONTHLY = 5
        YEARLY = 6

    created_at = DateTimeField(
        auto_now_add=True,
        db_index=True,
    )
    modified_at = DateTimeField(
        auto_now=True,
        db_index=True,
    )
    published_at = DateTimeField(
        null=True,
        blank=True,
    )
    expired_at = DateTimeField(
        null=True,
        blank=True,
    )

    category_id = IntegerField(
        null=True,
        choices=Category.choices,
    )
    place_type_id = IntegerField(
        null=True,
        choices=PlaceType.choices,
    )
    employment_type_id = IntegerField(
        null=True,
        choices=EmploymentType.choices,
    )
    seniority_id = IntegerField(
        null=True,
        choices=Seniority.choices,
    )
    gender_id = IntegerField(
        null=True,
        choices=Gender.choices,
    )
    military_status_id = IntegerField(
        null=True,
        choices=MilitaryStatus.choices,
    )
    status_id = IntegerField(
        null=True,
        choices=Status.choices,
    )
    salary_type_id = IntegerField(
        null=True,
        choices=SalaryType.choices,
    )
    is_intern = BooleanField(
        null=True,
        blank=True,
    )
    min_age = IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(AGE_MIN),
            MaxValueValidator(AGE_MAX),
        ],
    )
    max_age = IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(AGE_MIN),
            MaxValueValidator(AGE_MAX),
        ],
    )
    min_salary = BigIntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(SALARY_MIN),
            MaxValueValidator(SALARY_MAX),
        ],
    )
    max_salary = BigIntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(SALARY_MIN),
            MaxValueValidator(SALARY_MAX),
        ],
    )
    min_work_experience = IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(WORK_EXPERIENCE_MIN),
            MaxValueValidator(WORK_EXPERIENCE_MAX),
        ],
    )
    max_work_experience = IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(WORK_EXPERIENCE_MIN),
            MaxValueValidator(WORK_EXPERIENCE_MAX),
        ],
    )
    title = TextField(
        null=True,
        blank=True,
    )
    description = TextField(
        max_length=DESCRIPTION_MAX,
        null=True,
        blank=True,
    )
    public_address = TextField(
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True


class Post(BaseJob):
    company = ForeignKey(
        CompanyPage,
        on_delete=CASCADE,
        related_name="posts",
        null=True,
        blank=True,
    )
    url = URLField(
        max_length=URL_LENGTH,
        unique=True,
    )
