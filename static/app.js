async function carregarLivros() {
  const resposta = await fetch("/livros");
  const livros = await resposta.json();
  const lista = document.querySelector("#lista-livros");

  for (const livro of livros) {
    const item = document.createElement("li");
    item.textContent = `${livro.titulo} — ${livro.autor}`;
    lista.appendChild(item);
  }
}

carregarLivros();