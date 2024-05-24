import pandas
from core.models import Patient, User
from django.contrib.auth.models import Group
from utils import get_mongodb_client
from pathlib import Path


class ServiceProtocol1(object):
    pass


class ServiceProtocol2(object):
    pass


class CreatePatient():

    @staticmethod
    def from_excel_file(file):
        print("debut")
        df = pandas.read_excel(file)
        # db = get_mongodb_client()
        for index, p in df.iterrows():
            try:
                patient = Patient.objects.create(
                    code_patient=p['IDENT'],
                    nom=p['NOM'] if p['NOM'] is not None else "",
                    prenoms=p['PRENOM'] if p['PRENOM'] is not None else "",
                    genre=p['SEXE'] if p['SEXE'] is not None else "",
                    date_naissance=p['DATENAIS'] if p['DATENAIS'] is not None else "",
                    lieu_naissance=p['VILLE'] if p['VILLE'] is not None else "",
                    situation_matrimoniale=p['SITMAT'] if p['SITMAT'] is not None else "",
                    niveau_etude=p['NIVETU'],
                    nationalite=p['NATIONAL'] if p['NATIONAL'] is not None else "",
                    contact=p['TELEPHONE'] if p['TELEPHONE'] is not None else ""
                )
                patient.domiciles.create(ville=p['VILLE'],
                                         commune=p['COMMUNE'])
            except KeyError as e:
                raise e
            except Exception as e:
                pass
            finally:
                # db['patient_suivi'].insert_one(p)
                pass
        print('ending upload excel documents')


class CreateUser(object):

    @staticmethod
    def from_excel(file: Path):
        try:
            users_df = pandas.read_excel(file, )
            for index, p in users_df.iterrows():
                last_name, first_name = str(p["FULLNAME"]) \
                    .replace("'","")\
                    .replace(".","")\
                    .lower().split(" ")[:2]
                email = f"{first_name}.{last_name}{p['N°']}@smitci.com"
                user = User(
                    username=email,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                )
                user.set_password("password4smitci")
                user.save()

                if p['FONCTION'] in ("Chef de service",):
                    user.groups.add(Group.objects.get(name="administrateur"))
                if "Médecin" in p['FONCTION']:
                    user.groups.add(Group.objects.get(name="hospitalisation"))
                if "pharmacie" in p['FONCTION']:
                    user.groups.add(Group.objects.get(name="hospitalisation"))

                return True
        except Exception as e:
            raise e