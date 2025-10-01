import pandas as pd
from django.core.management.base import BaseCommand
from django.db import transaction
from api.models import Autor


class Command(BaseCommand):
    help = "Popula a tabela Autor a partir de um arquivo CSV."

    def add_arguments(self, parser):
        parser.add_argument("--csv", default="Population/autores.csv", help="Caminho para o arquivo CSV de autores.")
        parser.add_argument("--truncate", action="store_true", help="Limpa a tabela Autor antes de inserir os dados.")
        parser.add_argument("--update", action="store_true", help="Atualiza registros existentes em vez de pular.")

    @transaction.atomic
    def handle(self, *args, **options):
        caminho_csv = options["csv"]
        self.stdout.write(self.style.SUCCESS(f"Lendo arquivo: {caminho_csv}"))

        df = pd.read_csv(caminho_csv, encoding="utf-8-sig")
        df.columns = [c.strip().lower().lstrip("\ufeff") for c in df.columns]

        if options['truncate']:
            self.stdout.write(self.style.WARNING("Limpando a tabela Autor..."))
            Autor.objects.all().delete()

        obrigatorias = {"nome", "sobrenome", "data_nascimento"}
        if not obrigatorias.issubset(df.columns):
            self.stdout.write(self.style.ERROR(f"O CSV deve conter as colunas obrigatórias: {obrigatorias}"))
            return

        df["nome"] = df["nome"].astype(str).str.strip()
        df["sobrenome"] = df["sobrenome"].astype(str).str.strip()
        df["data_nascimento"] = pd.to_datetime(df["data_nascimento"], errors="coerce", format="%Y-%m-%d").dt.date
        df["nacionalidade"] = df["nacionalidade"].astype(str).str.strip().str.capitalize().replace({"": None})
        
        df.dropna(subset=["nome", "sobrenome", "data_nascimento"], inplace=True)
        df.drop_duplicates(subset=["nome", "sobrenome", "data_nascimento"], inplace=True)

        if options["update"]:
            criados = atualizados = 0
            for r in df.itertuples(index=False):
                _, created = Autor.objects.update_or_create(
                    nome=r.nome,
                    sobrenome=r.sobrenome,
                    data_nascimento=r.data_nascimento,
                    defaults={"nacionalidade": r.nacionalidade},
                )
                criados += int(created)
                atualizados += int(not created)
            self.stdout.write(self.style.SUCCESS(f"Operação concluída. Criados: {criados} | Atualizados: {atualizados}"))
        else:
            objs = [
                Autor(
                    nome=r.nome,
                    sobrenome=r.sobrenome,
                    data_nascimento=r.data_nascimento,
                    nacionalidade=r.nacionalidade,
                )
                for r in df.itertuples(index=False)
            ]
            Autor.objects.bulk_create(objs, ignore_conflicts=True)
            self.stdout.write(self.style.SUCCESS(f"Operação concluída. Criados: {len(objs)} (conflitos ignorados)"))