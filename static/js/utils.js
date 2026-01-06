function capitilize(string) {
  return string
    .toLowerCase()
    .split(" ")
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
    .join(" ");
}

document
  .getElementById("btnCnpj")
  .addEventListener("click", async function (event) {
    const cnpjLimpo = document
      .getElementById("id_cpf_cnpj")
      .value.replace(/\D/g, "");

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
      let elements = {
        id_nome_razao_social: "razao_social",
        id_telefone: "ddd_telefone_1",
        id_email: "email",
        id_cep: "cep",
      };
      Object.entries(elements).forEach(([key, value]) => {
        const html_element = document.getElementById(key);
        if (html_element) {
          html_element.value = data[value];
        }
      });
    } catch (error) {
      console.error("Erro na consulta:", error);
    }
  });

document
  .getElementById("btnCep")
  .addEventListener("click", async function (event) {
    const cepLimpo = document
      .getElementById("id_cep")
      .value.replace(/\D/g, "");

    if (cepLimpo.length !== 8) {
      return;
    }
    
    try {
      const response = await fetch(
        `https://viacep.com.br/ws/${cepLimpo}/json/`
      );

      if (!response.ok) {
        throw new Error("CEP não encontrado");
      }

      const data = await response.json();
      let elements = {
        id_uf: "uf",
        id_municipio: "localidade",
        id_codigo_municipio: "ibge",
        id_bairro: "bairro",
        id_logradouro: "logradouro",
      };
      Object.entries(elements).forEach(([key, value]) => {
        const html_element = document.getElementById(key);
        if (html_element) {
          html_element.value = data[value];
        }
      });
    } catch (error) {
      console.error("Erro na consulta:", error);
    }
  });
