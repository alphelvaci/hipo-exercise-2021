from .models import Company


def create_company(name):
    company = Company(name=name)
    company.save()
