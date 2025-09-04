import pandas as pd
from django.core.management.base import BaseCommand
from django.db import transaction
from api.models import Autor

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--arquivo", default="population/autores.csv")
        parser.add_argument("--truncate", action="store_true")
        parser.add_argument("--update", action="store_true")

    @transaction.atomic
    def handle(self, *a, **o):

        df = pd.read_csv(o["arquivo"], encoding="utf-8-sig")
        df.columns = [c.strip().lower().lstrip("\ufeff") for c in df.columns]

        if o["truncate"]:
            Autor.objects.all().delete()

        df["nome"] = df["nome"].astype(str).str.strip()
        df["sobrenome"] = df["sobrenome"].astype(str).str.strip()
        df["datanascimento"] = pd.to_datetime(df["datanascimento"], errors="coerce", format="%Y-%m-%d").dt.date
        df["nacao"] = df.get("nacao", "").astype(str).str.strip().str.capitalize().replace({"": None})

        df = df.query("nome != '' and sobrenome != ''")
        df = df.dropna(subset=["datanascimento"])

        if o["update"]:
            criados = atualizados = 0
            for r in df.itertuples(index=False):
                _, created = Autor.objects.update_or_create(
                    nome=r.nome,
                    sobrenome=r.sobrenome,
                    dataNascimento=r.datanascimento,  # usa o campo do model
                    defaults={"nacao": r.nacao}
                )
                criados += int(created)
                atualizados += int(not created)
            self.stdout.write(self.style.SUCCESS(f"Criados: {criads} | Atualizados: {atualizados}"))
        else:
            objs = [
                Autor(
                    nome=r.nome,
                    sobrenome=r.sobrenome,
                    dataNascimento=r.datanascimento,
                    nacao=r.nacao
                )
                for r in df.itertuples(index=False)
            ]
            Autor.objects.bulk_create(objs, ignore_conflicts=True)
            self.stdout.write(self.style.SUCCESS(f"Criados: {len(objs)} autores"))
