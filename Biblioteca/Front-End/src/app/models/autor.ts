export interface Autor {
    id: number;
    nome: string;
    sobrenome?: string | null;
    data_nascimento?: string | null;
    nacionalidade?: string | null;
    biografia?: string | null;
}
