// Funções JavaScript para carregar o JSON e mostrar no HTML

// Checa entradas
function sanitizeInput(data) {
  return String(data).replace(/[&<>"']/g, c => ({
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    "'": '&#39;'
  })[c]);
}

// Função para buscar e exibir o catálogo de filmes
async function displayMovieCatalog() {
  try {
    const response = await fetch('/api/filmes', { cache: 'no-store' });
    if (!response.ok) {
      throw new Error(`Erro de rede: status ${response.status}`);
    }
    const movies = await response.json();
    const listaFilmesContainer = document.getElementById('listaFilmesContainer');

    if (movies.length === 0) {
      listaFilmesContainer.innerHTML = '<p>Nenhum filme cadastrado.</p>';
      return;
    }

    // Realiza a contrução da tabela HTML
    let tableHtml = `
      <table>
        <thead>
          <tr>
            <th>Título</th>
            <th>Atores</th>
            <th>Diretor</th>
            <th>Ano</th>
            <th>Gênero</th>
            <th>Produtora</th>
            <th>Sinopse</th>
            <th>Ações</th>
          </tr>
        </thead>
        <tbody>
    `;

    movies.forEach((movie, index) => {
      tableHtml += `
        <tr>
          <td>${sanitizeInput(movie.titulo)}</td>
          <td>${sanitizeInput(movie.atores || '')}</td>
          <td>${sanitizeInput(movie.diretor || '')}</td>
          <td>${sanitizeInput(movie.ano || '')}</td>
          <td>${sanitizeInput(movie.genero || '')}</td>
          <td>${sanitizeInput(movie.produtora || '')}</td>
          <td>${sanitizeInput(movie.sinopse || '')}</td>
          <td>
            <button class="botaoEditar" onclick="window.location.href='/editar_filme.html?index=${index}'">Editar</button>
            <button class="botaoExcluir" onclick="deleteMovie(${index})">Excluir</button>
          </td>
        </tr>
      `;
    });

    tableHtml += `
        </tbody>
      </table>
    `;

    // Insere a tabela no container mosstrado
    listaFilmesContainer.innerHTML = tableHtml;
  } catch (error) {
    document.getElementById('listaFilmesContainer').textContent = `Falha ao carregar filmes: ${error.message}`;
  }
}

// Função para deletar um filme
async function deleteMovie(index) {
  if (confirm("Tem certeza que deseja excluir este filme?")) {
    try {
      const response = await fetch(`/api/filmes/${index}`, {
        method: 'DELETE'
      });

      if (!response.ok) {
        throw new Error(`Erro ao deletar: status ${response.status}`);
      }

      console.log('Filme deletado com sucesso!');
      displayMovieCatalog(); // Atualiza a lista
    } catch (error) {
      console.error('Falha ao deletar o filme:', error);
      alert(`Falha ao excluir o filme: ${error.message}`);
    }
  }
}

// Função para lidar com a página de edição
async function handleEditPage() {
    const params = new URLSearchParams(window.location.search);
    const index = params.get('index');
    const editForm = document.getElementById('formularioEdicao');
    
    if (!editForm) {
        return;
    }

    if (index === null) {
        alert("Nenhum filme selecionado para edição.");
        window.location.href = '/listar_filmes.html';
        return;
    }

    try {
        const response = await fetch(`/api/filmes/${index}`);
        if (!response.ok) {
            throw new Error(`Erro ao carregar dados do filme: ${response.status}`);
        }
        const movie = await response.json();

        // Preenche os campos do formulário
        document.getElementById('movieIndex').value = index;
        document.getElementById('nomeFilme').value = movie.nomeFilme || '';
        document.getElementById('atores').value = movie.atores || '';
        document.getElementById('diretor').value = movie.diretor || '';
        document.getElementById('ano').value = movie.ano || '';
        document.getElementById('genero').value = movie.genero || '';
        document.getElementById('produtora').value = movie.produtora || '';
        document.getElementById('sinopse').value = movie.sinopse || '';

        editForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const updatedData = {
                nomeFilme: document.getElementById('nomeFilme').value,
                atores: document.getElementById('atores').value,
                diretor: document.getElementById('diretor').value,
                ano: document.getElementById('ano').value,
                genero: document.getElementById('genero').value,
                produtora: document.getElementById('produtora').value,
                sinopse: document.getElementById('sinopse').value
            };

            try {
                const putResponse = await fetch(`/api/filmes/${index}`, {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(updatedData)
                });

                if (!putResponse.ok) {
                    throw new Error(`Erro ao salvar edição: ${putResponse.status}`);
                }

                alert("Filme editado com sucesso!");
                window.location.href = '/listar_filmes.html';
            } catch (error) {
                console.error('Falha ao editar o filme:', error);
                alert(`Falha ao editar o filme: ${error.message}`);
            }
        });
    } catch (error) {
        console.error('Erro ao carregar filme para edição:', error);
        alert(`Erro ao carregar filme: ${error.message}`);
        window.location.href = '/listar_filmes.html';
    }
}

// Inicia a exibição do catálogo ao carregar a página
document.addEventListener('DOMContentLoaded', () => {
    if (document.getElementById('listaFilmesContainer')) {
        displayMovieCatalog();
    }
    if (document.getElementById('formularioEdicao')) {
        handleEditPage();
    }
});