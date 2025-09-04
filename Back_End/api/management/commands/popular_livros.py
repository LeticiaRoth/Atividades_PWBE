import pandas as pd
from django.core.management.base import BaseCommand
from django.db import transaction
from api.models import Livro

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--arquivo", default="population/livros.csv")
        parser.add_argument("--truncate", action="store_true")
        parser.add_argument("--update", action="store_true")

    @transaction.atomic
    def handle(self, *args, **options):
        df = pd.read_csv(options["arquivo"], encoding="utf-8-sig")
        df.columns = [c.strip().lower().lstrip("\ufeff") for c in df.columns]

        if options["truncate"]:
            Livro.objects.all().delete()

        df["titulo"] = df["titulo"].astype(str).str.strip()
        df["subtitulo"] = df["subtitulo"].astype(str).str.strip()
        df["isbn"] = df["isbn"].apply(lambda x: str(x).zfill(13) if pd.notna(x) else None)
        df["descricao"] = df["descricao"].astype(str).str.strip()
        df["idioma"] = df["idioma"].astype(str).str.strip()
        df["ano_publicado"] = pd.to_numeric(df["ano_publicado"], errors="coerce")
        df["preco"] = pd.to_numeric(df["preco"], errors="coerce").fillna(0.0)
        df["estoque"] = pd.to_numeric(df["estoque"], errors="coerce").fillna(0).astype(int)
        df["desconto"] = pd.to_numeric(df["desconto"], errors="coerce").fillna(0.0)
        df["disponivel"] = df["disponivel"].apply(lambda x: bool(x) if pd.notna(x) else False)
        df["dimensoes"] = pd.to_numeric(df["dimensoes"], errors="coerce").fillna(0.0)
        df["peso"] = pd.to_numeric(df["peso"], errors="coerce").fillna(0.0)

        if options["update"]:
            criados = atualizados = 0
            for r in df.itertuples(index=False):
                _, created = Livro.objects.update_or_create(
                    isbn=r.isbn,
                    defaults={
                        "titulo": r.titulo,
                        "subtitulo": r.subtitulo,
                        "descricao": r.descricao,
                        "idioma": r.idioma,
                        "ano_publicado": r.ano_publicado,
                        "preco": r.preco,
                        "estoque": r.estoque,
                        "desconto": r.desconto,
                        "disponivel": r.disponivel,
                        "dimensoes": r.dimensoes,
                        "peso": r.peso,
                    }
                )
                criados += int(created)
                atualizados += int(not created)
            self.stdout.write(self.style.SUCCESS(f"Criados: {criados} | Atualizados: {atualizados}"))
        else:
            objs = [
                Livro(
                    titulo=r.titulo,
                    subtitulo=r.subtitulo,
                    isbn=r.isbn,
                    descricao=r.descricao,
                    idioma=r.idioma,
                    ano_publicado=r.ano_publicado,
                    preco=r.preco,
                    estoque=r.estoque,
                    desconto=r.desconto,
                    disponivel=r.disponivel,
                    dimensoes=r.dimensoes,
                    peso=r.peso
                )
                for r in df.itertuples(index=False)
            ]
            Livro.objects.bulk_create(objs)
