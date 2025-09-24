// Funções JavaScript para carregar o JSON e mostrar no HTML

// Checar entradas
function sanitizeInput(data) {
  return String(data).replace(/[&<>"']/g, c => ({
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    "'": '&#39;'
  })[c]);
}

// Função para buscar e exibir 
async function displayMovieCatalog() {
  try {
    const response = await fetch('/api/filmes', { cache: 'no-store' });
    if (!response.ok) {
      throw new Error(`Erro de rede: status ${response.status}`);
    }
    const movies = await response.json();
    const container = document.getElementById('listaFilmesContainer'); // <-- Linha corrigida

    if (movies.length === 0) {
      container.innerHTML = '<p>Nenhum filme cadastrado.</p>';
      return;
    }

    // Realiza a contrução a tabela HTML
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
          </tr>
        </thead>
        <tbody>
    `;

    movies.forEach(movie => {
      tableHtml += `
        <tr>
          <td>${sanitizeInput(movie.nomeFilme)}</td>
          <td>${sanitizeInput(movie.atores || '')}</td>
          <td>${sanitizeInput(movie.diretor || '')}</td>
          <td>${sanitizeInput(movie.ano || '')}</td>
          <td>${sanitizeInput(movie.genero || '')}</td>
          <td>${sanitizeInput(movie.produtora || '')}</td>
          <td>${sanitizeInput(movie.sinopse || '')}</td>
        </tr>
      `;
    });

    tableHtml += `
        </tbody>
      </table>
    `;

    container.innerHTML = tableHtml;
  } catch (error) {
    document.getElementById('listaFilmesContainer').textContent = `Falha ao carregar filmes: ${error.message}`;
  }
}

// Inicia o processo de exibição do catálogo de filmes quando a página é carregada
document.addEventListener('DOMContentLoaded', displayMovieCatalog);