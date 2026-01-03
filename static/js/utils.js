function capitilize(string) {
  return string
    .toLowerCase()
    .split(" ")
    .map(
      (word) =>
        word.charAt(0).toUpperCase() +
        word.slice(1)
    )
    .join(" ");
}

document
  .getElementById("btnCnpj")
  .addEventListener("click", async function (event) {
    const cnpjLimpo = document.getElementById("id_cnpj").value.replace(/\D/g, "");

    if (cnpjLimpo.length !== 14) {
      return;
    }

    try {
      const response = await fetch(
        `https://brasilapi.com.br/api/cnpj/v1/${cnpjLimpo}`
      );

      if (!response.ok) {
        throw new Error("CNPJ não encontrado");
      }

      const data = await response.json();

      document.getElementById("id_nome").value = data.razao_social || "";
      document.getElementById("id_telefone").value = data.ddd_telefone_1 || "";
      document.getElementById("id_email").value = data.email || "";
    } catch (error) {
      console.error("Erro na consulta:", error);
    }
  });

