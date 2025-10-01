import pandas as pd
import numpy as np
from django.core.management.base import BaseCommand
from django.db import transaction
from api.models import Editora

class Command(BaseCommand):
    help = "Popula a tabela Editora, cadastrando apenas registros com os campos essenciais."

    def add_arguments(self, parser):
        parser.add_argument("--csv", default="Population/editoras.csv", help="Caminho para o arquivo CSV de editoras.")
        parser.add_argument("--truncate", action="store_true", help="Limpa a tabela Editora antes de inserir os dados.")
        parser.add_argument("--update", action="store_true", help="Atualiza registros existentes em vez de pular.")

    @transaction.atomic
    def handle(self, *args, **options):
        caminho_csv = options["csv"]
        self.stdout.write(self.style.SUCCESS(f"Lendo arquivo: {caminho_csv}"))

        df = pd.read_csv(caminho_csv, encoding="utf-8-sig")
        df.replace('', np.nan, inplace=True)
        df.columns = [c.strip().lower().lstrip("\ufeff") for c in df.columns]

        if options['truncate']: 
            self.stdout.write(self.style.WARNING("Limpando a tabela Editora..."))
            Editora.objects.all().delete()

        # --- CORREÇÃO APLICADA AQUI ---
        # Apenas 'editora' e 'cnpj' são considerados obrigatórios.
        colunas_obrigatorias = ["editora", "cnpj"]
        df.dropna(subset=colunas_obrigatorias, inplace=True)
        
        for col in df.columns:
            if df[col].dtype == 'object':
                df[col] = df[col].str.strip()
        df.drop_duplicates(subset=["cnpj"], inplace=True)

        self.stdout.write(self.style.SUCCESS(f"Validação concluída. {len(df)} editoras válidas para processar."))

        if options["update"]:
            criados = atualizados = 0
            for r in df.itertuples(index=False):
                _, created = Editora.objects.update_or_create(
                    cnpj=r.cnpj,
                    defaults={
                        "editora": r.editora,
                        "endereco": r.endereco if pd.notna(r.endereco) else None,
                        "telefone": r.telefone if pd.notna(r.telefone) else None,
                        "email": r.email if pd.notna(r.email) else None,
                        "site": r.site if pd.notna(r.site) else None,
                    },
                )
                criados += int(created)
                atualizados += int(not created)
            self.stdout.write(self.style.SUCCESS(f'Operação concluída. Criados: {criados} | Atualizados: {atualizados}'))
        else:
            objs = [
                Editora(
                    editora=r.editora, 
                    cnpj=r.cnpj, 
                    endereco=r.endereco if pd.notna(r.endereco) else None, 
                    telefone=r.telefone if pd.notna(r.telefone) else None, 
                    email=r.email if pd.notna(r.email) else None, 
                    site=r.site if pd.notna(r.site) else None
                ) for r in df.itertuples(index=False)
            ]
            Editora.objects.bulk_create(objs, ignore_conflicts=True)
            self.stdout.write(self.style.SUCCESS(f'Operação concluída. Criados: {len(objs)} (conflitos ignorados)'))