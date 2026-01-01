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
    const cnpjLimpo = this.value.replace(/\D/g, "");

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

      console.log("Dados recebidos:", data);

      document.getElementById("id_nome").value = data.razao_social || "";
      document.getElementById("id_telefone").value = data.ddd_telefone_1 || "";
      document.getElementById("id_email").value = data.email || "";
      document.getElementById("id_cep").value = data.cep || "";
      document.getElementById("id_municipio").value = capitilize(data.municipio) || "";
      document.getElementById("id_bairro").value = capitilize(data.bairro) || "";
      document.getElementById("id_logradouro").value = capitilize(data.logradouro) || "";
      document.getElementById("id_complemento").value = capitilize(data.complemento) || "";
      document.getElementById("id_numero").value = data.numero || "";
      document.getElementById("id_uf").value = data.uf || "";
    } catch (error) {
      console.error("Erro na consulta:", error);
      alert("Não foi possível localizar o CNPJ informado.");
    }
  });

document
  .getElementById("btnCep")
  .addEventListener("click", async function (event) {
    const cepLimpo = this.value.replace(/\D/g, "");

    if (cepLimpo.length !== 8) {
      return;
    }

    try {
      const response = await fetch(
        `https://brasilapi.com.br/api/cep/v2/${cepLimpo}`
      );

      if (!response.ok) {
        throw new Error("CEP não encontrado");
      }

      const data = await response.json();

      console.log("Dados recebidos:", data);

      document.getElementById("id_municipio").value = data.city || "";
      document.getElementById("id_bairro").value = data.neighborhood || "";
      document.getElementById("id_logradouro").value = data.street || "";
      document.getElementById("id_uf").value = data.state || "";
    } catch (error) {
      console.error("Erro na consulta:", error);
      alert("Não foi possível localizar o CEP informado.");
    }
  });
