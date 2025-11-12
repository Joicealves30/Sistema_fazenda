const btnAdd = document.getElementById("btnAdd");
const modal = document.getElementById("modalAdd");
const btnCancelar = document.getElementById("btnCancelar");
const form = document.getElementById("formAdd");
const lista = document.getElementById("lista");
const total = document.getElementById("total-func");

btnAdd.onclick = () => modal.style.display = "flex";
btnCancelar.onclick = () => modal.style.display = "none";

form.onsubmit = (e) => {
    e.preventDefault();
    const nome = document.getElementById("nome").value;
    const idade = document.getElementById("idade").value;
    const cargo = document.getElementById("cargo").value;
    const cultura = document.getElementById("cultura").value;

    const li = document.createElement("li");
    li.innerHTML = `<strong>${nome}</strong> — ${idade} anos — ${cargo}<br>
                    Cultura: ${cultura} | Carga horária: 44h/semana`;
    lista.appendChild(li);

    // atualiza total
    total.textContent = lista.children.length;

    modal.style.display = "none";
    form.reset();
};
